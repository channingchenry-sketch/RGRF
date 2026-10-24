#!/usr/bin/env python3
"""
Four-rotor Halbach electrodynamic-wheel (EDW) hover: 6-DOF-lite control sim. License CC0.
Run: python3 sims/halbach_rotor_control_sim.py  -> sims/halbach_rotor_control_sim_output.txt + PNGs

Physics reused from sims/halbach_litz_drag_sim.py (2-D first-harmonic EDS model):
  per rotor  F_L = P_inf(z) A /(1+(vc/v)^2),  F_D = F_L vc/|v|,  P_inf ∝ exp(-2 k z)
  vc = 4 rho/(mu0 t eta) for the 20 mm Cu litz track (eta 0.6) = 4.46 m/s
  v = slip speed = s_i * omega_i * r + vx  (vehicle x-velocity adds to slip: built-in x damping)
Geometry: rotors at corners (±a, ±a), all spin axes along body y, so each rotor's drag
  reaction is an x-force (thrust). Spin signs s = (+,-,-,+) for (FL, RL, FR, RR):
  counter-rotating pairs -> x-thrusts cancel and net angular momentum H = 0.
Body: 88 kg, plate inertia; small angles; states z, theta(pitch), phi(roll), psi(yaw), x, y.
  gap at rotor i: z_i = z + x_i*theta + y_i*phi ; horizontal: Fx = ΣT_i - L*theta,
  Fy = -L*phi (+gust); yaw torque = -Σ y_i T_i; pitch/roll torque from lift differences.
Gyroscopic coupling: tau_gyro = -Omega_body x H_total, H_total = Σ I_r s_i omega_i ŷ.
Inherent EDS damping: parametric, zeta0 = 0.024 (value from the earlier POL sim) on heave,
  pitch, roll. The real EDW heave damping can even be negative (unmodelled).
Motors: first-order lag tau_m on rotor speed; speed command saturates at ±40 % of hover.
Controllability (Grounded, model): speed-only control of 4 rotors spans 4 wrench patterns:
  collective -> lift; (1,1,-1,-1) -> roll; (1,-1,1,-1) -> pitch AND yaw together (coupled);
  (1,-1,-1,1) -> pure x thrust. y needs roll tilt (quadcopter-style); yaw is not independently
  controllable without more rotors or tilting rotor axes.
Labels: all outputs Grounded (model); hardware behaviour Plausible-untested. No phi.
"""
import numpy as np, matplotlib, os
matplotlib.use("Agg"); import matplotlib.pyplot as plt
OUT = os.path.dirname(os.path.abspath(__file__)); L = []
def say(s=""): print(s); L.append(s)
mu0 = 4e-7*np.pi
# --- EDS / rotor parameters (from halbach_litz_drag_sim.py)
Br, M, g = 1.35, 8, 0.05
r, wdt, P = 0.10, 0.05, 4
lam = 2*np.pi*r/P; k = 2*np.pi/lam
B0 = Br*(1-np.exp(-k*lam/4))*np.sin(np.pi*(1-g)/M)/(np.pi/M)
A = wdt*r*np.pi/3
vc = 4*1.68e-8/(mu0*0.02*0.6)
m, gacc = 88.0, 9.81; W = m*gacc
a = 0.35; Iyy = Ixx = m*(0.8**2)/12; Izz = 2*Ixx
Ir = 0.5*3.0*r**2            # 3 kg rotor
xi = np.array([a, -a, a, -a]); yi = np.array([a, a, -a, -a]); s = np.array([1, -1, -1, 1])
tau_m, zeta0 = 0.02, 0.024
v0 = 1.5*vc                   # hover slip speed (L/D = 1.5): max lift-vs-speed authority; W/N = vc regardless
def Pinf(z): return B0**2*np.exp(-2*k*z)/(2*mu0)
def FL(z, v): return Pinf(z)*A/(1+(vc/np.maximum(abs(v), 1e-6))**2)
z0 = -np.log(W/4/(A/(1+(vc/v0)**2))*2*mu0/B0**2)/(2*k)
w0 = v0/r
kz = 2*k*W; wn = np.sqrt(kz/m)
say("Halbach EDW four-rotor hover control sim (CC0). Grounded (model) unless noted.")
say(f"vc={vc:.2f} m/s, hover slip v0={v0:.1f} m/s ({w0*60/2/np.pi:.0f} rpm), gap z0={z0*1e3:.1f} mm, lambda={lam*100:.1f} cm, B0={B0:.2f} T")
say(f"heave stiffness 2kW={kz/1e3:.1f} kN/m, wn={wn:.1f} rad/s ({wn/2/np.pi:.2f} Hz); rotor I={Ir:.3f} kg m^2, h={Ir*w0:.2f} N m s each")
say(f"hover magnetic drag power = W*vc = {W*vc/1e3:.2f} kW ({W/(W*vc)*1e3:.0f} N/kW)")
dFdv = (FL(z0, v0*1.001)-FL(z0, v0*0.999))/(0.002*v0)     # lift sens per slip (m/s)
dDdv = ((FL(z0, v0*1.001)*vc/(v0*1.001))-(FL(z0, v0*0.999)*vc/(v0*0.999)))/(0.002*v0)
say(f"per-rotor sensitivities at hover: dF_L/dv={dFdv:.1f} N/(m/s), dF_D/dv={dDdv:.1f} N/(m/s) (drag falls as speed rises)")

def best_gains(Mi, c, kst, tau=tau_m):
    best = None
    for Kp in np.linspace(0, 3, 31)*kst:
        for Kd in np.linspace(0, 4, 81)*np.sqrt(kst*Mi):
            Ki = 0.0
            poly = np.polymul([Mi, c, kst], [tau, 1]); poly = np.polyadd(poly, [Kd, Kp])
            rts = np.roots(poly); zt = min(-r_.real/abs(r_) for r_ in rts)
            if best is None or zt > best[0]: best = (zt, Kp, Kd, rts)
    return best
cz0 = 2*zeta0*np.sqrt(kz*m)
bz = best_gains(m, cz0, kz); Kz, Dz = bz[1], bz[2]
kr = kz*a**2; br = best_gains(Ixx, 2*zeta0*np.sqrt(kr*Ixx), kr); Kth, Dth = br[1], br[2]
say(f"Linear design with motor lag tau={tau_m*1e3:.0f} ms: best achievable min-zeta heave={bz[0]:.2f} (Kp={Kz/1e3:.0f} kN/m, Kd={Dz:.0f} N s/m), roll/pitch={br[0]:.2f}; open-loop zeta=0.024 (parametric)")
for tau_ in (0.005, 0.01, 0.05):
    say(f"   if motor lag were {tau_*1e3:.0f} ms: heave best zeta={best_gains(m, cz0, kz, tau_)[0]:.2f}")

def run(ctrl, T=4.0, dt=2e-4, load=0.0, tilt0=0.0, gust=0.0, xcmd=0.0, corot=True, T_load=0.5):
    sg = s; sgH = s if corot else np.ones(4)
    st = dict(z=z0, vz=0, th=0, q=0, ph=np.radians(tilt0), p=0, ps=0, rr=0, x=0, vx=0, y=0, vy=0)
    w = w0*np.ones(4); ie = 0.0; log = []
    cz = 2*zeta0*np.sqrt(kz*m); cth = 2*zeta0*np.sqrt(kz*a**2*Iyy)  # parametric inherent damping
    n = int(T/dt)
    for it in range(n):
        t = it*dt
        mass = m + (load if t >= T_load else 0)
        zi = st['z'] + xi*st['th'] + yi*st['ph']
        vsl = sg*w*r + st['vx']
        Fl = FL(zi, vsl); Fd = Fl*vc/np.abs(vsl); Tx = -np.sign(vsl)*Fd
        Ltot = Fl.sum()
        # control -> speed commands
        dw = np.zeros(4)
        if ctrl != "open":
            ez = z0 - st['z']; ie += ez*dt
            dLc = Kz*ez - Dz*st['vz'] + 0.5*Kz*ie  # PID heave (gains from linear design; slow integral)
            dTth = -(Kth*st['th'] + Dth*st['q']); dTph = -(Kth*st['ph'] + Dth*st['p'])
            ph_cmd = 0.0; dTx = 0.0
            if ctrl == "full":
                ph_cmd = np.clip(0.40*st['y'] + 0.40*st['vy'], -0.1, 0.1)   # y via roll tilt (Fy=-L*phi)
                dTph = -(Kth*(st['ph']-ph_cmd) + Dth*st['p']) + kr*ph_cmd   # feedforward against EDS roll stiffness
                dTx = 120*(xcmd - st['x']) - 160*st['vx']
            dv = (dLc/4 + dTth*xi/(4*a**2) + dTph*yi/(4*a**2))/dFdv
            # pure-x thrust pattern (1,-1,-1,1): rotor thrust Tx_i=-s_i F_D; dTx_i/dv_i = -s_i dDdv
            dv += -s*dTx/(4*dDdv)   # pure x-thrust pattern
            dw = np.clip(dv/r, -0.4*w0, 0.4*w0)
        wcmd = w0 + dw
        wdot = (wcmd - w)/tau_m
        # gyroscopic torque  -Omega x H, H along y
        H = Ir*(sgH*w).sum()
        tq_gx = -(-st['rr']*H)   # -(Omega x H)_x = -(q*0 - r*H)... Omega=(p,q,r), H=(0,H,0): Omega x H = (-r H, 0, p H)
        tq_gz = -(st['p']*H)
        az = (Ltot - mass*gacc - cz*st['vz'])/mass
        aq = ((Fl*xi).sum() - cth*st['q'])/Iyy
        ap = ((Fl*yi).sum() - cth*st['p'] + tq_gx)/Ixx
        ar = ((-yi*Tx).sum() + tq_gz)/Izz
        ax = (Tx.sum() - Ltot*st['th'])/mass
        ay = (-Ltot*st['ph'] + (gust if 0.5 <= t < 1.5 else 0))/mass
        for kk, dd in (('z', st['vz']), ('vz', az), ('th', st['q']), ('q', aq), ('ph', st['p']), ('p', ap),
                       ('ps', st['rr']), ('rr', ar), ('x', st['vx']), ('vx', ax), ('y', st['vy']), ('vy', ay)):
            st[kk] += dd*dt
        w += wdot*dt
        Pmag = (Fd*np.abs(vsl)).sum(); Pin = Pmag + (Ir*w*wdot).sum()
        if it % 10 == 0:
            log.append([t, st['z'], st['th'], st['ph'], st['ps'], st['x'], st['y'], Pmag, Pin, np.abs(w/w0-1).max(), tq_gz, tq_gx])
    return np.array(log)

def settle(tt, yy, ref, band, t0):
    m_ = tt >= t0; bad = np.where(np.abs(yy[m_]-ref) > band)[0]
    return (tt[m_][bad[-1]]-t0) if len(bad) else 0.0
def zeta_fit(tt, yy, t0):
    m_ = tt >= t0; y = yy[m_]-yy[m_][-1]; pk = [i for i in range(1, len(y)-1) if y[i] > y[i-1] and y[i] > y[i+1] and y[i] > 0]
    if len(pk) < 2: return float('nan')
    d = np.log(y[pk[0]]/y[pk[1]]); return d/np.sqrt(4*np.pi**2+d**2)

say("\n[Test 1] +10 kg load step at t=0.5 s")
for c in ("open", "pd"):
    lg = run(c, load=10.0)
    t, z = lg[:, 0], lg[:, 1]
    zf = z[-1]
    say(f"  {c:5s}: final gap shift {(zf-z0)*1e3:+.2f} mm, peak dip {(z.min()-z0)*1e3:+.2f} mm, zeta_fit={zeta_fit(t, z, 0.5):.3f}, "
        f"settle(±0.2mm)={settle(t, z, zf, 2e-4, 0.5):.2f} s, peak rotor-speed excursion {lg[:,9].max()*100:.1f} %, "
        f"magnetic P {lg[0,7]/1e3:.2f}->{lg[-1,7]/1e3:.2f} kW, peak input P {lg[:,8].max()/1e3:.2f} kW")
    if c == "open": lo = lg
    else: lp = lg
fig, ax = plt.subplots(figsize=(7, 4)); ax.plot(lo[:, 0], (lo[:, 1]-z0)*1e3, label="open loop (fixed rotor speed)")
ax.plot(lp[:, 0], (lp[:, 1]-z0)*1e3, label="PID via collective rotor speed"); ax.set_xlabel("t (s)"); ax.set_ylabel("gap change (mm)")
ax.set_title("+10 kg step: EDW heave"); ax.grid(alpha=.3); ax.legend(); fig.savefig(f"{OUT}/halbach_rotor_heave_step.png", dpi=110, bbox_inches="tight")

say("\n[Test 2] 5 deg roll disturbance (initial condition)")
for c, co in (("open", True), ("pd", True), ("pd", False)):
    lg = run(c, tilt0=5.0, corot=co, T=3.0)
    t = lg[:, 0]; ph = np.degrees(lg[:, 3]); ps = np.degrees(lg[:, 4])
    say(f"  {c:4s} {'counter-rot' if co else 'co-rot H (gyro only)'}: settle(±0.5deg)={settle(t, ph, 0, 0.5, 0):.2f} s, "
        f"final roll {ph[-1]:+.2f} deg, yaw drift {ps[-1]:+.2f} deg, peak gyro yaw torque {np.abs(lg[:,10]).max():.2f} N m, peak speed exc {lg[:,9].max()*100:.1f} %")
    if c == "pd" and co: l2a = lg
    if c == "pd" and not co: l2b = lg
fig, ax = plt.subplots(figsize=(7, 4))
for lg, lab in ((l2a, "counter-rotating pairs"), (l2b, "all co-rotating")):
    ax.plot(lg[:, 0], np.degrees(lg[:, 3]), label=f"roll, {lab}"); ax.plot(lg[:, 0], np.degrees(lg[:, 4]), "--", label=f"yaw, {lab}")
ax.set_xlabel("t (s)"); ax.set_ylabel("deg"); ax.grid(alpha=.3); ax.legend(fontsize=7); ax.set_title("5° roll recovery: gyroscopic yaw coupling")
fig.savefig(f"{OUT}/halbach_rotor_tilt_gyro.png", dpi=110, bbox_inches="tight")

say("\n[Test 3] lateral gust 50 N in y for 1 s (y has no EDS stiffness; corrected by roll tilt)")
for c in ("open", "full"):
    lg = run(c, gust=50.0, T=12.0)
    say(f"  {c:4s}: y at 1.5 s {lg[np.argmin(abs(lg[:,0]-1.5)),6]:+.3f} m, final y {lg[-1,6]:+.3f} m, max |roll| {np.degrees(np.abs(lg[:,3])).max():.2f} deg, settle(±2 cm)={settle(lg[:,0], lg[:,6], 0, 0.02, 1.5):.2f} s")

say("\n[Test 4] commanded 1 m x-move via pure x-thrust pattern (pair imbalance), counter-rotating")
lg = run("full", xcmd=1.0, T=8.0)
t = lg[:, 0]; x = lg[:, 5]
Pbase = lg[0, 7]; E_extra = np.trapezoid(lg[:, 8]-Pbase, t); E_noregen = np.trapezoid(np.clip(lg[:, 8]-Pbase, 0, None), t); dPmag = np.abs(lg[:, 7]-Pbase).max()
say(f"  overshoot {max(0, x.max()-1)*100:.1f} cm, settle(±2 cm)={settle(t, x, 1.0, 0.02, 0):.2f} s, yaw drift {np.degrees(lg[-1,4]):+.3f} deg, pitch max {np.degrees(np.abs(lg[:,2])).max():.2f} deg")
say(f"  peak rotor-speed excursion {lg[:,9].max()*100:.1f} %, peak input power {lg[:,8].max()/1e3:.2f} kW vs hover {Pbase/1e3:.2f} kW; manoeuvre energy above hover {E_extra/1e3:.2f} kJ with regenerative motors, {E_noregen/1e3:.2f} kJ without; max change in magnetic drag power {dPmag:.0f} W")
fig, ax = plt.subplots(2, 1, figsize=(7, 5), sharex=True)
ax[0].plot(t, x); ax[0].set_ylabel("x (m)"); ax[0].grid(alpha=.3); ax[0].set_title("1 m move by rotor-pair drag imbalance")
ax[1].plot(t, lg[:, 8]/1e3, label="input"); ax[1].plot(t, lg[:, 7]/1e3, label="magnetic drag"); ax[1].set_ylabel("kW"); ax[1].set_xlabel("t (s)"); ax[1].legend(); ax[1].grid(alpha=.3)
fig.savefig(f"{OUT}/halbach_rotor_lateral_move.png", dpi=110, bbox_inches="tight")

say("  co-rotating thrust if spin signs were all equal: net x-force = 4*F_D = %.0f N (drag-as-thrust; cancelled by counter-rotation)" % (W*vc/v0))
say("\n[Gyro] net angular momentum: counter-rotating H = 0; co-rotating H = %.1f N m s -> a 1 rad/s roll rate gives %.1f N m yaw torque (= %.0f%% of a 50 N gust x 0.35 m)" % (4*Ir*w0, 4*Ir*w0, 4*Ir*w0/(50*0.35)*100))
say("\nLimits: 2-D first-harmonic EDS per rotor, quasi-static forces (no eddy time constant), parametric inherent damping,")
say("small angles, no rotor-to-rotor field interaction, track edges, sensor noise or motor current limits. Hardware: Plausible-untested.")
open(f"{OUT}/halbach_rotor_control_sim_output.txt", "w").write("\n".join(L)+"\n")

"""Oloid on a magnetic track: the spine as a segmented stator, the oloid as the mover (CC0).

Compares (A) permanent-magnet mover (60 deg vs 45 deg arcs), (B) passive conductive shell
(induction / eddy drive) and (C) soft-iron reluctance mover; commutation tied to the oloid's
inversion points; EDS / EMS ride notes; energy ledger.
All numbers are MODEL OUTPUTS for the assumed bench parameters below, not measurements.
Outputs: sims/oloid_magnetic_track_motor_sim_output.txt, docs/images/oloid_track_*.png
"""
import numpy as np, matplotlib, os
matplotlib.use("Agg"); import matplotlib.pyplot as plt
here = os.path.dirname(os.path.abspath(__file__)); img = os.path.join(here, "..", "docs", "images")
os.makedirs(img, exist_ok=True); out = []
def say(s=""): print(s); out.append(s)
mu0 = 4e-7*np.pi

# ---- assumed bench parameters ----
r = 0.10                 # oloid circle radius (m)
m = 0.5                  # oloid mass (kg)
N = 50                   # turns per stator coil
Rph = 0.5                # ohm per phase
I = 2.0                  # A (phase amplitude)
Lact = 0.04              # m, active conductor length per coil side under the mover
g = 0.005                # m, mechanical air gap
v = 0.5                  # m/s, operating speed along the track
Bpm = 0.40               # T, PM air-gap field (NdFeB at 5 mm gap)
P_cu = 1.5*I**2*Rph      # 3-phase copper loss at amplitude I
say("Assumed: r = 0.10 m, m = 0.5 kg, N = 50, R = 0.5 ohm/phase, I = 2 A, gap 5 mm, v = 0.5 m/s, B_pm = 0.4 T")
say(f"3-phase copper loss P_cu = {P_cu:.1f} W")

res = {}
# (A) PM mover: 3-phase sinusoidal, F = 1.5 * N * B1 * L * I  (two sides in series ~ 1 coil-side-pair per phase)
for M, lab in ((6, "A60"), (8, "A45")):
    kf = np.sin(np.pi/M)/(np.pi/M)
    F = 1.5*N*Bpm*kf*Lact*I
    Pm = F*v; core = 0.1*Pm                     # 10 % iron/eddy allowance (assumed)
    res[lab] = (F, Pm/(Pm+P_cu+core))
# (B) induction: thin Al shell, eddy force F = sigma d A B^2 v_slip /(1+Rm^2), Rm = mu0 sigma d v_slip/(2 k g) ~ use pole pitch
sig, d = 3.5e7, 1e-3; A = 0.04*0.04
Bc = mu0*N*I/(2*g)                              # coil field at the gap (no iron, generous)
tau_p = 2*np.pi*r/6                             # pole pitch ~ 60 deg of the circle
def F_ind(vs):
    Rm = mu0*sig*d*vs/2.0/(g)                   # sheet magnetic Reynolds number (order of magnitude)
    return sig*d*A*Bc**2*vs/(1+Rm**2)
vs_grid = np.linspace(0.01, 20, 2000); Fg = F_ind(vs_grid); vs_opt = vs_grid[Fg.argmax()]
Fb = Fg.max(); s = vs_opt/(v+vs_opt)
res["B"] = (Fb, (1-s)*Fb*v/(Fb*v/(1-s)*1 + P_cu))   # rotor (shell) loss = s/(1-s) * P_mech
say(f"(B) with an iron-backed gap field of 0.3 T the force would scale by (0.3/B)^2 = {(0.3/(mu0*N*I/(2*g)))**2:.0f}x (rough)")
say(f"(B) coil gap field {Bc*1e3:.1f} mT; best slip speed {vs_opt:.2f} m/s; slip s = {s:.2f} at v = {v} m/s")
# (C) reluctance: soft-iron tooth, F = 0.5 I^2 dL/dx, L ~ mu0 N^2 A / g, Lmin = Lmax/4 over half a pitch
Lmax = mu0*N**2*A/g; dLdx = 0.75*Lmax/(tau_p/2)
Fc = 0.5*I**2*dLdx*0.5                          # 0.5 = average over the stroke with one phase on
Pc = I**2*Rph                                   # one phase on
res["C"] = (Fc, Fc*v/(Fc*v+Pc+0.15*Fc*v))
say(f"(C) L_max = {Lmax*1e3:.2f} mH, dL/dx = {dLdx*1e3:.2f} mH/m")
say("\nMover type                      F (N)   N/A     N/W     efficiency at 0.5 m/s")
names = {"A60": "(A) PM mover, 60 deg arcs", "A45": "(A) PM mover, 45 deg arcs", "B": "(B) passive Al shell (induction)", "C": "(C) soft-iron reluctance"}
for kk, (F, eta) in res.items():
    Pin = P_cu if kk != "C" else I**2*Rph
    say(f"{names[kk]:32s} {F:6.3f}  {F/I:6.3f}  {F/Pin:6.3f}  {eta*100:5.1f} %")

# ---- commutation tied to inversion points (1D track model) ----
# inversion every half-cycle of rolling: the mover's magnet polarity relative to the track flips.
# Rolling distance per cycle ~ 2*pi*r*(4/3)?  use path length per cycle Lc = 4*pi*r/ (assumed, [to verify])
Lc = 2*np.pi*r
def run(mode, T=8.0, dt=1e-4, err_deg=0.0):
    x = 0.0; vv = 0.05; E_in = E_cu = E_fr = 0.0; c_fr = 0.2; Ke = res["A60"][0]/I
    V = 3.0; X = []; Vt = []
    for n in range(int(T/dt)):
        t = n*dt; ph = 2*np.pi*x/Lc
        pol = np.sign(np.cos(ph))                         # mover polarity flips at inversions
        if mode == "none": sgn = 1.0
        elif mode == "hall": sgn = np.sign(np.cos(ph + np.deg2rad(err_deg)))
        elif mode == "sched": sgn = np.sign(np.cos(ph))*(1 if t < 4 else -1)   # deliberate reversal at t = 4 s
        k = Ke*pol*sgn
        Icur = (V - k*vv)/Rph if mode != "none" else (V - Ke*pol*vv)/Rph
        F = k*Icur if mode != "none" else Ke*pol*Icur
        E_in += V*Icur*dt; E_cu += Icur**2*Rph*dt; E_fr += c_fr*vv**2*dt
        vv += dt*(F - c_fr*vv)/m; x += vv*dt; Vt.append(vv)
    KE = 0.5*m*vv**2
    return np.array(Vt), E_in, E_cu, E_fr, KE
say("\nCommutation (1D track, PM 60 deg mover, 3 V drive, friction 0.2 N s/m, 8 s)")
fig, ax = plt.subplots(figsize=(8, 4)); tt = np.arange(int(8.0/1e-4))*1e-4
for mode, err, lab in (("none", 0, "no commutation"), ("hall", 0, "Hall, 0 deg error"), ("hall", 10, "Hall, 10 deg error"), ("hall", 30, "Hall, 30 deg error"), ("sched", 0, "hold, then scheduled reversal at 4 s")):
    Vt, Ei, Ec, Ef, KE = run(mode, err_deg=err)
    say(f"  {lab:38s} final v = {Vt[-1]:+.3f} m/s | E_in {Ei:7.2f} J = Cu {Ec:7.2f} + friction {Ef:6.2f} + KE {KE:5.3f} (residual {Ei-Ec-Ef-KE:+.3f} J)")
    ax.plot(tt, Vt, label=lab)
ax.set_xlabel("t (s)"); ax.set_ylabel("speed along track (m/s)"); ax.legend(fontsize=8); ax.set_title("Oloid track motor: commutation at inversion points (model)")
fig.tight_layout(); fig.savefig(os.path.join(img, "oloid_track_commutation.png"), dpi=120); plt.close(fig)

# ---- ride: EDS lift/drag and EMS ----
sCu, dCu = 5.8e7, 1e-3; w = 2/(mu0*sCu*dCu)
say(f"\nEDS over a 1 mm Cu sheet: characteristic speed w = {w:.1f} m/s; lift/drag = v/w")
for vv in (0.5, 5, 50):
    say(f"  v = {vv:5.1f} m/s: L/D = {vv/w:.3f}, lift fraction of max = {vv**2/(vv**2+w**2):.4f}")
Fw = m*9.81; Bems = np.sqrt(2*mu0*Fw/(2*A))
say(f"EMS attraction to hold {Fw:.1f} N over 2 x {A*1e4:.0f} cm^2 poles needs B = {Bems*1e3:.0f} mT (achievable; needs feedback, Earnshaw)")

fig, ax = plt.subplots(figsize=(6, 4)); vv = np.linspace(0, 60, 300)
ax.plot(vv, vv/w, label="EDS lift/drag (1 mm Cu)"); ax.axvline(0.5, ls="--", c="k", label="bench speed 0.5 m/s")
ax.set_xlabel("speed (m/s)"); ax.set_ylabel("L/D"); ax.legend(); ax.set_title("EDS needs speed; EMS needs control")
fig.tight_layout(); fig.savefig(os.path.join(img, "oloid_track_levitation.png"), dpi=120); plt.close(fig)
open(os.path.join(here, "oloid_magnetic_track_motor_sim_output.txt"), "w").write("\n".join(out)+"\n")

"""Oloid on an outer spine with a radial Lorentz drive: simple, honest bench-scale model (CC0).

Outputs: sims/oloid_spine_lorentz_sim_output.txt and docs/images/oloid_*.png.
All numbers are MODEL OUTPUTS for assumed parameters, not measurements.

Geometry: circle 1 (radius r) in body xy-plane centred at 0; circle 2 in body xz-plane
centred at (r,0,0). Centre of mass (uniform solid, by symmetry) at (r/2,0,0).
Rolling contact: the ground plane (outward normal -u in body frame) touches both circles.
Support of circle 1 in direction u: r*sqrt(ux^2+uy^2); of circle 2: r*ux + r*sqrt(ux^2+uz^2).
Writing u = (c cos t, c sin t, uz) (t = contact angle on circle 1) and equating supports gives
c^2 = 1/(2-2cos t), uz^2 = (1-2cos t)/(2-2cos t), t in [pi/3, 5pi/3].  Two signs of uz
= the two half-cycles. COM height H = r c (1 - cos t / 2).
"""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt, os
here = os.path.dirname(os.path.abspath(__file__)); img = os.path.join(here, "..", "docs", "images")
os.makedirs(img, exist_ok=True); out = []
def say(s=""): print(s); out.append(s)

# ---------------- 1. kinematics ----------------
r = 0.10
N = 2000
t = np.linspace(np.pi/3, 5*np.pi/3, N)
c = 1/np.sqrt(2-2*np.cos(t)); uz = np.sqrt(np.clip((1-2*np.cos(t))/(2-2*np.cos(t)), 0, None))
H = r*c*(1-np.cos(t)/2)
# full cycle: branch +uz forward, branch -uz back; phase theta in [0, 2pi)
theta = np.linspace(0, 2*np.pi, 2*N, endpoint=False)
UZ = np.concatenate([uz, -uz[::-1]]); HH = np.concatenate([H, H[::-1]])
# brute-force check of the support equality at a few points
for k in (100, 700, 1500):
    u = np.array([c[k]*np.cos(t[k]), c[k]*np.sin(t[k]), uz[k]]); s = np.linspace(0, 2*np.pi, 20001)
    p1 = np.stack([r*np.cos(s), r*np.sin(s), 0*s], 1); p2 = np.stack([r+r*np.cos(s), 0*s, r*np.sin(s)], 1)
    assert abs((p1@u).max()-(p2@u).max()) < 1e-6
say("1. Oloid rolling kinematics (r = 0.10 m)")
say(f"   COM height min {H.min()/r:.4f} r, max {H.max()/r:.4f} r, swing {(H.max()-H.min())/r*100:.2f} % of r")
say(f"   (analytic: min r/sqrt2 = {1/np.sqrt(2):.4f} r at t = pi/2, max 3r/4 at t = pi/3 and pi)")
say(f"   circle-1 normal vertical component (= -u_z) changes sign {int(np.sum(np.diff(np.sign(UZ[UZ!=0]))!=0))+1} times (incl. wrap) per cycle")

# ---------------- 2. drive schemes ----------------
B0 = 0.10     # T, spine field at the band (assumed, NdFeB-on-steel bench level)
A = np.pi*r**2
Rband = 0.05  # ohm, copper band + brushes (assumed)
I = 10.0      # A
P = I**2*Rband
g = UZ        # torque-per-amp profile shape: tau = I*A*B0*g(theta)  (flips with the axis inversion)
k = A*B0
tau_a = I*k*g.mean()
tau_b = I*k*np.abs(g).mean()
Lg, duty = 0.02, 0.30        # gapped junction: 20 mm active conductor, 30 % of cycle under field
tau_c = I*Lg*B0*r*duty
say("\n2. Radial Lorentz drive, I = 10 A, B = 0.10 T, R = 0.05 ohm -> P = %.1f W" % P)
for name, tau in (("(a) no commutation", tau_a), ("(b) commutated at inversions", tau_b), ("(c) gapped-junction baseline", tau_c)):
    say(f"   {name:32s} mean torque {tau*1e3:8.4f} mN m | {tau/I*1e3:8.4f} mN m/A | {tau/P*1e3:8.4f} mN m/W")

# ---------------- 3. motional EMF and drag ----------------
f = 1.0; w = 2*np.pi*f                # one rolling cycle per second
dg = np.gradient(g, theta)
emf = -k*dg*w                         # -dPhi/dt, Phi = k*g
drag = (k*dg)**2*w/Rband              # shorted band: tau = (k g')^2 w / R
say("\n3. Motional EMF at 1 cycle/s (phase taken uniform in time): rms = %.2f mV, median |EMF| = %.2f mV" % (np.sqrt((emf**2).mean())*1e3, np.median(abs(emf))*1e3))
say("   (peak %.0f mV is a spike at the inversion points where d(u_z)/dt is singular in this parametrisation)" % (abs(emf).max()*1e3))
say("   shorted-band eddy drag: mean %.3f uN m (dissipates %.2f uW)" % (drag.mean()*1e6, drag.mean()*w*1e6))

# ---------------- 4. kickstart: Bullard disc ----------------
Lself, M, Rd = 1e-6, 2e-7, 1e-3      # H, H, ohm (optimistic bench disc)
wc = Rd/M
say(f"\n4. Bullard homopolar dynamo: L dI/dt = (M w - R) I.  Threshold w_c = R/M = {wc:.0f} rad/s ({wc/2/np.pi:.0f} rev/s)")
tt = np.linspace(0, 0.02, 4001); dt = tt[1]-tt[0]
fig, ax = plt.subplots()
for wrel, I0 in ((0.8, 1e-3), (1.2, 1e-3), (1.2, 0.0)):
    Ii = np.empty_like(tt); Ii[0] = I0
    for n in range(1, len(tt)): Ii[n] = Ii[n-1] + dt*(M*wrel*wc-Rd)*Ii[n-1]/Lself
    ax.semilogy(tt*1e3, np.abs(Ii)+1e-12, label=f"w = {wrel} w_c, seed {I0} A")
    say(f"   w = {wrel} w_c, seed {I0:g} A -> I after 20 ms = {Ii[-1]:.3g} A")
ax.set_xlabel("t (ms)"); ax.set_ylabel("|I| (A)"); ax.legend(); ax.set_title("Bullard disc: needs seed AND M w > R")
fig.savefig(os.path.join(img, "oloid_kickstart_bullard.png"), dpi=120); plt.close(fig)

# ---------------- 5. Rikitake reversals + control ----------------
def rik(T=400, dt=1e-3, mu=1.0, Ak=1.0, ctrl=None):
    x, y, z = 1.0, 0.5, 1.0; X = np.empty(int(T/dt))
    for n in range(len(X)):
        tn = n*dt; u = 0.0
        if ctrl is not None: u = ctrl(tn, x)
        dx = -mu*x + z*y + u; dy = -mu*y + (z-Ak)*x; dz = 1 - x*y
        x += dt*dx; y += dt*dy; z += dt*dz; X[n] = x
    return X
mu, Ak = 1.0, 2.0
Xf = rik(mu=mu, Ak=Ak)
Xh = rik(mu=mu, Ak=Ak, ctrl=lambda tn, x: 2.0*(1.0 - x) if x < 1.0 else 0.0)
Xs = rik(mu=mu, Ak=Ak, ctrl=lambda tn, x: 2.0*((1 if (tn//100) % 2 == 0 else -1)*1.5 - x))
def nrev(X): s = np.sign(X[X != 0]); return int(np.sum(np.diff(s) != 0))
say(f"\n5. Rikitake two-disc dynamo (mu = {mu}, A = {Ak}), t = 0-400 (dimensionless)")
say(f"   free run: {nrev(Xf)} polarity reversals (irregular)")
say(f"   polarity-hold feedback u = 2(1-x) when x<1: {nrev(Xh)} reversals")
say(f"   scheduled reversal every 100 time units (target +/-1.5): {nrev(Xs)} reversals")
ts = np.arange(len(Xf))*1e-3
fig, axs = plt.subplots(3, 1, sharex=True, figsize=(8, 6))
for a, X, lab in zip(axs, (Xf, Xh, Xs), ("free (chaotic reversals)", "hold polarity", "timed reversals")):
    a.plot(ts, X, lw=0.6); a.set_ylabel("x (disc-1 current)"); a.set_title(lab, fontsize=9)
axs[-1].set_xlabel("t (dimensionless)"); fig.tight_layout()
fig.savefig(os.path.join(img, "oloid_rikitake_reversals.png"), dpi=120); plt.close(fig)

# ---------------- 6. energy ledger (commutated drive, rolling) ----------------
J = 0.5*0.5*r**2      # kg m^2 effective, 0.5 kg oloid (assumed)
cf = 2e-4             # N m s viscous/rolling loss (assumed)
V = 0.5               # V supply, commutated
dt = 1e-4; T = 20.0; ph = 0.0; om = 0.0
# start-up test from rest at the inversion point (g = 0): dead point
j0 = 0; say(f"\n6a. From rest at an inversion point g = {g[j0]:.3f}: zero torque, needs a kick")
om = 2*np.pi*0.3   # kickstart 0.3 cycles/s
Ein = Ej = Ef = 0.0
for n in range(int(T/dt)):
    j = int((ph % (2*np.pi))/(2*np.pi)*len(g)) % len(g)
    kk = k*abs(g[j]); s = 1.0                    # commutated: effective coupling |g|
    Icur = (V - kk*om)/Rband                     # back-EMF kk*om
    tau = kk*Icur
    Ein += V*Icur*dt; Ej += Icur**2*Rband*dt; Ef += cf*om**2*dt
    om += dt*(tau - cf*om)/J; ph += om*dt
KE = 0.5*J*om**2
say(f"\n6. Energy ledger (V = {V} V commutated, J = {J:.2e} kg m^2, c = {cf} N m s, 20 s)")
say(f"   E_in = {Ein:.3f} J; Joule = {Ej:.3f} J; friction = {Ef:.3f} J; KE = {KE:.4f} J")
say(f"   residual E_in - (Joule + friction + KE) = {Ein-Ej-Ef-KE:+.2e} J (integration error); efficiency to friction work {Ef/Ein*100:.1f} %")
say(f"   steady roll speed {om/2/np.pi:.2f} cycles/s. Output never exceeds input: no over-unity.")

# ---------------- 7. 60 deg vs 45 deg spine arc segments ----------------
say("\n7. Spine arc segments: 60 deg (6 per ring/wavelength) vs 45 deg (8)")
for Mseg in (6, 8):
    kf = np.sin(np.pi/Mseg)/(np.pi/Mseg)          # fundamental of a segmented Halbach (Mallinson/Halbach)
    say(f"   M = {Mseg}: fundamental field factor {kf*100:.1f} % of ideal; first harmonic order {Mseg-1} and {Mseg+1}")
# commutation can only change sign at arc boundaries; inversions sit at phase 0 and pi
G = np.abs(g).sum()
for Mseg in (6, 8):
    row = []
    for dd in (0, 5, 10, 15, 22.5, 30):
        d = np.deg2rad(dd); edges = (theta - d) % (2*np.pi)
        seg = np.floor(edges/(2*np.pi/Mseg)).astype(int)
        cap = sum(abs(g[seg == q].sum()) for q in range(Mseg))/G
        row.append(f"{dd:>4} deg: {cap*100:5.1f} %")
    say(f"   M = {Mseg} commutation capture vs boundary offset from inversion: " + "; ".join(row))
say("   Both 6 and 8 divide 180 deg evenly, so either aligns with the half-cycle inversion when phased correctly.")
Jk = J; kick = 0.5*Jk*(2*np.pi*0.3)**2
say(f"\n8. Nitinol kickstart: KE to reach 0.3 cycles/s = {kick*1e3:.1f} mJ; at an assumed 1-5 % SMA heat-to-work efficiency")
say(f"   the AC-coil heating needed is {kick/0.05:.2f}-{kick/0.01:.2f} J per kick. A static magnet gives dB/dt = 0: no heating.")

fig, ax = plt.subplots(2, 1, sharex=True)
ax[0].plot(theta, HH/r); ax[0].set_ylabel("COM height / r"); ax[0].set_title("Oloid: COM height and axis inversion")
ax[1].plot(theta, g, label="torque/amp shape (no commutation)"); ax[1].plot(theta, np.abs(g), "--", label="commutated")
ax[1].set_xlabel("rolling phase (rad)"); ax[1].legend(fontsize=8)
fig.savefig(os.path.join(img, "oloid_kinematics_drive.png"), dpi=120); plt.close(fig)
open(os.path.join(here, "oloid_spine_lorentz_sim_output.txt"), "w").write("\n".join(out)+"\n")

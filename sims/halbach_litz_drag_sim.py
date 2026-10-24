#!/usr/bin/env python3
"""
Halbach + EDS drag-reduction sweep: segmented Halbach arrays, insulated litz-loop
(Inductrack-style) tracks vs solid Cu/Al plates, and a spinning Halbach
electrodynamic wheel (EDW) for stationary hover.  License CC0.

Run:  python3 sims/halbach_litz_drag_sim.py   (numpy + matplotlib)
Writes sims/halbach_litz_drag_sim_output.txt and sims/halbach_litz_*.png

MODELS (all analytic, 2-D, first spatial harmonic only)
1. Halbach surface field (Halbach 1980; Post & Ryutov 2000):
       B0 = Br (1 - exp(-k d)) * sin(pi*(1-g)/M) / (pi/M),   k = 2 pi / lambda
   M = segments per wavelength, d = magnet thickness, g = insulating-gap fraction
   between magnet segments. Gap term: each segment's angular width shrinks to
   (1-g)*2pi/M with the same orientation step; the factor is the fundamental
   Fourier coefficient of that stepped magnetisation (g=0 recovers the standard
   formula). Higher harmonics, end effects and finite width are ignored.
   Field at gap y: |B| = B0 exp(-k y).
2. Common EDS lift/drag law. For both a ladder of shorted circuits (Post &
   Ryutov 2000) and a thin conducting sheet (Reitz 1970, J. Appl. Phys. 41,
   2067), with excitation frequency w = k v:
       F_L = P_inf * A * 1/(1 + (vc/v)^2),   F_D / F_L = vc / v  (= R/(wL))
   P_inf = B0^2 exp(-2 k y)/(2 mu0) (perfect-conductor image pressure; order-
   of-magnitude, equals Post's high-speed limit to within O(1) factors).
   Transition speed vc (L/D = 1):
     litz/ladder track: R/(wL) with L ~ mu0 w_t/(2 k dc) (mutual term only,
        leakage inductance omitted) and R = rho*2 w_t*F_R/(A_c) ->
        vc = 4 rho F_R / (mu0 t eta)   (t = conductor depth, eta = copper fill)
     thin plate (Reitz): vc = 2 /(mu0 sigma t_eff),
        t_eff = delta (1 - exp(-t/delta)) (skin-depth limited; crude interpolation
        between t<<delta and t>>delta; thick-plate exact result differs by O(1)).
   KEY CONSEQUENCE: drag power P_D = F_D v = F_L * vc (high-speed). So magnetic
   drag power per newton of lift = vc [W/N]; N/kW = 1000/vc. Reducing vc is THE
   drag lever; speed only buys L/D, not W/N, once v >> vc.
3. Litz AC resistance: per-strand skin factor 1 + (r_s/delta)^4/48 (round wire,
   r_s << delta) plus a bundle proximity term N_s * (d_s/delta)^4 / 32 (order of
   magnitude, after Sullivan 1999 IEEE TPEL 14(2)); stated approximate.
4. Electrodynamic wheel (Bird & Lipo 2003-2008, IEEE Trans. Magn.): rotor
   radius ro, surface slip speed vs = w_m ro over a stationary conductor, unrolled
   onto the flat model above with active area = width x active arc (ro * pi/3,
   assumption). Drag torque T = F_D ro; shaft power = F_D vs = F_L vc (+ windage,
   bearing, motor losses -> eta_motor). Hover: net thrust ~0 if wheels are paired
   counter-rotating (assumed).
Labels: model outputs are **Grounded (model-based)**; anything about a built POL
device is **Plausible-untested**. No phi used.
"""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt, os
mu0 = 4e-7*np.pi
RHO = {"Cu": 1.68e-8, "Al": 2.65e-8}
OUT = os.path.dirname(os.path.abspath(__file__)); lines = []
def say(s=""): print(s); lines.append(s)

def B0(Br, lam, d, M, g=0.0):
    k = 2*np.pi/lam
    return Br*(1-np.exp(-k*d))*np.sin(np.pi*(1-g)/M)/(np.pi/M)
def P_inf(B, lam, y): return (B*np.exp(-2*np.pi/lam*y))**2/(2*mu0)
def delta(rho, f): return np.sqrt(rho/(np.pi*f*mu0))
def litz_FR(rho, f, ds, Ns):
    dl = delta(rho, np.maximum(f, 1e-9)); x = ds/dl
    return 1 + (ds/2/dl)**4/48 + Ns*x**4/32
def vc_litz(rho, t, eta, FR=1.0): return 4*rho*FR/(mu0*t*eta)
def vc_plate(rho, t, f):
    dl = delta(rho, np.maximum(f, 1e-9)); teff = dl*(1-np.exp(-t/dl))
    return 2*rho/(mu0*teff)
def lift_factor(v, vc): return 1/(1+(vc/np.maximum(v,1e-9))**2)

Br, LOAD, BASE = 1.35, 88*9.81, 52.0
say("Halbach + EDS drag-reduction sweep (CC0). Br = %.2f T NdFeB; load 88 kg = %.0f N; baseline %.0f N/kW" % (Br, LOAD, BASE))
say("="*78)
# --- 1. Halbach field
say("\n[1] Halbach surface field B0 (T), d = lambda/4, Grounded (model)")
for lam in (0.05, 0.10, 0.20):
    for M in (4, 8):
        row = " ".join("g=%.2f:%.3f" % (g, B0(Br, lam, lam/4, M, g)) for g in (0, .05, .1, .2))
        say(f"  lambda={lam*100:4.0f} cm M={M}: {row}")
say("  -> gaps cost field ~linearly (B0 ~ (1-g) for small g); lift ~ B0^2 so 10% gap ~ -19% lift, M=8 vs 4 ~ +11% B0.")

# --- 2. conductors: transition speed vs speed
lam, t = 0.10, 0.010
v = np.linspace(0.5, 100, 400); f = v/lam
cases = {}
for c in ("Cu", "Al"):
    cases[f"{c} plate t=10mm"] = vc_plate(RHO[c], t, f)
ds, Ns = 0.1e-3, 1000
FR = litz_FR(RHO["Cu"], f, ds, Ns)
cases["Cu litz ladder eta=0.6"] = vc_litz(RHO["Cu"], t, 0.6, FR)
cases["Al litz ladder eta=0.6"] = vc_litz(RHO["Al"], t, 0.6, litz_FR(RHO["Al"], f, ds, Ns))
cases["Cu litz ladder t=20mm eta=0.6"] = vc_litz(RHO["Cu"], 0.02, 0.6, FR)
say("\n[2] Transition speed vc and magnetic-drag W per N of lift (= vc at v>>vc), lambda=10 cm. Grounded (model)")
say("    litz: strands %.2f mm, N_s=%d; max f=%.0f Hz, delta_Cu(min)=%.2f mm, F_R(max)=%.4f" % (ds*1e3, Ns, f.max(), delta(RHO['Cu'], f.max())*1e3, FR.max()))
for name, vc in cases.items():
    i10, i100 = np.argmin(abs(v-10)), -1
    say(f"  {name:32s} vc@10m/s={vc[i10]:6.2f} m/s  vc@100m/s={vc[i100]:6.2f}  L/D@100={v[-1]/vc[-1]:6.1f}  W/N@100={vc[-1]*(1):5.2f}  N/kW@100={1000/vc[-1]:6.0f}")
plt.figure(figsize=(7,4.5))
for name, vc in cases.items(): plt.plot(v, v/vc, label=name)
plt.xlabel("speed v (m/s)"); plt.ylabel("lift/drag L/D"); plt.title("Halbach EDS L/D vs speed (λ=10 cm)"); plt.grid(alpha=.3); plt.legend(fontsize=7)
plt.savefig(f"{OUT}/halbach_litz_LD_vs_speed.png", dpi=110, bbox_inches="tight"); plt.close()
plt.figure(figsize=(7,4.5))
for name, vc in cases.items():
    plt.plot(v, 1000/vc*lift_factor(v, vc)/(lift_factor(v,vc)), label=name)
plt.axhline(BASE, color="k", ls="--", label="POL baseline 52 N/kW")
plt.yscale("log"); plt.xlabel("speed v (m/s)"); plt.ylabel("N of lift per kW of magnetic drag power"); plt.grid(alpha=.3); plt.legend(fontsize=7)
plt.title("Magnetic drag only (drive/aero/motor losses excluded)")
plt.savefig(f"{OUT}/halbach_litz_N_per_kW.png", dpi=110, bbox_inches="tight"); plt.close()

# --- 3. lambda / hover gap / area needed
say("\n[3] Area of array needed to lift 863 N at v = 10*vc (lift factor 0.99), Cu litz eta=0.6, d=lambda/4, M=8, g=0.05. Grounded (model)")
for lam_ in (0.05, 0.10, 0.20, 0.40):
    row = []
    for y in (0.005, 0.010, 0.020, 0.030):
        P = P_inf(B0(Br, lam_, lam_/4, 8, 0.05), lam_, y)*0.99
        row.append(f"y={y*1e3:.0f}mm:{LOAD/P*1e4:7.1f}cm2")
    say(f"  lambda={lam_*100:3.0f}cm  " + " ".join(row))
say("  -> W/N is independent of gap and lambda in this model; gap and lambda set AREA and MAGNET MASS (lift ~ exp(-4 pi y/lambda)).")
ys = np.linspace(0.005, 0.03, 50)
plt.figure(figsize=(7,4.5))
for lam_ in (0.05, 0.1, 0.2, 0.4):
    plt.plot(ys*1e3, LOAD/(P_inf(B0(Br, lam_, lam_/4, 8, .05), lam_, ys))*1e4, label=f"λ={lam_*100:.0f} cm")
plt.yscale("log"); plt.xlabel("hover gap (mm)"); plt.ylabel("array area for 863 N (cm²)"); plt.grid(alpha=.3); plt.legend()
plt.savefig(f"{OUT}/halbach_litz_area_vs_gap.png", dpi=110, bbox_inches="tight"); plt.close()

# --- 4. electrodynamic wheel hover
say("\n[4] Electrodynamic-wheel hover (4 counter-rotating rotors, ro=0.10 m, width 0.10 m, active arc ro*pi/3,")
say("    lambda=2*pi*ro/P with P=4 pole pairs (lambda=15.7 cm), y=10 mm, M=8, g=0.05, conductor Cu litz eta=0.6, t=10 mm)")
ro, wdt, Prot, n = 0.10, 0.10, 4, 4
lamw = 2*np.pi*ro/Prot; Aact = n*wdt*ro*np.pi/3
Pm = P_inf(B0(Br, lamw, lamw/4, 8, .05), lamw, 0.010)
for vs in (5, 10, 20, 40, 60):
    fw = vs/lamw; vc = vc_litz(RHO["Cu"], 0.01, .6, litz_FR(RHO["Cu"], fw, ds, Ns))
    FL = Pm*Aact*lift_factor(vs, vc); FD = FL*vc/vs; Ps = FD*vs
    rpm = vs/ro*60/(2*np.pi)
    say(f"  vs={vs:3d} m/s ({rpm:6.0f} rpm): lift={FL:7.0f} N  drag={FD:6.0f} N  torque/rotor={FD*ro/n:5.1f} N·m  shaft P(magnetic)={Ps/1e3:6.2f} kW  N/kW={FL/Ps*1e3:6.0f}  (x{FL/Ps*1e3/BASE:4.1f} baseline)")
vc0 = vc_litz(RHO["Cu"], 0.01, .6)
say(f"  Need for 863 N: lift capacity {Pm*Aact:.0f} N > 863 N. At vs where lift = 863 N, P = 863*vc = {863*vc0/1e3:.2f} kW magnetic; with eta_motor=0.85 and +20% windage/bearing allowance: {863*vc0*1.2/0.85/1e3:.2f} kW -> {863/(863*vc0*1.2/0.85)*1e3:.0f} N/kW. Plausible-untested as hardware.")

# --- 5. drag levers ranked
say("\n[5] Drag levers (W/N = vc = 4 rho F_R/(mu0 t eta) for litz; 2 rho/(mu0 t_eff) plate):")
for lab, val in [("baseline Cu litz t=10mm eta=0.6", vc_litz(RHO['Cu'], .01, .6)),
                 ("t=20mm (more conductor depth)", vc_litz(RHO['Cu'], .02, .6)),
                 ("eta=0.8 (compact/rectangular litz)", vc_litz(RHO['Cu'], .01, .8)),
                 ("Al instead of Cu (same t)", vc_litz(RHO['Al'], .01, .6)),
                 ("Cu at 77 K (rho~0.2e-8, LN2)", vc_litz(0.2e-8, .01, .6)),
                 ("solid Cu plate t=10mm @ 10 m/s, lambda 10cm", vc_plate(RHO['Cu'], .01, 100.)),
                 ("solid Cu plate t=10mm @ 100 m/s", vc_plate(RHO['Cu'], .01, 1000.))]:
    say(f"  {lab:46s} vc = {val:5.2f} m/s -> {val:5.2f} W/N, {1000/val:6.0f} N/kW")
say("\nSeparation: everything above is MAGNETIC drag (eddy/I^2R heat). Drive power still needed: a moving craft must also supply")
say("aero drag and propulsion; a wheel hover must supply motor + windage + bearing losses and gyroscopic/thrust balancing.")
open(f"{OUT}/halbach_litz_drag_sim_output.txt", "w").write("\n".join(lines)+"\n")

#!/usr/bin/env python3
"""
Switched 45-degree Halbach arc (M = 8 segments per wavelength) with hybrid PM + switchable
litz trim/steer coil zones: mechanical, thermal, demagnetisation, switching-transient and
materials/cost check. License CC0.
Run: python3 sims/halbach_switched_arc_check.py -> sims/halbach_switched_arc_check_output.txt + PNGs

Approximations (stated):
 * Field and pressure: Halbach first harmonic B0 = Br(1-e^{-kd}) sin(pi(1-g)/M)/(pi/M) (Halbach 1980).
 * Inter-segment forces and internal reverse fields: 3-D magnetic surface-charge model of a straight
   M=8 array (charges sigma = Br/mu0 on faces normal to M; rigid, mu_r = 1 magnets; 16 segments, the
   middle 8 evaluated so end effects are reduced). An arc of 45 deg per segment on a large radius is
   treated as straight (radius >> segment).
 * Structure: retainer strip as simply-supported plate strip, sigma = 0.75 p L^2/t^2,
   deflection = 5 p L^4 /(32 E t^3).  Dynamic amplification for a step (hard switch) = 2;
   for a linear ramp of duration tr: DAF = 1 + |sin(pi tr/Tn)|/(pi tr/Tn).
 * Eddy loss in a magnet slab of thickness b in a uniform AC field Bac: thin-slab loss
   (pi f Bac b)^2/(6 rho) per volume, capped by the skin-limited surface loss Rs H^2/2.
 * Demag: knee approximated as HcJ(T) (NdFeB/SmCo/ferrite square loops); AlNiCo has no square
   loop, so its limit is taken as HcB (~HcJ); margin = HcJ(T) - |H_rev|.
Labels: model results Grounded (model); hardware Plausible-untested. Datasheet values are typical
(MMPA 0100-00; Arnold Magnetic Technologies & Electron Energy catalogues) and marked [to verify].
"""
import numpy as np, matplotlib, os
matplotlib.use("Agg"); import matplotlib.pyplot as plt
mu0 = 4e-7*np.pi; OUT = os.path.dirname(os.path.abspath(__file__)); LOG = []
def say(s=""): print(s); LOG.append(s)
lam, M, g = 0.10, 8, 0.05
wseg, hseg, dep = lam/M*(1-g), lam/4, 0.05     # segment along-array width, thickness, depth (m)
k = 2*np.pi/lam
say("Switched 45-deg Halbach arc check (CC0). lambda=10 cm, M=8 (45 deg steps), gap fraction 5 %%, segment %.1f x %.1f x %.0f mm" % (wseg*1e3, hseg*1e3, dep*1e3))

# ---------- 1. charge model
def seg_charges(i, Br, n=8):
    """surface charges for segment i (centre x_i), magnetisation angle i*45deg in x-z plane"""
    xc = i*lam/M; ang = i*2*np.pi/M; Mv = Br/mu0*np.array([np.cos(ang), 0, np.sin(ang)])
    pts, qs = [], []
    u = (np.arange(n)+0.5)/n - 0.5
    for ax, half, oth in ((0, wseg/2, (1, 2)), (2, hseg/2, (0, 1))):
        sizes = {0: wseg, 1: dep, 2: -hseg/2}
        for sgn in (1, -1):
            sig = Mv[ax]*sgn
            if abs(sig) < 1e-9: continue
            if ax == 0: A1, A2 = dep, hseg; P = [(xc+sgn*wseg/2, a*dep, -hseg/2 + (b+0.5)*hseg) for a in u for b in u]
            else:       A1, A2 = wseg, dep; P = [(xc+a*wseg, b*dep, sgn*hseg/2 - hseg/2) for a in u for b in u]
            dA = A1*A2/n**2
            pts += P; qs += [sig*dA]*len(P)
    return np.array(pts), np.array(qs)
def H_at(r, pts, qs):
    d = r - pts; R = np.linalg.norm(d, axis=1); R = np.maximum(R, 1e-4)
    return (qs[:, None]*d/(4*np.pi*R[:, None]**3)).sum(0)
Br = 1.30
segs = [seg_charges(i, Br, 16) for i in range(16)]
def pair_force(a, b):
    (pa, qa), (pb, qb) = a, b
    d = pa[:, None, :] - pb[None, :, :]; R = np.linalg.norm(d, axis=2)
    return mu0*(qa[:, None, None]*qb[None, :, None]*d/(4*np.pi*R[:, :, None]**3)).sum((0, 1))
def seg_forces(n):
    sg = [seg_charges(i, Br, n) for i in range(16)]
    return np.array([sum(pair_force(sg[i], sg[j]) for j in range(16) if j != i) for i in range(4, 12)])
conv = {}
for n_ in (10, 16, 22):
    conv[n_] = np.linalg.norm(seg_forces(n_), axis=1).max()
F = seg_forces(22); Fmag = np.linalg.norm(F, axis=1)
F_rich = (22**2*conv[22] - 16**2*conv[16])/(22**2 - 16**2)   # Richardson extrapolation assuming 1/n^2 error
say("\n[1] Mechanical (Grounded, model)")
B0 = Br*(1-np.exp(-k*hseg))*np.sin(np.pi*(1-g)/M)/(np.pi/M)
p0 = B0**2/(2*mu0)
say(f"  surface field B0={B0:.2f} T (N42-class Br {Br} T) -> magnetic pressure B0^2/2mu0 = {p0/1e6:.2f} MPa")
say(f"  inter-segment net force per segment (charge model, M=8): mean {Fmag.mean():.0f} N, peak {Fmag.max():.0f} N "
    f"(= {Fmag.max()/(wseg*dep)/1e6:.2f} MPa over the segment footprint, {Fmag.max()/(hseg*dep)/1e6:.2f} MPa over a side face)")
say("  convergence of peak force vs face grid n: " + ", ".join(f"n={a}: {b:.0f} N" for a, b in conv.items()) + " (not converged: grid spacing ~ the 0.6 mm gap)")
say(f"  Richardson estimate (1/n^2) of the converged peak: ~{F_rich:.0f} N; reference scale Br^2/2mu0 x side face = {Br**2/(2*mu0)*hseg*dep:.0f} N. Design value used: n=22 result {Fmag.max():.0f} N (conservative).")
say(f"  -> retainer must hold ~{Fmag.max():.0f} N per {wseg*1e3:.0f}x{dep*1e3:.0f} mm segment against ejection/slide; the 'push-out' segments alternate along the array.")
# coil zone trim: Bc on top of B0 at the surface
Bc = 0.15
dp_hard = ((B0+Bc)**2 - B0**2)/(2*mu0)
say(f"  coil trim zone Bc={Bc} T: pressure change {dp_hard/1e3:.0f} kPa per switching event (fraction {dp_hard/p0*100:.0f} % of static)")
# ramp: sin/cos blending keeps |B_trim| constant while steering (two zones in quadrature)
th = np.linspace(0, np.pi/2, 200)
p_ramp = ((B0+Bc*np.cos(th))**2 + (Bc*np.sin(th))**2 - B0**2)/(2*mu0)   # zone A in-phase, zone B quadrature
Tn = 1/800.0  # assumed first structural mode of retainer ~800 Hz
for tr in (0.0, 0.25e-3, 1e-3, 5e-3):
    daf = 2.0 if tr == 0 else 1 + abs(np.sin(np.pi*tr/Tn))/(np.pi*tr/Tn)
    say(f"  load step with ramp {tr*1e3:4.2f} ms (Tn={Tn*1e3:.2f} ms): dynamic amplification {daf:.2f} -> peak extra pressure {daf*dp_hard/1e3:.0f} kPa")
say("  sin/cos blending of adjacent zones (I_A = I cos th, I_B = I sin th) steers the trim-field angle with |B_trim| constant;")
say(f"  pressure swing during a 90-deg steer: {(p_ramp.max()-p_ramp.min())/1e3:.0f} kPa vs hard on/off of both zones {dp_hard/1e3:.0f} kPa (x2 dynamic)")
mats = {  # E (Pa), yield/strength (Pa), endurance fraction, density
    "Ti-6Al-4V": (114e9, 880e6, 0.50), "Al 7075-T6": (71.7e9, 503e6, 0.30), "G10/FR4": (18e9, 300e6, 0.30),
    "CFRP (quasi-iso)": (60e9, 600e6, 0.40), "mycelium composite (raw)": (5e6, 0.6e6, 0.3)}
Lspan, t = 0.05, 0.005
ptot = p0 + 2*dp_hard + Fmag.max()/(wseg*dep)
say(f"  retainer plate strip, span {Lspan*1e3:.0f} mm, t={t*1e3:.0f} mm, design pressure {ptot/1e6:.2f} MPa (static + hard-switch peak + inter-segment)")
for nme, (E, S, fe) in mats.items():
    sig = 0.75*ptot*Lspan**2/t**2; dfl = 5*ptot*Lspan**4/(32*E*t**3)
    say(f"   {nme:26s} stress {sig/1e6:7.1f} MPa vs strength {S/1e6:6.1f} (SF {S/sig:5.2f}; fatigue SF ~{fe*S/sig:4.2f}), deflection {dfl*1e3:9.3f} mm")
say("  mycelium composites: published compressive/flexural strength ~0.2-1.1 MPa (e.g. Jones et al. 2020, Mater. Des.) -> inadequate for magnet retention unless densified/hot-pressed.")

# ---------- 2. thermal
say("\n[2] Eddy heating in magnet segments at Tesla-coil frequencies (Grounded, model; ripple amplitude assumed)")
rhos = {"NdFeB (1.5 uOhm m)": 1.5e-6, "SmCo (0.8 uOhm m)": 0.8e-6}
fs = np.logspace(np.log10(5e4), 6, 60); h_conv = 50.0
def eddy(rho, f, Bac, b):
    dl = np.sqrt(rho/(np.pi*f*mu0))
    thin = (np.pi*f*Bac*b)**2/(6*rho)*b          # W per m^2 of face (slab thickness b)
    skin = (rho/dl)*(Bac/mu0)**2/2*2              # both faces
    return np.minimum(thin, skin), dl
A_face = wseg*dep; V = wseg*hseg*dep; A_cool = 2*(wseg*dep + hseg*dep + wseg*hseg)
fig, ax = plt.subplots(figsize=(7, 4.5))
for nm, rho in rhos.items():
    for b, lab in ((wseg, "solid"), (0.001, "1 mm laminations")):
        res = []
        for f in fs:
            q, dl = eddy(rho, f, 0.005, b)
            res.append(q*hseg*dep/(h_conv*A_cool))   # W per segment / (h A)
        ax.loglog(fs/1e3, res, label=f"{nm}, {lab}")
    for f in (1e5, 1e6):
        out = []
        for b, lab in ((wseg, "solid"), (0.001, "1 mm lam")):
            for Bac in (0.005, 0.02):
                q, dl = eddy(rho, f, Bac, b); P = q*hseg*dep
                out.append(f"{lab} Bac={Bac*1e3:.0f}mT: {P:7.2f} W, dT={P/(h_conv*A_cool):7.1f} K")
        say(f"  {nm} f={f/1e3:5.0f} kHz delta={np.sqrt(rho/(np.pi*f*mu0))*1e3:.2f} mm | " + " | ".join(out))
ax.set_xlabel("frequency (kHz)"); ax.set_ylabel("segment temperature rise (K), Bac=5 mT, h=50 W/m²K"); ax.grid(alpha=.3, which="both"); ax.legend(fontsize=7)
ax.set_title("Eddy heating of one magnet segment"); fig.savefig(f"{OUT}/halbach_arc_eddy_heating.png", dpi=110, bbox_inches="tight")
say("  NOTE: laminations must be cut perpendicular to the eddy-current loop (i.e. the stack normal along Bac's plane); thin-slab loss ~ b^2, so 1 mm vs 11.9 mm cuts loss ~140x until skin-limited.")
for f in (5e4, 1e5, 5e5, 1e6):
    dcu = np.sqrt(1.68e-8/(np.pi*f*mu0))
    say(f"  litz: f={f/1e3:5.0f} kHz Cu skin depth {dcu*1e3:.3f} mm -> strand diameter <= {dcu*1e3*0.5:.3f}-{dcu*1e3:.3f} mm (AWG ~{int(round(-39*np.log(dcu*0.75e3/0.127)/np.log(92)+36))})")

# ---------- 3. demag
say("\n[3] Demagnetisation margin (worst segment, charge-model reverse field + coil opposing field + temperature)")
Hrev = []
for i in range(4, 12):
    ang = i*2*np.pi/M; mhat = np.array([np.cos(ang), 0, np.sin(ang)])
    xc = i*lam/M
    worst = 0
    for corner in ((xc-wseg*0.35, 0, -0.15*hseg), (xc+wseg*0.35, 0, -0.15*hseg), (xc-wseg*0.35, 0, -0.85*hseg), (xc+wseg*0.35, 0, -0.85*hseg), (xc, 0, -hseg/2)):
        H = np.zeros(3)
        for j in range(16):
            pj, qj = segs[j]; H += H_at(np.array(corner), pj, qj)
        worst = min(worst, H @ mhat)
    Hrev.append(worst)
Hrev_T = -min(Hrev)*mu0/Br  # normalised: mu0*|H_rev| per tesla of Br
say(f"  worst internal reverse field (incl. self-demag, points 15 % in from corners): mu0*H = {Hrev_T:.2f} x Br")
Bcoil_rev = 0.15
mat = [ # name, Br(T), HcJ(kA/m), alpha_Br %/K, beta_HcJ %/K, Tmax C, Tc C, density, $/kg low-high, note
 ("N42", 1.30, 1000, -0.12, -0.60, 80, 310, 7.5, (40, 85)),
 ("N42SH", 1.30, 1590, -0.12, -0.55, 150, 340, 7.5, (45, 175)),
 ("N42UH", 1.29, 1990, -0.12, -0.50, 180, 350, 7.5, (50, 175)),
 ("N42EH", 1.28, 2390, -0.12, -0.50, 200, 350, 7.5, (55, 180)),
 ("Sm2Co17 (30 MGOe)", 1.10, 1990, -0.035, -0.25, 300, 820, 8.4, (150, 300)),
 ("SmCo5 (20 MGOe)", 0.90, 1990, -0.045, -0.30, 250, 720, 8.4, (150, 300)),
 ("AlNiCo 5", 1.25, 51, -0.02, 0.01, 525, 860, 7.3, (40, 90)),
 ("AlNiCo 8", 0.82, 150, -0.02, -0.01, 550, 860, 7.3, (50, 100)),
 ("Ferrite C8/Y30", 0.39, 240, -0.20, +0.27, 250, 450, 4.9, (8, 12)),
]
fig, ax = plt.subplots(figsize=(8, 4.5)); Ts = np.linspace(20, 200, 50)
for (nm, B, Hc, aB, bH, Tm, Tc, rho_, pr) in mat:
    marg = []
    for T in (20, 80, 120, 150):
        HcT = Hc*1e3*(1 + bH/100*(T-20)); BrT = B*(1 + aB/100*(T-20))
        Hr = (Hrev_T*BrT + Bcoil_rev)/mu0
        marg.append(f"{T}C: {(HcT-Hr)/1e3:+6.0f} kA/m ({'OK' if HcT > 1.2*Hr else ('MARGINAL' if HcT > Hr else 'DEMAG')})")
    say(f"  {nm:18s} Br {B:.2f} T HcJ {Hc:5d} kA/m Tmax {Tm:3d}C | " + " | ".join(marg))
    ax.plot(Ts, [(Hc*1e3*(1+bH/100*(T-20)) - (Hrev_T*B*(1+aB/100*(T-20))+Bcoil_rev)/mu0)/1e3 for T in Ts], label=nm)
ax.axhline(0, color="k"); ax.set_xlabel("magnet temperature (°C)"); ax.set_ylabel("margin HcJ(T) − |H_rev| (kA/m)"); ax.legend(fontsize=7); ax.grid(alpha=.3)
ax.set_title("Demag margin, worst Halbach segment + 0.15 T opposing coil field"); fig.savefig(f"{OUT}/halbach_arc_demag_margin.png", dpi=110, bbox_inches="tight")
say("  Pure nickel: soft ferromagnet (HcJ ~ 0.1 kA/m scale, Bs ~ 0.6 T): not a permanent magnet. Ni-Fe permalloy: soft back-iron/shield (Bs ~0.8-1.5 T).")

# ---------- 4. switching
say("\n[4] Switching transients (design level; Grounded circuit physics)")
Lc, I = 20e-6, 50.0
for tsw in (100e-9, 1e-6, 100e-6, 1e-3):
    say(f"  coil L={Lc*1e6:.0f} uH, I={I:.0f} A, current change in {tsw*1e6:8.2f} us -> L di/dt = {Lc*I/tsw:9.1f} V")
E_ = 0.5*Lc*I**2; Vclamp = 200.0; Cs = Lc*I**2/Vclamp**2; Rs = np.sqrt(Lc/Cs)
say(f"  stored energy 1/2 L I^2 = {E_*1e3:.0f} mJ per zone; RC snubber to clamp {Vclamp:.0f} V: C ~ {Cs*1e6:.2f} uF, R ~ {Rs:.1f} ohm (or TVS/flyback to bus)")
say("  creepage/clearance: IEC 60664-1 tables give roughly 5 mm creepage per kV rms (pollution degree 2, material IIIa) and ~1-1.5 mm clearance per kV")
say("  impulse in air (Paschen: ~3 kV/mm uniform field at 1 atm, less for sharp edges). A 1-2 mm insulating gap stands off a few hundred V to ~1 kV,")
say("  NOT Tesla-coil output (tens-hundreds of kV): keep switched trim zones on a low-voltage litz bus, galvanically separate from the Tesla secondary.")

# ---------- 5. cost / lift per dollar
say("\n[5] Field and lift per dollar for the 88 kg (863 N) hover array (assumptions: flat array, lambda=10 cm, d=lambda/4, gap 10 mm, lift factor 0.9)")
rows = []
for (nm, B, Hc, aB, bH, Tm, Tc, rho_, pr) in mat:
    B0m = B*(1-np.exp(-k*hseg))*np.sin(np.pi*(1-g)/M)/(np.pi/M)
    P = (B0m*np.exp(-k*0.010))**2/(2*mu0)*0.9
    A = 863/P; mass = A*hseg*rho_*1000*(1-g)
    lo, hi = pr
    rows.append((nm, B0m, A, mass, mass*lo, mass*hi))
    say(f"  {nm:18s} B0={B0m:.2f} T  area {A*1e4:7.0f} cm2  magnet mass {mass:6.2f} kg  cost ${mass*lo:7.0f}-{mass*hi:7.0f}  lift/$ {863/(mass*hi):6.2f}-{863/(mass*lo):6.2f} N/$  B0 per $/kg-of-magnet {B0m/((lo+hi)/2):.4f} T/($/kg)")
say("  (AlNiCo rows are not usable in a Halbach: they demagnetise; shown for cost only.)")
open(f"{OUT}/halbach_switched_arc_check_output.txt", "w").write("\n".join(LOG)+"\n")

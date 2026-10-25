"""Marklund convection toy model: Saha recombination radii of species drifting inward in a
force-free (Lundquist) flux tube with a hot rim and a cool core (CC0).

Marklund, Nature 277:370 (1979). All numbers are MODEL OUTPUTS for assumed profiles.
Saha (single stage, fixed n_e): n_i/n_0 = 2.415e21 T^1.5 (2 g_i/g_0) exp(-chi/kT) / n_e
Statistical-weight ratio set to 1 (order-of-magnitude), LTE assumed (not valid in the real corona).
Outputs: sims/marklund_convection_sim_output.txt, docs/images/marklund_*.png
"""
import numpy as np, matplotlib, os
from scipy.special import j0, j1
matplotlib.use("Agg"); import matplotlib.pyplot as plt
here = os.path.dirname(os.path.abspath(__file__)); img = os.path.join(here, "..", "docs", "images")
os.makedirs(img, exist_ok=True); out = []
def say(s=""): print(s); out.append(s)
kB = 8.617e-5   # eV/K
FIP = {"K": 4.341, "Na": 5.139, "Fe": 7.902, "Si": 8.152, "C": 11.260, "H": 13.598, "O": 13.618, "N": 14.534, "He": 24.587}  # NIST, eV

def ion_frac(T, ne, chi):
    S = 2.415e21*T**1.5*np.exp(-chi/(kB*T))/ne
    return S/(1+S)

cases = {
  "a": dict(name="(a) coronal-loop-like", a=1e6, ne=1e15, Tc=3e3, Tr=1e5, B0=1e-2, E=10.0,
            nn=1e14, sig=1e-19, mass=4*1.67e-27),
  "b": dict(name="(b) lab / RGRF bench (Tesla-coil plasma)", a=0.02, ne=1e19, Tc=1.16e3, Tr=5*1.16e4, B0=0.05, E=100.0,
            nn=1e21, sig=1e-19, mass=4*1.67e-27),
}
fig, axs = plt.subplots(1, 2, figsize=(11, 4.5))
for ax, (key, p) in zip(axs, cases.items()):
    a = p["a"]; r = np.linspace(0, a, 4001)
    T = p["Tc"] + (p["Tr"]-p["Tc"])*(r/a)**2
    alpha = 2.405/a                                # first zero of J0 at the rim
    Bz, Bth = p["B0"]*j0(alpha*r), p["B0"]*j1(alpha*r)
    Bmag = np.sqrt(Bz**2+Bth**2)
    say(f"\n{p['name']}: a = {a:g} m, n_e = {p['ne']:.0e} m^-3, T core {p['Tc']*kB:.2f} eV -> rim {p['Tr']*kB:.2f} eV, B0 = {p['B0']} T")
    say(f"  Lundquist field: |B| from {Bmag.max():.3g} T (axis) to {Bmag[-1]:.3g} T (rim), force-free J = alpha B with alpha = {alpha:.3g} 1/m")
    rad = {}
    for sp, chi in FIP.items():
        x = ion_frac(T, p["ne"], chi)
        i = np.where(x >= 0.5)[0]
        rad[sp] = r[i[0]] if len(i) else np.nan
        ax.plot(r/a, x, label=f"{sp} ({chi:.1f} eV)")
    order = sorted(rad, key=lambda s: -rad[s])
    say("  stopping radius (50 % ionised), outermost -> innermost:")
    for sp in order: say(f"    {sp:2s}  r = {rad[sp]/a:.3f} a  ({rad[sp]:.3g} m)  T = {(p['Tc']+(p['Tr']-p['Tc'])*(rad[sp]/a)**2)*kB:.3f} eV")
    # timescales
    vd = p["E"]/Bmag.mean(); t_drift = a/vd
    Tmid = 0.5*kB*(p["Tc"]+p["Tr"])/1.0
    alpha_rr = 4e-19*(max(Tmid, 0.05))**-0.7          # m^3/s radiative (approx)
    T3 = 0.3*kB*p["Tr"]                               # ~ layer temperature for 3-body
    alpha_3 = 8.75e-39*T3**-4.5*p["ne"]               # m^3/s effective three-body
    t_rec = 1/((alpha_rr+alpha_3)*p["ne"])
    lam = 1/(p["nn"]*p["sig"]); vth = np.sqrt(8*1.6e-19*Tmid/(np.pi*p["mass"]))
    D = vth*min(lam, a)/3; t_diff = a**2/D; Ldiff = np.sqrt(D*t_rec)
    spacing = np.nanmin(np.abs(np.diff(sorted([rad[s] for s in order if s not in ("O",)]))))
    say(f"  timescales: drift a/(E/B) = {t_drift:.3g} s; recombination = {t_rec:.3g} s; neutral diffusion a^2/D = {t_diff:.3g} s")
    say(f"  neutral diffusion length during recombination sqrt(D t_rec) = {Ldiff:.3g} m = {Ldiff/a:.3g} a; smallest layer gap (excl. H/O pair) = {spacing/a:.3g} a")
    say("  -> layering " + ("SURVIVES (diffusion length < layer gap)" if Ldiff < spacing else "WASHED OUT (neutrals diffuse farther than the layer spacing before/after recombining)"))
    ax.set_title(p["name"], fontsize=9); ax.set_xlabel("r / a  (core 0, hot rim 1)"); ax.set_ylabel("ionisation fraction (Saha)")
axs[0].legend(fontsize=7)
fig.tight_layout(); fig.savefig(os.path.join(img, "marklund_ionisation_profiles.png"), dpi=120); plt.close(fig)

# layering diagram for case a
p = cases["a"]; a = p["a"]; r = np.linspace(0, a, 4001); T = p["Tc"]+(p["Tr"]-p["Tc"])*(r/a)**2
fig, ax = plt.subplots(figsize=(5.5, 5.5)); th = np.linspace(0, 2*np.pi, 300)
rad = {}
for sp, chi in FIP.items():
    x = ion_frac(T, p["ne"], chi); rad[sp] = r[np.where(x >= 0.5)[0][0]]/a
for k, sp in enumerate(sorted(rad, key=lambda s: -rad[s])):
    ax.plot(rad[sp]*np.cos(th), rad[sp]*np.sin(th), lw=2, label=f"{sp}: {rad[sp]:.2f} a")
ax.set_aspect("equal"); ax.legend(fontsize=8, loc="upper right"); ax.set_title("Marklund layering, case (a): He outermost, K/Na innermost")
fig.savefig(os.path.join(img, "marklund_layering.png"), dpi=120); plt.close(fig)

# ion-wind rerun (Grok example in alcubierre review: I = 1 mA, V = 50 kV)
mu = 2e-4
say("\nIon-wind rerun (Grok-reported example: I = 1 mA, V = 50 kV, claimed ~0.5 N):")
for d in (0.02, 0.05):
    F = 1e-3*d/mu; say(f"  F = I d / mu = {F:.3f} N at d = {d*100:.0f} cm (mu = 2e-4 m^2/Vs) -> {F/50*1e3:.1f} N/kW")
open(os.path.join(here, "marklund_convection_sim_output.txt"), "w").write("\n".join(out)+"\n")

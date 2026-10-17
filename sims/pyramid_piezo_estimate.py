#!/usr/bin/env python3
"""
Honest order-of-magnitude estimate: piezoelectric output of quartz in granite
(CC0, RGRF). It rechecks the numbers Grok gave in "Electric Universe Ley Line
Docking Station" (2026-10-17): ~22 kV and ~2.5 W per "1 m quartz block".

Model: a 1 m x 1 m x 1 m block, used as a piezo element with electrodes on two faces.
  V_oc = g * t * sigma                 (open-circuit voltage)
  C    = eps0 * eps_r * A / t          (the element's own capacitance)
  Source = V_oc in series with C (Thevenin form). Max average power into a
  matched resistor R = 1/(omega C) is P_max = V_oc^2 * omega * C / 4.
Grok treated the piezo as an ideal voltage source. That ignores the ~100s of
MOhm source impedance at a few Hz, and it is why its "W per block" figures are
too high even on its own inputs.

Quartz: d11 = 2.3 pC/N, eps_r ~ 4.5 (so g11 = d11/(eps0 eps_r) ~ 0.058 V m/N).
Quartz (class 32) has d11 and d14 but no "d33". Grok's "g33 = 0.057" is the g11 value.
Bulk granite: grains are randomly oriented, so the net effect is a statistical
residue. A measured apparent coefficient is ~1.4e-15 C/N, ~1e-3 of single
crystal (GRL 1998, doi:10.1029/98GL51179). Bishop (1981) found <= ~1 %, and
Tuck et al. (1977) found no reliable signal (<~100 mV). We use factors 1e-3
and 1e-2.
"""
import numpy as np

EPS0 = 8.854e-12
d11, eps_r = 2.3e-12, 4.5
g = d11 / (EPS0 * eps_r)
A, t = 1.0, 1.0
C = EPS0 * eps_r * A / t


def report(label, sigma, f, factor=1.0, R=None):
    V = g * factor * t * sigma
    w = 2 * np.pi * f
    Xc = 1 / (w * C)
    Pmax = V**2 * w * C / 4
    line = f"{label:58s} sigma={sigma:9.3g} Pa  V_oc={V:9.3g} V  Xc={Xc/1e6:7.0f} MOhm  P_max={Pmax:9.3g} W"
    if R is not None:
        I = V / np.hypot(R, Xc)
        line += f"  P(R={R/1e6:.0f}M)={I**2*R/2:9.3g} W"
    print(line)
    return V, Pmax


print(f"g11 = {g:.4f} V m/N ; C(1 m^3 block) = {C*1e12:.1f} pF\n")
print("A. Grok's own inputs (5 um over 1 m -> strain 5e-6, quartz Y = 78.7 GPa), ideal aligned single crystal:")
s_grok = 78.7e9 * 5e-6
report("  16.4 Hz", s_grok, 16.4, R=100e6)
report("  7.83 Hz", s_grok, 7.83, R=100e6)
print("  Grok reported: 20,520-22,430 V; 2.1-2.5 W at 100 MOhm; 0.43 W 'matched' (the 0.43 W is right at 16.4 Hz).")
print("  Grok's 'ideal source' figure would be V^2/(2R) =", f"{(g*t*s_grok)**2/(2*100e6):.2f} W at 100 MOhm, ignoring Xc.\n")

print("B. Same strain, real granite (random grains):")
for fac in (1e-2, 1e-3):
    report(f"  7.83 Hz, granite factor {fac:g}", s_grok, 7.83, factor=fac)

print("\nC. Realistic ambient drive. Ground velocity ~1e-7 to 1e-6 m/s at ~8 Hz [to verify site noise],")
print("   strain = v / c_p (c_p ~ 5000 m/s), stress = E_granite * strain (E ~ 50 GPa):")
for v in (1e-7, 1e-6):
    eps = v / 5000
    sig = 50e9 * eps
    report(f"  v={v:g} m/s, eps={eps:.1e}, granite factor 1e-3", sig, 7.83, factor=1e-3)

print("\nD. 528 Hz acoustic drive in the chamber air, p = 1-10 Pa on 1 m^2 of wall:")
for p in (1, 10):
    # Pressure on the wall gives stress ~p. Upper bound: aligned single crystal.
    _, P = report(f"  p={p} Pa, aligned single crystal (upper bound)", p, 528)
    I_ac = p**2 / (2 * 1.2 * 343)
    print(f"      incident acoustic intensity p^2/(2 rho c) = {I_ac:.3g} W/m^2  (Grok claimed 0.8-12 W per resonator)")

V_c = g * 1e-3 * t * (50e9 * 1e-6 / 5000)
P_c = V_c**2 * 2 * np.pi * 7.83 * C / 4
print(f"\nE. Scale: even 1e4 m^3 of granite at case C (upper) gives {1e4 * P_c:.2g} W total.")

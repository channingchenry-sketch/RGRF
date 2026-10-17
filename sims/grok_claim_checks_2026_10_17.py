# SPDX-License-Identifier: CC0-1.0
# Resona-authored checks (2026-10-17) of numerical claims in Grok shares 16-21.
# Each block is a short, standard-physics calculation. Nothing here is a Grok result.
# Run: python3 sims/grok_claim_checks_2026_10_17.py
import numpy as np
mu0 = 4e-7 * np.pi; c = 299792458.0; g = 9.81
phi = (1 + 5 ** 0.5) / 2

def skin(rho, f, mur=1.0):
    return np.sqrt(2 * rho / (2 * np.pi * f * mu0 * mur))

print("== Share 17: Geodesic Organic Design ==")
L = 636e-6; f = 13.56e6
C = 1 / ((2 * np.pi * f) ** 2 * L)
print(f"resonance_calc claim 636 uH at 13.56 MHz needs C = {C*1e12:.3f} pF (coil self-capacitance is typically pF to tens of pF,"
      f" so the coil self-resonates below 13.56 MHz)")
for Cp in (2e-12, 10e-12):
    print(f"   self-resonance with {Cp*1e12:.0f} pF parasitic: {1/(2*np.pi*np.sqrt(L*Cp))/1e6:.2f} MHz")
print(f"rgrf_scaler radius 26.18 m = 10*phi^2 = {10*phi**2:.2f} m (phi put in by construction)")
print(f"Al skin depth at 1 Hz (heartbeat): {skin(2.65e-8, 1.0)*100:.1f} cm; at 1 kHz: {skin(2.65e-8, 1e3)*1000:.2f} mm")

print("\n== Share 18: Tungsten Toroid ==")
for OD in (0.45, 0.60):
    for d in (0.08, 0.12):
        R = (OD - d) / 2; r = d / 2
        V = 2 * np.pi ** 2 * R * r ** 2; A = 4 * np.pi ** 2 * R * r
        print(f"OD {OD*100:.0f} cm, tube {d*100:.0f} cm: R/r = {R/r:.2f}; solid W torus {V*19250:.0f} kg;"
              f" shell for 5-8 kg = {5/(19250*A)*1000:.2f}-{8/(19250*A)*1000:.2f} mm")
print(f"phi would need OD/d = {phi+1:.3f}")
tt = np.linspace(0, 1, 9)
B1 = np.stack([np.cos(2*np.pi*tt), np.sin(2*np.pi*tt)])      # right-handed rotating field
B2 = np.stack([np.cos(2*np.pi*tt), -np.sin(2*np.pi*tt)])     # equal, opposite-handed
S = B1 + B2
print("equal counter-rotating fields: sum By =", np.round(S[1], 12).tolist(), "-> the sum is a linear field 2B cos(wt) along x")
print(f"Magnetic pressure B^2/(2 mu0) at 1 T = {1/(2*mu0)/1e3:.0f} kPa")

print("\n== Share 19: Floquet Engineering ==")
T = 0.1; f0 = 196.0
for amp in (0.05, 0.06):
    tt = np.linspace(0, T, 200001)
    B = 1 + amp * np.sin(2 * np.pi * f0 * tt)
    an = amp * (1 - np.cos(2 * np.pi * f0 * T)) / (2 * np.pi * f0 * T)
    print(f"1 T + {amp*100:.0f}% at 196 Hz over 0.1 s ({f0*T:.1f} cycles): mean = {B.mean():.5f} T (analytic offset {an:.2e});"
          f" over 0.1020408 s (20 cycles): {np.mean(1+amp*np.sin(2*np.pi*f0*np.linspace(0,20/f0,200001))):.5f} T")
dT = 0.5
for name, k in (("NdFeB", -0.0012), ("ferrite", -0.002), ("SmCo", -0.00035)):
    print(f"  +/-{dT} K on a permanent magnet ({name}, {k*100:.3f} %/K): +/-{abs(k)*dT*1e3:.2f} mT per tesla")
print(f"Al skin depth: 196 Hz {skin(2.65e-8,196)*1000:.2f} mm; 13.56 MHz {skin(2.65e-8,13.56e6)*1e6:.1f} um")
print(f"wavelength at 196 Hz: {c/196/1e3:.0f} km (a 'cavity' at this frequency is a lumped LC, not a resonant cavity)")
w = 2*np.pi*196
print(f"induced E ~ w B r/2 with B = 1.12 T, r = 0.1 m: {w*1.12*0.1/2:.0f} V/m; r needed for 1.24e5 V/m: {2*1.24e5/(w*1.12):.0f} m")
print(f"hbar*Omega at 196 Hz = {6.582e-16*w:.1e} eV (far below any electronic band scale)")
W = 1 / (2 * mu0) * 1e-3
print(f"1 T in 1 L stores {W:.0f} J; at Q = 450 the drive must supply w W / Q = {w*W/450:.0f} W")
p_rad = 100.0; rho_air = 1.2; cs = 343.0
prms = np.sqrt(p_rad * rho_air * cs**2)
print(f"100 Pa acoustic radiation pressure needs p_rms ~ {prms:.0f} Pa = {20*np.log10(prms/20e-6):.0f} dB SPL")
for name, rho, chi in (("bismuth", 9780, -1.66e-4), ("pyrolytic graphite", 2200, -4.5e-4)):
    print(f"diamagnetic levitation of {name}: B dB/dz >= {mu0*rho*g/abs(chi):.0f} T^2/m")

print("\n== Share 20: E8 Gradients ==")
import itertools
roots = set()
for i, j in itertools.combinations(range(8), 2):
    for si in (1, -1):
        for sj in (1, -1):
            v = [0]*8; v[i] = si; v[j] = sj; roots.add(tuple(float(x) for x in v))
for signs in itertools.product((0.5, -0.5), repeat=8):
    if sum(1 for s in signs if s < 0) % 2 == 0:
        roots.add(signs)
print(f"E8 roots counted: {len(roots)}; dim E8 = roots + rank = {len(roots)+8}")
print(f"sum_k phi^-k (k = 0..inf) = {sum(phi**-k for k in range(200)):.4f} = phi^2 = {phi**2:.4f}")
print(f"4 + phi^3 with phi = 1/1.618: {4+(1/phi)**3:.3f}; with phi = 1.618: {4+phi**3:.3f}")
a = 6.371e6
print(f"ideal Schumann f1 = c/(2 pi a) sqrt(2) = {c/(2*np.pi*a)*np.sqrt(2):.1f} Hz (observed ~7.8 Hz, lossy cavity)")

print("\n== Share 21: Uniphysics ==")
for n2, nm in ((1.0, "air"), (1.5, "glass"), (1.33, "n=1.33")):
    s = phi*np.sin(np.radians(45))/n2
    print(f"Snell n1 = phi, 45 deg -> {nm}: sin(theta2) = {s:.3f} -> " + ("total internal reflection" if s > 1 else f"{np.degrees(np.arcsin(s)):.2f} deg"))
print(f"critical angle phi -> air: {np.degrees(np.arcsin(1/phi)):.2f} deg")
print(f"dovetail dims for 300 mm: 300/phi = {300/phi:.1f}, 300/phi^2 = {300/phi**2:.1f}, 300/phi^2.5 = {300/phi**2.5:.1f} mm")
print(f"flank angle implied by base 185.4, top 114.6, height 114.6: {np.degrees(np.arctan((185.4-114.6)/2/114.6)):.1f} deg (Grok said ~14 deg);"
      " a tab whose tip is narrower than its root does not lock")
print(f"binaural: 639 Hz and 639 - 7.83 = {639-7.83:.2f} Hz give a {7.83:.2f} Hz beat; 631 Hz is a carrier, not the beat")
mp, mpi = 938.272, 139.570
Tth = ((2*mp + mpi)**2 - 2*mp**2) / (2*mp) - mp   # threshold kinetic energy, p + p(at rest) -> p n pi+
print(f"pion production threshold, proton on proton at rest: T ~ {Tth:.0f} MeV (a 'few MeV' cyclotron cannot make muons)")
DH = 1.56e-4
print(f"natural D/H ~ {DH:.2e} (VSMOW): about {1/(DH*2*2.014/18.015):.0f} kg of water per kg of deuterium, plus isotope enrichment")

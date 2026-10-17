# SPDX-License-Identifier: CC0-1.0
"""Arithmetic checks of numbers Grok quoted in share #86 (e3f85fa0),
"Tesla Tower Waveguide Atmospheric Charge" (2026-10-17).

No code was shown in the conversation, so nothing could be rerun. These are
independent order-of-magnitude checks of the stated numbers. CC0-1.0.
Run: python3 sims/grok_claim_checks_share_86.py
"""
import math

MU0 = 4e-7 * math.pi
C = 2.998e8
EV = 1.602e-19

print("== msg 2: fair-weather field fit E(z) = 93.8 e^-4.527z + 44.4 e^-0.375z + 11.8 e^-0.121z (V/m, z km) ==")
def E(z):
    return 93.8 * math.exp(-4.527 * z) + 44.4 * math.exp(-0.375 * z) + 11.8 * math.exp(-0.121 * z)
for z in (0, 1, 2, 10, 30):
    print(f"  z = {z:3d} km -> |E| = {E(z):8.3f} V/m")
# potential = integral of E dz (km -> m)
def V(z):
    return 1e3 * (93.8 / 4.527 * (1 - math.exp(-4.527 * z)) + 44.4 / 0.375 * (1 - math.exp(-0.375 * z))
                  + 11.8 / 0.121 * (1 - math.exp(-0.121 * z)))
for z in (10, 15, 60):
    print(f"  potential 0->{z} km = {V(z)/1e3:6.1f} kV")
print(f"  fraction of the 0-60 km drop below 15 km = {V(15)/V(60):.2f}")
print("  -> E(10 km) ~4.6 V/m and E(30 km) ~0.3 V/m (matches Grok's '~4-5' and 'a few tenths'). The fit")
print("     integrates to ~237 kV, the right order for the 250-300 kV ionospheric potential; ~93 % of it is below 15 km.")

print("\n== msg 4: ion-pair floor power, q = alpha n^2, P = q * 34 eV ==")
alpha, q0 = 1.6e-6, 10.0  # cm^3/s, cm^-3 s^-1
n0 = math.sqrt(q0 / alpha)
print(f"  steady n0 = sqrt(q/alpha) = {n0:.0f} cm^-3")
vol = math.pi * 20**2 * 2000  # m^3, 2 km x 20 m radius
for F in (10, 100, 1000):
    n = F * n0
    q = alpha * n**2                       # cm^-3 s^-1
    P = q * 1e6 * 34 * EV                   # W/m^3
    tau = 1 / (alpha * n)
    print(f"  F={F:5d}: n={n:.2e} cm^-3, q={q:.2e} cm^-3 s^-1, lifetime={tau:6.2f} s, P={P:.2e} W/m^3,"
          f" corridor (2 km x r 20 m) = {P*vol:.3g} W")
print("  -> Grok's floor numbers (5 nW, 0.5 uW, 55 uW per m^3; ~0.14 kW corridor) reproduce.")

print("\n== msg 4: ELF skin depth delta = sqrt(2/(omega mu0 sigma)) at 7.83 Hz ==")
f = 7.83
for name, s in (("crust 0.001 S/m", 1e-3), ("wet soil 0.01", 1e-2), ("aquifer 0.05", 5e-2), ("seawater 4", 4.0)):
    d = math.sqrt(2 / (2 * math.pi * f * MU0 * s))
    print(f"  {name:18s} -> {d/1e3:6.2f} km")

print("\n== msg 4: rod-electrode resistance R = rho/(2 pi L) [ln(4L/a) - 1], L = 100 m, a = 5 cm ==")
for rho in (20, 1000, 10000):
    L, a = 100.0, 0.05
    R = rho / (2 * math.pi * L) * (math.log(4 * L / a) - 1)
    print(f"  rho = {rho:6d} ohm m -> R = {R:7.2f} ohm")
print("  -> 20 ohm m gives ~0.25 ohm (Grok 'order 0.3 ohm'). Dry sand at 1e3-1e4 ohm m gives ~13-130 ohm.")

print("\n== msg 4: ideal Schumann f_n = c/(2 pi R) sqrt(n(n+1)) ==")
R_E = 6.371e6
for n in (1, 2, 3):
    print(f"  n={n}: {C/(2*math.pi*R_E)*math.sqrt(n*(n+1)):5.2f} Hz")

print("\n== msg 6: aerosol attachment with beta*Z values implied by Grok's table ==")
for Z, bZ in ((200, 4e-4), (1000, 2e-3), (3000, 7.5e-3), (6000, 1.8e-2), (12000, 3.6e-2)):
    # alpha n^2 + bZ n - q = 0
    n = (-bZ + math.sqrt(bZ**2 + 4 * alpha * q0)) / (2 * alpha)
    print(f"  Z={Z:6d}, beta*Z={bZ:.1e} s^-1 -> n = {n:6.0f} cm^-3 (implied beta = {bZ/Z:.1e} cm^3/s)")
print("  flush time 20 m / 3 m/s =", round(20 / 3, 1), "s")

print("\n== msg 24: Saturn north-polar jet as a Gaussian ==")
OMEGA, RS = 1.64e-4, 5.82e7   # s^-1 ; mean radius m (equatorial 6.03e7)
lat = math.radians(75.8)
U0, FWHM, b = 104.0, 2275e3, 8.0e-11
sigma_fwhm = FWHM / (2 * math.sqrt(2 * math.log(2)))
sigma_b = math.sqrt(U0 / b)
beta = 2 * OMEGA * math.cos(lat) / RS
fcor = 2 * OMEGA * math.sin(lat)
be = beta + b
lam = 2 * math.pi * math.sqrt(U0 / be)
Ccirc = 2 * math.pi * RS * math.cos(lat)
print(f"  sigma from FWHM = {sigma_fwhm/1e3:.0f} km; sigma from b = sqrt(U0/b) = {sigma_b/1e3:.0f} km")
print(f"  planetary beta = {beta:.2e} m^-1 s^-1; f = {fcor:.2e} s^-1; Ro = U0/(f sigma_b) = {U0/(fcor*sigma_b):.2f}")
print(f"  crest beta_e = {be:.2e}; lambda_s = 2 pi sqrt(U0/beta_e) = {lam/1e6:.2f} Mm")
print(f"  latitude circle C = 2 pi R cos(lat) = {Ccirc/1e7:.2f} x 10^7 m; n = C/lambda_s = {Ccirc/lam:.1f}")
lam6 = Ccirc / 6
print(f"  lambda_6 = {lam6/1e7:.2f} x 10^7 m; beta_e needed = 4 pi^2 U0 / lambda_6^2 = {4*math.pi**2*U0/lam6**2:.2e}")
print(f"  sigma_eff = sqrt(U0/beta_e_needed) = {math.sqrt(U0/(4*math.pi**2*U0/lam6**2))/1e3:.0f} km")
print("  -> Grok's n ~ 13, beta_e(n=6) ~ 1.7e-11 and sigma_eff ~ 2500 km reproduce to ~10 % (Grok's C = 9.4e7 m")
print("     implies the equatorial radius; the mean radius gives 9.0e7 m). Crest curvature b is ~58x planetary beta.")

print("\n== msg 4: stored Schumann-band energy at 1 mV/m (electric + equal magnetic share) ==")
EPS0 = 8.854e-12
h = 60e3  # m, effective cavity height
vol_cav = 4 * math.pi * R_E**2 * h
u = EPS0 * (1e-3)**2 / 2
print(f"  cavity volume ~ {vol_cav:.2e} m^3; electric energy ~ {u*vol_cav:.0f} J; x2 for magnetic ~ {2*u*vol_cav:.0f} J")
print("  -> 'only hundreds of joules' is the right order.")

print("\n== msg 20: hexagon drift 0.036 m/s (Sanchez-Lavega 2014) in deg/day at 75.8 N ==")
drift = 0.036 * 86400 / Ccirc * 360
print(f"  {drift:.4f} deg/day  (Grok quoted '~0.06 deg/day' as the observed drift)")

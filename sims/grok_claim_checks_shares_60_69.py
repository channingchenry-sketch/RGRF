# SPDX-License-Identifier: CC0-1.0
"""Arithmetic checks of numbers Grok quoted in shares #60-#69 (2026-10-17).

No code was shown in any of these ten conversations, so nothing could be rerun.
These are independent order-of-magnitude checks of stated numbers. CC0-1.0.
Run: python3 sims/grok_claim_checks_shares_60_69.py
"""
import math

MU0 = 4e-7 * math.pi
EPS0 = 8.854e-12
C = 2.998e8
G = 9.81

print("== #61 hemp oil: dielectric charge-relaxation time tau = eps/sigma ==")
for sigma in (1e-13, 1e-12, 1e-11):  # S/m, i.e. 0.1-10 pS/m
    print(f"  eps_r=3, sigma={sigma*1e12:5.1f} pS/m -> tau = {3*EPS0/sigma:8.1f} s")

print("\n== #62 aluminium skin depth delta = sqrt(rho/(pi f mu0)) ==")
RHO_AL = 2.65e-8  # ohm m, 20 C
for f in (60, 1e3, 1e5, 1e6, 2.45e9):
    d = math.sqrt(RHO_AL / (math.pi * f * MU0))
    print(f"  f = {f:10.3g} Hz -> delta = {d*1e6:10.2f} um")
lam = C / 2.45e9
print(f"  2.45 GHz free-space wavelength = {lam*100:.2f} cm; lambda/10 = {lam*1000/10:.1f} mm, lambda/20 = {lam*1000/20:.1f} mm")

print("\n== #66 magnetic tension B^2/(mu0 Rc) vs magnetic pressure B^2/(2 mu0) ==")
for B, Rc in ((0.1, 0.05), (1.0, 0.5)):
    print(f"  B={B} T, Rc={Rc} m -> tension {B**2/(MU0*Rc):.3g} N/m^3, pressure {B**2/(2*MU0):.3g} Pa")

print("\n== #68 Meyer-cell numbers ==")
v, gap = 600.0, 1.587e-3
print(f"  600 m/s / 1.587 mm = {v/gap/1e3:.0f} kHz  (the 600 m/s velocity is an assumption, not a measured property)")
for f in (40e3, 145e3, 378e3, 400e3):
    print(f"  f = {f/1e3:5.0f} kHz: EM wavelength in vacuum = {C/f/1e3:6.2f} km;"
          f" acoustic wavelength in water (1480 m/s) = {1480/f*1e3:6.2f} mm")
print("  -> EM wavelength at 40-400 kHz is 0.75-7.5 km, not 'tens of km'.")
GIBBS = 237.1e3  # J/mol H2O at 25 C
print(f"  Gibbs minimum to split water: {GIBBS/1e3:.1f} kJ/mol -> reversible cell voltage {GIBBS/(2*96485):.3f} V")

print("\n== #69 helium diamagnetic force vs its own weight and buoyancy ==")
CHI_HE = -1.07e-9  # SI volume susceptibility of He gas at STP (molar -1.9e-6 cm^3/mol, CGS)
RHO_HE = 0.1786    # kg/m^3 at STP
for B, gradB in ((1, 10), (10, 100)):
    f_mag = abs(CHI_HE) / MU0 * B * gradB
    print(f"  B={B} T, dB/dz={gradB} T/m -> |f_mag| = {f_mag:.3g} N/m^3 vs He weight {RHO_HE*G:.3g} N/m^3"
          f" and air-He buoyancy {(1.225-RHO_HE)*G:.3g} N/m^3")
print("  -> diamagnetic 'repulsion' of helium is negligible at lab fields.")

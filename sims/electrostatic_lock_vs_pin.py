#!/usr/bin/env python3
"""
Electrostatic locking vs. mechanical lock pins: order-of-magnitude check (CC0).

Companion to docs/electrostatic_locking_pins.md (rebuilt "Electrostatic locking
linch pins" section, Grok share 9a31b5c7, 2026-10-17).

Grok proposed "hybrid electro-mechanical locking": barbed BN pins engage
mechanically and "electrostatic fields provide rigid, vibration-resistant
clamping". This script asks how much clamping electrostatics can give per unit
area, and how that compares with one ordinary pin.

Physics (Grounded):
  Electrostatic (Maxwell) pressure on a conductor/dielectric boundary with field E
  in a medium of relative permittivity eps_r:      P = eps0 * eps_r * E^2 / 2
  In real electroadhesion the holding force acts across the microscopic AIR gaps
  between rough surfaces, so the useful number is P = eps0 * E_gap^2 / 2 with
  E_gap capped by gas breakdown (Paschen), not by the solid dielectric.
  Friction lock (shear) from a normal clamp:        F_shear = mu * P * A
  Pin in single shear:                               F = tau_allow * pi d^2 / 4

All inputs are textbook / datasheet-level values; ranges are noted in the doc.
No phi or resonance parameter appears because none changes these limits.
"""
import math

EPS0 = 8.8541878128e-12  # F/m

def p_es(E, eps_r=1.0):
    """Electrostatic pressure in Pa for field E (V/m) in medium eps_r."""
    return 0.5 * EPS0 * eps_r * E**2

cases = [
    # label, E (V/m), eps_r, note
    ("Air, cm-scale gap, ~3 MV/m breakdown", 3.0e6, 1.0, "macro gap in air"),
    ("Air micro-gap ~7.5 um at Paschen minimum (~327 V)", 327/7.5e-6, 1.0, "best case for air gaps"),
    ("Polyimide film, 100 MV/m (ideal, no air gap)", 1.0e8, 3.4, "upper bound, not reached in practice"),
    ("h-BN, 1.2 GV/m = 12 MV/cm (nm films, ideal)", 1.2e9, 3.5, "Hattori 2015 breakdown; nm-thin only"),
]

print("== Electrostatic pressure P = eps0*eps_r*E^2/2 ==")
for lab, E, er, note in cases:
    print(f"{lab:55s} E={E:9.3e} V/m  P={p_es(E,er):11.4g} Pa  ({note})")

print("\n== Measured electroadhesion (for scale) ==")
print("Diller, Majidi & Collins, ICRA 2016: one electrode pair bears up to 100 N,")
print("engages/releases in <30 ms, leakage ~310 nA, ~0.6 mW while walking.")

print("\n== One mechanical pin in single shear ==")
pins = [
    ("Steel pin d=3 mm, tau_allow=200 MPa", 3e-3, 200e6),
    ("Aluminium pin d=3 mm, tau_allow=100 MPa", 3e-3, 100e6),
    ("Glass-fibre/epoxy pin d=5 mm, tau_allow=50 MPa", 5e-3, 50e6),
    ("Mycelium composite peg d=10 mm, tau_allow=0.3 MPa", 10e-3, 0.3e6),
]
for lab, d, tau in pins:
    F = tau * math.pi * d**2 / 4
    print(f"{lab:52s} F = {F:9.1f} N")

print("\n== Clamp area needed to match one 3 mm steel pin (1414 N) by friction, mu=0.5 ==")
F_pin = 200e6 * math.pi * (3e-3)**2 / 4
for lab, E, er, note in cases:
    P = p_es(E, er)
    A = F_pin / (0.5 * P)
    print(f"{lab:55s} A = {A:10.4g} m^2")
for P_meas in (1e3, 10e3):
    print(f"Practical electroadhesion {P_meas/1e3:4.0f} kPa normal{'':24s} A = {F_pin/(0.5*P_meas):10.4g} m^2")

print("\n== Holding cost ==")
for V, I in ((1000, 1e-6), (1000, 1e-5)):
    print(f"V={V} V, leakage {I*1e6:.0f} uA -> {V*I*1e3:.1f} mW per lock while held")
print("A mechanical pin holds with 0 W.")

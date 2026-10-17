"""Checks for shares 69319299 (hexagrammic TENG node) and 1b684616 (nitinol loop). CC0.
Standard library only."""
import math

print("== 1. Circular-membrane fundamental, Grok's parameters (share 69319299 msg 10) ==")
T, sigma = 200.0, 5.0          # N/m, kg/m^2 (Grok's values)
c = math.sqrt(T / sigma)
j01 = 2.404825557695773
phi = (1 + 5 ** 0.5) / 2
for a in (0.5, 0.3):
    f = j01 * c / (2 * math.pi * a)
    print(f"a = {a} m: f01 = {f:.2f} Hz ; with the claimed phi path-length factor f01/phi = {f/phi:.2f} Hz")
print("-> Grok's 4.84 / 8.07 Hz are the plain membrane values; the phi factor it describes was not applied.")
print("   Matching 7.83 Hz needs a = %.3f m (no phi) for these T, sigma." % (j01 * c / (2 * math.pi * 7.83)))

print("\n== 2. Schumann field strength vs mechanical drive ==")
E_sr, B_sr = 1e-3, 1e-12       # ~mV/m and ~pT order of magnitude (typical SR amplitudes)
eps0 = 8.854e-12
p_e = 0.5 * eps0 * E_sr ** 2
p_b = B_sr ** 2 / (2 * 4e-7 * math.pi)
print(f"Schumann EM pressure ~ {p_e:.1e} Pa (E) and {p_b:.1e} Pa (B): no usable mechanical coupling to a membrane")

print("\n== 3. Nitinol transformation-temperature shift under hydrostatic pressure (share 1b684616 msg 4) ==")
dH = 20e3                      # J/kg latent heat (typical NiTi, ~20 J/g)
rho = 6450.0                   # kg/m^3
dV_over_V = 0.002              # ~0.1-0.4 % transformation volume change, order of magnitude
Tk = 320.0
dTdP = Tk * dV_over_V / (dH * rho)
for bar in (10, 100):
    print(f"{bar:4d} bar -> dT ~ {dTdP * bar * 1e5 * 1e3:.2f} mK")
print("-> Clausius-Clapeyron gives milli-kelvin shifts at 10-100 bar, not 'a few to 10-20 C'.")
print("   (Uniaxial stress is different: ~6-7 MPa per K for NiTi, which is the effect actuators use.)")

"""Checks for share ebe77445 (muons, acoustics) and 1a396707 (3-path waves). CC0.
Reruns the numbers quoted in docs/muon_cathode_acoustic_water_review.md and
docs/lab_grown_crystals_bom_review.md. Standard library + numpy only."""
import math
import numpy as np

print("== 1. Muon g-2 anomalous precession per revolution ==")
a_mu = 116592059e-11          # muon anomaly, ~1.166e-3 (CODATA-scale value)
m_mu = 105.6583755            # MeV/c^2
p_magic = 3094.0              # MeV/c ("magic" momentum used at BNL/Fermilab)
gamma = math.sqrt(1 + (p_magic / m_mu) ** 2)
deg_per_turn = 360 * a_mu * gamma
print(f"gamma_magic = {gamma:.2f}")
print(f"spin advance relative to momentum per turn = a*gamma*360 deg = {deg_per_turn:.2f} deg")
B = 1.45; e = 1.602176634e-19; m_kg = m_mu * 1.78266192e-30
omega_c = e * B / (gamma * m_kg)
R = (p_magic * 1e6 * e / 2.99792458e8) / (e * B)
print(f"orbit radius at 1.45 T = {R:.2f} m (diameter {2*R:.1f} m)")
omega_a = a_mu * e * B / m_kg
print(f"omega_a/2pi = {omega_a/2/math.pi/1e3:.1f} kHz  (period {2*math.pi/omega_a*1e6:.2f} us)")
tau = 2.1969811e-6 * gamma
print(f"lab lifetime gamma*tau = {tau*1e6:.1f} us  -> ~{tau*omega_a/2/math.pi:.1f} g-2 cycles per lifetime")
B_earth = 50e-6
print(f"in Earth's field (50 uT) omega_a/2pi = {a_mu*e*B_earth/m_kg/2/math.pi:.2f} Hz -> "
      f"{a_mu*e*B_earth/m_kg*2.2e-6*180/math.pi:.2e} deg per rest lifetime")

print("\n== 2. Water density change under acoustic pressure ==")
rho, c = 998.0, 1482.0
kappa = 1 / (rho * c * c)
for p in (1e3, 1e4, 1e5):
    print(f"p = {p/1e3:6.0f} kPa -> drho/rho = {kappa*p:.2e}")
print(f"kappa = {kappa:.2e} 1/Pa")

print("\n== 3. Gor'kov contrast factors (Bruus 2012 form) ==")
def factors(rho_p, c_p, rho_f, c_f):
    kp, kf = 1/(rho_p*c_p**2), 1/(rho_f*c_f**2)
    f1 = 1 - kp/kf
    f2 = 2*(rho_p - rho_f)/(2*rho_p + rho_f)
    phi = f1/3 + f2/2          # 1-D standing-wave contrast factor
    return f1, f2, phi
for name, rp, cp in (("polystyrene bead in water", 1050, 2350),
                     ("helium bubble in water (Gor'kov limit, far below resonance)", 0.166, 1007)):
    f1, f2, phi = factors(rp, cp, rho, c)
    where = "pressure NODES (velocity antinodes)" if phi > 0 else "pressure ANTINODES"
    print(f"{name}: f1={f1:.3g}, f2={f2:.3g}, Phi={phi:.3g} -> collects at {where}")

print("\n== 4. Dimensions of u_s ~ alpha*I/(rho*omega*nu) ==")
# alpha [1/m], I [W/m^2 = kg/s^3], rho [kg/m^3], omega [1/s], nu [m^2/s]
num = {"kg": 1, "m": -1, "s": -3}            # alpha*I : (1/m)(kg s^-3)
den = {"kg": 1, "m": -3 + 2, "s": -1 - 1}    # rho*omega*nu
res = {k: num[k] - den[k] for k in num}
print("units of alpha*I/(rho*omega*nu):", res, "-> 1/s, not m/s (dimensionally inconsistent)")
U0 = 1.0
print(f"Rayleigh outer streaming amplitude (3/8)U0^2/c for U0=1 m/s in air: {3/8*U0**2/343*1e3:.2f} mm/s")

print("\n== 5. Three equal paths with 120 deg offsets (share 1a396707 msg 38) ==")
t = np.linspace(0, 2, 2001)
w = 2*math.pi
s = sum(np.sin(w*t + k*2*math.pi/3) for k in range(3))
print(f"max |sum| of three equal-amplitude, equal-frequency waves = {np.max(np.abs(s)):.2e} (cancels exactly)")
s2 = np.sin(w*t) + np.sin(4*w*t + 2*math.pi/3) + np.sin(5*w*t + 4*math.pi/3)
print(f"fundamental + 4th + 5th harmonic with 120 deg offsets: peak {np.max(np.abs(s2)):.2f}, "
      f"rms {np.sqrt(np.mean(s2**2)):.3f} (= sqrt(3/2)={math.sqrt(1.5):.3f}; no 'balance' beyond orthogonality)")

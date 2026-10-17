"""Numerical checks for Grok shares 70-80 (2026-10-17). CC0.

None of these shares contained runnable code, so nothing could be rerun
verbatim. This script checks the numbers and formulas Grok stated in the
replies. Each section names the share and message it checks.
Run:  python3 sims/s70_80_claim_checks.py
"""
import math
import numpy as np

def hdr(s):
    print("\n" + "=" * 72 + "\n" + s + "\n" + "=" * 72)

# ---------------------------------------------------------------------------
hdr("1. Rubik's Cube order in Archimedes' orders of myriads (share 6bded219, msgs 8, 10)")
G = math.factorial(8) * 3**8 * math.factorial(12) * 2**12 // (2 * 2 * 3)
print(f"|G| = 8! 3^8 12! 2^12 / 12 = {G:,}")
print(f"matches 43,252,003,274,489,856,000: {G == 43252003274489856000}")
u2, u3 = 10**8, 10**16          # unit of the 2nd and 3rd orders
print(f"units of the third order  (10^16): {G // u3:,}  remainder {G % u3:,}")
print(f"units of the second order (10^8) : {G // u2:,}")
print("Grok said '432 units of the third order' (msg 8), 'more than 43,000 units of the")
print("third order' (msg 10) and '43,252,003,274 units of the second order' (msg 8).")
print("Correct: 4,325 units of the third order; 432,520,032,744 units of the second order.")
pocket = math.factorial(7) * 3**6
print(f"2x2x2: 7! 3^6 = {pocket:,} (Grok: 3,674,160)")
c4 = (math.factorial(8) * 3**7 * math.factorial(24)**2) // math.factorial(4)**6 // 24
print(f"4x4x4 (standard formula, fixed centres convention): {c4:.3e} (Grok: ~7.4e45)")
lo, hi = 3 + 10/71, 3 + 1/7
print(f"Archimedes: 3 10/71 = {lo:.5f} < pi = {math.pi:.5f} < 3 1/7 = {hi:.5f}")
print("Sand Reckoner's largest number: (10^8)^(10^8 * 10^8) = 10^(8e16) -> 8e16 zeros (Grok: OK)")

# ---------------------------------------------------------------------------
hdr("2. '40 octaves' from sound to light (share 9917ff9b, msg 8)")
c = 2.998e8
for f0 in (192.0, 196.0):
    for n in (40, 41):
        f = f0 * 2**n
        print(f"{f0:5.0f} Hz x 2^{n} = {f/1e12:6.1f} THz -> {c/f*1e9:6.0f} nm")
print("Visible ~400-790 THz (380-750 nm). 2^40 lands in the near-infrared (~1400 nm);")
print("it takes 41 doublings to reach deep red. Ratio 790/400 =", round(790/400, 3), "(< one octave: OK)")
for P in (25920, 25772):
    print(f"precession {P} yr / 360 = {P/360:.2f} yr per degree")

# ---------------------------------------------------------------------------
hdr("3. Sheath surface Maxwell stress and its eigenvalues (share f9e0da6d, msgs 8-10)")
eps0, mu0 = 8.854e-12, 4e-7 * math.pi
def T_surface(En, Et, Bn, Bt):
    """2x2 in-plane block of the Maxwell stress in the (n, t) frame, no z components."""
    E = np.array([En, Et]); B = np.array([Bn, Bt])
    T = eps0 * (np.outer(E, E) - 0.5 * np.eye(2) * (E @ E)) + (np.outer(B, B) - 0.5 * np.eye(2) * (B @ B)) / mu0
    return T
def grok_lambda(En, Bn, Bt):
    # Grok's matrix as far as the garbled PDF extraction can be read:
    # mean term (Bn^2 - Bt^2)/(4 mu0), radius as below.
    m = (Bn**2 - Bt**2) / (4 * mu0)
    r = math.sqrt((eps0 * En**2 / 2 - (Bn**2 + Bt**2) / (4 * mu0))**2 + (Bn * Bt / mu0)**2)
    return m + r, m - r
rng = np.random.default_rng(1)
worst = 0
for _ in range(5):
    En, Bn, Bt = rng.uniform(1e4, 1e6), rng.uniform(0, 0.1), rng.uniform(0, 0.1)
    lam = np.linalg.eigvalsh(T_surface(En, 0, Bn, Bt))[::-1]
    g = grok_lambda(En, Bn, Bt)
    print(f"En={En:9.3e} V/m Bn={Bn:.3f} T Bt={Bt:.3f} T | exact {lam[0]:+.3e} {lam[1]:+.3e} | Grok {g[0]:+.3e} {g[1]:+.3e}")
print("Exact in-plane block is traceless (Tnn + Ttt = 0 with no z components), so the")
print("eigenvalues are +/- r with r = sqrt((eps0 En^2/2 + (Bn^2-Bt^2)/2mu0)^2 + (Bn Bt/mu0)^2).")
print("Grok's entries (as extracted) carry a nonzero mean (Bn^2-Bt^2)/4mu0, so its lambda+/- are shifted.")
# degeneracy test: Bn = 0 and eps0 En^2 = Bt^2/mu0  (En = c Bt) -> r = 0 even though En != 0
Bt = 0.01; En = Bt / math.sqrt(eps0 * mu0)
lam = np.linalg.eigvalsh(T_surface(En, 0, 0.0, Bt))
print(f"Degenerate case Bn=0, Bt={Bt} T, En=c*Bt={En:.3e} V/m -> eigenvalues {lam[0]:+.2e}, {lam[1]:+.2e} (equal)")
lam = np.linalg.eigvalsh(T_surface(0.0, 0, 0.05, 0.0))
print(f"Purely normal B=0.05 T, En=0 -> eigenvalues {lam[0]:+.1f}, {lam[1]:+.1f} (distinct)")
print("So 'distinct wherever En != 0 or Bn Bt != 0' is not right: En != 0 with Bn = 0 and En = c Bt")
print("is degenerate, and a purely normal B with En = 0 is distinct.")
# order of magnitude: sheath electrostatic pressure vs body weight
e, kB = 1.602e-19, 1.381e-23
for Te_eV, n in ((3, 1e16), (3, 1e18), (10, 1e19)):
    lamD = math.sqrt(eps0 * Te_eV * e / (n * e**2))
    phi = 3 * Te_eV                       # ~3 Te floating-wall drop (order of magnitude)
    E = phi / (5 * lamD)                  # drop across ~5 Debye lengths
    pE = eps0 * E**2 / 2
    pi_ram = n * Te_eV * e                # ~ion ram pressure at Bohm entry, order n Te
    print(f"Te={Te_eV:>2} eV n={n:.0e} m^-3: lambda_D={lamD*1e6:7.1f} um, E~{E:.2e} V/m, eps0E^2/2={pE:.2e} Pa, n kTe={pi_ram:.2e} Pa")
w = 88 * 9.81
print(f"For scale: 88 kg on 1 m^2 needs {w:.0f} Pa. Lab glow/RF sheaths give mPa-Pa: the sheath term is 2-6 orders too small.")
print(f"Magnetic pressure B^2/2mu0 at 0.1 T = {0.1**2/(2*mu0):.0f} Pa, but it acts on the wall only through a jump (surface current).")

# ---------------------------------------------------------------------------
hdr("4. 'Larmor precession as master clock' (shares fe4cc5d7 msgs 18-40, 6547c372 msgs 2-6)")
gam_e, gam_p = 1.760859e11, 2.675222e8      # rad s^-1 T^-1
for B in (0.01, 0.1, 0.5):
    print(f"B={B:4} T: electron f_L={gam_e*B/2/math.pi/1e9:6.2f} GHz, proton f_L={gam_p*B/2/math.pi/1e6:6.2f} MHz")
# a small permanent magnet (not spinning) in a field oscillates like a compass needle
m_dip = 0.1      # A m^2 (small NdFeB disc)
I = 1e-7         # kg m^2
for B in (1e-3, 1e-2):
    f = math.sqrt(m_dip * B / I) / (2 * math.pi)
    print(f"non-spinning magnet m={m_dip} A m^2, I={I} kg m^2 in {B} T: torsional oscillation {f:.1f} Hz (sqrt(mB/I), not gamma*B)")
print("Ferrofluid particles relax by Neel/Brownian processes (~1e-9-1e-4 s); there is no")
print("coherent macroscopic Larmor precession of a ferrofluid ribbon at Hz-kHz.")

# ---------------------------------------------------------------------------
hdr("5. Hot/cold zones: adiabatic compression then expansion (share fe4cc5d7, msgs 14-16)")
g = 1.4; T0 = 293.15
for r in (1.5, 2.0, 3.0):
    Th = T0 * r**((g - 1) / g)
    Tc_noreject = Th * (1 / r)**((g - 1) / g)
    Tc_reject = T0 * (1 / r)**((g - 1) / g)
    print(f"p ratio {r}: compress -> {Th-273.15:6.1f} C; expand back without heat rejection -> {Tc_noreject-273.15:5.1f} C;"
          f" with heat rejected at high p -> {Tc_reject-273.15:6.1f} C")
print("A cold zone needs the compression heat removed first (a refrigeration cycle: work in, heat out).")
print("Liquids barely compress (water: dT/dp ~0.02 K/MPa at 20 C), so the gas fraction must do it.")

# ---------------------------------------------------------------------------
hdr("6. Faraday cage 'tunnelling' slots for Tesla-coil pulses (share fe4cc5d7, msg 32)")
for f in (50e3, 200e3, 1e6):
    print(f"Tesla coil {f/1e3:6.0f} kHz: wavelength {c/f:8.0f} m")
for a in (0.01, 0.1, 0.3):
    print(f"slot width {a*100:4.0f} cm: TE10-like cutoff {c/(2*a)/1e9:6.2f} GHz")
print("Every practical slot is far below cutoff at coil frequencies; the pulse must enter through a")
print("wired feed-through or capacitive/inductive port, not a 'resonant aperture'.")

# ---------------------------------------------------------------------------
hdr("7. Earth-Moon tidal tensor scale (share 229ef999, msg 8)")
GM_moon, R = 4.9028e12, 3.844e8
tid = GM_moon / R**3
Om = 7.292e-5
print(f"GM_moon/R^3 = {tid:.2e} s^-2 (tidal strain-rate scale); Earth Omega^2 = {Om**2:.2e} s^-2")
print(f"tidal acceleration at Earth's surface ~ 2 GM r/R^3 = {2*tid*6.371e6:.2e} m/s^2")
print("Sign: tidal tensor -d_i d_j Phi = +GM/R^3 (3 R_i R_j - delta_ij); Grok wrote Phi,ij with a minus sign")
print("(that is the Hessian of the potential, the opposite sign convention: consistent if read that way).")

# ---------------------------------------------------------------------------
hdr("8. Minnaert bubble resonance for the 'bubble -> well' concept (share 604dca24, msg 10)")
p0, rho = 101325.0, 998.0
for Rb in (1e-5, 1e-4, 1e-3, 3e-3):
    f = math.sqrt(3 * 1.4 * p0 / rho) / (2 * math.pi * Rb)
    print(f"air bubble R={Rb*1e3:6.3f} mm in water: f_M = {f/1e3:8.2f} kHz")
print("f_M * R ~ 3.3 m/s: a 20-40 kHz ultrasonic field addresses ~0.1 mm bubbles.")

# ---------------------------------------------------------------------------
hdr("9. Mercury vapour hazard (share 604dca24, msg 2)")
# saturated vapour concentration from vapour pressure (Hg: ~0.17 Pa at 20 C, ~0.26 Pa at 25 C)
M = 0.20059
for T, p in ((293.15, 0.170), (298.15, 0.261), (313.15, 0.80)):
    conc = p * M / (8.314 * T) * 1e6     # mg/m^3
    print(f"T={T-273.15:4.0f} C: p_sat~{p} Pa -> saturated air ~{conc:5.1f} mg/m^3")
print("Occupational limits are ~0.025-0.05 mg/m^3 (8 h TWA; ACGIH TLV / NIOSH REL), so")
print("saturated air over open mercury is ~300-500x over the limit at room temperature.")

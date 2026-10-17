#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""
grok_s81_85_claim_checks.py -- order-of-magnitude checks for Grok shares #81-#85
(archived 2026-10-17 in docs/grok_archive/):

  81 373a0a5b "Joseph Newman Energy Machine Investigation"
  82 28a95833 "Nickel Superalloys: Gamma Prime Phase"
  85 ace6ad75 "Grassmann vs Lorentz Force Laws"

Sections
  A. Electrohydraulic bubble periods vs Rayleigh collapse time (81, msg 6)
  B. Baghdad-style Cu/Fe cell and how slow plating from it would be (81, msgs 22-24)
  C. Potassium-40 specific activity (82, msg 20)
  D. Magnetic pressure table B^2/2mu0 (85, msg 10)
  E. RERUN of Grok's "pol-simulation-engine" pressure sweep (85, msgs 12, 18, 22, 24).
     The engine is the legacy Grok v0.1 hover_dynamics.py kept in the sister repo
     Resona-POL-Modular-Core (legacy/grok_v0.1/hover_dynamics.py). Its lift_force()
     and efficiency() are copied here unchanged so the numbers can be compared.
  F. Physical floor-loss bound for the same lift (thick plate, P/F >= omega*delta)
  G. "Same coil inflates into a magnetic sail": standoff and thrust at 1 AU (85, msg 26)
  H. Solar-wind energy flux available to piezo "drops" (85, msg 28)

Nothing here uses phi as an input. Run: python3 grok_s81_85_claim_checks.py
"""
import numpy as np

mu0 = 4e-7 * np.pi
g = 9.81
print(__doc__.split("Sections")[0].strip().splitlines()[0])

# ---------------------------------------------------------------- A
print("\nA. Electrohydraulic bubble: Rayleigh period 2 x 0.915 R sqrt(rho/dp)")
rho_w, p_inf = 1000.0, 1.013e5
for R, grok_ms in [(0.008, 1.7), (0.0135, 3.0)]:
    T = 2 * 0.915 * R * np.sqrt(rho_w / p_inf)
    print(f"  R_max = {R*1e3:4.1f} mm -> T = {T*1e3:4.2f} ms (Grok: ~{grok_ms} ms)")

# ---------------------------------------------------------------- B
print("\nB. Cu/Fe cell in vinegar and plating rate")
E_cu, E_fe = 0.34, -0.44
print(f"  ideal Cu2+/Cu vs Fe2+/Fe: {E_cu-E_fe:.2f} V (open circuit; replicas report ~0.5-0.9 V"
      " because the copper side runs on dissolved O2 / H+, not Cu2+)")
F = 96485.0
# gold, 1 um over 10 cm^2
rho_au, M_au, z_au = 19.32e3, 0.19697, 1     # Au(I) as in cyanide baths
m = rho_au * 1e-6 * 10e-4
for I in (1e-3, 1e-4):
    t = m / M_au * z_au * F / I
    print(f"  1 um of Au on 10 cm^2 = {m*1e6:.1f} mg; at {I*1e3:.1f} mA (100% efficiency) -> {t/3600:.1f} h")

# ---------------------------------------------------------------- C
print("\nC. K-40 specific activity of natural potassium")
NA, MK, ab, T12 = 6.02214e23, 39.098, 1.17e-4, 1.248e9 * 3.15576e7
A = NA / MK * ab * np.log(2) / T12
print(f"  {A:.1f} Bq per g K (Grok: ~31)")

# ---------------------------------------------------------------- D
print("\nD. Magnetic pressure B^2/(2 mu0)")
for B in (0.01, 0.05, 0.08, 0.10, 0.15, 0.20):
    print(f"  B = {B:4.2f} T -> {B**2/(2*mu0)/1e3:6.3f} kPa")
for Fw, A_ in ((800, 0.40), (1100, 0.25)):
    P = Fw / A_
    print(f"  {Fw} N over {A_} m^2 -> {P/1e3:.2f} kPa -> B = {np.sqrt(2*mu0*P):.3f} T")

# ---------------------------------------------------------------- E
print("\nE. Rerun of the legacy Grok v0.1 lift model (the 'pol-simulation-engine')")
def coupling_k(h, h0=0.12):
    return 0.28 * np.exp(-h / h0)
def efficiency(f, h, sigma, L_uH=50.0, Q_tx=180, Q_rx=160):   # verbatim logic
    k = coupling_k(h)
    floor_factor = 0.92 if sigma > 3e7 and h < 0.18 else 0.15
    k2QQ = k**2 * Q_tx * Q_rx
    return np.clip((k2QQ / (1 + k2QQ)) * floor_factor, 0.01, 0.95)
def lift_force(h, f, P_del, sigma):                            # verbatim logic
    h = max(h, 0.005)
    F_ = 0.22 * P_del * (13.56e6 / max(f, 1e6)) * (sigma / 3.5e7) / (h ** 1.1)
    return float(np.clip(F_, 0, 1450))
sig, f0, Aeff, m_sys = 3.8e7, 13.56e6, 0.30, 105.0
def F_of(h, P=520.0, f=f0):
    return lift_force(h, f, P * efficiency(f, h, sig), sig)
print(f"  {'h (m)':>6} {'eta':>6} {'F (N)':>7} {'P (kPa)':>8} {'B_eq (T)':>8}")
for h in (0.05, 0.08, 0.10, 0.12, 0.15, 0.18):
    Fh = F_of(h)
    print(f"  {h:6.2f} {efficiency(f0,h,sig):6.3f} {Fh:7.0f} {Fh/Aeff/1e3:8.2f} {np.sqrt(2*mu0*Fh/Aeff):8.3f}")
print(f"  weight {m_sys*g:.0f} N; at 300 W F(0.10) = {F_of(0.10,300):.0f} N; at 800 W = {F_of(0.10,800):.0f} N")
print(f"  frequency x2 (27.12 MHz): F(0.10) = {F_of(0.10, 520, 2*f0):.0f} N  (model lift falls as 1/f)")
print(f"  at 1 kHz the same formula gives F(0.10) = {F_of(0.10, 520, 1e3):.0f} N (clipped; f is floored at 1 MHz)")
hh = np.linspace(0.05, 0.15, 2001)
FF = np.array([F_of(h) for h in hh])
def W(a, b):
    s = (hh >= a - 1e-12) & (hh <= b + 1e-12)
    return np.trapezoid(FF[s], hh[s])
for a, b in ((0.05, 0.10), (0.10, 0.15), (0.05, 0.15)):
    print(f"  work {a:.2f}->{b:.2f} m: {W(a,b):6.1f} J   (PE change {m_sys*g*(b-a):5.1f} J)")
print("  Grok msg 18 gave 67 / 52 / 124 J; msg 24 gave 70.4 / 51.0 / ~121 J for the same baseline.")
# Multi-Egg factor as described (alpha floor-coupled, beta ~ 1/h^0.4, 'mild boost'):
# Grok did not give the boost term, so we test the two stated parts only.
def F_me(h, alpha=0.55, beta=0.45):
    return alpha * F_of(h) + beta * F_of(0.10) * (0.10 / h) ** 0.4
for h in (0.10, 0.15):
    print(f"  Multi-Egg (alpha/beta only) h={h:.2f}: {F_me(h):6.0f} N   (Grok: 1620 N at 0.10, 863 N at 0.15)")
print("  -> with alpha+beta = 1 the factor is exactly 1.00 at h = 0.10 m and RAISES force at 0.15 m;")
print("     Grok's 1.12 boost at 0.10 m and lower force at 0.15 m need an unstated extra term,")
print("     i.e. the 'Multi-Egg factor' is a chosen multiplier, not a geometry result.")

# ---------------------------------------------------------------- F
print("\nF. Physical floor-loss bound for 1030 N (thick Al plate, P/F >= omega*delta)")
for f in (13.56e6, 1e3):
    delta = np.sqrt(2 / (2 * np.pi * f * mu0 * sig))
    print(f"  f = {f:10.0f} Hz: delta = {delta*1e6:8.1f} um, P_floor >= {2*np.pi*f*delta*m_sys*g/1e3:9.1f} kW"
          "  (coil copper loss comes on top)")
print("  Sister repo (sim/README.md): ~16.7 kW at the default design, ~10 kW best design; not 520 W.")

# ---------------------------------------------------------------- G
print("\nG. POL coil as a magnetic sail at 1 AU")
n_sw, v_sw, mp = 5e6, 4.0e5, 1.6726e-27
pdyn = n_sw * mp * v_sw**2
Bmp = np.sqrt(2 * mu0 * pdyn)
print(f"  solar-wind dynamic pressure {pdyn*1e9:.2f} nPa -> balancing field {Bmp*1e9:.0f} nT")
for label, mdip in (("POL coil, 8 turns x 100 A x 0.28 m^2", 8 * 100 * 0.28),
                    ("100 km-class loop (Zubrin-Andrews scale), m = 1e13 A m^2", 1e13)):
    r = (mu0 * mdip / (2 * np.pi * Bmp)) ** (1 / 3)
    Fs = 0.5 * 1.0 * pdyn * np.pi * r**2
    print(f"  {label}: standoff ~{r:.3g} m, thrust ~{Fs:.2g} N (Cd = 1, MHD picture)")
print("  (below the ~100 km ion gyroradius the MHD picture over-predicts; real thrust is lower.)")

# ---------------------------------------------------------------- H
print("\nH. Energy available to piezo 'drops' from the solar wind")
flux = 0.5 * n_sw * mp * v_sw**3
print(f"  kinetic energy flux 0.5 rho v^3 = {flux*1e3:.2f} mW per m^2 (all of it, before any conversion loss)")
print("  raindrop piezo harvesters: ~uJ to tens of uJ per drop (Guigon et al. 2008) [to verify the exact range]")

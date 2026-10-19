"""Ambipolar electric field from the electron pressure gradient in the solar wind.

Inertialess electron momentum (field-aligned / radial part, collisions dropped):
    0 = -e n_e E - grad(p_e)   =>   E_amb = -grad(p_e) / (e n_e)
Isothermal (p_e = n k T_e, T_e const):  E = -(k T_e / e) grad ln n_e
Polytropic (p_e ~ n^gamma):             E = -(gamma k T_e(r) / e) grad ln n_e
With n ~ r^-2 (constant-speed wind): grad ln n = -2/r, so
    E_amb(r) = 2 gamma k T_e(r) / (e r),  T_e(r) = T_e0 (r/r0)^(-2(gamma-1)).

Outputs:
  1. E_amb(r) for 0.05-5 AU, isothermal and polytropic (gamma = 1.2).
  2. eE/(m_p g) (ratio > 1 means the electric force on a proton beats gravity).
     Pannekoek-Rosseland hydrostatic reference: ratio = 1/2 (T_e = T_p).
  3. Cumulative potential (numerical integral vs analytic
     gamma/(gamma-1) k T_e / e for the polytrope; log-divergent for isothermal).
  4. Comparison with the motional (convective) field |v x B| for a Parker spiral.
Optional PNG: docs/images/2026-10-18_ambipolar_field_solar_wind.png

CC0. Model inputs are round textbook values, not fitted data.
"""
from __future__ import annotations

import math
import os

import numpy as np

E_CH = 1.602176634e-19      # C (also J per eV)
M_P = 1.67262192e-27        # kg
GM_SUN = 1.32712440018e20   # m^3 s^-2
AU = 1.495978707e11         # m
R_SUN = 6.957e8             # m
OMEGA_SUN = 2.0 * math.pi / (25.38 * 86400.0)  # sidereal rotation, rad/s

R0_AU = 0.1                 # reference radius for T_e0


def T_e(r_au: np.ndarray, Te0_eV: float, gamma: float) -> np.ndarray:
    """Electron temperature in eV for p ~ n^gamma with n ~ r^-2."""
    return Te0_eV * (np.asarray(r_au) / R0_AU) ** (-2.0 * (gamma - 1.0))


def E_amb(r_au: np.ndarray, Te0_eV: float, gamma: float) -> np.ndarray:
    """|E_amb| in V/m (points outward)."""
    r_m = np.asarray(r_au) * AU
    return 2.0 * gamma * T_e(r_au, Te0_eV, gamma) / r_m  # kT/e in volts = T in eV


def grav(r_au: np.ndarray) -> np.ndarray:
    r_m = np.asarray(r_au) * AU
    return GM_SUN / r_m**2


def ratio_eE_mpg(r_au, Te0_eV, gamma):
    return E_CH * E_amb(r_au, Te0_eV, gamma) / (M_P * grav(r_au))


def potential_numeric(r1_au: float, r2_au: float, Te0_eV: float, gamma: float, n: int = 200001) -> float:
    r = np.geomspace(r1_au, r2_au, n)
    return float(np.trapezoid(E_amb(r, Te0_eV, gamma), r * AU))


def potential_to_inf_polytrope(r_au: float, Te0_eV: float, gamma: float) -> float:
    return gamma / (gamma - 1.0) * float(T_e(r_au, Te0_eV, gamma))


def escape_energy_eV(r_m: float) -> float:
    return GM_SUN * M_P / r_m / E_CH


def vxB(r_au, v_kms=400.0, B1_nT=5.0):
    """Parker spiral |v x B| (V/m) for radial v; only B_phi contributes.
    Normalised so |B| = B1_nT at 1 AU. Also returns the 'total-B' upper bound v|B|."""
    r_m = np.asarray(r_au) * AU
    v = v_kms * 1e3
    tan1 = OMEGA_SUN * AU / v
    Br1 = B1_nT * 1e-9 / math.sqrt(1.0 + tan1**2)
    Br = Br1 * (AU / r_m) ** 2
    Bphi = Br * OMEGA_SUN * r_m / v
    Btot = np.hypot(Br, Bphi)
    return v * Bphi, v * Btot


def main() -> None:
    cases = [
        ("isothermal Te=40 eV", 40.0, 1.0),
        ("isothermal Te=10 eV", 10.0, 1.0),
        ("polytrope g=1.2 Te0=40 eV", 40.0, 1.2),
        ("polytrope g=1.2 Te0=70 eV", 70.0, 1.2),
        ("polytrope g=1.2 Te0=100 eV", 100.0, 1.2),
        ("polytrope g=1.2 Te(1AU)=10 eV", 10.0 * 10 ** 0.4, 1.2),
    ]
    radii = [0.05, 0.1, 0.3, 1.0, 2.0, 5.0]

    print("=== 1-2. E_amb(r) [V/m] and eE/(m_p g), n ~ r^-2 ===")
    print(f"(T_e0 given at r0 = {R0_AU} AU; polytrope T_e ~ r^-0.4 for gamma=1.2)")
    for label, Te0, g in cases:
        print(f"-- {label}")
        for r in radii:
            print(f"   r={r:5.2f} AU  Te={float(T_e(r, Te0, g)):6.2f} eV  "
                  f"E={float(E_amb(r, Te0, g)):.3e} V/m  eE/(m_p g)={float(ratio_eE_mpg(r, Te0, g)):.3f}")
    print("   (n ~ r^-2 is poor inside ~0.1 AU where the wind still accelerates; 0.05 AU rows are indicative.)")
    print("   Pannekoek-Rosseland hydrostatic reference: eE/(m_p g) = 0.5 (Te = Tp).")
    print("   Isothermal ratio = 2 kTe r/(GM m_p): grows linearly with r.")
    print("   Polytrope ratio ~ r^(1-2(gamma-1)) = r^0.6.")
    print()

    print("=== Check of the user estimates ===")
    e01 = float(E_amb(0.1, 40.0, 1.0)); q01 = float(ratio_eE_mpg(0.1, 40.0, 1.0))
    print(f"0.1 AU, Te=40 eV isothermal: E={e01:.3e} V/m, ratio={q01:.3f}  (estimate 5e-9, 0.9)")
    e1 = float(E_amb(1.0, 10.0, 1.0)); q1 = float(ratio_eE_mpg(1.0, 10.0, 1.0))
    Te0_1 = 10.0 * 10 ** 0.4  # Te(1 AU) = 10 eV on the gamma=1.2 polytrope
    e1p = float(E_amb(1.0, Te0_1, 1.2)); q1p = float(ratio_eE_mpg(1.0, Te0_1, 1.2))
    print(f"1 AU, Te=10 eV isothermal:   E={e1:.3e} V/m, ratio={q1:.3f}")
    print(f"1 AU, Te(1AU)=10 eV, g=1.2: E={e1p:.3e} V/m, ratio={q1p:.3f}")
    Te_low = 0.8e-10 * AU / 2.0
    print(f"   (estimate 0.8-1.3e-10 V/m, 1.3-2.2: the 0.8e-10 end needs Te ~ {Te_low:.1f} eV "
          f"isothermal, or a density slope ~{0.8e-10*AU/10.0:.1f} instead of 2 at 10 eV)")
    print()

    print("=== 3. Cumulative potential ===")
    for label, Te0, g in cases:
        num = potential_numeric(0.1, 5.0, Te0, g)
        if g > 1.0:
            ana_5 = potential_to_inf_polytrope(0.1, Te0, g) - potential_to_inf_polytrope(5.0, Te0, g)
            inf = potential_to_inf_polytrope(0.1, Te0, g)
            inf1 = potential_to_inf_polytrope(1.0, Te0, g)
            print(f"{label:32s} Phi(0.1->5 AU) num={num:7.1f} V ana={ana_5:7.1f} V | "
                  f"Phi(0.1 AU->inf)={inf:6.1f} V  Phi(1 AU->inf)={inf1:5.1f} V")
        else:
            ana_5 = 2.0 * Te0 * math.log(5.0 / 0.1)
            print(f"{label:32s} Phi(0.1->5 AU) num={num:7.1f} V ana={ana_5:7.1f} V | "
                  f"Phi(->inf) diverges (2kTe/e ln r)")
    print()
    e10 = escape_energy_eV(10 * R_SUN); e01e = escape_energy_eV(0.1 * AU)
    print(f"Proton escape energy GM m_p/r: 10 R_sun = {e10:.1f} eV; 0.1 AU (= {0.1*AU/R_SUN:.1f} R_sun) = {e01e:.1f} eV")
    for Te0 in (40.0, 100.0):
        phi = potential_to_inf_polytrope(0.1, Te0, 1.2)
        net = phi - e01e
        v_inf = math.sqrt(2 * net * E_CH / M_P) / 1e3 if net > 0 else float('nan')
        print(f"  gamma=1.2, Te0={Te0:.0f} eV: Phi(0.1 AU->inf)={phi:.0f} V; minus escape at 0.1 AU -> "
              f"{net:.0f} eV -> proton v_inf from rest ~ {v_inf:.0f} km/s (electrostatic share only)")
    print("Halekas et al. 2021 (ApJ 916:16, PSP SPAN-E): Phi ~ 285 V near perihelion; 50-300 V for")
    print("  core Te ~ 10-60 eV; Phi/Te slope ~5 (gamma/(gamma-1)=5 -> gamma=1.25; 1.2 gives 6).")
    print()

    print("=== 4. Motional field |v x B| (Parker spiral, v=400 km/s, |B|=5 nT at 1 AU) ===")
    for r in radii:
        m, mtot = vxB(r)
        ea = float(E_amb(r, 40.0, 1.2))
        print(f"   r={r:5.2f} AU  |v x B|={float(m):.3e} V/m (v|B| bound {float(mtot):.3e})  "
              f"E_amb(g1.2,40eV)={ea:.3e}  ratio vxB/E_amb={float(m)/ea:.2e}")
    print(f"   1 AU check: 400 km/s x 5 nT = {400e3*5e-9:.1e} V/m (upper bound, total B);"
          f" B_phi only (spiral ~{math.degrees(math.atan(OMEGA_SUN*AU/400e3)):.0f} deg) -> {float(vxB(1.0)[0]):.2e} V/m")
    for lab, v, B in (("inner heliosheath", 100.0, 0.1), ("heliosheath", 100.0, 0.2), ("VLISM", 26.0, 0.5)):
        print(f"   {lab:18s} v={v:5.1f} km/s B={B} nT -> v*B = {v*1e3*B*1e-9*1e6:5.1f} uV/m")
    ea120 = float(E_amb(120.0, 40.0, 1.2))
    print(f"   E_amb extrapolated to 120 AU (g1.2, 40 eV at 0.1 AU) = {ea120:.1e} V/m")
    print("   => the ~uV/m E in electrostatic_maxwell_stress_check.py is motional (v x B), not ambipolar.")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        r = np.geomspace(0.05, 5.0, 400)
        fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
        for label, Te0, g in cases:
            ax[0].loglog(r, E_amb(r, Te0, g), label=label)
            ax[1].loglog(r, ratio_eE_mpg(r, Te0, g), label=label)
        ax[0].loglog(r, vxB(r)[0], "k--", label="|v x B| Parker spiral")
        ax[0].set_xlabel("r [AU]"); ax[0].set_ylabel("E [V/m]"); ax[0].set_title("Ambipolar vs motional field")
        ax[1].axhline(1.0, color="k", lw=0.8); ax[1].axhline(0.5, color="k", ls=":", lw=0.8)
        ax[1].set_xlabel("r [AU]"); ax[1].set_ylabel("eE / (m_p g)"); ax[1].set_title("Electric force / gravity on a proton")
        ax[0].legend(fontsize=7); ax[1].legend(fontsize=7)
        fig.tight_layout()
        here = os.path.dirname(os.path.abspath(__file__))
        out = os.path.join(here, "..", "docs", "images", "2026-10-18_ambipolar_field_solar_wind.png")
        fig.savefig(out, dpi=120)
        print(f"\nPNG saved: docs/images/{os.path.basename(out)}")
    except ImportError:
        print("\nmatplotlib not available; PNG skipped.")


if __name__ == "__main__":
    main()

"""Eigenvalue and heliosphere-magnitude checks for Grok share #90 (18a292a6).

Electrostatic Maxwell stress:
    sigma_ij = eps0 (E_i E_j - 1/2 delta_ij E^2)

Checks:
  1. Eigenvalues: +1/2 eps0 E^2 along E, -1/2 eps0 E^2 transverse (twice).
  2. Trace = -1/2 eps0 E^2 (not zero; the 3D electrostatic stress is not
     traceless, unlike the 4D EM stress-energy tensor in vacuum).
  3. Heliosphere order-of-magnitude: electric vs magnetic stress ~ (E/cB)^2
     for E ~ few uV/m and B ~ 0.1-0.5 nT.

CC0. No third-party data.
"""
from __future__ import annotations

import math

import numpy as np

EPS0 = 8.854187817e-12
MU0 = 4.0e-7 * math.pi
C = 1.0 / math.sqrt(EPS0 * MU0)


def sigma_E(E: np.ndarray) -> np.ndarray:
    E = np.asarray(E, dtype=float)
    E2 = float(E @ E)
    return EPS0 * (np.outer(E, E) - 0.5 * np.eye(3) * E2)


def main() -> None:
    print("=== 1. Eigenvalues of electrostatic Maxwell stress ===")
    E0 = 1.0  # V/m
    E = np.array([E0, 0.0, 0.0])
    sig = sigma_E(E)
    w = np.linalg.eigvalsh(sig)
    along = 0.5 * EPS0 * E0**2
    across = -0.5 * EPS0 * E0**2
    print(f"E = ({E0}, 0, 0) V/m")
    print(f"sigma =\n{sig}")
    print(f"eigenvalues (sorted): {w}")
    print(f"expected along E:     {along:+.6e} Pa")
    print(f"expected transverse:  {across:+.6e} Pa (degeneracy 2)")
    print(f"trace:                {np.trace(sig):+.6e} Pa")
    print(f"expected trace:       {across:+.6e} Pa  (= -1/2 eps0 E^2)")
    ok_eig = (
        abs(sig[0, 0] - along) < 1e-24
        and abs(sig[1, 1] - across) < 1e-24
        and abs(sig[2, 2] - across) < 1e-24
        and abs(np.trace(sig) - across) < 1e-24
    )
    print(f"eigenvalue + trace check: {'PASS' if ok_eig else 'FAIL'}")
    print()
    print("Note: tension along field lines (+), pressure/compression")
    print("perpendicular (-). Trace is NOT zero (unlike the 4D EM")
    print("stress-energy tensor in vacuum Minkowski spacetime).")
    print()

    print("=== 2. Heliosphere E vs B stress ratio ~ (E/cB)^2 ===")
    cases = [
        (1e-6, 0.1e-9, "E=1 uV/m, B=0.1 nT"),
        (5e-6, 0.3e-9, "E=5 uV/m, B=0.3 nT"),
        (10e-6, 0.5e-9, "E=10 uV/m, B=0.5 nT"),
    ]
    print(f"c = {C:.6e} m/s")
    for E_mag, B_mag, label in cases:
        ratio = (E_mag / (C * B_mag)) ** 2
        pE = 0.5 * EPS0 * E_mag**2
        pB = B_mag**2 / (2.0 * MU0)
        print(
            f"{label}: (E/cB)^2 = {ratio:.3e}, "
            f"pE = {pE:.3e} Pa, pB = {pB:.3e} Pa, pE/pB = {pE / pB:.3e}"
        )
    print()
    print("Magnetic stress dominates by ~8-9 orders of magnitude at these")
    print("heliospheric scales. Ambipolar E is still essential locally for")
    print("wind acceleration; it is secondary for global heliopause balance.")


if __name__ == "__main__":
    main()

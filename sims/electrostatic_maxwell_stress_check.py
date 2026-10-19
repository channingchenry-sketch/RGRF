"""Eigenvalue and heliosphere-magnitude checks for Grok share #90 (18a292a6).

Electrostatic Maxwell stress:
    sigma_ij = eps0 (E_i E_j - 1/2 delta_ij E^2)

Checks:
  1. Eigenvalues: +1/2 eps0 E^2 along E, -1/2 eps0 E^2 transverse (twice).
  2. Trace = -1/2 eps0 E^2 (not zero; the 3D electrostatic stress is not
     traceless, unlike the 4D EM stress-energy tensor in vacuum).
  3. Heliosphere order-of-magnitude: electric vs magnetic stress ~ (E/cB)^2
     for E ~ few uV/m and B ~ 0.1-0.5 nT.
  4. Full EM Maxwell stress trace equals -u_EM for a random E and B.
  5. (share #91, 753ca89b) Radial magnetic force for a Parker-spiral field at
     the equator: J x B from a finite-difference curl vs Grok's radial-shell
     form  -d/dr(B^2/2mu0) + (B_theta^2 + B_phi^2)/(mu0 r)  vs the corrected
     form  -d/dr(B_perp^2/2mu0) - B_perp^2/(mu0 r)  (B_perp^2 = B_theta^2 + B_phi^2;
     B_r drops out because B_r dB_r/dr cancels its own pressure gradient).

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


def sigma_EM(E: np.ndarray, B: np.ndarray) -> np.ndarray:
    E = np.asarray(E, dtype=float)
    B = np.asarray(B, dtype=float)
    E2 = float(E @ E)
    B2 = float(B @ B)
    return (
        EPS0 * (np.outer(E, E) - 0.5 * np.eye(3) * E2)
        + (1.0 / MU0) * (np.outer(B, B) - 0.5 * np.eye(3) * B2)
    )


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
    print()

    print("=== 3. Trace of total EM Maxwell stress equals -u_EM ===")
    rng = np.random.default_rng(20261018)
    E_rand = rng.normal(size=3)
    B_rand = rng.normal(size=3)
    sig_em = sigma_EM(E_rand, B_rand)
    u_em = 0.5 * (EPS0 * float(E_rand @ E_rand) + float(B_rand @ B_rand) / MU0)
    tr = float(np.trace(sig_em))
    print(f"random E = {E_rand}")
    print(f"random B = {B_rand}")
    print(f"tr(sigma_EM) = {tr:+.6e} Pa")
    print(f"-u_EM         = {-u_em:+.6e} Pa")
    ok_tr = abs(tr + u_em) <= 1e-9 * max(1.0, abs(u_em))
    print(f"trace == -u_EM check: {'PASS' if ok_tr else 'FAIL'}")


def _parker_B(x: np.ndarray, B0: float, r0: float, k: float) -> np.ndarray:
    """Parker-type field: B_r = B0 (r0/r)^2, B_phi = -B_r k r sin(theta)."""
    r = float(np.linalg.norm(x))
    rho = math.hypot(x[0], x[1])
    st = rho / r
    rhat = x / r
    phihat = np.array([-x[1], x[0], 0.0]) / rho
    Br = B0 * (r0 / r) ** 2
    Bphi = -Br * k * r * st
    return Br * rhat + Bphi * phihat


def _curl(f, x: np.ndarray, h: float) -> np.ndarray:
    J = np.zeros((3, 3))
    for j in range(3):
        d = np.zeros(3)
        d[j] = h
        J[:, j] = (f(x + d) - f(x - d)) / (2.0 * h)
    return np.array([J[2, 1] - J[1, 2], J[0, 2] - J[2, 0], J[1, 0] - J[0, 1]])


def radial_shell_check() -> None:
    print()
    print("=== 5. Radial magnetic force, Parker spiral at the equator (share #91) ===")
    AU = 1.495978707e11
    B0, r0 = 5e-9, AU            # |B_r| = 5 nT at 1 AU (round value)
    k = 2.0 * math.pi / (25.38 * 86400.0) / 4.0e5   # Omega / v, v = 400 km/s
    f = lambda x: _parker_B(x, B0, r0, k)
    print(" r[AU]  FD (JxB)_r [N/m^3]   Grok form          corrected form")
    for r_au in (0.3, 1.0, 5.0):
        r = r_au * AU
        x = np.array([r, 0.0, 0.0])
        h = 1e-4 * r
        B = f(x)
        Jv = _curl(f, x, h) / MU0
        Fr = float(np.cross(Jv, B)[0])
        Br = lambda rr: B0 * (r0 / rr) ** 2
        Bp = lambda rr: Br(rr) * k * rr
        B2 = lambda rr: Br(rr) ** 2 + Bp(rr) ** 2
        dB2 = (B2(r + h) - B2(r - h)) / (2 * h)
        dBp2 = (Bp(r + h) ** 2 - Bp(r - h) ** 2) / (2 * h)
        grok = -dB2 / (2 * MU0) + Bp(r) ** 2 / (MU0 * r)
        corr = -dBp2 / (2 * MU0) - Bp(r) ** 2 / (MU0 * r)
        print(f" {r_au:4.1f}  {Fr:+.3e}          {grok:+.3e}         {corr:+.3e}")
    print("Corrected form matches the FD force (Parker B_phi ~ 1/r gives r*B_phi const,")
    print("so the equatorial radial magnetic force vanishes). Grok's form is non-zero and")
    print("outward: wrong sign on the hoop-tension term and a spurious B_r^2 pressure term.")
    # pure azimuthal test: B_phi = const -> hoop tension inward
    Bc = 1e-9
    r = AU
    corr = -0.0 - Bc**2 / (MU0 * r)
    grok = +Bc**2 / (MU0 * r)
    print(f"Uniform B_phi = 1 nT at 1 AU: corrected (inward) {corr:+.3e}, Grok {grok:+.3e} N/m^3")


if __name__ == "__main__":
    main()
    radial_shell_check()

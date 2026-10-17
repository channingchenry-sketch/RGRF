#!/usr/bin/env python3
"""
Maxwell stress tensor of a magnetic dipole, evaluated in a 2D plane (CC0).

Honest rebuild of the "2D dipole on a 50x50 grid" that Grok reported in the
conversation "Electromagnetic Pressure Density Measurement" (2026-10-17).
Grok's code and image were not shared, so this is NOT a reproduction of its
numbers. It shows what the physics gives.

Magnetic-only stress tensor (SI):
    T_ij = (1/mu0) * (B_i B_j - 1/2 delta_ij B^2)
In the x-z plane through a dipole, B has only in-plane components (B_y = 0), so
the 2x2 in-plane block is traceless: T_xx + T_zz = (Bx^2 + Bz^2 - B^2)/mu0 = 0.
That is why Grok's T_xx ~ -0.215 and T_yy ~ +0.215 are mutually consistent.
(The full 3D tensor is not traceless: T_yy = -B^2/2mu0, trace = -B^2/2mu0.)
Grok's three numbers also fix a field direction: tan(2 theta) = T_xy / T_xx.

Check 2 (lift): a dipole above a perfect diamagnet / ideal conductor (high-
frequency eddy-current limit) feels a repulsion. We get it two ways:
  (a) image-dipole formula F = 3 mu0 m^2 / (32 pi h^4);
  (b) integrating the Maxwell stress over the surface: F = integral B_t^2/(2 mu0) dA.
They must agree.

Check 3 (cost): over a real conductor, lift per watt of eddy loss is
mu0*sigma*delta/2 (skin-effect limit, coil copper losses not included). That links
the stress tensor to the POL power gap (~520 W claimed vs ~10-17 kW).

Run:  python3 sims/maxwell_stress_dipole_2d.py
Output: docs/images/maxwell_stress_dipole_2d.png and printed numbers.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

MU0 = 4e-7 * np.pi


def dipole_B(x, z, m=1.0, x0=0.0, z0=0.0, mu0=MU0):
    """Field of a point dipole m*z_hat at (x0, 0, z0), evaluated in the y=0 plane."""
    rx, rz = x - x0, z - z0
    r = np.sqrt(rx**2 + rz**2)
    r = np.where(r == 0, np.nan, r)
    mdotr = m * rz
    pref = mu0 / (4 * np.pi)
    Bx = pref * (3 * rx * mdotr / r**5)
    Bz = pref * (3 * rz * mdotr / r**5 - m / r**3)
    return Bx, Bz


def stress_2d(Bx, Bz, mu0=MU0):
    B2 = Bx**2 + Bz**2
    Txx = (Bx * Bx - 0.5 * B2) / mu0
    Tzz = (Bz * Bz - 0.5 * B2) / mu0
    Txz = (Bx * Bz) / mu0
    return Txx, Tzz, Txz, B2 / (2 * mu0)


def main():
    # ---- 1. Normalised 50x50 grid (mu0 = 1, m = 1), like Grok's description ----
    n = 50
    xs = np.linspace(-1, 1, n)
    X, Z = np.meshgrid(xs, xs)
    Bx, Bz = dipole_B(X, Z, m=1.0, mu0=1.0)
    Txx, Tzz, Txz, pB = stress_2d(Bx, Bz, mu0=1.0)
    trace = Txx + Tzz
    print("1) Normalised grid 50x50 (mu0=1, m=1):")
    print(f"   max |Txx+Tzz| / max|Txx| = {np.nanmax(np.abs(trace))/np.nanmax(np.abs(Txx)):.2e}  (traceless in-plane)")

    # Grok's sample point: Txx=-0.215, Tyy=+0.215, Txy=+0.161
    txx, txy = -0.215, 0.161
    two_theta = np.degrees(np.arctan2(txy, txx))
    mag = np.hypot(txx, txy)
    print("   Grok's sample (Txx, Tyy, Txy) = (-0.215, +0.215, +0.161):")
    print(f"     consistent with a 2D in-plane field: B^2/2mu0 = {mag:.3f} (normalised),"
          f" field angle theta = {two_theta/2:.1f} deg from x")
    print("     units, dipole strength and point location were not given -> not reproducible as numbers.")

    # ---- 2. SI example: dipole sized so that |B| = 0.1 T at 5 cm on axis ----
    r0, Btarget = 0.05, 0.1
    m_SI = Btarget * 4 * np.pi * r0**3 / (MU0 * 2)   # on-axis |B| = mu0 m /(2 pi r^3)
    print(f"\n2) SI example: m = {m_SI:.1f} A*m^2 gives |B| = 0.1 T at 5 cm on axis")
    print(f"   magnetic pressure B^2/2mu0 at 0.1 T = {0.1**2/(2*MU0):.0f} Pa (~4 kPa)")
    print(f"   at 0.1 T peak AC, time-averaged pressure = B_pk^2/4mu0 = {0.1**2/(4*MU0):.0f} Pa")
    W = 88 * 9.81
    print(f"   area needed to carry 88 kg ({W:.0f} N) at 4 kPa: {W/(0.1**2/(2*MU0)):.2f} m^2")

    # ---- 3. Lift check: dipole at height h above an ideal conductor plane z=0 ----
    h = 0.05
    F_image = 3 * MU0 * m_SI**2 / (32 * np.pi * h**4)
    rho = np.linspace(0, 40 * h, 400001)
    # tangential field at the plane = 2 x radial component of the source dipole
    rr = np.sqrt(rho**2 + h**2)
    Brho_src = MU0 / (4 * np.pi) * 3 * rho * (-h) * m_SI / rr**5
    Bt = 2 * Brho_src
    _trap = getattr(np, "trapezoid", None) or np.trapz
    F_stress = _trap(Bt**2 / (2 * MU0) * 2 * np.pi * rho, rho)
    print(f"\n3) Dipole at h = {h*100:.0f} cm above an ideal (perfectly diamagnetic) plane:")
    print(f"   image formula F = 3 mu0 m^2/(32 pi h^4) = {F_image:.2f} N")
    print(f"   Maxwell-stress surface integral       = {F_stress:.2f} N  (ratio {F_stress/F_image:.4f})")
    print(f"   peak surface field = {np.max(np.abs(Bt)):.3f} T, peak pressure = {np.max(Bt**2)/(2*MU0):.0f} Pa")

    # ---- 4. Lift per watt over a real conductor (thick sheet, skin-effect limit) ----
    # Surface tangential field H_t (peak). Time-averaged pressure = mu0 H_t^2 / 4,
    # loss per area = R_s H_t^2 / 2 with R_s = 1/(sigma delta).  Ratio = mu0 sigma delta / 2.
    print("\n4) Lift per watt of eddy loss, AC coil over a thick conducting floor (F/P = mu0*sigma*delta/2):")
    for name, sigma in (("aluminium", 3.5e7), ("copper", 5.8e7)):
        for f in (100.0, 1e3, 1e4):
            delta = np.sqrt(2 / (2 * np.pi * f * MU0 * sigma))
            FP = MU0 * sigma * delta / 2
            print(f"   {name:9s} f={f:7.0f} Hz  delta={delta*1e3:6.2f} mm  F/P={FP*1e3:6.1f} N/kW"
                  f"  -> P for 88 kg = {W/FP/1e3:6.1f} kW")
    print("   (needs floor thickness >~ delta; the repo's POL sim gives ~52 N/kW, i.e. ~10-17 kW for 88 kg)")

    # ---- Plot ----
    os.makedirs("docs/images", exist_ok=True)
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.8))
    with np.errstate(divide="ignore", invalid="ignore"):
        im0 = ax[0].pcolormesh(X, Z, np.log10(pB), shading="auto", cmap="viridis")
    ax[0].streamplot(xs, xs, np.nan_to_num(Bx), np.nan_to_num(Bz), color="w", density=1.2, linewidth=0.6)
    ax[0].set_title("log10(B^2/2mu0)  + field lines\n(dipole m z-hat at origin, normalised)")
    fig.colorbar(im0, ax=ax[0])
    # signed log scaling, asinh(T/T0), so the far field is visible as well as the core
    T0 = np.nanpercentile(np.abs(Txx), 20)
    sl = lambda T: np.arcsinh(T / T0)
    lim = np.nanmax(np.abs(sl(Txx)))
    im1 = ax[1].pcolormesh(X, Z, sl(Txx), shading="auto", cmap="RdBu_r", vmin=-lim, vmax=lim)
    ax[1].set_title("asinh(T_xx/T0)  (T_zz = -T_xx in-plane)\nred = tension, blue = pressure (along x)")
    fig.colorbar(im1, ax=ax[1])
    im2 = ax[2].pcolormesh(X, Z, sl(Txz), shading="auto", cmap="PuOr", vmin=-lim, vmax=lim)
    ax[2].set_title("asinh(T_xz/T0)  (shear)")
    fig.colorbar(im2, ax=ax[2])
    for a in ax:
        a.set_aspect("equal"); a.set_xlabel("x"); a.set_ylabel("z")
    fig.suptitle("Maxwell stress of a magnetic dipole in a 2D plane (50x50 grid). CC0, RGRF.")
    fig.tight_layout()
    fig.savefig("docs/images/maxwell_stress_dipole_2d.png", dpi=110)
    print("\nSaved docs/images/maxwell_stress_dipole_2d.png")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""
toroidal_particle_trace_boris.py  --  honest companion to the archived Grok "Suite element 3".

Dimensionless units: R0 = 1, B0 = 5, charge/mass = 1 (so the on-axis gyrofrequency is 5).

PART A: Boris-pusher test particles in a simple tokamak-like vacuum field
  B_tor   = B0 R0 / R                                (toroidal, along phi-hat)
  B_theta = (B0 r / (q R0)) * (R0 / R)               (poloidal, from a constant safety factor q)
  r, theta: minor radius and poloidal angle about the magnetic axis (R0, 0).
  Cases: no poloidal field (pure toroidal), q = 3, 2, 1.5, sqrt(2), phi (golden ratio).
  Particles: N = 400, start at r in [0.05, 0.2], random angles, speed v = 0.1 with an
  isotropic pitch (passing and trapped). Gyroradius ~ 0.02, minor radius a = 0.35.
  Lost when r > a. Fixed time T = 300 (~240 gyro-periods). The Boris rotation is exact,
  so |v| is conserved to round-off with no electric field (this is checked).
  Expected (Grounded): with pure toroidal B, the grad-B + curvature drift is vertical,
  v_d ~ (v_par^2 + v_perp^2/2)/(omega_c R), charge-dependent and uncompensated, so
  particles leave in ~ a / v_d. A poloidal field (rotational transform 1/q) carries each
  guiding centre around the minor cross-section and averages the vertical drift out.

PART B: field-line Poincare map with a resonant perturbation (islands vs KAM-like surfaces)
  Cylinder-like map in (r, theta, zeta): d(theta)/d(zeta) = 1/q(r),
  dr/d(zeta) = eps * a * sin(m theta - n zeta),  q(r) = 1.2 + 1.5 (r/a)^2,
  with m/n = 3/2 (resonant at q = 1.5). It reports the radial spread of the Poincare traces
  started on the q = 1.5, sqrt(2) and phi surfaces. A perturbation opens an island only where
  q = m/n is rational and matches it. Irrational surfaces far from low-order rationals
  survive (KAM; the golden mean is the most robust, Greene 1979), but only relative to the
  perturbations present. Without perturbations, every surface is intact.

Label: confinement by rotational transform = Grounded physics; any phi advantage is reported
only if the numbers show it. Requires numpy and matplotlib.
"""
import argparse
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PHI = (1 + 5 ** 0.5) / 2
R0, B0, A_MINOR = 1.0, 5.0, 0.35


def field(x, q):
    """B at positions x (N,3), Cartesian; torus axis = z."""
    X, Y, Z = x[:, 0], x[:, 1], x[:, 2]
    R = np.hypot(X, Y)
    cphi, sphi = X / R, Y / R
    Bt = B0 * R0 / R
    Bx, By, Bz = -Bt * sphi, Bt * cphi, np.zeros_like(R)
    if q is not None:
        dR, dZ = R - R0, Z
        r = np.hypot(dR, dZ)
        Bp = B0 * r / (q * R0) * (R0 / R)
        # theta-hat in the poloidal plane = (-dZ/r) R-hat + (dR/r) Z-hat
        rs = np.maximum(r, 1e-12)
        BR = -Bp * dZ / rs
        Bx = Bx + BR * cphi
        By = By + BR * sphi
        Bz = Bz + Bp * dR / rs
    return np.stack([Bx, By, Bz], axis=1)


def boris(q, N=400, v=0.1, T=300.0, dt=0.05, seed=3):
    rng = np.random.default_rng(seed)
    r0 = rng.uniform(0.05, 0.2, N)
    th0 = rng.uniform(0, 2 * np.pi, N)
    ph0 = rng.uniform(0, 2 * np.pi, N)
    R = R0 + r0 * np.cos(th0)
    x = np.stack([R * np.cos(ph0), R * np.sin(ph0), r0 * np.sin(th0)], axis=1)
    u = rng.normal(size=(N, 3))
    u *= v / np.linalg.norm(u, axis=1, keepdims=True)
    alive = np.ones(N, bool)
    t_lost = np.full(N, np.inf)
    nsteps = int(T / dt)
    ts, frac = [0.0], [1.0]
    e0 = (u ** 2).sum(1)
    for k in range(nsteps):
        B = field(x, q)
        tvec = 0.5 * dt * B                     # q/m = 1, E = 0
        s = 2 * tvec / (1 + (tvec ** 2).sum(1, keepdims=True))
        up = u + np.cross(u, tvec)
        u = u + np.cross(up, s)
        x = x + dt * u
        R = np.hypot(x[:, 0], x[:, 1])
        rmin = np.hypot(R - R0, x[:, 2])
        newly = alive & (rmin > A_MINOR)
        t_lost[newly] = (k + 1) * dt
        alive &= ~newly
        if k % 50 == 49:
            ts.append((k + 1) * dt)
            frac.append(alive.mean())
    de = np.abs((u ** 2).sum(1) / e0 - 1).max()
    return dict(t=np.array(ts), frac=np.array(frac), final=alive.mean(),
                t_med=np.median(t_lost[np.isfinite(t_lost)]) if np.isfinite(t_lost).any() else np.inf,
                dE=de)


def poincare(r_start, eps, m=3, n=2, turns=400, steps_per_turn=200, th_start=None):
    qf = lambda r: 1.2 + 1.5 * (r / A_MINOR) ** 2
    h = 2 * np.pi / steps_per_turn
    r = np.array(r_start, float)
    th = np.zeros(len(r)) if th_start is None else np.array(th_start, float)
    z = 0.0
    pr, pt = [], []

    def f(r, th, z):
        return eps * A_MINOR * np.sin(m * th - n * z), 1.0 / qf(r)

    for k in range(turns):
        for _ in range(steps_per_turn):
            k1 = f(r, th, z)
            k2 = f(r + 0.5 * h * k1[0], th + 0.5 * h * k1[1], z + 0.5 * h)
            k3 = f(r + 0.5 * h * k2[0], th + 0.5 * h * k2[1], z + 0.5 * h)
            k4 = f(r + h * k3[0], th + h * k3[1], z + h)
            r = r + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
            th = th + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
            z += h
        pr.append(r.copy())
        pt.append(np.mod(th, 2 * np.pi))
    return np.array(pr), np.array(pt)


def r_of_q(qv):
    return A_MINOR * np.sqrt((qv - 1.2) / 1.5)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                                  "docs", "images", "toroidal_particle_trace_boris.png"))
    args = ap.parse_args()
    cases = [("pure toroidal (no B_pol)", None), ("q = 3", 3.0), ("q = 2", 2.0), ("q = 1.5", 1.5),
             ("q = sqrt2", 2 ** 0.5), ("q = phi", PHI)]
    res = {}
    print("PART A: Boris test particles (N=400, v=0.1, B0=5, T=300, lost if r > a=0.35)")
    print(f"{'case':26s} {'confined':>9s} {'median t_loss':>13s} {'max |dE/E|':>11s}")
    for name, q in cases:
        r = boris(q)
        res[name] = r
        print(f"{name:26s} {r['final']:9.3f} {r['t_med']:13.1f} {r['dE']:11.2e}")

    print("\nPART B: field-line Poincare, q(r) = 1.2 + 1.5 (r/a)^2, perturbation m/n = 3/2")
    labels = [("q = 1.5 (resonant)", 1.5), ("q = sqrt2", 2 ** 0.5), ("q = phi", PHI)]
    starts = [r_of_q(qv) for _, qv in labels]
    nth = 8                                     # several launch angles per surface (avoid sitting on an X/O point)
    th_l = np.tile(np.linspace(0, 2 * np.pi / 3, nth, endpoint=False), len(starts))
    r_l = np.repeat(starts, nth)
    print("radial spread / a = max over launch angles of (max r - min r) on the Poincare section")
    for eps in (0.0, 2e-4, 1e-3):
        pr, pt = poincare(r_l, eps, th_start=th_l)
        spread = ((pr.max(0) - pr.min(0)) / A_MINOR).reshape(len(starts), nth).max(1)
        print(f"eps = {eps:6.0e}:  " + "  ".join(f"{lab}: {sp:.4f}" for (lab, _), sp in zip(labels, spread)))

    # dense Poincare for the plot
    rs_dense = np.linspace(0.12, 0.33, 22) * 1.0
    th_d = np.concatenate([np.zeros(len(rs_dense)), np.full(len(starts), 0.5)])
    prd, ptd = poincare(list(rs_dense) + starts, 1e-3, turns=250, th_start=th_d)

    fig, axes = plt.subplots(1, 3, figsize=(16, 5), constrained_layout=True)
    for name, r in res.items():
        axes[0].plot(r["t"], r["frac"], label=name)
    axes[0].set_xlabel("t (dimensionless; on-axis omega_c = 5)")
    axes[0].set_ylabel("confined fraction")
    axes[0].set_title("A. Boris pusher: confinement vs time", fontsize=10)
    axes[0].legend(fontsize=8)
    names = list(res)
    axes[1].bar(range(len(names)), [res[n]["final"] for n in names],
                color=["tab:red"] + ["tab:blue"] * 3 + ["tab:green", "tab:orange"])
    axes[1].set_xticks(range(len(names)))
    axes[1].set_xticklabels(names, rotation=25, ha="right", fontsize=8)
    axes[1].set_ylim(0, 1.05)
    axes[1].set_title("A. confined fraction at T = 300", fontsize=10)
    ax = axes[2]
    ax.scatter(ptd[:, :len(rs_dense)].ravel(), prd[:, :len(rs_dense)].ravel() / A_MINOR, s=0.2, c="grey")
    for j, ((lab, _), col) in enumerate(zip(labels, ["tab:red", "tab:green", "tab:orange"])):
        ax.scatter(ptd[:, len(rs_dense) + j], prd[:, len(rs_dense) + j] / A_MINOR, s=0.8, c=col, label=lab)
    ax.set_xlabel("theta (Poincare section, zeta = 0 mod 2pi)")
    ax.set_ylabel("r / a")
    ax.set_title("B. field lines, m/n = 3/2 perturbation, eps = 1e-3", fontsize=10)
    ax.legend(fontsize=8, markerscale=8)
    fig.suptitle("Toroidal particle tracing (Boris) and field-line islands: rotational transform confines; "
                 "irrational q only matters relative to a perturbation", fontsize=10)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    fig.savefig(args.out, dpi=100)
    print("saved", os.path.abspath(args.out))


if __name__ == "__main__":
    main()

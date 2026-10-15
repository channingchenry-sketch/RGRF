#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""
floquet_ssh_pi_modes.py  --  periodically driven (two-step) SSH chain: 0-modes, pi-modes, winding numbers, phi ablation.

Model (Asboth, Tarasinski & Delplace 2014, PRB 90, 125143; dimensionless, hbar = 1):
  One drive period = step 1 (intracell hopping only, for time T1) then step 2 (intercell hopping only, T2).
      U = exp(-i theta2 H_w) exp(-i theta1 H_v),   theta1 = v T1,  theta2 = w T2,
  where H_v couples A_n-B_n and H_w couples B_n-A_{n+1} (each with eigenvalues +-1 on its dimers).
  Quasienergy eps = -arg(eigenvalue of U), defined mod 2pi (the quasienergy Brillouin zone).
  Bulk: cos eps(k) = cos theta1 cos theta2 - sin theta1 sin theta2 cos k, so gaps close (at eps = 0 or pi)
  only on the lines theta1 +- theta2 = m pi.

PART A: open chain of N_CELLS = 40 cells. Count edge-localised eigenstates at eps ~ 0 and eps ~ pi
  (weight > 0.6 in the outer 4 cells on either side) across the (theta1, theta2) plane.
PART B: bulk invariants. Chiral symmetry (Gamma = sigma_z) holds in the two symmetric time frames
      U1 = e^{-i theta1 H_v/2} e^{-i theta2 H_w} e^{-i theta1 H_v/2},
      U2 = e^{-i theta2 H_w/2} e^{-i theta1 H_v} e^{-i theta2 H_w/2}.
  Write U_j(k) = cos eps - i sin eps (n_j(k) . sigma), with n_j in the xy plane. nu_j = winding of n_j over k.
  Then W0 = (nu1 + nu2)/2 and Wpi = (nu1 - nu2)/2 (sign convention fixed by matching the edge count).
  The script checks |W0|, |Wpi| against the edge-mode counts per edge (bulk-boundary correspondence).
PART C: phi ablation. Equal hoppings v = w = J; fixed total period T, split T1/T2 = r.
  r in {phi, 8/5, 3/2, sqrt2, 5/3, 2, 1}. Scan J*T in (0, 4 pi). Record the phase (W0, Wpi) along the scan,
  where transitions occur, and the mean bulk gap at 0 and pi. Topology depends only on which gap-closing lines
  the path (theta1, theta2) = J T (r, 1)/(1 + r) crosses, so a "phi advantage" would have to show up here.

Labels: Floquet SSH 0/pi edge modes and W0/Wpi bulk-boundary correspondence = Grounded (textbook physics,
reproduced numerically). This is a single-particle, non-interacting, lossless lattice toy; it says nothing
directly about plasmas or craft. Requires numpy and matplotlib.
"""
import argparse
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PHI = (1 + 5 ** 0.5) / 2
N_CELLS = 40
EDGE_CELLS = 4


# ---------- open chain ----------
def chain_hams(n=N_CELLS):
    d = 2 * n
    Hv = np.zeros((d, d))
    Hw = np.zeros((d, d))
    for c in range(n):
        Hv[2 * c, 2 * c + 1] = Hv[2 * c + 1, 2 * c] = 1.0
        if c < n - 1:
            Hw[2 * c + 1, 2 * c + 2] = Hw[2 * c + 2, 2 * c + 1] = 1.0
    return Hv, Hw


def expm_h(H, theta):
    w, V = np.linalg.eigh(H)
    return (V * np.exp(-1j * theta * w)) @ V.conj().T


_EIG = {}


def open_floquet(theta1, theta2, n=N_CELLS):
    if n not in _EIG:
        Hv, Hw = chain_hams(n)
        _EIG[n] = (np.linalg.eigh(Hv), np.linalg.eigh(Hw))
    (wv, Vv), (ww, Vw) = _EIG[n]
    Uv = (Vv * np.exp(-1j * theta1 * wv)) @ Vv.conj().T
    Uw = (Vw * np.exp(-1j * theta2 * ww)) @ Vw.conj().T
    return Uw @ Uv


def edge_counts(theta1, theta2, n=N_CELLS, tol=0.05):
    U = open_floquet(theta1, theta2, n)
    lam, V = np.linalg.eig(U)
    eps = -np.angle(lam)
    w = np.abs(V) ** 2
    w /= w.sum(0, keepdims=True)
    edge_w = w[: 2 * EDGE_CELLS].sum(0) + w[-2 * EDGE_CELLS:].sum(0)
    loc = edge_w > 0.6
    n0 = np.sum(loc & (np.abs(eps) < tol))
    npi = np.sum(loc & (np.abs(np.abs(eps) - np.pi) < tol))
    return n0 // 2, npi // 2, eps  # per edge


# ---------- bulk ----------
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]])
I2 = np.eye(2)


def rot(theta, nvec):
    return np.cos(theta) * I2 - 1j * np.sin(theta) * nvec


def bulk_windings(theta1, theta2, nk=401):
    """Vectorised over k: windings nu1, nu2 of n_j(k) in the two chiral frames, and min bulk gaps at 0 and pi."""
    ks = np.linspace(-np.pi, np.pi, nk)
    hv = np.broadcast_to(SX, (nk, 2, 2))
    hw = np.cos(ks)[:, None, None] * SX + np.sin(ks)[:, None, None] * SY
    U1 = rot(theta1 / 2, hv) @ rot(theta2, hw) @ rot(theta1 / 2, hv)
    U2 = rot(theta2 / 2, hw) @ rot(theta1, hv) @ rot(theta2 / 2, hw)
    nu = {}
    for j, U in ((1, U1), (2, U2)):
        c = np.real(np.trace(U, axis1=1, axis2=2)) / 2
        M = U - c[:, None, None] * I2
        nx = np.real(1j * np.trace(M @ SX, axis1=1, axis2=2) / 2)
        ny = np.real(1j * np.trace(M @ SY, axis1=1, axis2=2) / 2)
        a = np.unwrap(np.arctan2(ny, nx))
        nu[j] = int(np.round((a[-1] - a[0]) / (2 * np.pi)))
    eps = np.arccos(np.clip(np.real(np.trace(U1, axis1=1, axis2=2)) / 2, -1, 1))
    return nu[1], nu[2], eps.min(), (np.pi - eps).min()


def invariants(theta1, theta2, sign=1):
    n1, n2, g0, gpi = bulk_windings(theta1, theta2)
    W0 = sign * (n1 + n2) // 2 if (n1 + n2) % 2 == 0 else np.nan
    Wpi = sign * (n1 - n2) // 2 if (n1 - n2) % 2 == 0 else np.nan
    return W0, Wpi, g0, gpi


def main():
    ap = argparse.ArgumentParser(description="Floquet SSH 0/pi modes + phi ablation")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                                  "docs", "images", "floquet_ssh_pi_modes.png"))
    ap.add_argument("--grid", type=int, default=41)
    args = ap.parse_args()

    # PART A + B: phase diagram over (theta1, theta2) in (0, pi)^2, avoiding exact gap-closing lines
    g = np.linspace(0, np.pi, args.grid + 2)[1:-1] + 1e-3
    E0 = np.zeros((len(g), len(g)), int)
    Epi = np.zeros_like(E0)
    B0 = np.zeros_like(E0, float)
    Bpi = np.zeros_like(B0)
    for i, t2 in enumerate(g):
        for j, t1 in enumerate(g):
            E0[i, j], Epi[i, j], _ = edge_counts(t1, t2)
            W0, Wpi, g0, gpi = invariants(t1, t2)
            B0[i, j], Bpi[i, j] = W0, Wpi
    # mask points within 0.06 of a gap-closing line (finite-size / tolerance region)
    T1, T2 = np.meshgrid(g, g)
    near = np.zeros_like(T1, bool)
    for m in range(-2, 3):
        near |= np.abs(T1 + T2 - m * np.pi) < 0.08
        near |= np.abs(T1 - T2 - m * np.pi) < 0.08
    ok = ~near
    agree = np.mean((np.abs(B0[ok]) == E0[ok]) & (np.abs(Bpi[ok]) == Epi[ok]))
    print(f"PART A/B: open chain {N_CELLS} cells, (theta1, theta2) grid {args.grid}x{args.grid} in (0, pi)^2")
    print(f"  bulk |W0|,|Wpi| == edge-mode counts per edge at {agree*100:.1f}% of points away from gap-closing lines")
    for lab, (a, b) in {"theta1=0.5, theta2=1.0 (static-SSH-like)": (0.5, 1.0),
                        "theta1=1.0, theta2=0.5 (trivial)": (1.0, 0.5),
                        "theta1=2.6, theta2=1.0": (2.6, 1.0),
                        "theta1=2.0, theta2=2.6": (2.0, 2.6)}.items():
        e0, epi, _ = edge_counts(a, b)
        W0, Wpi, g0, gpi = invariants(a, b)
        print(f"  {lab:40s} edge 0-modes {e0}, pi-modes {epi};  W0 = {W0}, Wpi = {Wpi};  gaps {g0:.2f}, {gpi:.2f}")

    # PART C: phi ablation
    ratios = [("phi", PHI), ("8/5", 1.6), ("5/3", 5 / 3), ("3/2", 1.5), ("sqrt2", 2 ** 0.5), ("2", 2.0)]  # r = 1 sits exactly on the theta1 = theta2 gap-closing line (critical), so it is excluded
    JT = np.linspace(0.02, 4 * np.pi - 0.02, 400)
    print("\nPART C: v = w = J, total period T split T1/T2 = r; scan J*T in (0, 4 pi)")
    print(f"{'r':>6s} {'frac(W0!=0)':>11s} {'frac(Wpi!=0)':>12s} {'frac(both)':>10s} {'mean gap0':>9s} {'mean gapPi':>10s}  transitions (J*T/pi)")
    traces = {}
    for name, r in ratios:
        th1 = JT * r / (1 + r)
        th2 = JT / (1 + r)
        inv = np.array([invariants(a, b) for a, b in zip(th1, th2)], float)
        W0, Wpi, g0, gpi = inv.T
        traces[name] = (W0, Wpi)
        valid = np.isfinite(W0) & np.isfinite(Wpi)
        key = np.where(valid, np.abs(W0) * 10 + np.abs(Wpi), -1)
        tr = JT[1:][np.diff(key) != 0] / np.pi
        print(f"{name:>6s} {np.mean(np.abs(W0[valid]) > 0):11.3f} {np.mean(np.abs(Wpi[valid]) > 0):12.3f} "
              f"{np.mean((np.abs(W0[valid]) > 0) & (np.abs(Wpi[valid]) > 0)):10.3f} {g0.mean():9.3f} {gpi.mean():10.3f}  "
              + ", ".join(f"{x:.2f}" for x in tr))
    print("  analytic transitions: J*T = m*pi (theta1+theta2) for every r, and J*T*(r-1)/(r+1) = m*pi (theta1-theta2)")

    # ---------- plot ----------
    fig, axes = plt.subplots(1, 4, figsize=(20, 4.8), constrained_layout=True)
    code = np.where(ok, E0 * 2 + Epi, np.nan)
    im = axes[0].imshow(code, origin="lower", extent=[g[0], g[-1], g[0], g[-1]], cmap="viridis", vmin=0, vmax=3)
    cb = fig.colorbar(im, ax=axes[0], ticks=[0, 1, 2, 3])
    cb.ax.set_yticklabels(["none", "pi only", "0 only", "0 and pi"])
    for name, r in ratios:
        if name in ("phi", "3/2", "2"):
            tt = np.linspace(0, np.pi * (1 + r) / r, 50)
            axes[0].plot(np.clip(tt * r / (1 + r), 0, np.pi), np.clip(tt / (1 + r), 0, np.pi), lw=1,
                         label=f"r = {name}")
    axes[0].set_xlim(0, np.pi); axes[0].set_ylim(0, np.pi)
    axes[0].set_xlabel("theta1 = v T1"); axes[0].set_ylabel("theta2 = w T2")
    axes[0].set_title(f"A. edge modes per edge, open chain ({N_CELLS} cells)", fontsize=10)
    axes[0].legend(fontsize=7, loc="upper right")

    t2s = np.linspace(0.01, np.pi - 0.01, 160)
    t1 = 2.0
    for t2 in t2s:
        _, _, eps = edge_counts(t1, t2)
        axes[1].plot(np.full_like(eps, t2), eps, ",k")
    axes[1].set_xlabel("theta2 (theta1 = 2.0 fixed)"); axes[1].set_ylabel("quasienergy eps")
    axes[1].set_yticks([-np.pi, 0, np.pi]); axes[1].set_yticklabels(["-pi", "0", "pi"])
    axes[1].set_title("B. open-chain quasienergy spectrum: 0 and pi edge modes", fontsize=10)

    for name, (W0, Wpi) in traces.items():
        if name in ("phi", "8/5", "3/2", "sqrt2", "2"):
            axes[2].plot(JT / np.pi, np.abs(W0) + 0.03 * list(traces).index(name), label=f"|W0|, r = {name}", lw=1)
            axes[3].plot(JT / np.pi, np.abs(Wpi) + 0.03 * list(traces).index(name), label=f"|Wpi|, r = {name}", lw=1)
    for ax, t in ((axes[2], "C. |W0| vs J*T (phi ablation)"), (axes[3], "C. |Wpi| vs J*T (phi ablation)")):
        ax.set_xlabel("J T / pi"); ax.set_title(t, fontsize=10); ax.legend(fontsize=7)
    fig.suptitle("Floquet SSH chain: 0- and pi-modes follow gap closings; the split ratio r = phi only moves "
                 "transitions smoothly, like any nearby rational", fontsize=10)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    fig.savefig(args.out, dpi=100)
    print("saved", os.path.abspath(args.out))


if __name__ == "__main__":
    main()

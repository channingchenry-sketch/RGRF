#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""
toroidal_induction_2d_ablation.py  --  ABLATION TOY, NOT MHD, NOT A DYNAMO.

Companion to sims/toroidal_induction_1d.py (docs/tungsten_bismuth_core.md 7b-dyn.2).
Grok's second recreation (code not supplied) added a shear-advection proxy, mild
high-k filtering, soft saturation and a drive "locked to low modes". This script
holds those ingredients FIXED and changes only the drive, to ask whether the
golden ratio (phi) adds anything beyond them.

MODEL (doubly periodic 2D, pseudo-spectral, RK4)
  dB/dt + U(y) dB/dx = eta Lap B + S(x, y, t) - lam * B * (B/Bs)^2
  U(y) = U0 sin(y)       shear-advection proxy (passive advection of a scalar B,
                         NOT the induction term curl(u x B); no field stretching)
  high-k filter          exponential spectral filter applied every step (|k| > kc)
  soft saturation        cubic damping -lam B (B/Bs)^2 (bounds the amplitude)
  eta = 0.01, f = 7.8 (scaled units, not physical Hz).
  Initial field: fixed-seed multi-mode random field (|k| <= 8), RMS 0.6.

DRIVES (all locked to the low modes cos x, cos y; amplitude A)
  low-mode lock (no phi): A sin(w t) [cos x + cos y]
  phi:     A sin(w t) [cos x + (1 + 0.5 sin(w t/phi)) cos(y + 2pi/phi^2)]
  control: same with sqrt(2) in place of phi
  control 1/2: same with 2 in place of phi
  no drive

WHAT IT IS NOT
  No u x B induction term, no stretching, no current/q profile, no kink or tearing
  physics: it cannot show a dynamo or tokamak shear stabilization. Low-mode
  coherence, bounded amplitude and high-k suppression are BUILT IN by the drive,
  saturation and filter. Label: Plausible-untested, insight only; behavior
  "reproduced by construction".
Requires numpy and matplotlib.
"""
import argparse
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PHI = (1 + 5 ** 0.5) / 2
TWO_PI = 2 * np.pi


def run(drive, N=64, eta=0.01, U0=0.5, f=7.8, A=30.0, lam=1.0, Bs=1.0, kc=8.0,
        T=40.0, dt=0.005, seed=1):
    x = np.linspace(0, TWO_PI, N, endpoint=False)
    X, Y = np.meshgrid(x, x, indexing="ij")
    k = np.fft.fftfreq(N, 1.0 / N)
    KX, KY = np.meshgrid(k, k, indexing="ij")
    K2 = KX ** 2 + KY ** 2
    filt = np.exp(-36.0 * np.clip((np.sqrt(K2) - kc) / (N / 2 - kc), 0, None) ** 4)  # mild high-k filter
    low = (np.abs(KX) <= 1) & (np.abs(KY) <= 1) & (K2 > 0)
    rng = np.random.default_rng(seed)
    Bh = np.where((K2 > 0) & (K2 <= 64), rng.normal(size=K2.shape) + 1j * rng.normal(size=K2.shape), 0)
    B = np.real(np.fft.ifft2(Bh))
    B *= 0.6 / B.std()
    U = U0 * np.sin(Y)
    w = TWO_PI * f
    cx, cy = np.cos(X), np.cos(Y)

    def S(t):
        if drive == "none":
            return 0.0
        if drive == "lock":
            return A * np.sin(w * t) * (cx + cy)
        r = {"phi": PHI, "sqrt2": 2 ** 0.5, "half": 2.0}[drive]
        return A * np.sin(w * t) * (cx + (1 + 0.5 * np.sin(w * t / r)) * np.cos(Y + TWO_PI / r ** 2))

    def rhs(B, t):
        Bh = np.fft.fft2(B)
        dBdx = np.real(np.fft.ifft2(1j * KX * Bh))
        lap = np.real(np.fft.ifft2(-K2 * Bh))
        return -U * dBdx + eta * lap + S(t) - lam * B * (B / Bs) ** 2

    def share(B):
        P = np.abs(np.fft.fft2(B)) ** 2
        return P[low].sum() / max(P[K2 > 0].sum(), 1e-30)

    n = int(round(T / dt))
    t = 0.0
    ts, sh, mx = [0.0], [share(B)], [np.abs(B).max()]
    for i in range(n):
        k1 = rhs(B, t)
        k2 = rhs(B + 0.5 * dt * k1, t + 0.5 * dt)
        k3 = rhs(B + 0.5 * dt * k2, t + 0.5 * dt)
        k4 = rhs(B + dt * k3, t + dt)
        B = B + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        B = np.real(np.fft.ifft2(np.fft.fft2(B) * filt))
        t += dt
        if i % 20 == 19:
            ts.append(t)
            sh.append(share(B))
            mx.append(np.abs(B).max())
    ts, sh, mx = map(np.array, (ts, sh, mx))
    late = ts > T / 2
    return dict(x=x, B=B, t=ts, share=sh, maxB=mx, share_T=sh[-1], max_T=mx[-1],
                share_late=sh[late].mean(), max_late=mx[late].mean())


def main():
    ap = argparse.ArgumentParser(description="Ablation toy (not MHD, not a dynamo).")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                                  "docs", "images", "toroidal_induction_2d_ablation.png"))
    args = ap.parse_args()
    cases = [("phi drive", "phi"), ("control sqrt2", "sqrt2"), ("control 1/2", "half"),
             ("low-mode lock, no phi", "lock"), ("no drive", "none")]
    res = {}
    print("ABLATION TOY (no u x B, no dynamo). Shear proxy + filter + saturation fixed in all cases.")
    print(f"{'case':24s} {'share t=0':>9s} {'share T':>8s} {'share late':>10s} {'max|B| T':>9s} {'max|B| late':>11s}")
    for name, d in cases:
        r = run(d)
        res[name] = r
        print(f"{name:24s} {r['share'][0]:9.3f} {r['share_T']:8.3f} {r['share_late']:10.3f} "
              f"{r['max_T']:9.4f} {r['max_late']:11.4f}")
    fig, axes = plt.subplots(2, 3, figsize=(15, 8.5), constrained_layout=True)
    for ax, name in zip(axes[0], ["phi drive", "control sqrt2", "low-mode lock, no phi"]):
        r = res[name]
        v = np.abs(r["B"]).max()
        im = ax.pcolormesh(r["x"], r["x"], r["B"].T, cmap="RdBu_r", vmin=-v, vmax=v, shading="auto")
        ax.set_title(f"B(x, y) at t = 40: {name}", fontsize=9)
        ax.set_aspect("equal")
        fig.colorbar(im, ax=ax)
    for name, r in res.items():
        axes[1, 0].plot(r["t"], r["share"], lw=1, label=name)
        axes[1, 1].plot(r["t"], r["maxB"], lw=0.8, label=name)
    axes[1, 0].set_title("low-mode share (|kx|,|ky| <= 1)", fontsize=9)
    axes[1, 0].legend(fontsize=7)
    axes[1, 1].set_title("max |B| vs time", fontsize=9)
    for a in axes[1, :2]:
        a.set_xlabel("t (scaled)")
    names = list(res)
    axes[1, 2].bar(range(len(names)), [res[n]["max_late"] for n in names])
    axes[1, 2].set_xticks(range(len(names)))
    axes[1, 2].set_xticklabels(names, rotation=25, ha="right", fontsize=7)
    axes[1, 2].set_title("mean max |B| over t > 20", fontsize=9)
    fig.suptitle("2D ablation toy: shear-advection proxy + high-k filter + soft saturation held fixed; only the drive changes. "
                 "NOT MHD, no u×B, no dynamo. Plausible-untested, insight only", fontsize=10)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    fig.savefig(args.out, dpi=100)
    print("saved", os.path.abspath(args.out))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""
toroidal_induction_1d.py  --  LINEAR DIFFUSION-PLUS-FORCING TOY, NOT MHD, NOT A DYNAMO.

Rebuild (2026-10-15) of the lost "1D periodic toroidal induction model with
Schumann/phi drive" described in docs/tungsten_bismuth_core.md section 7b-dyn.2.
The original code was not supplied; this is an independent re-implementation.

MODEL
  Periodic x in [0, 2*pi) stands in for the closed toroidal loop.
      dB/dt = eta * d2B/dx2 + S(x, t),        eta = 0.01
  S = A * sin(2*pi*f*t + psi_j) * Gaussian(x - x_j), summed over drive sites j,
  with f = 7.8 in SCALED units (a nod to the Schumann fundamental, NOT physical:
  nothing here has units of seconds or Hz).
  Initial "helical-like" field: a few Fourier modes.
  Integrated with scipy solve_ivp (RK45); second derivative by periodic finite
  differences.

CASES
  no drive; single drive; and two-site drives whose second site and phase use
    phi     : offset 2*pi/phi along the loop, phase offset 2*pi/phi^2 (golden angle)
    1/2     : offset pi,       phase offset pi
    1/3     : offset 2*pi/3,   phase offset 2*pi/3
    sqrt2   : offset 2*pi/sqrt2 (mod 2*pi), phase offset 2*pi/sqrt2 (another irrational)

WHAT IT IS NOT
  There is NO u x B term (no flow), so there is no field stretching and NO dynamo
  action: consistent with Cowling-type anti-dynamo limits, this field can only
  decay or follow the forcing. The equation is LINEAR, so every response is a
  superposition of the decaying initial modes and the forced response to each
  drive site. "Resonance" here is a forced response, not self-sustaining.
  "Coherence" growth is expected because diffusion damps mode k at rate eta*k^2.
  Label: Plausible-untested, as insight only. Phi "optimization": Speculative
  unless the metrics below show a real advantage (they are printed honestly).

Requires numpy, scipy, matplotlib.
"""
import argparse
import os

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PHI = (1 + 5 ** 0.5) / 2
TWO_PI = 2 * np.pi


def gauss(x, x0, s):
    d = (x - x0 + np.pi) % TWO_PI - np.pi        # periodic distance
    return np.exp(-d ** 2 / (2 * s ** 2))


def run(sites, N=256, eta=0.01, f=7.8, A=10.0, sigma=0.3, T=40.0, nt=801):
    x = np.linspace(0, TWO_PI, N, endpoint=False)
    dx = x[1] - x[0]
    B0 = np.sin(x) + 0.5 * np.sin(3 * x + 0.7) + 0.3 * np.sin(7 * x + 1.3)
    G = [(gauss(x, x0, sigma), psi) for x0, psi in sites]

    def rhs(t, B):
        d2 = (np.roll(B, -1) - 2 * B + np.roll(B, 1)) / dx ** 2
        s = np.zeros_like(B)
        for g, psi in G:
            s += A * np.sin(TWO_PI * f * t + psi) * g
        return eta * d2 + s

    ts = np.linspace(0, T, nt)
    sol = solve_ivp(rhs, (0, T), B0, method="RK45", t_eval=ts, rtol=1e-7, atol=1e-9, max_step=0.01)
    Bt = sol.y.T                                    # (nt, N)
    E = (Bt ** 2).mean(axis=1)
    Bk = np.abs(np.fft.rfft(Bt, axis=1)) ** 2
    low = Bk[:, 1:3].sum(axis=1) / np.maximum(Bk[:, 1:].sum(axis=1), 1e-30)   # energy share in k = 1, 2
    late = ts > T / 2
    # forced part = B minus the (analytically known) decaying initial modes
    decay = (np.exp(-eta * ts)[:, None] * np.sin(x)[None]
             + 0.5 * np.exp(-9 * eta * ts)[:, None] * np.sin(3 * x + 0.7)[None]
             + 0.3 * np.exp(-49 * eta * ts)[:, None] * np.sin(7 * x + 1.3)[None])
    forced = Bt - decay
    return dict(x=x, t=ts, B=Bt, E=E, low=low, maxB=np.abs(Bt[-1]).max(),
                forced_rms=np.sqrt((forced[late] ** 2).mean()),
                drive_rms=np.sqrt(sum(((A * g) ** 2).mean() / 2 for g, _ in G)) if G else 0.0)


def main():
    ap = argparse.ArgumentParser(description="Linear diffusion+forcing toy (not MHD, not a dynamo).")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                                  "docs", "images", "toroidal_induction_1d.png"))
    ap.add_argument("--A", type=float, default=10.0)
    args = ap.parse_args()
    x0 = 1.0
    cases = {
        "no drive": [],
        "single drive": [(x0, 0.0)],
        "phi (2pi/phi, golden angle)": [(x0, 0.0), (x0 + TWO_PI / PHI, TWO_PI / PHI ** 2)],
        "control 1/2 (pi, pi)": [(x0, 0.0), (x0 + np.pi, np.pi)],
        "control 1/3": [(x0, 0.0), (x0 + TWO_PI / 3, TWO_PI / 3)],
        "control sqrt2": [(x0, 0.0), (x0 + (TWO_PI / 2 ** 0.5) % TWO_PI, (TWO_PI / 2 ** 0.5) % TWO_PI)],
    }
    res = {}
    print("LINEAR DIFFUSION+FORCING TOY (no u x B, no dynamo). Label: Plausible-untested, insight only.")
    print(f"{'case':30s} {'max|B| final':>12s} {'E(0)':>7s} {'E(T)':>7s} {'low-k share T':>13s} "
          f"{'forced RMS':>10s} {'forced/drive':>12s}")
    for name, sites in cases.items():
        r = run(sites, A=args.A)
        res[name] = r
        eff = r["forced_rms"] / r["drive_rms"] if r["drive_rms"] else float("nan")
        print(f"{name:30s} {r['maxB']:12.4f} {r['E'][0]:7.4f} {r['E'][-1]:7.4f} {r['low'][-1]:13.3f} "
              f"{r['forced_rms']:10.5f} {eff:12.5f}")

    fig, axes = plt.subplots(2, 3, figsize=(15, 8.5), constrained_layout=True)
    for ax, name in zip(axes[0], ["no drive", "phi (2pi/phi, golden angle)", "control 1/2 (pi, pi)"]):
        r = res[name]
        v = np.abs(r["B"]).max()
        im = ax.pcolormesh(r["x"], r["t"], r["B"], cmap="RdBu_r", vmin=-v, vmax=v, shading="auto")
        ax.set_title(f"B(x, t): {name}", fontsize=9)
        ax.set_xlabel("x (loop coordinate)")
        ax.set_ylabel("t (scaled)")
        fig.colorbar(im, ax=ax)
    ax = axes[1, 0]
    for name, r in res.items():
        ax.plot(r["t"], r["E"], lw=1, label=name)
    ax.set_title("energy <B²> vs time", fontsize=9)
    ax.set_xlabel("t")
    ax.legend(fontsize=7)
    ax = axes[1, 1]
    for name, r in res.items():
        ax.plot(r["t"], r["low"], lw=1, label=name)
    ax.set_title("'coherence': energy share in k = 1, 2", fontsize=9)
    ax.set_xlabel("t")
    ax = axes[1, 2]
    names = [n for n in res if n != "no drive"]
    ax.bar(range(len(names)), [res[n]["forced_rms"] / res[n]["drive_rms"] for n in names])
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=25, ha="right", fontsize=7)
    ax.set_title("forced response RMS / drive RMS ('efficiency')", fontsize=9)
    fig.suptitle("1D periodic 'toroidal' induction toy: dB/dt = η B'' + S (η = 0.01, f = 7.8 scaled). "
                 "LINEAR, no u×B, no dynamo. Label: Plausible-untested, insight only", fontsize=10)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    fig.savefig(args.out, dpi=100)
    print("saved", os.path.abspath(args.out))


if __name__ == "__main__":
    main()

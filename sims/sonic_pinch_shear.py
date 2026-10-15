#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""
sonic_pinch_shear.py  --  TOY ACOUSTIC PROXY, NOT MHD.

Rebuild (2026-10-15) of the lost simplified "sonic pinching" sim described in
docs/tungsten_bismuth_core.md section 3a, following the "Grok recreation
description" archived there (Grok's own code was not supplied, so this is an
independent re-implementation of that description, not the original).

MODEL (2D finite difference, c = 1)
  Background shear flow U_x(y) = U0 tanh(y / delta)   (divergence-free).
  Linearized continuity:  d(rho)/dt + U d(rho)/dx + div(v) = S(x, y, t)
  Linearized momentum:    dv/dt + U dv/dx + (v . grad) U   = -c^2 grad(rho)
                          ((v . grad)U = (v_y U'(y), 0))
  Acoustic relation p = c^2 rho.  Initial Gaussian density pulse at the centre.
  S = intermittent (pulsed) Gaussian source at the centre, standing in for pulsed
  electrode modulation / localized gas injection.
  Reflective walls (normal velocity = 0, d(rho)/dn = 0), RK4, CFL-limited dt,
  a small numerical diffusion nu for stability of the central differences.
  Cases: shear +/- source, and no-shear +/- source.

WHAT IT IS NOT
  There is NO magnetic field: no j x B (no actual pinch force), no magnetic
  pressure or tension, no induction, no ambipolar diffusion, no Alfven waves and
  no kink / sausage growth physics.  It CANNOT show real pinch stabilization by
  sheared flow (Shumlak & Hartman 1995).  A pulsed central source adds density at
  the centre by construction, so any "sustained central peak" is a FORCED
  balance between injection and spreading, not self-organization.
  Label of all outputs: Plausible-untested, as an analog only.

OUTPUT
  Prints a metrics table and saves a PNG (default docs/images/sonic_pinch_shear.png):
  rho snapshots and peak |rho| / central rho vs time.
Requires numpy and matplotlib only.
"""
import argparse
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def run(shear=True, source=True, U0=0.5, delta=0.2, N=129, T=3.0, nu=1e-3,
        src_amp=20.0, src_sigma=0.05, period=0.2, duty=0.25, snap_times=(0.0, 0.5, 1.0, 3.0)):
    x = np.linspace(-1, 1, N)
    y = np.linspace(-1, 1, N)
    h = x[1] - x[0]
    X, Y = np.meshgrid(x, y, indexing="ij")
    if shear:
        U = U0 * np.tanh(Y / delta)
        dU = U0 / delta / np.cosh(Y / delta) ** 2
    else:
        U = np.zeros_like(Y)
        dU = np.zeros_like(Y)
    g = np.exp(-(X ** 2 + Y ** 2) / (2 * src_sigma ** 2))
    centre = (X ** 2 + Y ** 2) < 0.1 ** 2

    def S(t):
        if not source:
            return 0.0
        return src_amp * g if (t % period) < duty * period else 0.0

    def pad(f, ax, odd):
        f = np.moveaxis(f, ax, 0)
        lo, hi = f[1:2], f[-2:-1]
        if odd:
            lo, hi = -lo, -hi
        return np.moveaxis(np.concatenate([lo, f, hi], 0), 0, ax)

    def d(f, ax, odd):
        fp = pad(f, ax, odd)
        sl = [slice(None)] * 2
        a, b = list(sl), list(sl)
        a[ax], b[ax] = slice(2, None), slice(None, -2)
        return (fp[tuple(a)] - fp[tuple(b)]) / (2 * h)

    def lap(f, oddx, oddy):
        fx, fy = pad(f, 0, oddx), pad(f, 1, oddy)
        return ((fx[2:] - 2 * f + fx[:-2]) + (fy[:, 2:] - 2 * f + fy[:, :-2])) / h ** 2

    def rhs(r, vx, vy, t):
        dr = -U * d(r, 0, False) - d(vx, 0, True) - d(vy, 1, True) + S(t) + nu * lap(r, False, False)
        dvx = -U * d(vx, 0, True) - vy * dU - d(r, 0, False) + nu * lap(vx, True, False)
        dvy = -U * d(vy, 0, False) - d(r, 1, False) + nu * lap(vy, False, True)
        return dr, dvx, dvy

    r = np.exp(-(X ** 2 + Y ** 2) / (2 * 0.1 ** 2))
    vx = np.zeros_like(r)
    vy = np.zeros_like(r)
    dt = 0.25 * h / (1 + U0)
    n = int(round(T / dt))
    t = 0.0
    ts, peak, cen, snaps = [0.0], [np.abs(r).max()], [r[centre].mean()], {0.0: r.copy()}
    pending = sorted(s for s in snap_times if s > 0)
    for _ in range(n):
        f = (r, vx, vy)
        k1 = rhs(*f, t)
        k2 = rhs(*(a + 0.5 * dt * b for a, b in zip(f, k1)), t + 0.5 * dt)
        k3 = rhs(*(a + 0.5 * dt * b for a, b in zip(f, k2)), t + 0.5 * dt)
        k4 = rhs(*(a + dt * b for a, b in zip(f, k3)), t + dt)
        r, vx, vy = (a + dt / 6 * (b1 + 2 * b2 + 2 * b3 + b4)
                     for a, b1, b2, b3, b4 in zip(f, k1, k2, k3, k4))
        vx[0], vx[-1] = 0.0, 0.0
        vy[:, 0], vy[:, -1] = 0.0, 0.0
        t += dt
        ts.append(t)
        peak.append(np.abs(r).max())
        cen.append(r[centre].mean())
        while pending and t >= pending[0] - 0.5 * dt:
            snaps[pending.pop(0)] = r.copy()
    return dict(x=x, y=y, t=np.array(ts), peak=np.array(peak), cen=np.array(cen), snaps=snaps)


def summarize(name, res):
    t, pk, c = res["t"], res["peak"], res["cen"]
    def at(tt):
        return pk[np.argmin(np.abs(t - tt))]
    i_min = np.argmin(pk[t <= 1.0])
    late = (t > 1.0)
    print(f"{name:22s} peak t=0 {pk[0]:6.3f} | min (t<=1) {pk[i_min]:6.3f} at t={t[i_min]:4.2f} | "
          f"t=0.5 {at(0.5):6.3f} | t=1 {at(1.0):6.3f} | t>1 centre mean {c[late].mean():7.3f} "
          f"(range {c[late].min():6.3f}..{c[late].max():6.3f})")


def main():
    ap = argparse.ArgumentParser(description="Toy acoustic proxy (not MHD) for 'sonic pinching'.")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                                  "docs", "images", "sonic_pinch_shear.png"))
    ap.add_argument("--T", type=float, default=3.0)
    args = ap.parse_args()
    cases = [("shear + source", True, True), ("shear, no source", True, False),
             ("no shear + source", False, True), ("no shear, no source", False, False)]
    res = {}
    print("TOY ACOUSTIC PROXY (not MHD). Label: Plausible-untested analog.")
    for name, sh, so in cases:
        res[name] = run(sh, so, T=args.T)
        summarize(name, res[name])

    snap_t = [0.0, 0.5, 1.0, args.T]
    fig, axes = plt.subplots(3, 4, figsize=(15, 10.5), constrained_layout=True)
    for row, name in enumerate(["shear + source", "shear, no source"]):
        rr = res[name]
        vmax = max(np.abs(rr["snaps"][s]).max() for s in snap_t if s in rr["snaps"])
        for col, s in enumerate(snap_t):
            ax = axes[row, col]
            im = ax.pcolormesh(rr["x"], rr["y"], rr["snaps"][s].T, cmap="RdBu_r",
                               vmin=-vmax, vmax=vmax, shading="auto")
            ax.set_title(f"{name}: rho at t={s:g}", fontsize=9)
            ax.set_aspect("equal")
            fig.colorbar(im, ax=ax, shrink=0.8)
    ax = axes[2, 0]
    yy = np.linspace(-1, 1, 200)
    ax.plot(0.5 * np.tanh(yy / 0.2), yy)
    ax.set_title("background U_x(y) = 0.5 tanh(y/0.2)", fontsize=9)
    ax.set_xlabel("U_x")
    ax.set_ylabel("y")
    ax = axes[2, 1]
    for name in res:
        ax.plot(res[name]["t"], res[name]["peak"], lw=1, label=name)
    ax.set_title("peak |rho| vs time", fontsize=9)
    ax.set_xlabel("t")
    ax.legend(fontsize=7)
    ax = axes[2, 2]
    for name in res:
        ax.plot(res[name]["t"], res[name]["cen"], lw=1, label=name)
    ax.set_title("mean rho in central disc r<0.1 vs time", fontsize=9)
    ax.set_xlabel("t")
    ax = axes[2, 3]
    ax.axis("off")
    ax.text(0, 0.95, "TOY ACOUSTIC PROXY, NOT MHD\n\nno j×B, no magnetic tension/pressure,\n"
            "no ambipolar diffusion, no kink physics.\n\nPulsed central source adds density by\n"
            "construction: a sustained central peak\nis a forced balance, not self-organization.\n\n"
            "Label: Plausible-untested analog only.", va="top", fontsize=9)
    fig.suptitle("Sonic pinching toy: linearized convected acoustics on a shear flow U_x(y), "
                 "pulsed central source (c = 1)", fontsize=11)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    fig.savefig(args.out, dpi=100)
    print("saved", os.path.abspath(args.out))


if __name__ == "__main__":
    main()

# CC0-1.0. Grok share #89 (eed5005d) follow-up, 2026-10-18.
# Label: Grounded (standard numerical method). Convergence and structure checks for the
# 4th-order Magnus integrator (2-point Gauss-Legendre + sqrt(3)/12 h^2 [A2,A1]) on the
# Mathieu equation x'' + (w0^2 + eps cos(omega t)) x = 0, w0=1, eps=0.2, omega=5, 20 periods.
#
# Checks:
#  1. Final-state error vs a tight DOP853 reference at 8/16/32 steps per period (expect ~16x per doubling).
#  2. Same with the commutator sign flipped (expect 2nd order, ~4x per doubling).
#  3. Monodromy matrix, det (symplectic / area preservation) and trace (|tr| < 2 -> stable).
#  4. NumPy-only expm_simple vs scipy.linalg.expm.
#  5. Optional coarse Mathieu stability chart (|tr M| < 2 over an (omega, eps) grid) -> docs/images/magnus_mathieu_stability_chart.png
# Note: the state norm is NOT a conserved quantity of this time-dependent system; det M = 1 is the structural check.
import os
import sys
import numpy as np
from scipy.linalg import expm
from scipy.integrate import solve_ivp

W0, EPS, OMEGA = 1.0, 0.2, 5.0
N_PERIODS = 20
C = np.array([0.5 - np.sqrt(3) / 6, 0.5 + np.sqrt(3) / 6])


def A(t, w0=W0, eps=EPS, omega=OMEGA):
    return np.array([[0.0, 1.0], [-w0**2 - eps * np.cos(omega * t), 0.0]])


def expm_simple(M, terms=12):
    n = M.shape[0]
    nrm = np.linalg.norm(M, ord=1)
    s = max(0, int(np.ceil(np.log2(nrm / 2.0)))) if nrm > 0 else 0
    Ms = M / (2**s)
    E = np.eye(n)
    X = np.eye(n)
    for k in range(1, terms + 1):
        X = X @ Ms / k
        E = E + X
    for _ in range(s):
        E = E @ E
    return E


def magnus_integrate(y0, t_end, n_steps, sign=+1.0, w0=W0, eps=EPS, omega=OMEGA):
    h = t_end / n_steps
    y = np.array(y0, dtype=float)
    t = 0.0
    for _ in range(n_steps):
        A1 = A(t + C[0] * h, w0, eps, omega)
        A2 = A(t + C[1] * h, w0, eps, omega)
        Om = 0.5 * h * (A1 + A2) + sign * (np.sqrt(3) / 12) * h**2 * (A2 @ A1 - A1 @ A2)
        y = expm(Om) @ y
        t += h
    return y


def main(make_plot=True):
    T = 2 * np.pi / OMEGA
    t_end = N_PERIODS * T
    y0 = np.array([1.0, 0.0])
    ref = solve_ivp(lambda t, y: A(t) @ y, [0, t_end], y0, method="DOP853", rtol=1e-13, atol=1e-14).y[:, -1]
    print(f"Mathieu: w0={W0}, eps={EPS}, omega={OMEGA}, {N_PERIODS} periods, T={T:.6f}")
    print("Reference final state (DOP853, rtol 1e-13):", np.array2string(ref, precision=10))

    for label, sign in (("correct commutator sign (+sqrt3/12 [A2,A1])", +1.0),
                        ("FLIPPED commutator sign (-sqrt3/12 [A2,A1])", -1.0)):
        print(f"\nConvergence, {label}:")
        prev = None
        for n in (8, 16, 32):
            y = magnus_integrate(y0, t_end, N_PERIODS * n, sign)
            err = np.max(np.abs(y - ref))
            ratio = "" if prev is None else f"  ratio {prev / err:6.2f}  observed order {np.log2(prev / err):.2f}"
            print(f"  {n:2d} steps/period: max error {err:.3e}{ratio}")
            prev = err

    M = magnus_integrate(np.eye(2), T, 8)
    print("\nMonodromy matrix (8 steps/period):")
    print(np.array2string(M, precision=6))
    print(f"det M = {np.linalg.det(M):.16f}  |det-1| = {abs(np.linalg.det(M) - 1):.2e}")
    tr = np.trace(M)
    print(f"trace M = {tr:.6f}  -> {'stable (|tr|<2)' if abs(tr) < 2 else 'unstable (|tr|>2)'}")
    mu = np.linalg.eigvals(M)
    print("Floquet multipliers:", np.array2string(mu, precision=6), " |mu| =", np.array2string(np.abs(mu), precision=12))
    print(f"Floquet exponent (rad per period) = {np.arccos(tr / 2):.6f}; omega/w0 = {OMEGA / W0:.2f} (first resonance at omega ~ 2 w0)")

    rng = np.random.default_rng(0)
    worst = 0.0
    for _ in range(200):
        X = rng.normal(size=(2, 2)) * rng.uniform(0.01, 5.0)
        worst = max(worst, np.max(np.abs(expm_simple(X) - expm(X))) / max(1.0, np.max(np.abs(expm(X)))))
    Om = 0.5 * (T / 8) * (A(0.1) + A(0.2))
    print(f"\nexpm_simple vs scipy expm: typical Magnus step diff {np.max(np.abs(expm_simple(Om) - expm(Om))):.1e}; "
          f"worst relative diff over 200 random 2x2 matrices {worst:.1e}")
    y_np = np.array(y0)
    h = t_end / (N_PERIODS * 8)
    t = 0.0
    for _ in range(N_PERIODS * 8):
        A1, A2 = A(t + C[0] * h), A(t + C[1] * h)
        y_np = expm_simple(0.5 * h * (A1 + A2) + (np.sqrt(3) / 12) * h**2 * (A2 @ A1 - A1 @ A2)) @ y_np
        t += h
    y_sp = magnus_integrate(y0, t_end, N_PERIODS * 8)
    print(f"Full 20-period run, NumPy expm vs SciPy expm: max diff {np.max(np.abs(y_np - y_sp)):.1e}")
    print(f"State norm at end: {np.linalg.norm(y_sp):.6f} (start 1.0; not conserved, not a structural check)")

    # 6. Kapitza / high-frequency check of Grok's msg-6 claim. Averaging gives an effective
    #    stiffness w0^2 + eps^2/(2 omega^2) (eps in units of w0^2), i.e. order eps^2/omega^2, not eps^2/omega.
    print("\nHigh-frequency (Kapitza) check, w_eff from monodromy vs sqrt(w0^2 + eps^2/(2 omega^2)):")
    for e, om in ((0.2, 5.0), (0.15, 10.0), (0.15, 20.0), (0.5, 10.0)):
        Tm = 2 * np.pi / om
        Mm = magnus_integrate(np.eye(2), Tm, 64, w0=W0, eps=e, omega=om)
        trm = np.trace(Mm)
        w_eff = np.arccos(np.clip(trm / 2, -1, 1)) / Tm
        print(f"  eps={e:4.2f} omega={om:5.1f}: tr M={trm:.6f} ({'stable' if abs(trm) < 2 else 'unstable'}); "
              f"w_eff={w_eff:.7f}, Kapitza={np.sqrt(W0**2 + e**2 / (2 * om**2)):.7f}, shift {w_eff - W0:.2e}")

    if make_plot:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        oms = np.linspace(0.4, 6.0, 141)
        epss = np.linspace(0.0, 2.0, 81)
        trace = np.zeros((len(epss), len(oms)))
        for i, e in enumerate(epss):
            for j, om in enumerate(oms):
                Mm = magnus_integrate(np.eye(2), 2 * np.pi / om, 64, w0=W0, eps=e, omega=om)
                trace[i, j] = abs(np.trace(Mm))
        stable = trace < 2
        fig, ax = plt.subplots(figsize=(7, 4.5))
        ax.contourf(oms, epss, stable.astype(float), levels=[-0.5, 0.5, 1.5], colors=["#d95f02", "#e8f4ea"])
        ax.contour(oms, epss, trace, levels=[2.0], colors="k", linewidths=0.8)
        ax.plot([OMEGA], [EPS], "k*", ms=12, label=f"case run (omega={OMEGA}, eps={EPS})")
        for n in (1, 2, 3):
            ax.axvline(2 * W0 / n, color="gray", ls=":", lw=0.8)
        ax.set_xlabel("drive frequency omega (w0 = 1)")
        ax.set_ylabel("modulation depth eps")
        ax.set_title("Mathieu stability (undamped): light = |tr M| < 2 stable, orange = unstable\n"
                     "Monodromy via 4th-order Magnus, 64 steps/period; dotted: omega = 2 w0 / n")
        ax.legend(loc="upper right", fontsize=8)
        fig.tight_layout()
        out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "images", "magnus_mathieu_stability_chart.png")
        fig.savefig(out, dpi=110)
        frac = stable.mean()
        print(f"\nStability chart: {len(oms)}x{len(epss)} grid, omega 0.4-6.0, eps 0-2.0; stable fraction {frac:.3f}")
        print("Saved docs/images/magnus_mathieu_stability_chart.png")


if __name__ == "__main__":
    main(make_plot="--no-plot" not in sys.argv)

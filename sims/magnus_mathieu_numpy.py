# CC0-1.0. Grok share #89 (eed5005d) follow-up: script Channing ran on 2026-10-18 (copied unchanged below this header).
# Label: Grounded (standard numerical method: 4th-order Magnus, 2-point Gauss-Legendre, on the Mathieu equation).
# Mathieu: x'' + (w0^2 + eps cos(omega t)) x = 0, w0=1, eps=0.2, omega=5, 8 steps/period, 20 periods.

# Variant: NumPy-only scaling-and-squaring Taylor expm (expm_simple).

import numpy as np

def expm_simple(A, terms=12):
    n = A.shape[0]
    s = max(0, int(np.ceil(np.log2(np.linalg.norm(A, ord=1) / 2.0))))
    A_scaled = A / (2**s)
    E = np.eye(n)
    X = np.eye(n)
    for k in range(1, terms+1):
        X = X @ A_scaled / k
        E = E + X
    for _ in range(s):
        E = E @ E
    return E

w0 = 1.0
eps = 0.2
omega = 5.0
T = 2 * np.pi / omega

def A(t):
    return np.array([[0.0, 1.0],
                     [-w0**2 - eps * np.cos(omega * t), 0.0]])

def magnus_step(t, y, h):
    c = np.array([0.5 - np.sqrt(3)/6, 0.5 + np.sqrt(3)/6])
    A1 = A(t + c[0]*h)
    A2 = A(t + c[1]*h)
    Omega1 = (h/2) * (A1 + A2)
    Omega2 = (np.sqrt(3)/12) * h**2 * (A2 @ A1 - A1 @ A2)
    Omega = Omega1 + Omega2
    return expm_simple(Omega) @ y

def magnus_integrate(y0, t_end, n_steps):
    h = t_end / n_steps
    y = y0.copy()
    t = 0.0
    for _ in range(n_steps):
        y = magnus_step(t, y, h)
        t += h
    return y

y_mono = magnus_integrate(np.eye(2), T, n_steps=8)
det_magnus = np.linalg.det(y_mono)

print("Monodromy matrix (Magnus, 8 steps):")
print(np.round(y_mono, 6))
print("Determinant:", det_magnus)
print("Deviation from 1:", abs(det_magnus - 1.0))

y0 = np.array([1.0, 0.0])
y_final = magnus_integrate(y0, 20*T, n_steps=20*8)
print("\nFinal state after 20 periods:", np.round(y_final, 6))
print("Norm of final state:", np.linalg.norm(y_final))

# CC0-1.0. Grok share #89 (eed5005d) follow-up: script Channing ran on 2026-10-18 (copied unchanged below this header).
# Label: Grounded (standard numerical method: 4th-order Magnus, 2-point Gauss-Legendre, on the Mathieu equation).
# Mathieu: x'' + (w0^2 + eps cos(omega t)) x = 0, w0=1, eps=0.2, omega=5, 8 steps/period, 20 periods.

# Variant: SciPy expm vs a solve_ivp (RK45) reference.

import numpy as np
from scipy.linalg import expm
from scipy.integrate import solve_ivp

w0 = 1.0
eps = 0.2
omega = 5.0
T = 2*np.pi/omega

def A(t):
    return np.array([[0.0, 1.0],
                     [-w0**2 - eps*np.cos(omega*t), 0.0]])

def magnus_step(t, y, h):
    c = np.array([0.5 - np.sqrt(3)/6, 0.5 + np.sqrt(3)/6])
    A1 = A(t + c[0]*h)
    A2 = A(t + c[1]*h)
    Omega1 = (h/2) * (A1 + A2)
    Omega2 = (np.sqrt(3)/12) * h**2 * (A2 @ A1 - A1 @ A2)
    Omega = Omega1 + Omega2
    return expm(Omega) @ y

def magnus_integrate(y0, t_end, n_steps):
    h = t_end / n_steps
    y = y0.copy()
    t = 0.0
    for _ in range(n_steps):
        y = magnus_step(t, y, h)
        t += h
    return y

y0 = np.array([1.0, 0.0])
n_periods = 20
t_end = n_periods * T
n_steps = n_periods * 8

y_magnus = magnus_integrate(y0, t_end, n_steps)

def f(t, y):
    return A(t) @ y

sol = solve_ivp(f, [0, t_end], y0, rtol=1e-10, atol=1e-12, method='RK45')
y_ref = sol.y[:, -1]

y_mono_magnus = magnus_integrate(np.eye(2), T, 8)
det_magnus = np.linalg.det(y_mono_magnus)

print("Magnus final state:     ", y_magnus)
print("Reference final state:  ", y_ref)
print("Difference:             ", np.abs(y_magnus - y_ref))
print("Monodromy det (Magnus): ", det_magnus)
print("Expected det:            1.0")

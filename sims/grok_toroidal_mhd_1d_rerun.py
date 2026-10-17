#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""
grok_toroidal_mhd_1d_rerun.py -- rerun of Grok's shown "simplified toroidal MHD"
code (Grok share 'Earth's EM Field Magnetic Pressure', message 12; verbatim in
docs/grok_archive/2026-10-17_earths_em_field_magnetic_pressure.md).

This is the ORIGINAL code behind the excerpt in docs/tungsten_bismuth_core.md
section 7b-dyn.2 (reported "Final max |B| ~ 1.0399"). The shared page clipped one
line on the right:

    drive = 0.05 * np.sin(omega*t + phi*2*np.pi*x/L) * np.exp(- (x - L/2)**2

so the Gaussian width is unknown [Channing to supply the full line]. This script
completes it as  np.exp(-(x - L/2)**2 / (2*sigma**2))  and scans sigma. Everything
else is Grok's code unchanged (L=10, N=256, eta=0.01, B0 = sin + 0.5 cos(2.),
omega = 2*pi*7.8*0.01, RK45, rtol=atol=1e-5, t in [0, 50]).

It also swaps phi for controls (0, 1.5, sqrt2, 2) to test whether the golden
ratio does anything.

WHAT THE EQUATION IS: dB/dt = eta d2B/dx2 + S(x,t). Linear diffusion plus a
forcing term. No u x B, no flow, no dynamo, no instability physics. "phi
boundaries" are a phase gradient in the forcing, not boundary conditions (the
grid is periodic).

RESULT (run 2026-10-17): sigma = 1 with the phi gradient gives final max|B| =
1.0399, Grok's number to 4 digits. But the initial peak is 1.500 and the
undriven field ends at 1.048: this is decay, not amplification, and phi sits
inside the spread of the controls (1.036-1.045). B0 holds only k = 1, 2, so there
was no "multi-mode chaos" to damp. See docs/tungsten_bismuth_core.md 7b-dyn.3.
"""
import numpy as np
from scipy.integrate import solve_ivp

L, N, eta = 10.0, 256, 0.01
dx = L / N
x = np.linspace(0, L, N, endpoint=False)
B0 = np.sin(2 * np.pi * x / L) + 0.5 * np.cos(4 * np.pi * x / L)
omega = 2 * np.pi * 7.8 * 0.01
PHI = (1 + np.sqrt(5)) / 2


def run(k, sigma, amp=0.05, t_end=50.0):
    def dBdt(t, B):
        Bp = np.concatenate(([B[-1]], B, [B[0]]))
        d2B = (Bp[2:] - 2 * Bp[1:-1] + Bp[:-2]) / dx**2
        drive = amp * np.sin(omega * t + k * 2 * np.pi * x / L) * np.exp(-(x - L / 2) ** 2 / (2 * sigma**2))
        return eta * d2B + drive
    sol = solve_ivp(dBdt, (0, t_end), B0, method='RK45', rtol=1e-5, atol=1e-5, dense_output=True)
    return sol


def low_mode_share(B):
    F = np.abs(np.fft.rfft(B)) ** 2
    return F[1:3].sum() / F[1:].sum()


if __name__ == '__main__':
    print(f"initial max|B| = {np.max(np.abs(B0)):.4f}, low-mode (k=1,2) share = {low_mode_share(B0):.3f}")
    nod = solve_ivp(lambda t, B: eta * (np.roll(B, -1) - 2 * B + np.roll(B, 1)) / dx**2, (0, 50), B0,
                    method='RK45', rtol=1e-5, atol=1e-5)
    print(f"no drive     : final max|B| = {np.max(np.abs(nod.y[:, -1])):.4f}")
    print("sigma  k(phase gradient)  final max|B|  min..max of max|B| over t in [40,50]")
    for sigma in (0.5 ** 0.5, 1.0, 2.0):
        for name, k in (("phi", PHI), ("0", 0.0), ("1.5", 1.5), ("sqrt2", 2 ** 0.5), ("2", 2.0)):
            s = run(k, sigma)
            tt = np.linspace(40, 50, 201)
            m = np.max(np.abs(s.sol(tt)), axis=0)
            print(f"{sigma:5.3f}  {name:6s}  {np.max(np.abs(s.y[:, -1])):.4f}   {m.min():.4f}..{m.max():.4f}")
    # drive-only contribution (B0 = 0) for scale
    s = solve_ivp(lambda t, B: eta * (np.roll(B, -1) - 2 * B + np.roll(B, 1)) / dx**2
                  + 0.05 * np.sin(omega * t + PHI * 2 * np.pi * x / L) * np.exp(-(x - L / 2) ** 2),
                  (0, 50), np.zeros(N), method='RK45', rtol=1e-5, atol=1e-5)
    print(f"drive alone (sigma^2=0.5), B0=0: final max|B| = {np.max(np.abs(s.y[:, -1])):.4f}")

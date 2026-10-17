#!/usr/bin/env python3
"""Rerun of the Grok-described "tungsten + muonic bismuth" coupled oscillators.

CC0. Source: Grok share "Zeeman Coupling in Regenerative Physics", message 8 (no code shown;
parameters were listed): x1'' = -w1^2 x1 - kc (x1 - x2) - g x1',  x2'' = -w2^2 x2 - kc (x2 - x1) - g x2',
w1 = 1.0, w2 = 5.0 + B_effect 0.8 = 5.8, kc = 0.3, x1(0) = 1, x2(0) = 0. Grok reported "clear
oscillatory exchange and beating", with energy transferring "from tungsten into the
muonic-bismuth mode and back". gamma was not given; 0 and 0.01 are tried here.

Also message 16 (two-layer "mycelium base / strained Bi-W" stack): w1 not given; the run below
assumes w1 = 1, w2 = 1.15 (15% strain shift), kc = 0.4, gammas 0.05 / 0.01, drive 0.2 at w2.
The tuned-pair case is shown to contrast with message 8: transfer is strong only when the two
frequencies are close.
Usage: python3 coupled_oscillator_detuning_check.py
"""
import numpy as np
from scipy.integrate import solve_ivp

def run(w1, w2, kc, g1, g2, F=0.0, wd=0.0, T=60.0):
    def f(t, y):
        x1, v1, x2, v2 = y
        a1 = -w1**2 * x1 - kc * (x1 - x2) - g1 * v1
        a2 = -w2**2 * x2 - kc * (x2 - x1) - g2 * v2 + F * np.cos(wd * t)
        return [v1, a1, v2, a2]
    t = np.linspace(0, T, 60001)
    s = solve_ivp(f, (0, T), [1, 0, 0, 0], t_eval=t, rtol=1e-10, atol=1e-12)
    x1, v1, x2, v2 = s.y
    E1 = 0.5 * v1**2 + 0.5 * w1**2 * x1**2
    E2 = 0.5 * v2**2 + 0.5 * w2**2 * x2**2
    return t, E1, E2

if __name__ == "__main__":
    for g in (0.0, 0.01):
        t, E1, E2 = run(1.0, 5.8, 0.3, g, g)
        print(f"msg 8 (w2=5.8, kc=0.3, gamma={g}): max E2/E1(0) = {E2.max()/E1[0]:.2e}")
    # analytic mixing for the undamped normal modes
    d = 5.8**2 - 1.0**2
    th = 0.5 * np.arctan2(2 * 0.3, d)
    print(f"analytic max transfer sin^2(2 theta) = {np.sin(2*th)**2:.2e}")
    t, E1, E2 = run(1.0, 1.0, 0.3, 0, 0)
    print(f"same coupling, tuned (w2 = w1 = 1): max E2/E1(0) = {E2.max()/E1[0]:.2f}")
    t, E1, E2 = run(1.0, 1.15, 0.4, 0.05, 0.01, F=0.2, wd=1.15)
    print(f"msg 16 assumed (w2 = 1.15, kc = 0.4, drive 0.2): max E2/E1(0) = {E2.max()/E1[0]:.2f}")
    print("Result: with w2 = 5.8 and kc = 0.3 only ~1% of the energy ever sits in the second "
          "oscillator (a small forced, off-resonance response; normal-mode mixing ~3e-4), so 'clear sympathetic exchange' is not what these parameters give. Exchange "
          "is complete only when the two oscillators are nearly tuned (E2 here also excludes the coupling energy, so ratios can exceed 1). The model also has no "
          "physical link to tungsten, muonic bismuth or gamma rays; it is a generic linear pair.")

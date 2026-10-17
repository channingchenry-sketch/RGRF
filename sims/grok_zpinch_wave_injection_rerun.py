#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""
grok_zpinch_wave_injection_rerun.py -- checks of the three wave-injection
starters Grok showed in the share 'Tungsten Nodes for Z-Pinch Plasma Filaments'
(verbatim in docs/grok_archive/2026-10-17_tungsten_nodes_z_pinch_plasma_filaments.md):

  msg 6  acoustic injection         (named later as part of the "saved" set)
  msg 8  RGRF_Magnetoacoustic_Coupling_v0.1.py
  msg 10 RGRF_Alfven_Resonance_v0.2.py
  msg 12 RGRF_PhiTungsten_ICR_Magnetron_v0.3.py (fragment only, solver omitted)

The shared page clipped the right end of the update lines (u_new[i] = ... and
u_tx = ...), so none of the three can be rerun exactly [Channing to supply the
full files]. What CAN be checked from the visible parameters:

  1. Time actually simulated. Each loop does ONE time step per saved frame, so
     the run covers (save_steps - 1) * dt seconds, not the T passed in and used
     for the plot's time axis.
  2. Wave travel distance and number of drive periods in that time.
  3. Whether the phi-scaled drive frequencies sit on a resonance of the system
     (standing waves on a length-L filament: f_n = n v / (2L); ion cyclotron:
     f = f_ci or a harmonic).
  4. A rerun of the msg-6 acoustic case with the clipped update completed as the
     equation in Grok's own comment, u_tt = c^2 u_xx - 2 v u_tx (ASSUMED),
     keeping Grok's grid, source, boundaries and loop structure.
"""
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
E, MP = 1.602e-19, 1.673e-27


def coverage(name, L, Nx, dt, T, save_steps, v, freqs):
    t_sim = (save_steps - 1) * dt
    print(f"\n{name}")
    print(f"  dt = {dt:.3e} s, simulated time = {t_sim:.3e} s vs plotted T = {T:.1e} s "
          f"({100 * t_sim / T:.1f} %)")
    print(f"  wave travel v*t = {v * t_sim:.3f} m on a {L} m filament; transit time L/v = {L / v:.2e} s "
          f"({t_sim / (L / v):.2f} transits)")
    for lab, f in freqs:
        n = f / (v / (2 * L))
        print(f"  drive {lab}: f = {f:,.0f} Hz -> {f * t_sim:.2f} periods simulated; "
              f"f / (v/2L) = {n:.3f} (integer = standing-wave harmonic)")


if __name__ == '__main__':
    # msg 6 acoustic
    L, Nx, c = 1.0, 200, 5000.0
    dx = L / (Nx - 1)
    coverage("msg 6 acoustic injection", L, Nx, 0.5 * dx / c, 0.002, 100, c,
             [("node 1, 5000*phi", 5000 * PHI), ("node 2, 5000*phi^2", 5000 * PHI ** 2)])
    # msg 8 magnetoacoustic v0.1
    cs, vA = 5000.0, 8000.0
    cf = (cs ** 2 + vA ** 2) ** 0.5
    coverage("msg 8 magnetoacoustic v0.1", 1.0, 300, 0.4 * 1.0 / (300 * cf), 0.0015, 120, cf,
             [("node 1, 8000*phi", 8000 * PHI), ("node 2, 8000", 8000.0)])
    # msg 10 Alfven v0.2
    dx = 1.0 / 299
    fA = (vA / 1.0) * PHI * 2
    coverage("msg 10 Alfven resonance v0.2", 1.0, 300, 0.35 * dx / vA, 0.002, 150, vA,
             [("node 1, (vA/L)*phi*2", fA), ("node 2, that / phi = 2 vA/L", fA / PHI)])
    # msg 12 ICR
    wci = 1.2e7
    print("\nmsg 12 ICR v0.3")
    for ion, m in (("H+", MP), ("D+", 2 * MP), ("Ar+", 39.95 * MP)):
        print(f"  omega_ci = 1.2e7 rad/s needs B = {wci * m / E:.3f} T for {ion}")
    for B in (0.5, 1.0):
        print(f"  H+ at B = {B} T: omega_ci = {E * B / MP:.2e} rad/s")
    print(f"  drive f = f_ci * phi = {PHI:.3f} f_ci: not f_ci or an integer harmonic -> off resonance")
    # physical scale of the chosen speeds
    Te = MP * cs ** 2 / E
    print(f"\n  c_s = 5 km/s corresponds to T_e ~ {Te:.2f} eV for hydrogen (c_s = sqrt(kTe/m_i)); "
          f"a keV pinch has c_s ~ {np.sqrt(1e3 * E / MP):.1e} m/s")

    # msg 6 rerun with the ASSUMED completion
    L, Nx, c = 1.0, 200, 5000.0
    dx = L / (Nx - 1)
    x = np.linspace(0, L, Nx)
    dt = 0.5 * dx / c
    v_shear = 1000 * (1 - 2 * (x / L - 0.5) ** 2)

    def run(f1, f2, amp=1e4, steps=100, shear=True):
        src = lambda t: amp * (np.sin(2 * np.pi * f1 * t) * np.exp(-((x - 0.05) / 0.02) ** 2)
                               + np.sin(2 * np.pi * f2 * t) * np.exp(-((x - 0.95) / 0.02) ** 2))
        u = np.zeros((steps, Nx))
        u[0] = 0.01 * np.sin(2 * np.pi * 3 * x / L)
        t = 0.0
        for s in range(steps - 1):
            prev = u[s - 1] if s > 0 else u[0]
            uxx = np.zeros(Nx)
            uxx[1:-1] = (u[s, 2:] - 2 * u[s, 1:-1] + u[s, :-2]) / dx ** 2
            utx = np.zeros(Nx)
            utx[1:-1] = ((u[s, 2:] - prev[2:]) - (u[s, :-2] - prev[:-2])) / (2 * dx * dt)
            new = 2 * u[s] - prev + (c * dt) ** 2 * uxx - (2 * v_shear * utx * dt ** 2 if shear else 0)
            new += dt ** 2 * src(t)
            new[0], new[-1] = 0.8 * new[1], 0.8 * new[-2]
            u[s + 1] = new
            t += dt
        return u

    print("\nmsg 6 rerun (assumed completion of the clipped update line):")
    print(f"  source added per step: dt^2 * amp = {dt ** 2 * 1e4:.2e} (initial field amplitude 0.01)")
    for lab, f1, f2, sh in (("phi, phi^2 (Grok)", 5000 * PHI, 5000 * PHI ** 2, True),
                            ("1.5, 2.25 control", 7500.0, 11250.0, True),
                            ("phi, no shear", 5000 * PHI, 5000 * PHI ** 2, False)):
        u = run(f1, f2, shear=sh)
        print(f"  {lab:20s}: max|u| final = {np.max(np.abs(u[-1])):.6f}, "
              f"max|u - initial| = {np.max(np.abs(u[-1] - u[0])):.2e}")

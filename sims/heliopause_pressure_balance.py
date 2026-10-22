"""Heliopause pressure balance from Voyager numbers (RGRF leaky-boundary F_net check).

F_net = integral over the boundary of (P_in - P_out - sigma_EM,in + sigma_EM,out) . dA, dA outward.
For a thin boundary with B tangential to it, the normal EM stress reduces to the magnetic
pressure B^2/(2 mu0), so per unit area the balance is
    p_in + B_in^2/2mu0 (+ rho v_n^2 terms)  vs  p_out + B_out^2/2mu0 (+ rho v_n^2 terms).
Electric stress is dropped: (E/cB)^2 ~ 1e-9 at the heliopause (see electrostatic_maxwell_stress_check.py).

Sources (Grounded):
  Inside total effective pressure 267 +/- 55 fPa, for ~20,000 K just outside the HP:
    Rankin, McComas, Richardson & Schwadron, ApJ 883, 101 (2019), doi:10.3847/1538-4357/ab3d9d
  Outside electron density 0.08 cm^-3 (2.6 kHz plasma oscillations), 0.05 cm^-3 earlier:
    Gurnett et al., Science 341, 1489 (2013), doi:10.1126/science.1241681
  Outside |B| = 0.486 +/- 0.045 nT (range 0.38-0.59 nT):
    Burlaga & Ness, ApJ 784, 146 (2014), doi:10.1088/0004-637X/784/2/146
Assumed [to verify]: T_out range 7,500-30,000 K, T_e = T_p, He ignored; ISM inflow 26 km/s
for the far-field ram comparison (at the nose stagnation point the ram term converts to p + B^2 terms).
"""
import numpy as np

kB, mu0, mp = 1.380649e-23, 4e-7 * np.pi, 1.67262e-27
fPa = 1e-15

P_in, dP_in = 267 * fPa, 55 * fPa
print("Inside (heliosheath, Rankin+2019): P_total = %.0f +/- %.0f fPa" % (P_in / fPa, dP_in / fPa))
print()
print("Outside (VLISM, Voyager 1):")
print("  n_e [cm^-3]  T [K]    p_th [fPa]  B [nT]  B^2/2mu0 [fPa]  P_out [fPa]  P_in-P_out [fPa]")
for n_cc in (0.05, 0.08):
    n = n_cc * 1e6
    for T in (7500, 20000, 30000):
        p_th = 2 * n * kB * T  # electrons + protons
        for B_nT in (0.38, 0.486, 0.59):
            pB = (B_nT * 1e-9) ** 2 / (2 * mu0)
            P_out = p_th + pB
            print("  %5.2f       %6d   %7.1f     %5.3f   %7.1f         %7.1f      %+7.1f" % (
                n_cc, T, p_th / fPa, B_nT, pB / fPa, P_out / fPa, (P_in - P_out) / fPa))
print()
v = 26e3
for n_cc in (0.05, 0.08):
    ram = n_cc * 1e6 * mp * v ** 2
    print("Far-field ISM ram rho v^2 (n_p = %.2f, v = 26 km/s) = %.1f fPa" % (n_cc, ram / fPa))
print()
n, T, B = 0.08e6, 20000, 0.486e-9
P_out_nom = 2 * n * kB * T + B ** 2 / (2 * mu0)
print("Nominal (n=0.08, T=20,000 K, B=0.486 nT): P_out = %.0f fPa, P_in = %.0f fPa, ratio P_in/P_out = %.2f"
      % (P_out_nom / fPa, P_in / fPa, P_in / P_out_nom))
ram = n * mp * v ** 2
print("Nominal P_out + full far-field ram = %.0f fPa, inside the 267 +/- 55 fPa band (212-322)." % ((P_out_nom + ram) / fPa))
print("Reading: thermal + magnetic pressure outside (~0.07-0.2 pPa) alone falls short of the ~0.27 pPa")
print("inferred inside. Adding the stagnated ISM ram term closes most of the gap, and the remainder sits")
print("inside the error bar (plus unmeasured outside components such as pickup ions [to verify]). So the")
print("normal stress jump, and F_net per unit area, is small next to either side: a near-equilibrium boundary.")
print("Numbers: Grounded (sources above). RGRF 'leaky boundary' reading: Speculative.")

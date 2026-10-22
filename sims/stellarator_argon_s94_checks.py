"""Share #94 (3fcd1ac6) number checks: argon filament critical density, plasma frequency,
argon ionization energies (NIST ASD values, Grounded), 1/phi rotational transform (Symbolic),
solar-wind 1/r^2 dilution to the heliopause."""
import numpy as np
e, me, eps0 = 1.602176634e-19, 9.1093837e-31, 8.8541878128e-12
f = 24e9; w = 2*np.pi*f
ncr = eps0*me*w**2/e**2
print("1) Critical density at 24 GHz: %.3e m^-3 = %.2e cm^-3 (Grok-reported ~7e12 cm^-3)" % (ncr, ncr/1e6))
print("   free-space wavelength %.3f cm (Grok: ~1 cm)" % (2.998e8/f*100))
for n_cc in (1e14, 1e15):
    print("   Ne=%.0e cm^-3 -> Ne/Ncr = %.0f, f_p = %.0f GHz" % (n_cc, n_cc*1e6/ncr, np.sqrt(n_cc*1e6*e**2/(eps0*me))/2/np.pi/1e9))
print("2) Argon ionization energies (NIST ASD, eV): Ar0->1+ 15.760, Ar15+->16+ 918.4, Ar16+->17+ 4120.7, Ar17+->18+ 4426.2")
print("   He-like Ar16+ is a closed shell: wide temperature window -> core X-ray diagnostics (XICS)")
phi = (1+5**0.5)/2
print("3) 1/phi = %.6f ; continued fraction [0;1,1,1,...] -> 'most irrational' (Hurwitz). Symbolic for coil design." % (1/phi))
print("   W7-X standard configuration edge iota ~ 5/5 = 1 (island divertor uses that low-order resonance)")
n1au = 5.0  # cm^-3, typical
for r in (1, 10, 40, 90, 120):
    print("4) solar wind n(%3d AU) ~ %.2e cm^-3 (n1AU=5, 1/r^2, no TS jump)" % (r, n1au/r**2))
print("   VLISM n_e ~0.08 cm^-3 (Gurnett 2013) / ~0.002 cm^-3 heliosheath -> ratio ~40")

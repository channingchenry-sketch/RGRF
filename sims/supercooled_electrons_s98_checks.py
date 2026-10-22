"""Checks for Grok share #98 "Exploring Supercooled Free Electrons" (CC0).
Reruns Grok's numbers: Brillouin density, cyclotron frequency, proton limit,
rim field, cyclotron cooling time, Feynman vortex density, He surface-state scales."""
import numpy as np
from scipy import constants as C
e, me, mp, eps0, c, h = C.e, C.m_e, C.m_p, C.epsilon_0, C.c, C.h
m4 = 4.002602 * C.atomic_mass

print("1. Brillouin density n_B = eps0 B^2 / (2 m)")
print(f"   electron coefficient: {eps0/(2*me):.3e} m^-3 per T^2 (Grok: 4.86e18)")
print(f"   f_c per tesla: {e/(2*np.pi*me)/1e9:.2f} GHz (Grok: 28.0)")
print(" B(T)   nB_e(cm^-3)  f_c(GHz)  f_rot@limit(GHz)  nB_p(cm^-3)")
for B in [0.01, 0.05, 0.1, 0.2, 0.5, 1, 2, 4, 5, 10]:
    ne = eps0*B**2/(2*me)/1e6; npb = eps0*B**2/(2*mp)/1e6
    fc = e*B/(2*np.pi*me)/1e9
    print(f" {B:5.2f}  {ne:10.3e}  {fc:8.2f}  {fc/2:8.2f}  {npb:10.3e}")
print(f"   mass ratio m_p/m_e = {mp/me:.1f}")

print("2. Rim field of a uniform column, n = 0.2 n_B, B = 1 T, R = 1 cm")
n = 0.2*eps0/(2*me); R = 0.01
E = n*e*R/(2*eps0)
print(f"   n = {n:.2e} m^-3, E_rim = {E:.2e} V/m = {E/1e5:.0f} kV/cm (Grok: 'tens of kV/cm')")

print("3. Cyclotron cooling time tau = 3 pi eps0 me^3 c^3 / (e^4 B^2)")
for B in [0.1, 1, 5]:
    tau = 3*np.pi*eps0*me**3*c**3/(e**4*B**2)
    print(f"   B={B} T: tau = {tau:.3g} s")

print("4. Feynman rule n_v = 2 Omega / kappa, kappa = h/m4")
k = h/m4
print(f"   kappa = {k:.3e} m^2/s (Grok: 9.97e-8)")
for W in [1, 3.5]:
    print(f"   Omega={W} rad/s: n_v = {2*W/k:.2e} m^-2, spacing ~ {1/np.sqrt(2*W/k)*1e6:.0f} um")

print("5. Electrons on liquid helium (1D hydrogenic model, Lambda = e^2 (eps-1)/(4(eps+1)) / (4 pi eps0))")
epsHe = 1.0572
Lam = (epsHe-1)/(4*(epsHe+1))
Ry = me*(e**2*Lam/(4*np.pi*eps0))**2/(2*C.hbar**2)
aB = 4*np.pi*eps0*C.hbar**2/(me*e**2*Lam)
print(f"   ground binding {Ry/e*1e3:.3f} meV = {Ry/C.k:.2f} K (Grok: ~7.6 K; measured ~0.7 meV)")
print(f"   <z> = 1.5 a_B = {1.5*aB*1e9:.1f} nm (Grok: ~11 nm)")
print(f"   1->2 transition (hydrogenic) {Ry*0.75/h/1e9:.0f} GHz (Grok: ~125 GHz; measured 125.9 GHz, Grimes et al. 1976)")

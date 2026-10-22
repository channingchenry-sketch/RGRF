"""Share #117 check: synchrotron critical frequency and the SSA slab spectrum.
Homogeneous slab, power-law electrons N(E) ~ E^-p, source function S ~ nu^(5/2),
optical depth tau ~ nu^-(p+4)/2.  I = S (1 - exp(-tau)).  Fits the log slopes well
below and above the turnover and compares with 5/2 and -(p-1)/2."""
import numpy as np
e, m, c = 4.803e-10, 9.109e-28, 2.998e10   # cgs
def nu_c(gamma, B, pitch=np.pi/2):           # nu_c = (3/2) gamma^2 nu_g sin(alpha), nu_g = eB/(2 pi m c)
    return 1.5 * gamma**2 * e*B/(2*np.pi*m*c) * np.sin(pitch)
for g, B in [(1e3, 1e-3), (1e4, 1e-5), (1e6, 1e-4)]:
    print(f"gamma={g:.0e} B={B:.0e} G -> nu_c = {nu_c(g,B):.3e} Hz")
print("rule of thumb nu_c ~ 4.2 MHz * gamma^2 * B[G]; nu_g/B =", e/(2*np.pi*m*c)/1e6, "MHz/G")
for p in (2.0, 2.5, 3.0):
    nu = np.logspace(-3, 3, 2001)            # in units of tau=1 frequency
    tau = nu**(-(p+4)/2)
    I = nu**2.5 * (1 - np.exp(-tau))
    lo, hi = nu < 1e-2, nu > 1e2
    s_lo = np.polyfit(np.log(nu[lo]), np.log(I[lo]), 1)[0]
    s_hi = np.polyfit(np.log(nu[hi]), np.log(I[hi]), 1)[0]
    print(f"p={p}: slope below {s_lo:.3f} (expect 2.5), above {s_hi:.3f} (expect {-(p-1)/2:.3f}), peak at nu/nu_tau1 = {nu[I.argmax()]:.3f}")
# SSA brightness temperature ceiling ~ electron kinetic temperature at the turnover
k = 1.381e-16
for g in (1e2, 1e3):
    print(f"gamma={g:.0e}: T_b,max ~ gamma m c^2 / 3k = {g*m*c**2/(3*k):.1e} K (inverse-Compton limit ~1e12 K, equipartition ~1e11 K)")

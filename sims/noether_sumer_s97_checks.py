"""Share #97 checks: Sumer arithmetic, Noether symmetry->conservation demos,
friction-coupled counter-rotation, and the sign of Grok's phase coupler.
Pure numpy; deterministic. Run: python3 sims/noether_sumer_s97_checks.py"""
import numpy as np

print("1. Sexagesimal: divisors of 60")
d = [k for k in range(1, 61) if 60 % k == 0]
print("   divisors:", d, "count", len(d), "| proper (excl 1,60):", d[1:-1])
print("   60*60 =", 3600, "; 360 = 6*60 ->", 360 // 60)

print("2. Emmy Noether age at death (b. 1882-03-23, d. 1935-04-14):", 1935 - 1882, "(birthday passed)")

print("3. C60 Euler count: V-E+F with V=60, E=90, F=12 pent + 20 hex")
V, E, F = 60, 90, 32
print("   V-E+F =", V - E + F, "; pentagons forced: 12 for any trivalent pent/hex cage")

def rk4(f, y, dt, n):
    out = [y.copy()]
    for _ in range(n):
        k1 = f(y); k2 = f(y + dt/2*k1); k3 = f(y + dt/2*k2); k4 = f(y + dt*k3)
        y = y + dt/6*(k1 + 2*k2 + 2*k3 + k4); out.append(y.copy())
    return np.array(out)

print("4. Noether demo: planar particle, central vs. non-central potential")
def central(y):
    x, yy, vx, vy = y; r3 = (x*x + yy*yy)**1.5
    return np.array([vx, vy, -x/r3, -yy/r3])
def noncentral(y):  # adds a quadrupole-like term that breaks rotation symmetry
    x, yy, vx, vy = y; r3 = (x*x + yy*yy)**1.5
    return np.array([vx, vy, -x/r3 - 0.05*x, -yy/r3 - 0.15*yy])
y0 = np.array([1.0, 0.0, 0.0, 0.9])
for name, f in [("central (rotation-symmetric)", central), ("anisotropic (rotation broken)", noncentral)]:
    tr = rk4(f, y0, 1e-3, 20000)
    L = tr[:, 0]*tr[:, 3] - tr[:, 1]*tr[:, 2]
    print(f"   {name}: L range = {L.min():.6f} .. {L.max():.6f}  (spread {L.max()-L.min():.2e})")
print("   Energy is conserved in both (time-translation symmetry kept); L only in the first.")

print("5. Friction from inertial momentum -> opposite angular momentum (two rotors, viscous coupling)")
I1, I2, c = 1.0, 3.0, 0.5
def rotors(y):
    w1, w2 = y; tq = c*(w2 - w1)
    return np.array([tq/I1, -tq/I2])
tr = rk4(rotors, np.array([10.0, 0.0]), 1e-3, 20000)
Ltot = I1*tr[:, 0] + I2*tr[:, 1]
print(f"   total L start {Ltot[0]:.6f} end {Ltot[-1]:.6f}; rotor-1 L change {I1*(tr[-1,0]-tr[0,0]):+.4f}, rotor-2 {I2*(tr[-1,1]-tr[0,1]):+.4f}")
print(f"   KE start {0.5*I1*100:.3f} end {0.5*I1*tr[-1,0]**2+0.5*I2*tr[-1,1]**2:.3f} (friction dissipates energy, not total L)")
print("   With the pair fixed to a frame (anchored stator), the reaction torque goes to the frame:")
print("   equal-and-opposite L is Newton III + rotation symmetry (Noether), not a new effect.")

print("6. Grok's coupler sign: U = A cos(dphi), lock at pi")
A = 1.0; eps = 1e-3
for dphi in [np.pi - 0.1, np.pi + 0.1]:
    tau_true = -(A*np.cos(dphi + eps) - A*np.cos(dphi - eps))/(2*eps)  # -dU/dphi
    tau_grok = -A*np.sin(dphi)
    print(f"   dphi=pi{dphi-np.pi:+.1f}: -dU/dphi = {tau_true:+.4f} (restoring={np.sign(tau_true)==-np.sign(dphi-np.pi)}); Grok's -A sin = {tau_grok:+.4f}")
Upp = -A*np.cos(np.pi)
print(f"   U''(pi) = -A cos(pi) = {Upp:+.1f} > 0 -> a well. Grok wrote d2U = A cos(dphi)(d dphi)^2 = negative at pi; sign slip.")
print("   Corrected: tau = +A sin(dphi) (restoring toward pi); second variation = -A cos(dphi)(d dphi)^2 (positive at pi).")

print("7. Boundary-layer scale: delta/L ~ Re^-1/2 ~ sqrt(nu)")
for Re in [1e2, 1e4, 1e6]:
    print(f"   Re={Re:.0e}: delta/L ~ {Re**-0.5:.1e}")

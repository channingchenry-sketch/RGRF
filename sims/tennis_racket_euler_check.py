"""Share #102 check: torque-free Euler equations, I = (1, 2, 3), spin on the
intermediate axis with a 2 % perturbation. Reports E and L^2 drift, the first
omega_2 zero crossing, and the linear growth rate vs the closed form."""
import numpy as np
from scipy.integrate import solve_ivp
I1, I2, I3 = 1.0, 2.0, 3.0
def f(t, w):
    w1, w2, w3 = w
    return [(I2-I3)*w2*w3/I1, (I3-I1)*w3*w1/I2, (I1-I2)*w1*w2/I3]
def run(w0, T=60):
    s = solve_ivp(f, (0, T), w0, rtol=1e-11, atol=1e-13, dense_output=True, max_step=0.01)
    w = s.y; E = 0.5*(I1*w[0]**2+I2*w[1]**2+I3*w[2]**2); L2 = (I1*w[0])**2+(I2*w[1])**2+(I3*w[2])**2
    z = np.where(np.diff(np.sign(w[1])))[0]
    return s.t, w, abs(E/E[0]-1).max(), abs(L2/L2[0]-1).max(), s.t[z]
lam = np.sqrt((I2-I1)*(I3-I2)/(I1*I3))
print(f"closed-form growth rate lambda/omega = sqrt((I2-I1)(I3-I2)/(I1 I3)) = {lam:.6f}")
for name, w0 in [("2% on w1 and w3", [0.02, 1.0, 0.02]), ("2% on w1 only", [0.02, 1.0, 0.0]), ("2% on w3 only", [0.0, 1.0, 0.02])]:
    t, w, dE, dL, zc = run(w0)
    print(f"{name}: max|dE/E|={dE:.1e} max|dL2/L2|={dL:.1e} omega2 zero crossings t={np.round(zc[:4],2)}")
# measured early growth
t, w, *_ = run([1e-6, 1.0, 0.0], T=8)
m = (t > 2) & (t < 7)
print(f"fitted early growth rate of |w1|: {np.polyfit(t[m], np.log(abs(w[0][m])), 1)[0]:.6f}")
# stable axes: perturbation stays bounded
for ax in (0, 2):
    w0 = [0.02, 0.02, 0.02]; w0[ax] = 1.0
    _, w, *_ = run(w0); print(f"spin on I{ax+1}: max |other comps| = {np.abs(np.delete(w, ax, 0)).max():.3f}")

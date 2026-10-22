"""Share #96 checks: Hau slow-light units, jitterbug stations, FPUT recurrence.
CC0-1.0. numpy only."""
import numpy as np

print("== Hau 1999 group velocity ==")
v = 17.0
print(f"17 m/s = {v*3600/1609.344:.1f} mph; c/v = {299792458/v:.2e}")

print("\n== Jitterbug (pyritohedral family: cyclic perms of (0,+-1,+-t)) ==")
def verts(t):
    base = []
    for s1 in (1, -1):
        for s2 in (1, -1):
            p = (0, s1*1.0, s2*t)
            base += [p, (p[2], p[0], p[1]), (p[1], p[2], p[0])]
    return np.array(base)
def stats(t):
    a = np.array([0, 1, t]); b = np.array([t, 0, 1])      # rigid-triangle edge
    e = np.linalg.norm(a-b)
    V = verts(t)
    r = np.linalg.norm(V[0]) / e                          # circumradius / edge
    # twist of triangle about (1,1,1): angle of vertex a vs VE vertex (0,1,1)
    n = np.ones(3)/np.sqrt(3)
    def proj(x): x = x - x.dot(n)*n; return x/np.linalg.norm(x)
    g = np.degrees(np.arccos(np.clip(proj(a).dot(proj(np.array([0,1,1.]))), -1, 1)))
    d = sorted({round(np.linalg.norm(V[i]-V[j])/e, 6) for i in range(12) for j in range(i+1, 12)})
    return e, r, g, d[:3]
phi = (1+5**0.5)/2
for name, t in [("VE (cuboctahedron)", 1.0), ("regular icosahedron", 1/phi),
                ("Jessen", 0.5), ("octahedron (doubled)", 1e-9)]:
    e, r, g, d = stats(t)
    print(f"{name:22s} t={t:.4f} R/edge={r:.4f} twist={g:6.2f} deg  shortest dists/edge={d}")

print("\n== FPUT alpha-chain recurrence (N=32, alpha=0.25, mode 1, amplitude 1) ==")
N, alpha, dt = 32, 0.25, 0.05
j = np.arange(1, N+1)
modes = np.sqrt(2/(N+1))*np.sin(np.outer(j, j)*np.pi/(N+1))
omega = 2*np.sin(j*np.pi/(2*(N+1)))
q = 1.0*modes[0]; p = np.zeros(N)
def force(q):
    x = np.concatenate(([0], q, [0])); d = np.diff(x)
    f = d + alpha*d**2
    return f[1:] - f[:-1]
def E1(q, p):
    Q = modes @ q; P = modes @ p
    return 0.5*(P**2 + (omega*Q)**2)
E0 = E1(q, p)[0]; best = (0, 0); minfrac = 1
T_steps = int(30000/dt); a = force(q)
for s in range(1, T_steps+1):
    p += 0.5*dt*a; q += dt*p; a = force(q); p += 0.5*dt*a
    if s % 200 == 0:
        fr = E1(q, p)[0]/E0
        t = s*dt
        if t > 5000 and fr > best[1]: best = (t, fr)
        minfrac = min(minfrac, fr)
print(f"mode-1 energy fraction min={minfrac:.3f}; best return after t>5000: {best[1]:.3f} at t~{best[0]:.0f}")

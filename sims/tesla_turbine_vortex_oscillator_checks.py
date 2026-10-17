"""Checks for Grok share b4089e69 ("Tesla Turbine" thread: EHD, induction, nitinol oscillator,
hyperbolic vortex, digital roots). CC0. Standard library only.
Grok's code was not in the capture; the oscillator and vortex models are rebuilt from the
equations and parameters Grok printed (msgs 10, 12, 20). Unstated values are marked ASSUMED."""
import math

print("== 1. EHD thrust example (msg 10) ==")
I, V, v_ion = 1e-3, 50e3, 100.0
print(f"Grok: F ~ I*V/v_ion = {I*V/v_ion:.2f} N at P = I*V = {I*V:.0f} W  (-> {I*V/v_ion/(I*V)*1e3:.0f} N/kW)")
mu = 2.0e-4          # m^2/(V s), positive-ion mobility in air (approx.)
for d in (0.02, 0.05):
    print(f"Standard 1D model F = I*d/mu, gap d = {d*100:.0f} cm: {I*d/mu:.2f} N  ({I*d/mu/(I*V)*1e3:.1f} N/kW)")
print("-> Same order (0.1-0.5 N for 50 W). The repo ledger gives 6-50 N/kW (lift_and_equilibrium_systems.md);")
print("   lifting an ASSUMED 50 kg by ion wind alone at 10 N/kW would need ~9.8*50/10 = ~49 kW.")

print("\n== 2. Induced EMF example (msg 10) ==")
print(f"N=1, A=0.01 m^2, dB/dt=1000 T/s: EMF = {1*0.01*1000:.0f} V (Grok: ~10 V; correct)")

print("\n== 3. Single-mass frequency and the coupled pair (msgs 10, 12) ==")
k, m1, m2 = 1000.0, 0.5, 0.3
print(f"f = sqrt(k/m1)/2pi = {math.sqrt(k/m1)/(2*math.pi):.2f} Hz (Grok 7.1 Hz; correct for one mass)")
kg = 1000.0          # ASSUMED: ground spring on m1 equal to the coupling spring (Grok: 'optional ground spring')
a, b, c = m1*m2, -((kg+k)*m2 + k*m1), kg*k
w2 = sorted(((-b - s*math.sqrt(b*b-4*a*c))/(2*a)) for s in (1, -1))
print(f"Linear normal modes with k_ground = k_coupling = 1000 N/m: {', '.join(f'{math.sqrt(x)/(2*math.pi):.2f}' for x in w2)} Hz")
fm = [math.sqrt(x)/(2*math.pi) for x in w2]
print(f"-> A 7.1 Hz drive sits between the two normal modes ({fm[0]:.1f} and {fm[1]:.1f} Hz), not on a resonance of the coupled pair.")

def run(F_amp, f_drive, T=10.0, dt=2e-4, alpha=500.0, cdamp=5.0, ground=True):
    w = 2*math.pi*f_drive
    Fn = lambda x: -(k + alpha*abs(x))*x
    def acc(t, s):
        x1, v1, x2, v2 = s
        a1 = (F_amp*math.sin(w*t) + Fn(x1-x2) + (Fn(x1) if ground else 0.0) - cdamp*v1)/m1
        a2 = (-Fn(x1-x2) - cdamp*v2)/m2
        return (v1, a1, v2, a2)
    s, t, rec = (0.0, 0.0, 0.0, 0.0), 0.0, []
    while t < T:
        k1 = acc(t, s)
        k2 = acc(t+dt/2, tuple(s[i]+dt/2*k1[i] for i in range(4)))
        k3 = acc(t+dt/2, tuple(s[i]+dt/2*k2[i] for i in range(4)))
        k4 = acc(t+dt, tuple(s[i]+dt*k3[i] for i in range(4)))
        s = tuple(s[i]+dt/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i]) for i in range(4)); t += dt
        if t > T-2.0: rec.append(s)
    x1s, x2s = [r[0] for r in rec], [r[2] for r in rec]
    v1s = [r[1] for r in rec]
    P_in = sum(F_amp*math.sin(w*(T-2.0+i*dt))*v1s[i] for i in range(len(rec)))/len(rec)
    return max(x1s)-min(x1s), max(x2s)-min(x2s), sum(x1s)/len(x1s), P_in

F_amp = 10.0         # ASSUMED (Grok did not state F_amp; it suggested ~0.5 N EHD thrust as a scale)
for f in (7.1, round(fm[0], 2), round(fm[1], 2)):
    p1, p2, mean1, P = run(F_amp, f)
    print(f"F_amp {F_amp} N at {f:4.1f} Hz: peak-to-peak x1 {p1*100:.2f} cm, x2 {p2*100:.2f} cm, mean x1 {mean1*1e3:+.3f} mm, drive power {P:.2f} W")
p1, p2, mean1, P = run(0.5, 7.1)
print(f"F_amp 0.5 N (EHD scale) at 7.1 Hz: peak-to-peak x1 {p1*1e3:.2f} mm, x2 {p2*1e3:.2f} mm, mean x1 {mean1*1e3:+.4f} mm")
print("-> Amplitudes are mm-to-cm and set by drive and damping; the mean offset is ~0 (the force law is odd in x).")
print("   Grok's 'final positions stabilize near ~0.01 m offset due to drive' does not follow from its own model.")
print("   All the motion is paid for by the drive: the average drive power equals the damping loss.")

print("\n== 4. 'Hyperbolic' vortex (msg 20) ==")
kv, cs, r0 = 1.0, 0.1, 2.0   # v_theta = k/r, v_r = -c/r (Grok's form; values ASSUMED)
# dr/dtheta = r*v_r/v_theta = -c*r/k  ->  r = r0*exp(-c*theta/k)
for th in (0.0, 5.0, 10.0, 20.0):
    r = r0*math.exp(-cs*th/kv)
    print(f"theta {th:5.1f} rad: r = {r:.4f} ; r*theta = {r*th:.3f}")
print("-> A free vortex plus a 1/r sink gives a LOGARITHMIC spiral, r = r0*exp(-c*theta/k), at a constant angle;")
print("   r*theta is not constant, so the paths are not hyperbolic spirals. (A log spiral is golden only for one")
print("   specific c/k; nothing in the model selects it.)")

print("\n== 5. Digital roots of atomic numbers (msgs 28, 30) ==")
dr = lambda z: 9 if z % 9 == 0 else z % 9
groups = {
 "alkali (Li..Fr)": [3, 11, 19, 37, 55, 87],
 "halogens (F..At)": [9, 17, 35, 53, 85],
 "noble gases (He..Rn)": [2, 10, 18, 36, 54, 86],
 "3d transition (Sc..Zn)": list(range(21, 31)),
}
for name, zs in groups.items():
    roots = [dr(z) for z in zs]
    share = sum(r in (3, 6, 9) for r in roots)/len(roots)
    print(f"{name:24s} roots {roots}  share of 3/6/9 = {share:.0%}")
allz = range(1, 119)
print(f"all elements 1-118: share of 3/6/9 = {sum(dr(z) in (3,6,9) for z in allz)/118:.0%} (one third by construction)")
print("-> Ar, Kr, Xe = 18, 36, 54 land on 9 because the periods have 8 and 18 elements; Rn (86) -> 5, Og (118) -> 1.")
print("   Halogen F = 9 and alkali Li = 3 are 3/6/9 too; no reactive/inert split exists in the roots.")

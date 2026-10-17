"""Checks for Grok share 3fbfa3e5 (Fuller, tensegrity, synergetics, vortex node). CC0.
Standard library only. Volumes are in Fuller tetravolumes (regular tetrahedron of unit edge = 1)."""
import math, itertools

phi = (1 + 5 ** 0.5) / 2
sub = lambda a, b: [x - y for x, y in zip(a, b)]
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
norm = lambda a: math.sqrt(dot(a, a))
cross = lambda a, b: [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]

def cyc(t):
    """12 points: cyclic permutations of (0, +-1, +-t)."""
    pts = set()
    for s1, s2 in itertools.product((1, -1), repeat=2):
        p = (0.0, s1 * 1.0, s2 * t)
        pts |= {p, (p[2], p[0], p[1]), (p[1], p[2], p[0])}
    return sorted(pts)

def edge_stats(pts):
    d = sorted(round(norm(sub(a, b)), 9) for a, b in itertools.combinations(pts, 2))
    m = d[0]
    return m, sum(1 for x in d if abs(x - m) < 1e-6)

print("== 1. Icosahedron coordinates (msg 2) ==")
m, n = edge_stats(cyc(phi))
print(f"cyclic (0,+-1,+-phi): shortest distance {m:.6f}, count {n} (an icosahedron has 30 equal edges)")
# Grok's example list mixes (0,1,phi),(phi,1,0),(1,0,phi): test whether (1,0,phi) belongs to the same set
print("(1,0,phi) in the cyclic set of (0,1,phi)?", (1.0, 0.0, phi) in set(cyc(phi)))
print("(phi,1,0) in the cyclic set of (0,1,phi)?", (phi, 1.0, 0.0) in set(cyc(phi)))
print("-> (1,0,phi) and (phi,1,0) belong to the mirror-image icosahedron (anticyclic set);"
      " Grok's example list mixes the two orientations.")

print("\n== 2. Vector equilibrium counts (msgs 4, 6, 8) ==")
ve = cyc(1.0)
m, n = edge_stats(ve)
print(f"VE: 12 vertices, outer edges {n} of length {m:.6f}; radius {norm(ve[0]):.6f} (= edge)")
print("-> 24 outer edges plus 12 radial vectors, all equal. Grok's '24 unit edges radiating from the centre' should read 12 radial.")

print("\n== 3. Jitterbug twist angle (msg 6) ==")
def twist(t):
    P = [(0.0, 1.0, t), (t, 0.0, 1.0), (1.0, t, 0.0)]
    c = [sum(x) / 3 for x in zip(*P)]; nn = [x / norm(c) for x in c]
    def proj(p, cc):
        v = sub(p, cc); k = dot(v, nn); return [v[i] - k * nn[i] for i in range(3)]
    Q = [(0.0, 1.0, 1.0), (1.0, 0.0, 1.0), (1.0, 1.0, 0.0)]
    cq = [sum(x) / 3 for x in zip(*Q)]
    v, w = proj(P[0], c), proj(Q[0], cq)
    return math.degrees(math.atan2(dot(cross(w, v), nn), dot(w, v)))
for t, name in [(1.0, "VE"), (phi, "icosahedron"), (1e7, "octahedron (limit)")]:
    P = [(0.0, 1.0, t), (t, 0.0, 1.0)]
    L = norm(sub(*P))
    print(f"{name:20s} triangle twist {twist(t):7.3f} deg ; square-diagonal / edge = {2 / L:.4f}")
print("-> The regular icosahedron is a single point of the twist (22.24 deg from the VE; by symmetry 97.76 deg on the return),")
print("   not the ranges '22.2-37.8 deg' and '82.2-97.8 deg' in msg 6. Octahedron at 60 deg is correct.")

print("\n== 4. Quanta-module volumes (msg 6) ==")
E = math.sqrt(2) / 8 * phi ** -3
S = phi ** -5 / 2
print(f"A = B = T = 1/24 = {1/24:.6f}; MITE = 2A + B = {3/24:.6f} (1/8)")
print(f"E = (sqrt2/8) * phi^-3 = {E:.6f}   (note phi^-3 = 2phi - 3 = {2*phi-3:.6f}; Grok's '2phi-3 ~ 0.041731' drops the sqrt2/8 factor)")
print(f"S = phi^-5 / 2 = {S:.6f}")
print(f"E3 = E*phi^3 = {E*phi**3:.6f} ; E6 = E*phi^6 = {E*phi**6:.6f} (Grok: 0.176766, 0.748838)")
print(f"RT(5+) = 120 E = {120*E:.6f} (Grok 5.007758); RT(5) = 120 T = {120/24:.1f}")
print(f"Icosahedron, unit edge: 5*sqrt2*phi^2 = {5*math.sqrt(2)*phi**2:.4f} tetravolumes"
      f" (check: Euclidean volume {5*(3+5**0.5)/12:.5f} / tetra {1/(6*math.sqrt(2)):.5f} = {5*(3+5**0.5)/12*6*math.sqrt(2):.4f})")

print("\n== 5. Great circles (msg 4) ==")
print("VE: 4 + 3 + 6 + 12 = 25 ; icosahedron: 6 + 10 + 15 = 31 (Fuller's counts; Grounded)")

print("\n== 6. Maxwell's rule (msg 4) ==")
j, b = 12, 24     # a 6-strut tensegrity icosahedron: 12 nodes, 6 struts + 24 cables = 30 members
print(f"j = {j}: 3j - 6 = {3*j-6}; the 6-strut tensegrity icosahedron has {6+24} members, i.e. exactly Maxwell's count.")
print("Calladine's extension b - 3j + 6 = s - m: it has s = 1 state of self-stress and m = 1 infinitesimal mechanism,")
print("and the prestress stiffens that mechanism (Calladine 1978). Grok's 'fewer bars than Maxwell' is true of some tensegrities, not this one.")

print("\n== 7. Nitinol and a static magnet (msg 14) ==")
print("Induction heating needs a changing field: dP ~ (dB/dt)^2. A permanent 60-deg arc magnet at rest gives dB/dt = 0 -> no heating.")
print("Only a rotor sweeping past the nitinol, or an AC coil, can induction-heat it, and that power comes from the drive.")
Af_low, Af_high = -10.0, 100.0
print(f"Typical NiTi A_f range {Af_low:.0f} to {Af_high:.0f} C: liquid-nitrogen (-196 C) or helium (-269 C) cooling is not needed to hold martensite.")
Th, Tc = 273.15 + 80, 273.15 + 20
print(f"Carnot limit for an SMA heat engine between 80 C and 20 C: {1 - Tc/Th:.1%}; real SMA engines run well below it [to verify: measured values].")

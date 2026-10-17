"""Numerical checks for Grok share #87 `4eaafec3` (Hardy-Ramanujan, mock theta,
crop-circle geometry, IT3 topology), 2026-10-17. CC0.

The share contained no runnable code. This script recomputes the numbers and
formulas Grok stated. Standard library only (float precision is enough here).
Run:  python3 sims/s87_hardy_ramanujan_checks.py
"""
import math
from fractions import Fraction


def hdr(s):
    print("\n" + "=" * 72 + "\n" + s + "\n" + "=" * 72)


N = 200

# ---------------------------------------------------------------------------
hdr("1. p(n) by Euler's pentagonal recurrence (msg 4)")
p = [0] * (N + 1)
p[0] = 1
for n in range(1, N + 1):
    s, k = 0, 1
    while True:
        g1 = k * (3 * k - 1) // 2
        if g1 > n:
            break
        sign = 1 if k % 2 else -1
        s += sign * p[n - g1]
        g2 = k * (3 * k + 1) // 2
        if g2 <= n:
            s += sign * p[n - g2]
        k += 1
    p[n] = s
print("generalised pentagonals:", sorted({k * (3 * k - 1) // 2 for k in range(-5, 6) if k})[:8])
print("p(4), p(3), p(0) =", p[4], p[3], p[0], "-> p(5) =", p[5])
print("Note: the recurrence uses BOTH k(3k-1)/2 and k(3k+1)/2 (generalised pentagonals),")
print("so p(5) = p(4) + p(3) - p(0) = 5 + 3 - 1 = 7 is right (terms for 1, 2, 5).")
for n in (5, 10, 15, 20, 50, 100, 200):
    print(f"  p({n}) = {p[n]:,}")
print("p(200) = 3,972,999,029,388 (MacMahon's value):", p[200] == 3972999029388)

# brute-force cross-check for small n
def count_parts(n, maxpart):
    if n == 0:
        return 1
    return sum(count_parts(n - k, k) for k in range(1, min(n, maxpart) + 1))
assert all(count_parts(n, n) == p[n] for n in range(0, 25))
print("brute-force partition count agrees for n <= 24")

# ---------------------------------------------------------------------------
hdr("2. Hardy-Ramanujan leading term exp(pi sqrt(2n/3)) / (4 n sqrt3) (msgs 2, 4)")
def hr(n):
    return math.exp(math.pi * math.sqrt(2 * n / 3)) / (4 * n * math.sqrt(3))
print(" n   exact     HR leading   Grok-reported   ratio")
grok = {5: 8.94, 10: 48.10, 15: 198.53, 20: 692.38}
for n in (5, 10, 15, 20, 50, 100, 200):
    g = grok.get(n, "")
    print(f"{n:3d}  {p[n]:>14,}  {hr(n):>16,.2f}  {str(g):>8}  {hr(n)/p[n]:.4f}")

# ---------------------------------------------------------------------------
hdr("3. Rademacher exact series, term by term (msg 4: 'k = 2 is tens of units')")
def dedekind_s(h, k):
    s = Fraction(0)
    for r in range(1, k):
        x = Fraction(h * r, k)
        s += Fraction(r, k) * (x - math.floor(x) - Fraction(1, 2))
    return s

def A(k, n):
    tot = 0j
    for h in range(k):
        if math.gcd(h, k) == 1:
            tot += complex(math.cos(math.pi * float(dedekind_s(h, k)) - 2 * math.pi * n * h / k),
                           math.sin(math.pi * float(dedekind_s(h, k)) - 2 * math.pi * n * h / k))
    return tot.real

def rad_term(k, n):
    # p(n) = 1/(pi sqrt2) sum_k A_k(n) sqrt(k) d/dn[ sinh(C x / k) / x ],
    # x = sqrt(n - 1/24), C = pi sqrt(2/3)
    C = math.pi * math.sqrt(2 / 3)
    lam = math.sqrt(n - 1 / 24)
    # d/dn [sinh(C lam/k)/lam] with dlam/dn = 1/(2 lam)
    d = (C / k * math.cosh(C * lam / k) / lam - math.sinh(C * lam / k) / lam**2) / (2 * lam)
    return A(k, n) * math.sqrt(k) * d / (math.pi * math.sqrt(2))

for n in (5, 10, 20, 100, 200):
    terms = [rad_term(k, n) for k in range(1, 9)]
    partial = sum(terms)
    print(f"n={n:3d} exact {p[n]:,}")
    print("   k=1..4 terms:", ", ".join(f"{t:,.3f}" for t in terms[:4]))
    print(f"   A_2(n) = {A(2, n):+.0f};  sum k<=8 = {partial:,.4f}  -> round = {round(partial):,}  ok={round(partial) == p[n]}")
print("A_2(n) = (-1)^n here, so Grok's 'phase that flips with n' is right.")
print("Reading for n = 20: the HR leading formula gives 692.38 (gap +65), but the EXACT")
print("Rademacher k = 1 term already gives ~625.8; the k = 2 term is only ~+1.3.")
print("So the 65-count gap is mostly the crude asymptotic (dropping sinh->exp/2 and the")
print("1/24 shift, and the 1/sqrt(n) correction), NOT the k = 2 arc. Grok's 'p2 is tens")
print("of units' is too large for n = 20.")

# ---------------------------------------------------------------------------
hdr("4. Ramanujan congruences (msg 2)")
for (a, b, m) in ((5, 4, 5), (7, 5, 7), (11, 6, 11)):
    ok = all(p[a * n + b] % m == 0 for n in range((N - b) // a + 1))
    print(f"p({a}n+{b}) = 0 mod {m} for all {a}n+{b} <= {N}: {ok}")

# ---------------------------------------------------------------------------
hdr("5. 1729 and taxicab (msg 2)")
reps = {}
for a in range(1, 30):
    for b in range(a, 30):
        reps.setdefault(a**3 + b**3, []).append((a, b))
first2 = min(v for v, r in reps.items() if len(r) >= 2)
print("smallest sum of two positive cubes in 2 ways:", first2, reps[first2])

# ---------------------------------------------------------------------------
hdr("6. Ramanujan tau, Delta = q prod (1-q^n)^24 (msg 2)")
M = 30
coef = [0] * (M + 1)
coef[0] = 1
for n in range(1, M + 1):
    for _ in range(24):
        for i in range(M, n - 1, -1):
            coef[i] -= coef[i - n]
tau = {n: coef[n - 1] for n in range(1, M + 1)}
print("tau(1..10):", [tau[n] for n in range(1, 11)])
sig11 = lambda n: sum(d**11 for d in range(1, n + 1) if n % d == 0)
print("tau(n) = sigma_11(n) mod 691 for n <= 30:", all((tau[n] - sig11(n)) % 691 == 0 for n in tau))
print("tau(n) != 0 for n <= 30 (Lehmer's conjecture is open in general):", all(tau[n] for n in tau))

# ---------------------------------------------------------------------------
hdr("7. Third-order mock theta f(q) = sum q^{n^2} / (-q;q)_n^2 (msgs 2, 4)")
M = 30
def mul(a, b):
    c = [0] * (M + 1)
    for i, x in enumerate(a):
        if x:
            for j in range(0, M + 1 - i):
                c[i + j] += x * b[j]
    return c
def inv(a):  # power-series inverse, a[0] = 1
    b = [0] * (M + 1)
    b[0] = 1
    for n in range(1, M + 1):
        b[n] = -sum(a[i] * b[n - i] for i in range(1, n + 1))
    return b
f = [0] * (M + 1)
f[0] = 1
den = [1] + [0] * M
n = 1
while n * n <= M:
    one_plus = [0] * (M + 1); one_plus[0] = 1
    if n <= M:
        one_plus[n] = 1
    den = mul(den, mul(one_plus, one_plus))
    term = [0] * (M + 1); term[n * n] = 1
    t = mul(term, inv(den))
    f = [x + y for x, y in zip(f, t)]
    n += 1
print("f(q) coefficients a(0..20):", f[:21])
print("Known (OEIS A000025): 1, 1, -2, 3, -3, 3, -5, 7, -6, 6, -10, 12, -11, 13, -17, 20, -21, 21, -27, 34, -33")
print("These equal (number of partitions of n with even rank) - (odd rank), as Andrews-")
print("Dragonette / Bringmann-Ono use.")

# ---------------------------------------------------------------------------
hdr("8. Vesica and Hawkins' Theorem I (msgs 4, 6)")
# two unit circles centred at (0,0) and (1,0)
y = math.sqrt(3) / 2
print(f"vesica: intersection points (0.5, +/-{y:.6f}); chord = {2*y:.6f} = sqrt3 ({math.sqrt(3):.6f})")
print("sqrt3 comes straight from the vesica; sqrt2 and sqrt5 need extra construction lines")
print("(e.g. a square on the radius, or the 1x2 rectangle diagonal).")
# Hawkins Theorem I: three equal circles (radius r) centred on an equilateral triangle,
# with three straight lines each tangent to all three circles. Each common tangent is
# parallel to a triangle side at distance r on the outside... For a line to touch all
# three circles, two centres lie at distance r on one side and the third at r on the other:
# the line is parallel to a side, at distance r from it, toward the opposite vertex;
# so the opposite vertex is at distance r too: altitude h = 2r.
r = 1.0
h = 2 * r
side = h / (math.sqrt(3) / 2)
R = side / math.sqrt(3)
print(f"Theorem I: circumcircle diameter / corner-circle diameter = {2*R/(2*r):.6f} (4/3 = {4/3:.6f})")
print("Configuration: three EQUAL, SEPARATE circles touched by three common tangent lines,")
print("not 'three mutually tangent circles' as Grok paraphrased.")

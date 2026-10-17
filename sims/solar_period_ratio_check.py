#!/usr/bin/env python3
"""Solar-system "frequency layout": period ratios, small-integer resonances, phi (CC0).

Review: docs/three_body_living_universe_review.md

1. Adjacent planet period ratios (sidereal periods in days), the nearest
   small-integer ratio p:q (q <= 5), and the distance from phi = 1.618...
2. A Monte-Carlo check: how often would 8 random ratios (drawn log-uniformly
   between the smallest and largest adjacent ratio, 1.5 to 6.3) include at least one
   within the same distance of phi? This tests whether "phi in the planets"
   is more than chance.
3. The Laplace relation for Io, Europa, Ganymede from their mean motions:
   n1 - 3 n2 + 2 n3 should be ~0 deg/day.

Run: python3 sims/solar_period_ratio_check.py
"""
from fractions import Fraction
import numpy as np

phi = (1 + 5 ** 0.5) / 2
P = dict(Mercury=87.969, Venus=224.701, Earth=365.256, Mars=686.980, Jupiter=4332.59,
         Saturn=10759.22, Uranus=30688.5, Neptune=60182.0, Pluto=90560.0)
names = list(P)
print(f"{'pair':18s} ratio   nearest p:q (q<=5)  off-by    |ratio-phi|/phi")
best = 1.0
ratios = []
for a, b in zip(names, names[1:]):
    r = P[b] / P[a]
    ratios.append(r)
    fr = Fraction(r).limit_denominator(5)
    off = abs(r / float(fr) - 1)
    dphi = abs(r - phi) / phi
    best = min(best, dphi)
    print(f"{a+'-'+b:18s} {r:6.3f}   {fr.numerator}:{fr.denominator:<14d}  {off*100:5.2f} %   {dphi*100:6.2f} %")

rng = np.random.default_rng(1)
lo, hi = min(ratios), max(ratios)
trials = rng.uniform(np.log(lo), np.log(hi), size=(200000, len(ratios)))
hits = (np.abs(np.exp(trials) - phi) / phi <= best).any(axis=1).mean()
print(f"\nclosest ratio to phi is {best*100:.2f} % away (Venus-Earth ~13:8).")
print(f"chance that {len(ratios)} random ratios in [{lo:.2f}, {hi:.2f}] include one at least that close: {hits*100:.1f} %")

# Laplace resonance (mean motions in deg/day, JPL mean elements)
n_io, n_eu, n_ga = 203.488992, 101.374761, 50.317646
print(f"\nLaplace: n_Io - 3 n_Eu + 2 n_Ga = {n_io - 3*n_eu + 2*n_ga:+.6f} deg/day (~0: locked)")
print(f"         n_Io/n_Eu = {n_io/n_eu:.4f}, n_Eu/n_Ga = {n_eu/n_ga:.4f} (each near 2:1, offset by the precession rates)")

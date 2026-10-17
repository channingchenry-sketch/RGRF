#!/usr/bin/env python3
"""Rebuild (not Grok's code): Jansen linkage foot path + a Margolin-style wave skin (CC0).

Review: docs/kinetic_sculpture_linkage_review.md

Grok said it "prototyped basic versions in our sandbox (jansen_linkage_sim.py and
wave_overlay.py)", but no code was shown in the share. This script is an independent
rebuild from published geometry, so its numbers are ours, not Grok's.

Part 1, Jansen linkage. Theo Jansen's published "holy numbers" (arbitrary units):
  a=38.0 b=41.5 c=39.3 d=40.1 e=55.8 f=39.4 g=36.7 h=65.7 i=49.0 j=50.0 k=61.9 l=7.8 m=15.0
Crank (radius m) turns about O=(0,0); fixed pivot B=(-a,-l). Joints are found by
circle-circle intersection each step. Reports stride length, the share of the crank
cycle the foot spends within 1 % (of path height) of its lowest point (the "flat"
ground-contact part), and foot speed uniformity there.

Part 2, Margolin-style wave skin. Margolin's wave sculptures sum several sinusoids
mechanically (camshafts or helices driving strings over pulleys). Here a 1D skin of N points
is z(x,t) = sum_i sin(k_i x - w_i t). Ratios w2/w1, w3/w1 = (2, 3) [integer] are compared
with (phi, phi^2) [golden]. Reports the repeat period and how often the skin
reaches 90 % of its maximum possible peak (3.0).

Part 3, skin over walker: the skin is phase-locked to the crank angle, and the script
reports peak skin amplitude during foot ground contact vs swing.

Run: python3 sims/jansen_linkage_margolin_wave_rebuild.py
"""
import numpy as np

a, b, c, d, e, f, g, h, i, j, k, l, m = 38.0, 41.5, 39.3, 40.1, 55.8, 39.4, 36.7, 65.7, 49.0, 50.0, 61.9, 7.8, 15.0
B = np.array([-a, -l])


def cc(p0, r0, p1, r1):
    """Both intersections of circle(p0,r0) and circle(p1,r1)."""
    dvec = p1 - p0
    dist = np.hypot(*dvec)
    x = (dist**2 + r0**2 - r1**2) / (2 * dist)
    y = np.sqrt(max(r0**2 - x**2, 0.0))
    u = dvec / dist
    n = np.array([-u[1], u[0]])
    return p0 + x * u + y * n, p0 + x * u - y * n


def leg(theta):
    A = m * np.array([np.cos(theta), np.sin(theta)])
    C = max(cc(A, j, B, b), key=lambda p: p[1])          # upper rocker joint
    D = min(cc(A, k, B, c), key=lambda p: p[1])          # lower rocker joint
    E = min(cc(B, d, C, e), key=lambda p: p[0])          # upper-left triangle
    F = min(cc(E, f, D, g), key=lambda p: p[0])          # left joint
    G = min(cc(F, h, D, i), key=lambda p: p[1])          # foot
    return G


th = np.linspace(0, 2 * np.pi, 3601)
foot = np.array([leg(t) for t in th])
ymin, ymax = foot[:, 1].min(), foot[:, 1].max()
height = ymax - ymin
ground = foot[:, 1] <= ymin + 0.01 * height
stride = foot[ground, 0].max() - foot[ground, 0].min()
vx = np.gradient(foot[:, 0], th)
print("Part 1, Jansen linkage (rebuild)")
print(f"  foot path: width {np.ptp(foot[:,0]):.1f}, height {height:.1f} (units of the holy numbers)")
print(f"  ground-contact (within 1 % of lowest point): {ground.mean()*100:.0f} % of crank cycle, stride {stride:.1f}")
print(f"  foot x-speed during contact: mean {np.abs(vx[ground]).mean():.1f}, spread (std/mean) {np.std(np.abs(vx[ground]))/np.abs(vx[ground]).mean()*100:.0f} %")

print("\nPart 2, Margolin-style 3-wave skin")
x = np.linspace(0, 2 * np.pi, 64)
t = np.linspace(0, 200, 40001)
phi = (1 + 5 ** 0.5) / 2
for label, ratios in [("integer 1:2:3", (1, 2, 3)), ("golden 1:phi:phi^2", (1, phi, phi**2))]:
    ks = (1.0, 1.3, 0.7)
    z = sum(np.sin(kk * x[None, :] - r * t[:, None]) for kk, r in zip(ks, ratios))
    peak = np.abs(z).max(axis=1)
    frac = (peak >= 0.9 * 3).mean()
    # repeat test: correlation of skin shape at t and t+T for T = 2*pi (period of w1)
    s0 = z[0]
    mis = np.linalg.norm(z - s0, axis=1) / np.linalg.norm(s0)
    after = np.arange(len(t)) > 200          # skip the first ~1 time unit
    rep = np.where(after & (mis < 1e-2))[0]
    first = f"repeats (to grid precision) at t={t[rep[0]]:.3f}" if len(rep) else f"never repeats in t<=200 (best misfit {mis[after].min():.3f})"
    print(f"  {label:20s}: skin peak >= 2.7 for {frac*100:4.1f} % of time; {first}")

print("\nPart 3, skin phase-locked to the crank (w1 = crank rate)")
ph = th
zskin = np.array([np.abs(sum(np.sin(kk * x - r * p) for kk, r in zip((1.0, 1.3, 0.7), (1, 2, 3)))).max() for p in ph])
print(f"  mean skin peak during ground contact {zskin[ground].mean():.2f} vs swing {zskin[~ground].mean():.2f}")
print("  (with integer ratios the skin repeats every crank turn; golden ratios would never repeat, so no fixed gait-skin sync)")

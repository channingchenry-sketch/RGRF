#!/usr/bin/env python3
"""Which Platonic solids "breathe"? A bar-and-joint rigidity check (CC0).

Review: docs/platonic_breathing_craft_sketch_review.md

Each solid is modelled as a frame: vertices are pin joints, edges are rigid
bars. The rigidity matrix R (one row per bar, 3 columns per joint) gives the
infinitesimal motions that keep every bar length fixed. A frame in 3D always
has 6 trivial motions (3 translations, 3 rotations), so

    internal flexes (mechanisms) = 3V - rank(R) - 6.

Frames with only triangular faces (tetrahedron, octahedron, icosahedron) are
rigid (Cauchy/Dehn). The cube and dodecahedron frames flex. A second check
gives each bar the same spring constant and unit joint masses, and lists the
lowest non-zero vibration frequencies. The fully symmetric "breathing" mode
(every vertex moving radially in phase) is found and reported.

Run: python3 sims/platonic_frame_rigidity_check.py
"""
import itertools
import numpy as np

phi = (1 + 5 ** 0.5) / 2


def solid(name):
    if name == "tetrahedron":
        v = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
    elif name == "cube":
        v = list(itertools.product((-1, 1), repeat=3))
    elif name == "octahedron":
        v = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    elif name == "icosahedron":
        v = []
        for a, b in itertools.product((-1, 1), repeat=2):
            v += [(0, a, b * phi), (a, b * phi, 0), (b * phi, 0, a)]
    elif name == "dodecahedron":
        v = list(itertools.product((-1, 1), repeat=3))
        for a, b in itertools.product((-1, 1), repeat=2):
            v += [(0, a / phi, b * phi), (a / phi, b * phi, 0), (b * phi, 0, a / phi)]
    v = np.array(v, float)
    d = np.linalg.norm(v[:, None] - v[None], axis=2)
    emin = d[d > 1e-9].min()
    edges = [(i, j) for i in range(len(v)) for j in range(i + 1, len(v)) if abs(d[i, j] - emin) < 1e-6]
    return v, edges


def rigidity(v, edges):
    R = np.zeros((len(edges), 3 * len(v)))
    for k, (i, j) in enumerate(edges):
        u = v[i] - v[j]
        R[k, 3 * i:3 * i + 3] = u
        R[k, 3 * j:3 * j + 3] = -u
    return R


print(f"{'solid':13s} V  E  rank  flexes  lowest non-zero modes (rel.)  breathing mode (rel.)")
for name in ["tetrahedron", "cube", "octahedron", "icosahedron", "dodecahedron"]:
    v, edges = solid(name)
    R = rigidity(v, edges)
    rank = np.linalg.matrix_rank(R, tol=1e-9)
    flex = 3 * len(v) - rank - 6
    # spring network: K = R^T diag(1/L^2) R (unit k, unit mass)
    L2 = np.array([np.dot(v[i] - v[j], v[i] - v[j]) for i, j in edges])
    K = R.T @ np.diag(1 / L2) @ R
    w2, modes = np.linalg.eigh(K)
    nz = np.sqrt(np.clip(w2[w2 > 1e-9], 0, None))
    # breathing mode: overlap with uniform radial displacement
    rad = (v / np.linalg.norm(v, axis=1)[:, None]).ravel()
    rad /= np.linalg.norm(rad)
    # by symmetry the radial pattern is an exact eigenvector; check the residual
    lam = rad @ K @ rad
    resid = np.linalg.norm(K @ rad - lam * rad)
    wb = np.sqrt(max(lam, 0))
    ref = nz.max()
    print(f"{name:13s} {len(v):2d} {len(edges):2d} {rank:4d} {flex:6d}   "
          + ", ".join(f"{x / ref:.2f}" for x in nz[:3]).ljust(28)
          + f"  {wb / ref:.2f} (eigen-residual {resid:.0e})")
print("\nflexes > 0: the bar-and-joint frame has zero-energy mechanisms (it 'breathes' freely).")
print("All five have a fully symmetric breathing mode once bars are elastic.")

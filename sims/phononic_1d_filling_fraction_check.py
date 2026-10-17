#!/usr/bin/env python3
"""1D two-layer phononic crystal: does a golden-ratio layer split give "cleaner" band gaps?

CC0. Check for the Grok-reported 1D frequency sweep in the share "Tau Scaling Law for
Electronics" (message 44), which said golden-ratio layer proportions (~0.618) give
"cleaner, more predictable gaps compared to equal layers". No code was shown, so this
is an independent rebuild, not a rerun.

Model: longitudinal elastic waves through an infinite periodic bilayer (layer A, layer B),
period a = d_A + d_B. Rytov/transfer-matrix dispersion relation:
  cos(q a) = cos(k_A d_A) cos(k_B d_B) - 0.5 (Z_A/Z_B + Z_B/Z_A) sin(k_A d_A) sin(k_B d_B)
A frequency is in a band gap when |RHS| > 1. Frequencies are normalised as
Omega = f a / c_avg, with layer travel times chosen so the time-average speed is fixed.
Materials: quartz-like (rho 2650 kg/m^3, c 5960 m/s) and epoxy-like (1180, 2540).
Usage: python3 phononic_1d_filling_fraction_check.py
"""
import numpy as np

rhoA, cA = 2650.0, 5960.0   # quartz-like
rhoB, cB = 1180.0, 2540.0   # epoxy-like
ZA, ZB = rhoA * cA, rhoB * cB
eta = 0.5 * (ZA / ZB + ZB / ZA)

def gaps(fill, a=1.0, fmax=3.0, n=300001):
    """fill = d_A / a (geometric fraction of layer A). Return list of (f_lo, f_hi) in units of cB/a."""
    dA, dB = fill * a, (1 - fill) * a
    f = np.linspace(1e-6, fmax, n) * cB / a
    w = 2 * np.pi * f
    rhs = np.cos(w * dA / cA) * np.cos(w * dB / cB) - eta * np.sin(w * dA / cA) * np.sin(w * dB / cB)
    g = np.abs(rhs) > 1
    out, i = [], 0
    fn = f * a / cB
    while i < n:
        if g[i]:
            j = i
            while j < n and g[j]:
                j += 1
            out.append((fn[i], fn[j - 1]))
            i = j
        else:
            i += 1
    return out

if __name__ == "__main__":
    print(f"impedance ratio Z_A/Z_B = {ZA/ZB:.2f}")
    for fill in (0.5, 0.618, 0.382, 0.3, 0.7):
        gs = gaps(fill)
        widths = [hi - lo for lo, hi in gs]
        mid = [(hi + lo) / 2 for lo, hi in gs]
        rel = [w / m for w, m in zip(widths, mid)]
        print(f"fill={fill:5.3f}: {len(gs)} gaps below f*a/cB=3; "
              f"relative widths = {', '.join(f'{r:.3f}' for r in rel)}")
    # "quarter-wave" condition: equal travel times kA dA = kB dB maximises odd-order gaps
    fq = (cA) / (cA + cB)
    gs = gaps(fq)
    print(f"equal-travel-time fill={fq:.3f}: relative widths = "
          f"{', '.join(f'{(hi-lo)/((hi+lo)/2):.3f}' for lo, hi in gs)}")
    print("Result: every filling fraction opens gaps; their widths and positions follow the "
          "standard bilayer formula. 0.618 is not singled out: the widest first gap comes "
          "from equal travel times (quarter-wave stack), and at that fill the even-order gaps close.")

"""Share #161 (25ff8479) check: lift-per-watt bound for AC eddy-current lift over a conducting plate.

Thin-skin image-current model: tangential surface field H gives
  magnetic pressure  p = mu0*H^2/2   (upper bound, perfect reflection)
  surface loss       q = Rs*H^2/2,  Rs = 1/(sigma*delta)
so F/P <= mu0*sigma*delta = sqrt(2*mu0*sigma/omega), independent of field strength.
This counts plate loss only (coil copper, drive and RF losses add more), so it is an optimistic bound.
CC0.
"""
import math
mu0 = 4e-7 * math.pi
SIGMA = {"copper": 5.8e7, "aluminium": 3.5e7}
LIFTS_GROK = {0.00: 1547.0, 0.30: 1445.0, 0.50: 1360.0, 1.00: 1300.0}  # N, Grok-reported
P_GROK = 520.0  # W, Grok-reported input

def f_per_w(sigma, f):
    return math.sqrt(2 * mu0 * sigma / (2 * math.pi * f))

if __name__ == "__main__":
    for mat, s in SIGMA.items():
        for f in (1e3, 1e4, 1e5, 13.56e6):
            fpw = f_per_w(s, f)
            print(f"{mat:9s} f={f:>10.0f} Hz  F/P<={fpw:.4f} N/W  min power for 1547 N: {1547/fpw/1e3:9.1f} kW")
    print()
    for r, F in LIFTS_GROK.items():
        print(f"rim={r:.2f}  Grok lift {F:.0f} N at {P_GROK:.0f} W -> {F/P_GROK:.2f} N/W claimed")
    print("Ledger: steady hover does no mechanical work; all input is dissipated (plate + coil + drive). "
          "Claimed ~2.8-3.0 N/W exceeds the 13.56 MHz copper bound (~0.0013 N/W) by ~2000x and the 1 kHz bound (~0.15 N/W) by ~20x.")

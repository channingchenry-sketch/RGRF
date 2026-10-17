#!/usr/bin/env python3
"""
Moving-magnet eddy-current lift and drag check for Grok's 'v0.1 demo' sim claim
(Grok conversation "Open Source Regenerative Infrastructure Blueprint", msg 6, 2026-10-17).

Grok reported (no code shown): "At realistic B ~0.2 T and effective area ~0.8 m^2 over a 5 mm Al
plate, lift can overcome 80 kg weight even at low walking speeds in this idealized model."

This script is an independent, reproducible order-of-magnitude check using the standard thin-sheet
model for a magnet moving at speed v over a conducting sheet (Reitz 1970, J. Appl. Phys. 41, 2067):

    w   = 2 / (mu0 * sigma * d)               characteristic speed of the sheet
    F_L = F_img * v^2   / (v^2 + w^2)          lift
    F_D = F_img * v * w / (v^2 + w^2)          eddy drag   ->  F_L / F_D = v / w
    P_D = F_D * v                              mechanical power the mover must supply

F_img (the perfect-conductor image force) is bounded here by the magnetic pressure
B^2/(2 mu0) times the area. This is generous: it assumes the full 0.2 T acts uniformly over 0.8 m^2.
Key consequence: to hold a required lift F_L, the drag power is P_D = F_L * w (exactly, in this model),
independent of v. Speed buys lift from a given magnet; it does not reduce the power bill.

Validity: thin-sheet model needs d <~ skin depth at the pole-passing frequency f = v / pitch.
Labels: model Grounded (textbook); Grok's numbers Grok-reported (not reproducible, no code).
License CC0.
"""
import math

MU0 = 4e-7 * math.pi
G = 9.81
SIGMA = {"aluminum": 3.5e7, "copper": 5.96e7}

def run(B=0.2, area=0.8, d=0.005, plate="aluminum", mass=80.0, pitch=0.10):
    s = SIGMA[plate]
    w = 2.0 / (MU0 * s * d)
    F_img = B**2 / (2 * MU0) * area
    W = mass * G
    out = {"plate": plate, "d_mm": d * 1e3, "w": w, "F_img": F_img, "weight": W}
    rows = []
    for v in (1.0, 1.5, 2.0, 3.0, 5.0, 10.0, 20.0):
        FL = F_img * v * v / (v * v + w * w)
        FD = F_img * v * w / (v * v + w * w)
        f = v / pitch
        delta = math.sqrt(2.0 / (2 * math.pi * f * MU0 * s))
        rows.append((v, FL, FD, FD * v, delta * 1e3))
    out["rows"] = rows
    # speed at which lift = weight (if reachable) and the power then
    if W < F_img:
        v_need = w * math.sqrt(W / (F_img - W))
        out["v_need"] = v_need
        out["P_at_hover"] = W * w   # = F_D * v at that point
    return out

def report(o):
    print(f"\nPlate {o['plate']} {o['d_mm']:.0f} mm : w = 2/(mu0 sigma d) = {o['w']:.2f} m/s ; "
          f"image-force bound B^2 A/2mu0 = {o['F_img']:.0f} N ; weight = {o['weight']:.0f} N")
    print("   v [m/s]   lift [N]   drag [N]   drag power [W]   skin depth [mm] (pitch 10 cm)")
    for v, FL, FD, P, dl in o["rows"]:
        print(f"   {v:6.1f}   {FL:8.0f}   {FD:8.0f}   {P:12.0f}   {dl:10.1f}")
    if "v_need" in o:
        print(f"   lift = weight at v = {o['v_need']:.2f} m/s ; drag power there = m g w = {o['P_at_hover']:.0f} W "
              f"(= {o['P_at_hover']/250:.0f}x a strong cyclist's sustained 250 W)")

if __name__ == "__main__":
    print("Check of Grok msg-6 scenario: B 0.2 T, area 0.8 m^2, rider 80 kg, moving magnets over a sheet")
    for plate, d in (("aluminum", 0.005), ("copper", 0.005), ("aluminum", 0.010)):
        report(run(d=d, plate=plate))
    print("\nReading: 'low walking speed' (1-1.5 m/s) over 5 mm Al gives only ~150-340 N of lift (< 785 N),")
    print("and holding 80 kg needs ~2.3 m/s with ~7 kW of drag power, independent of speed (P = m g w).")
    print("Human sustained output is ~100-300 W. Thin-sheet validity: d=5 mm is below the skin depth")
    print("at walking speeds for a 10 cm pole pitch, so the model applies there.")

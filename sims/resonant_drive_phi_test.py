#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""
resonant_drive_phi_test.py -- square-wave half-bridge driving a series-RLC tank:
frequency sweep, drive efficiency (conduction + switching), Q / damping, and a phi ablation.

Thread: 'transistors' (Channing + Grok, "Adding Transistors to POL v0.1"); see docs/transistor_drive_stages.md.

MODEL (steady state, exact for a linear tank; Grounded circuit theory)
  Half-bridge switch node: v(t) = Vdc for 0 < t < T/2, 0 for T/2 < t < T (50 % duty, ideal dead-time-free
  waveform for the voltage). Fourier: v = Vdc/2 + sum_{n odd} (2 Vdc / (n pi)) sin(n w t).
  The DC part is blocked by the series C. Tank: Z_n = R_tot + j (n w L - 1/(n w C)),
  R_tot = R_load + R_esr + R_sw (R_sw = on-resistance of the ONE conducting switch; a half-bridge has one
  device in the current path at any time, a full H-bridge has two).
  i(t) = sum_n |V_n|/|Z_n| sin(n w t - angle Z_n), summed over odd n up to N_HARM.
  Power in each resistor = sum_n |I_n|^2 R / 2.
  Switching loss (toy, per edge, 2 edges per period, symmetric):
    i_sw = i(0+) (current out of the switch node at the high-side turn-on instant).
    i_zvs = 2 Coss_eff Vdc / t_dead  (current needed to swing the node in the dead time).
    i_sw <= -i_zvs           : full ZVS, E = 0
    -i_zvs < i_sw < 0        : partial ZVS, E = Eoss_hard (1 - |i_sw|/i_zvs)^2
    i_sw >= 0 (capacitive)   : hard switching + body-diode reverse recovery,
                               E = Coss_eff Vdc^2 + Qrr Vdc + 0.5 Vdc |i_sw| t_ov
    with Eoss_hard = Coss_eff Vdc^2. This is a first-order bookkeeping model, not a SPICE device model.
  Driver efficiency eta = P(R_load) / [P(R_load) + P(R_esr) + P(R_sw) + P_sw].

CASES
  A. Generic resonant tank (bench / ZVS / Class-D context): L = 100 uH, f0 = 100 kHz, Vdc = 48 V,
     R_esr = 50 mOhm, R_load chosen for loaded Q in {2, 5, 10, 30, 100}.
     Devices (datasheet values, see the doc): Wolfspeed C3M0065090D SiC (RDS(on) 65 mOhm typ @25 C,
     Qrr 185 nC, Coss 66 pF typ) vs Vishay IRFP460 (0.27 Ohm max, Qrr 5.7 uC typ, Coss 870 pF @25 V).
     Coss_eff (charge-equivalent at 48 V) is an ASSUMPTION: 150 pF (SiC), 600 pF (IRFP460). t_dead = 100 ns,
     t_ov = 20 ns (SiC) / 60 ns (IRFP460).
  B. POL v0.1 lift coil from Resona-POL-Modular-Core/sim/hover_dynamics.py default run:
     L = 20.3 uH (with floor), f0 = 100 Hz, R(copper + plate) = w L / Q with Q = 1.78, 763 A rms per coil, 4 coils.
     Switches: IRLB3034 (1.4 mOhm typ @10 V, ~1.7x hot) paralleled N per position.
  PHI ABLATION
     drive at f0, f0*phi, f0/phi (and f0/3 as a sanity check: the 3rd harmonic of a square wave hits f0);
     four quadrant tanks tuned f0_k = f0 * phi^k (k = 0..3) vs all tuned to f0, driven by one frequency;
     and each quadrant driven at its own f0_k (equal power, but the 2 f_k force ripples no longer cancel as
     a common heave and instead appear as rocking torques at four incommensurate frequencies).

Labels: series-RLC / half-bridge physics = Grounded (textbook). Switching-loss bookkeeping = Plausible-untested
(order-of-magnitude). Phi as a tuning rule = Symbolic; this script is the honest test.
Requires numpy and matplotlib.
"""
import argparse
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PHI = (1 + 5 ** 0.5) / 2
N_HARM = 199  # odd harmonics up to this order

DEVICES = {
    "SiC C3M0065090D": dict(rds=0.065, qrr=185e-9, coss=150e-12, t_ov=20e-9),
    "Si IRFP460": dict(rds=0.27, qrr=5.7e-6, coss=600e-12, t_ov=60e-9),
}


def tank_response(f, L, C, R_load, R_esr, R_sw, Vdc, ns=None):
    """Return dict of harmonic currents and powers for a half-bridge square wave at frequency f."""
    if ns is None:
        ns = np.arange(1, N_HARM + 1, 2)
    w = 2 * np.pi * f
    Rt = R_load + R_esr + R_sw
    Z = Rt + 1j * (ns * w * L - 1.0 / (ns * w * C))
    Vn = 2 * Vdc / (ns * np.pi)                    # amplitude of sin(n w t)
    In = Vn / np.abs(Z)                             # amplitude
    ph = np.angle(Z)
    i0 = float(np.sum(In * np.sin(-ph)))            # current at t = 0+ (high-side turn-on)
    I2 = 0.5 * np.sum(In ** 2)                      # mean-square current
    return dict(I2=I2, i0=i0, P_load=I2 * R_load, P_esr=I2 * R_esr, P_sw_cond=I2 * R_sw,
                I1=In[0], phase1=ph[0])


def switching_loss(i0, f, Vdc, dev, t_dead=100e-9):
    coss, qrr, t_ov = dev["coss"], dev["qrr"], dev["t_ov"]
    e_hard = coss * Vdc ** 2
    i_zvs = 2 * coss * Vdc / t_dead
    if i0 <= -i_zvs:
        E = 0.0
    elif i0 < 0:
        E = e_hard * (1 - abs(i0) / i_zvs) ** 2
    else:
        E = e_hard + qrr * Vdc + 0.5 * Vdc * abs(i0) * t_ov
    return 2 * f * E


def evaluate(f, L, C, R_load, R_esr, dev, Vdc, t_dead=100e-9, n_par=1):
    r = tank_response(f, L, C, R_load, R_esr, dev["rds"] / n_par, Vdc)
    Psw = switching_loss(r["i0"], f, Vdc, dev, t_dead)
    Pin = r["P_load"] + r["P_esr"] + r["P_sw_cond"] + Psw
    r.update(P_switching=Psw, P_in=Pin, eta=r["P_load"] / Pin if Pin > 0 else 0.0)
    return r


def case_a(out_lines, Qs=(2, 5, 10, 30, 100)):
    L, f0, Vdc, R_esr = 100e-6, 100e3, 48.0, 0.05
    C = 1 / ((2 * np.pi * f0) ** 2 * L)
    w0L = 2 * np.pi * f0 * L
    fr = np.linspace(0.3, 2.0, 3401)
    res = {}
    dev_sic = DEVICES["SiC C3M0065090D"]
    pr = out_lines.append
    pr("CASE A  generic tank: L = 100 uH, f0 = 100 kHz (C = %.2f nF), Vdc = 48 V, R_esr = 50 mOhm" % (C * 1e9))
    pr("  loaded Q = w0 L / R_tot ; R_load set so that Q (with SiC R_ds) equals the target")
    for Q in Qs:
        R_tot = w0L / Q
        R_load = max(R_tot - R_esr - dev_sic["rds"], 1e-3)
        P = np.array([evaluate(x * f0, L, C, R_load, R_esr, dev_sic, Vdc)["P_load"] for x in fr])
        eta = np.array([evaluate(x * f0, L, C, R_load, R_esr, dev_sic, Vdc)["eta"] for x in fr])
        res[Q] = dict(P=P, eta=eta, R_load=R_load)
        k_pk = int(np.argmax(P[(fr > 0.6)])) + int(np.sum(fr <= 0.6))
        k_eta = int(np.argmax(eta[(fr > 0.6)])) + int(np.sum(fr <= 0.6))
        def at(x):
            return evaluate(x * f0, L, C, R_load, R_esr, dev_sic, Vdc)
        p0, pphi, pinv, p3 = at(1.0), at(PHI), at(1 / PHI), at(1 / 3)
        tau_cycles = Q / np.pi  # ring-down (1/e amplitude) in cycles: tau = 2L/R = Q/(pi f0)
        pr("  Q=%5.0f  R_load=%7.3f Ohm | P(f0)=%8.1f W eta=%5.1f%% | P(f0*phi)/P(f0)=%.4f eta=%5.1f%% | "
           "P(f0/phi)/P(f0)=%.4f eta=%5.1f%% | P(f0/3)/P(f0)=%.4f | peak P at f/f0=%.3f, peak eta at f/f0=%.3f | "
           "tank Vc peak ~ %.0f V | ring-down %.1f cycles"
           % (Q, R_load, p0["P_load"], 100 * p0["eta"], pphi["P_load"] / p0["P_load"], 100 * pphi["eta"],
              pinv["P_load"] / p0["P_load"], 100 * pinv["eta"], p3["P_load"] / p0["P_load"],
              fr[k_pk], fr[k_eta], p0["I1"] / (2 * np.pi * f0 * C), tau_cycles))
    # device comparison at Q = 10
    Q = 10
    R_load = res[Q]["R_load"]
    dev_res = {}
    for name, dev in DEVICES.items():
        ev = [evaluate(x * f0, L, C, R_load, R_esr, dev, Vdc) for x in fr]
        dev_res[name] = dict(eta=np.array([e["eta"] for e in ev]), P=np.array([e["P_load"] for e in ev]),
                             i0=np.array([e["i0"] for e in ev]))
        e1 = evaluate(f0, L, C, R_load, R_esr, dev, Vdc)
        e_hi = evaluate(1.05 * f0, L, C, R_load, R_esr, dev, Vdc)
        e_lo = evaluate(0.95 * f0, L, C, R_load, R_esr, dev, Vdc)
        e_phi = evaluate(PHI * f0, L, C, R_load, R_esr, dev, Vdc)
        pr("  Q=10, %-16s: eta(0.95 f0)=%5.1f%% [capacitive, hard + Qrr]  eta(f0)=%5.1f%%  eta(1.05 f0)=%5.1f%% "
           "[inductive, ZVS]  eta(phi f0)=%5.1f%%  P_load(f0)=%.0f W  P_switching(0.95 f0)=%.1f W"
           % (name, 100 * e_lo["eta"], 100 * e1["eta"], 100 * e_hi["eta"], 100 * e_phi["eta"], e1["P_load"],
              e_lo["P_switching"]))
    return fr, res, dev_res


def case_b(out_lines, n_par_list=(1, 4, 8, 16)):
    pr = out_lines.append
    L, f0, Q, I_rms, n_coils = 20.3e-6, 100.0, 1.78, 763.0, 4
    R_plant = 2 * np.pi * f0 * L / Q
    P_plant = n_coils * I_rms ** 2 * R_plant
    pr("CASE B  POL v0.1 lift coil (hover_dynamics.py default): L = 20.3 uH, f0 = 100 Hz, Q = 1.78, "
       "R(copper+plate) = %.2f mOhm, I = 763 A rms/coil, 4 coils" % (R_plant * 1e3))
    pr("  plant loss (the hover bill, independent of the driver) = %.0f W" % P_plant)
    rds_hot = 1.4e-3 * 1.7
    for topo, n_series in (("half-bridge", 1), ("H-bridge", 2)):
        for n_par in n_par_list:
            R_sw = n_series * rds_hot / n_par
            P_sw = n_coils * I_rms ** 2 * R_sw
            pr("  %-11s IRLB3034 x%-2d per position: R_sw=%.3f mOhm  conduction loss %6.0f W  -> total %6.0f W "
               "(driver eta %.1f%%), per-device current %.0f A rms (package limit 195 A DC)"
               % (topo, n_par, R_sw * 1e3, P_sw, P_plant + P_sw, 100 * P_plant / (P_plant + P_sw), I_rms / n_par))
    # IRFP460 for comparison (wrong voltage/current class)
    P460 = n_coils * I_rms ** 2 * 0.27
    pr("  IRFP460 (0.27 Ohm) single device per position: conduction loss would be %.0f kW (wrong part class)"
       % (P460 / 1e3))
    # phi detuning of the broad POL tank
    C = 1 / ((2 * np.pi * f0) ** 2 * L)
    fr = np.linspace(0.3, 2.0, 1701)
    dev = dict(rds=rds_hot / 8, qrr=0, coss=0, t_ov=0)
    P = np.array([tank_response(x * f0, L, C, R_plant, 0, dev["rds"], 1.0)["P_load"] for x in fr])
    P = P / P.max()
    p = lambda x: tank_response(x * f0, L, C, R_plant, 0, dev["rds"], 1.0)["P_load"] / \
        tank_response(f0, L, C, R_plant, 0, dev["rds"], 1.0)["P_load"]
    pr("  POL tank (Q~1.8): P(f0*phi)/P(f0)=%.3f, P(f0/phi)/P(f0)=%.3f (broad, but still peaked at f0, "
       "not at a phi ratio)" % (p(PHI), p(1 / PHI)))
    return fr, P


def quadrants(out_lines, Q=10):
    pr = out_lines.append
    L, f0, Vdc, R_esr = 100e-6, 100e3, 48.0, 0.05
    w0L = 2 * np.pi * f0 * L
    dev = DEVICES["SiC C3M0065090D"]
    R_load = w0L / Q - R_esr - dev["rds"]
    pr("QUADRANTS (Case A tank, Q = %d), one common drive frequency f0" % Q)
    for label, ks in (("all tuned to f0", [0, 0, 0, 0]), ("phi ladder f0*phi^k, k=0..3", [0, 1, 2, 3]),
                      ("phi ladder centred, f0*phi^(k-1.5)", [-1.5, -0.5, 0.5, 1.5])):
        Ps, etas = [], []
        for k in ks:
            fk = f0 * PHI ** k
            Ck = 1 / ((2 * np.pi * fk) ** 2 * L)
            e = evaluate(f0, L, Ck, R_load, R_esr, dev, Vdc)
            Ps.append(e["P_load"]); etas.append(e["eta"])
        Ps = np.array(Ps)
        pr("  %-34s P per quadrant = %s W | total %.0f W | max/min imbalance %.1fx | eta %s"
           % (label, np.array2string(Ps, precision=1), Ps.sum(), Ps.max() / max(Ps.min(), 1e-12),
              np.array2string(100 * np.array(etas), precision=1)))
    # each quadrant at its own f0_k: ripple bookkeeping (force ~ i^2 -> DC + 2 f_k component)
    fk = f0 * PHI ** np.arange(4)
    pr("  each quadrant driven at its own f0_k (k=0..3): equal power each, but 2f force ripple at "
       "%s kHz on different corners -> rocking torques at 4 incommensurate frequencies; with equal tuning the "
       "ripple is one common 2 f0 = %.0f kHz heave term (cancels in roll/pitch if phased together)."
       % (np.array2string(2 * fk / 1e3, precision=1), 2 * f0 / 1e3))
    return


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "docs", "images",
                                                  "resonant_drive_phi_test.png"))
    a = ap.parse_args()
    lines = []
    fr, res, dev_res = case_a(lines)
    frB, PB = case_b(lines)
    quadrants(lines)
    print("\n".join(lines))

    fig, ax = plt.subplots(2, 2, figsize=(13, 9))
    for Q, d in res.items():
        ax[0, 0].semilogy(fr, d["P"], label="Q=%d" % Q)
    for x, lab in ((1, "f0"), (PHI, "f0*phi"), (1 / PHI, "f0/phi"), (1 / 3, "f0/3")):
        ax[0, 0].axvline(x, ls="--", c="k" if x == 1 else "gray", lw=0.8)
        ax[0, 0].text(x, 0.98, " " + lab, rotation=90, va="top", fontsize=8, transform=ax[0, 0].get_xaxis_transform())
    ax[0, 0].set_xlabel("drive frequency f / f0"); ax[0, 0].set_ylabel("power to load [W]")
    ax[0, 0].set_title("A. Half-bridge -> series RLC (48 V, SiC): power peaks at f0 = 1/(2 pi sqrt(LC))")
    ax[0, 0].legend(fontsize=8)
    for name, d in dev_res.items():
        ax[0, 1].plot(fr, 100 * d["eta"], label=name)
    ax[0, 1].axvspan(fr[0], 1.0, color="r", alpha=0.07, label="capacitive (hard switching + diode Qrr)")
    ax[0, 1].axvspan(1.0, fr[-1], color="g", alpha=0.07, label="inductive (ZVS possible)")
    for x in (1, PHI, 1 / PHI):
        ax[0, 1].axvline(x, ls="--", c="gray", lw=0.8)
    ax[0, 1].set_ylim(0, 100); ax[0, 1].set_xlabel("f / f0"); ax[0, 1].set_ylabel("driver efficiency [%]")
    ax[0, 1].set_title("A. Q = 10: efficient plateau just above f0 (ZVS); below f0 hard switching\n(dips near f0/3, f0/5: a harmonic hits f0)", fontsize=9)
    ax[0, 1].legend(fontsize=8)
    ax[1, 0].plot(frB, PB)
    for x in (1, PHI, 1 / PHI):
        ax[1, 0].axvline(x, ls="--", c="gray", lw=0.8)
    ax[1, 0].set_xlabel("f / f0 (f0 = 100 Hz)"); ax[1, 0].set_ylabel("relative power")
    ax[1, 0].set_title("B. POL v0.1 lift coil (Q ~ 1.8): broad peak, still at f0")
    # quadrant bar chart
    L, f0, Vdc, R_esr = 100e-6, 100e3, 48.0, 0.05
    dev = DEVICES["SiC C3M0065090D"]; R_load = 2 * np.pi * f0 * L / 10 - R_esr - dev["rds"]
    width = 0.38
    for j, (lab, ks) in enumerate((("all tuned f0", [0, 0, 0, 0]), ("phi ladder", [0, 1, 2, 3]))):
        Ps = [evaluate(f0, L, 1 / ((2 * np.pi * f0 * PHI ** k) ** 2 * L), R_load, R_esr, dev, Vdc)["P_load"]
              for k in ks]
        ax[1, 1].bar(np.arange(4) + (j - 0.5) * width, Ps, width, label=lab)
    ax[1, 1].set_yscale("log"); ax[1, 1].set_xticks(range(4)); ax[1, 1].set_xticklabels(["Q1", "Q2", "Q3", "Q4"])
    ax[1, 1].set_ylabel("power per quadrant [W]"); ax[1, 1].legend(fontsize=8)
    ax[1, 1].set_title("Quadrants on one drive at f0: phi-ratio tuning starves 3 of 4")
    fig.suptitle("resonant_drive_phi_test.py (CC0): resonance is set by L and C; phi ratios add nothing", fontsize=12)
    fig.tight_layout()
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    fig.savefig(a.out, dpi=110)
    print("plot:", os.path.relpath(a.out))


if __name__ == "__main__":
    main()

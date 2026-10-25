# The leaky bound-state family: heliosphere, craft boundary and cavity in one framework (2026-10-25)

*License CC0. Channing on H285f (2026-10-25): "All of them, linked". Labels: **Grounded**, **Plausible-untested**, **Speculative**, **Symbolic**. Sim: [../sims/leaky_bound_state_family_sim.py](../sims/leaky_bound_state_family_sim.py) (illustration).*

**Linked docs:** [leaky_boundary_tunneling_review.md](leaky_boundary_tunneling_review.md) (tunneling, Gamow states, gradients) · [it3_leaky_bound_states_review.md](it3_leaky_bound_states_review.md) (msg 7: "Let’s explore the bound states (almost sound like our cavity) also let’s see how closely it aligns to our cosmological path"; msg 9: the heliosphere "leaky bound state") · [pol_v0_1_zones.md](pol_v0_1_zones.md) line 153 ("Material choice the loops typically going around the outside much like on our craft creating a sort of control for the leaky boundary") · heliopause balance: [electrostatic_isotropic_stress_review.md](electrostatic_isotropic_stress_review.md) and `sims/heliopause_pressure_balance.py` (commit 44423b3).

## 1. One framework

Every member has the same six entries:
1. a **confinement mechanism**;
2. **what is trapped**;
3. a **leak channel**;
4. a **leak rate Γ**, with lifetime τ = 1/Γ (or ħ/Γ for the quantum case);
5. a **quality factor Q = ωτ** where an oscillation frequency exists;
6. a **gating knob** and an **energy source** that keeps the state filled.

Steady state: stored energy U = P_in·τ. The maths is the same leaky-resonator (Lorentzian / exponential-decay) equation in every row, which is **Grounded** in each row's own physics. Using one language across scales is **Symbolic**: the mechanisms differ.

## 2. Comparison table

| Row | Confinement | Trapped | Leak channel(s) | τ (Γ = 1/τ) | Q = ωτ | Gating knob | Energy source | Label |
|---|---|---|---|---|---|---|---|---|
| **A: heliosphere** | Solar-wind ram pressure vs interstellar pressure (heliopause ~120 au; balance 267 ± 55 vs ~229 fPa) | Solar-wind plasma, pickup ions, ACRs; also shields against GCRs | Charge exchange, reconnection at the heliopause, ACR escape along the "magnetic highway", GCR inward diffusion | Plasma residence ~2.5 yr (estimate: 94 au at ~400 km/s ≈ 1.1 yr to the termination shock, plus ~1.4 yr across the heliosheath at ~100 km/s) **Plausible-untested** [to verify against models]. GCR modulation follows the ~11 yr solar cycle **Grounded** | n/a (no oscillation) | Solar activity (wind pressure, field) | Solar wind, ~10²⁰ W kinetic [to verify] | Data **Grounded**; "bound state" **Symbolic** |
| **B: craft controlled boundary** | Perimeter piezo-helium/diamond–quartz loop as a thermal/acoustic guard (pol_v0_1_zones) | Heat / acoustic energy / plasma near the hull [Channing to supply] | Designed, switchable leak (vents, conduction, field opening) | Bench-assumed 0.1 s (sim) [Channing to supply] | [Channing to supply] | Duty cycle of the switched leak, loop material | Onboard power only | **Plausible-untested** (guard loop); field "leak control" **Speculative** |
| **C: cavity as engineered bound state** | Walls / impedance mismatch (acoustic, water or EM cavity) | Standing-wave energy | Wall loss, ports, radiation | Bench-assumed Q = 100 at 1 kHz gives τ = 16 ms | 100 (assumed) | Port coupling, damping | Driver | **Grounded** as cavity physics; the IT³ / cosmological alignment is **Symbolic** |
| Ref: quantum double barrier (our sim) | Two 0.3 eV barriers, 10 nm well | One electron in a quasi-bound level | Tunneling out | ħ/Γ = 4.5 ps (Γ = 0.146 meV at 34.1 meV) | E/Γ ≈ 230 | Bias voltage (detunes the level) | Leads / bias | **Grounded** |
| Ref: optical microresonator | Total internal reflection in a microtoroid/sphere | Photons | Scattering, absorption, the coupling taper | Q~10⁸ at 194 THz gives τ ≈ 82 ns | ~10⁸ (Armani et al., *Nature* 421, 925 (2003) [to verify]) | Taper gap (evanescent coupling) | Laser | **Grounded** |
| Ref: SRF niobium cavity | Superconducting walls | Microwave photons | Surface resistance, couplers | Q₀~10¹⁰ at 1.3 GHz gives τ ≈ 1.2 s | ~10¹⁰ (typical TESLA-type 2 K [to verify]) | Input coupler Q_ext | RF klystron | **Grounded** |
| Ref: Earth's magnetosphere (ring current) | Geomagnetic dipole vs solar-wind pressure (magnetopause ~10 R_E) | Ring-current ions | Charge exchange with geocorona, precipitation, outflow at the magnetopause | e-folding 7.7 h (Burton, McPherron & Russell, *JGR* 80, 4204 (1975)); ~3 h in main phase; τ ≈ 2.40 exp[9.74/(4.69+VBs)] h (O'Brien & McPherron 2000, doi 10.1029/1998JA000437) | n/a | IMF Bz (southward opens Dungey reconnection) | Solar wind via reconnection | **Grounded** |

τ spans about 20 orders of magnitude, from 4.5 ps to ~8×10⁷ s. That spread is the point of the family view. Each member is "filled + leaking", and in steady state its stored energy is P_in·τ, never more.

## 3. Sim (illustration)

`sims/leaky_bound_state_family_sim.py`. The energy-envelope equation is dU/dt = P_in − U/τ_d − g(t)U/τ_L.
- **(i)** Normalised decay e^(−t/τ) for all seven rows on a log time axis.
- **(ii)** Craft gating demo with bench-assumed values: P_in = 1 W, τ_d = 1 s, τ_leak = 0.1 s, gate at 2 Hz. After 10 s (10 J in):

| Duty | Stored | Leaked | Dissipated |
|---|---|---|---|
| 0 (closed) | 1.00 J | 0 J | 9.00 J |
| 0.25 | 0.435 J | 6.59 J | 2.98 J |
| 0.50 | 0.303 J | 7.88 J | 1.82 J |

The ledger residual is ~10⁻¹¹ J and out/in = 1.000000 in every case. Opening the gate trades stored energy for leakage. Sustaining the boundary costs exactly the power that leaks plus the power dissipated, with no surplus. **Grounded** (energy conservation).

Plot: `/workspace/leaky_bound_state_family_plot.png` (box only).

## 4. What the family view adds, honestly
- A shared test language: for any proposed "leaky boundary", ask for τ, Γ, Q, the knob and the source. This is **Plausible-untested** as a design discipline.
- B can borrow from A and the magnetosphere: an Earth-like "Bz knob" (switched opening) is the gating concept; the ring-current τ shows how a natural boundary refills and drains. This is an analogy, **Symbolic**.
- Nothing in the family creates energy, and quantum tunneling plays no role in rows A–C. **Grounded.**

## 5. Gaps
- Craft: what is trapped, the target τ/Q, the leak hardware and the power budget [Channing to supply].
- Cavity C: medium, frequency, measured Q [Channing to supply].
- [to verify]: heliosheath residence time from models; solar-wind power figure; Armani 2003 Q; SRF Q₀ reference.

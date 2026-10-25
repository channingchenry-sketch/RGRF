# Segmented Halbach arrays, litz-loop tracks and drag reduction (POL lift, open item 8)

*License CC0. Sim: [`sims/halbach_litz_drag_sim.py`](../sims/halbach_litz_drag_sim.py) → [`sims/halbach_litz_drag_sim_output.txt`](../sims/halbach_litz_drag_sim_output.txt), plots `sims/halbach_litz_LD_vs_speed.png`, `sims/halbach_litz_N_per_kW.png`, `sims/halbach_litz_area_vs_gap.png`. Requested by Channing (2026-10-24): segmented Halbach arrays with insulating gaps connected by litz wire, with the focus on **drag reduction**. Answers [DESIGN_FORCE_FLOW_MAP.md](DESIGN_FORCE_FLOW_MAP.md) open item 8 against the POL baseline of ~52 N/kW (10–17 kW for 88 kg = 863 N). Labels: model outputs **Grounded (model-based)**; hardware claims **Plausible-untested**; no φ used.*

## 1. Models (analytic, 2-D, first harmonic)
- **Halbach field** (Halbach 1980; Post & Ryutov 2000): B₀ = B_r(1 − e^{−kd})·sin(π(1−g)/M)/(π/M), k = 2π/λ, M segments per wavelength, d magnet depth, **g = insulating-gap fraction between magnet segments**. The gap term is the fundamental Fourier coefficient of a stepped magnetisation whose segments are narrowed to (1−g) of their pitch (g = 0 gives the standard formula). Higher harmonics, end effects and finite width ignored. B_r = 1.35 T NdFeB, d = λ/4. Field at gap y: B₀e^{−ky}.
- **EDS lift/drag** (Inductrack: R. F. Post & D. D. Ryutov, *IEEE Trans. Appl. Supercond.* 10, 901 (2000); thin sheet: J. R. Reitz, *J. Appl. Phys.* 41, 2067 (1970)): F_L = P∞A/(1 + (v_c/v)²), F_D/F_L = v_c/v = R/ωL, ω = kv, P∞ = B₀²e^{−2ky}/2μ₀.
  - **Litz ladder** (insulated, shorted loops): v_c = 4ρF_R/(μ₀tη) (t conductor depth, η copper fill, F_R AC/DC resistance ratio; mutual inductance only, leakage omitted).
  - **Solid plate**: v_c = 2ρ/(μ₀t_eff), t_eff = δ(1 − e^{−t/δ}), δ = skin depth at f = v/λ (crude interpolation; the exact thick-plate result differs by O(1)).
  - **Litz F_R:** strand skin 1 + (r_s/δ)⁴/48 plus an order-of-magnitude bundle proximity term N_s(d_s/δ)⁴/32 (after Sullivan, *IEEE TPEL* 14, 283 (1999)).
- **Electrodynamic wheel** (J. Bird & T. A. Lipo, *IEEE Trans. Magn.* 2003–2008 series [to verify exact refs]): Halbach rotor spun over a stationary conductor, unrolled onto the flat model with slip speed v_s = ω_m r_o and active arc r_oπ/3 (assumption). Drag torque T = F_D r_o; shaft power = F_D v_s.

**Key result (Grounded, model):** magnetic drag power P_D = F_D v = **F_L·v_c**. Drag power per newton of lift is just the transition speed v_c (W/N), so N/kW = 1000/v_c, independent of speed, gap or λ. Speed buys L/D (drag force falls as 1/v) but not watts per newton. Every drag lever is therefore a v_c lever.

## 2. Results (λ = 10 cm unless stated; from the output file)
| Case | v_c (m/s) = W/N | L/D at 100 m/s | N/kW (magnetic drag only) | vs 52 N/kW | Label |
|---|---|---|---|---|---|
| Cu litz ladder, t = 10 mm, η = 0.6 | 8.9 | 11 | 112 | ×2.2 | Grounded (model) |
| Cu litz ladder, t = 20 mm | 4.5 | 22 | 224 | ×4.3 | Grounded (model) |
| Cu litz, η = 0.8 | 6.7 | 15 | 150 | ×2.9 | Grounded (model) |
| Al litz, t = 10 mm | 14.1 | 7 | 71 | ×1.4 | Grounded (model) |
| Cu solid plate 10 mm, at 10 m/s / 100 m/s | 5.2 / 13.1 | 7.7 (100 m/s) | 191 / 77 | ×3.7 / ×1.5 | Grounded (model) |
| Cu litz cooled to 77 K (ρ ≈ 0.2 µΩ·cm) | 1.06 | 94 | ~940 | ×18 | Grounded (model); cryo cost excluded |

- **Litz AC resistance:** at f ≤ 1 kHz (100 m/s, λ = 10 cm) δ_Cu ≥ 2.1 mm; 0.1 mm strands × 1000 give F_R ≈ 1.0002. Skin/proximity losses in litz are negligible here. **Grounded (model).**
- **Plate vs litz:** a solid plate is skin-depth limited once t > δ, so its v_c grows ~√v. Below ~20–30 m/s at λ = 10 cm a 10 mm Cu plate actually beats a 60 %-fill litz ladder; litz wins at high speed or short λ (high f), where the plate's current is squeezed into δ. **Grounded (model), O(1) model uncertainty.**
- **Halbach segment gaps:** B₀ falls ~(1 − g): g = 0.05/0.10/0.20 gives 0.99/0.94/0.84 T (M = 8). Lift ∝ B₀², so a 10 % gap costs ~19 % lift. Gaps don't change W/N, only the area/magnet mass needed. M = 8 gives ~8 % more B₀ than M = 4. **Grounded (model).**
- **Hover gap 5–30 mm and λ:** they set the area, not the drag efficiency. For 863 N at λ = 10 cm you need 42 / 78 / 275 / 965 cm² at y = 5/10/20/30 mm; at λ = 40 cm, 26–57 cm². Rule: keep y ≲ λ/10. **Grounded (model).**
- **Transition speed:** 4.5–14 m/s (16–50 km/h) for room-temperature 10–20 mm conductors; ~1 m/s at 77 K. Post & Ryutov's "few km/h" relies on deeper, denser conductor stacks plus leakage inductance, which this model omits. **Grounded (model).**
- **Electrodynamic wheel, stationary hover:** 4 counter-rotating rotors (r_o = 0.10 m, 0.10 m wide, 4 pole pairs, λ = 15.7 cm, y = 10 mm, Cu litz 10 mm). Capacity ~7.4 kN, so 863 N needs only modest v_s. Magnetic drag = 863 N × 8.9 m/s ≈ **7.7 kW (112 N/kW)**. Add a motor at η = 0.85 and a +20 % windage/bearing allowance: ≈ **10.9 kW → ~79 N/kW**, about 1.5× the 52 N/kW baseline. With a 20 mm conductor, ≈ 5.4 kW (~160 N/kW). **Plausible-untested** as hardware (net thrust, gyroscopic torques and stability not modelled).

## 3. Magnetic drag vs drive power (kept separate)
- Everything in §2 is **magnetic drag** (I²R/eddy heat in the conductor).
- A **moving craft** on a track still needs propulsion against aero drag (not included).
- A **wheel hover** needs motor input = magnetic drag + motor loss + windage + bearings, and the track/plate must be underneath. There is no free hover: the power just moves from coil drive (baseline) to rotor drive.

## 4. Top drag-reduction levers (ranked)
1. **More conductor per circuit at lower resistivity (t·η/ρ).** Doubling depth halves W/N; fill 0.6 → 0.8 gives −25 %; Cu over Al gives −37 %; cooling Cu to 77 K gives ~8×. This is the dominant lever. **Grounded (model).**
2. **Match conductor type to frequency.** Use litz/insulated loops (Channing's segmented-gap idea) only where t > δ at f = v/λ: high speed or short λ. Otherwise a thick solid plate is as good or better. Litz also fixes the current paths (defined L/R) and avoids edge-eddy spreading. **Grounded (model).**
3. **Run well above v_c, with a field-efficient array.** L/D = v/v_c, so operate at v ≥ 3–5 v_c to keep lift ≥ 90 % without wasting drag force. Use M = 8, small magnet gaps (≤ 5 %) and λ ≳ 10y to shrink area/magnet mass for the same W/N. **Grounded (model).**

## 5. Honest caveats
- 2-D, first-harmonic, infinite-width model; leakage inductance, end effects, track edge returns and rail resistance omitted. Expect O(1) (factor ~2) errors in v_c. **Model limitation.**
- P∞ = B²/2μ₀ is an order-of-magnitude high-speed pressure.
- The wheel active arc (r_oπ/3) is an assumption; Bird & Lipo give exact 2-D rotor results [to verify].
- Cryogenic cooling power, magnet cost/mass and thermal limits are excluded.
- No bench data yet. The open bench test stays: Al/Cu plate vs litz ladder under a spinning Halbach rotor, N per W vs rpm. **Plausible-untested** until measured.

*Materials / switched-arc follow-up: [halbach_switched_arc_materials_check.md](halbach_switched_arc_materials_check.md) (45° M = 8 arc, hard vs ramped switching, NdFeB vs SmCo vs ferrite vs nickel).*

*Control follow-up: [halbach_rotor_control_vs_perturbation_sections.md](halbach_rotor_control_vs_perturbation_sections.md) (four-rotor EDW hover: height/tilt/lateral/precession mapping, control sim).*

*See also: [lift_and_equilibrium_systems.md §9](lift_and_equilibrium_systems.md), [DESIGN_FORCE_FLOW_MAP.md](DESIGN_FORCE_FLOW_MAP.md) §4 and open item 8.*

- **See also (2026-10-25):** [stator_review.md](stator_review.md): stator topologies, windings, losses, cogging and the track as an unrolled stator.

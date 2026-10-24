# Halbach electrodynamic-wheel hover vs the earlier perturbation sections (height, tilt, lateral, egg precession)

*License CC0. Compares [shifting_phase_order_review.md §A4](shifting_phase_order_review.md) (perturbation sections 1–3) and [DESIGN_FORCE_FLOW_MAP.md §1](DESIGN_FORCE_FLOW_MAP.md) (laminar precession in the egg) with the four counter-rotating Halbach electrodynamic-wheel (EDW) hover from [halbach_litz_drag_reduction.md](halbach_litz_drag_reduction.md). Sim: [`sims/halbach_rotor_control_sim.py`](../sims/halbach_rotor_control_sim.py) → [`sims/halbach_rotor_control_sim_output.txt`](../sims/halbach_rotor_control_sim_output.txt), plots `sims/halbach_rotor_heave_step.png`, `sims/halbach_rotor_tilt_gyro.png`, `sims/halbach_rotor_lateral_move.png`. Labels: **Grounded** (physics / model output), **Plausible-untested** (hardware), **Symbolic** (φ phasing; not used in the sim).*

**Key reframe.** The drag on each rotor is also its thrust. Counter-rotating pairs cancel it (and their angular momentum) in steady hover, and unbalancing a pair "borrows" that drag as steering force. In the model, manoeuvring this way barely changes the magnetic drag power, because P = Σ F_L·v_c stays fixed while lift is fixed.

## 1. Mapping
| Earlier section | Earlier mechanism | EDW-hover equivalent | Label |
|---|---|---|---|
| A4.1 Height | Load step → steep F(h) restores → damping → power/frequency modulation | **Height = rotor speed (collective).** EDS lift ∝ e^{−2kz} gives the steep F(z); lift rises with slip speed (strongest near v ≈ v_c) | **Grounded** |
| A4.2 Tilt | Differential coil power + gyroscopic moment | **Tilt = differential rotor speed** (front/back for pitch, left/right for roll) | **Grounded** |
| A4.3 Lateral | Coil phase shift → travelling field (LIM) | **Each rotor's drag force is also thrust.** It cancels in counter-rotating pairs and is unbalanced to steer (pure-x pattern (1, −1, −1, 1)). A spinning Halbach rotor is the rotary analogue of the LIM travelling wave | **Grounded** |
| §1 Laminar precession in the egg (torque, not lift) | Precession redistributes angular momentum; no net lift | **The rotors are gyros.** Counter-rotation nulls net angular momentum; tilting a pair's axes gives CMG-style attitude torque. Torque only, **no lift**, the same conclusion as the egg | **Grounded** |
| "Laminar" / "sympathetic gaps" | Smooth flow, gaps for sympathetic response | **Insulated litz sections** confine the induced-current paths (lower eddy loss, defined L/R) | **Grounded** for loss; the "laminar" comparison is **analogy only** |
| A4.1 damping (ζ target 0.7) | Old POL sim ζ ≈ 0.024 | EDS is inherently lightly damped (ζ ≈ 0.016–0.024 open loop here); active control is required | **Grounded** |
| Power | Coil-over-plate baseline ~52 N/kW | EDW: ~224 N/kW magnetic for a 20 mm Cu litz track; ~79 N/kW for the 10 mm case with motor and windage allowance | **Plausible-untested** (hardware) |
| Phase choice (φ, golden-angle phasing) | φ-phased drive | Not needed; no φ test done | **Symbolic** |

Channing's earlier egg line ([DESIGN_FORCE_FLOW_MAP §1b](DESIGN_FORCE_FLOW_MAP.md)): *"…also, utilized phase shifts in the eggs design. The design parameters were built off of what it would take to be buoyant and gaps that allowed sympathetic responses."* In the EDW the phase shifts become rotor speed and spin-sense differences, and the gaps become insulated litz sections and the hover gap.

## 2. Sim results (88 kg, four EDW rotors at the corners (±0.35 m), 20 mm Cu litz track, v_c = 4.46 m/s; all **Grounded (model)**)
- **Hover point.** Slip speed 6.7 m/s (1.5 v_c, chosen for maximum lift-vs-speed authority; W/N = v_c regardless), 638 rpm, gap 23.6 mm. Magnetic drag 3.85 kW (224 N/kW). Heave stiffness 69 kN/m, f_n = 4.5 Hz.
- **Damping vs the 0.7 target.**
  - Open loop: ζ ≈ 0.016 (fit; 0.024 parametric). A +10 kg step makes the gap ring for 3.4 s (dip 2.6 mm).
  - Best PID through collective rotor speed with a **20 ms motor lag: ζ ≈ 0.36 heave, 0.24 roll/pitch.**
  - ζ ≥ 0.70 needs a motor-speed lag ≤ 10 ms (5 ms → ~1.0); a 50 ms lag gives only 0.15. **Motor speed bandwidth is the limiting lever.**
- **+10 kg step (PID).** Peak dip 1.35 mm, settles (±0.2 mm) in ~0.07 s after the transient. Rotor-speed excursion 13 %, peak input 5.1 kW. Steady magnetic power 4.3 kW.
- **5° roll disturbance.** PID settles to ±0.5° in 0.72 s (open loop 2.5 s), but hits the ±40 % speed limit.
  - Counter-rotating: net gyro torque 0, yaw drift 0.
  - Co-rotating spin (same H, H = 4 N·m·s): peak gyro yaw torque 15 N·m, yaw drift 7.3°.
- **Drag-as-thrust.** If all four spun the same way, the net thrust would be 4F_D ≈ 576 N; counter-rotation cancels it.
- **1 m x-move by pair imbalance.** Overshoot 8.6 cm, settles (±2 cm) in 5.1 s, zero yaw/pitch coupling. Peak input 4.3 kW vs 3.85 kW hover; magnetic power changes ≤ 214 W. Net manoeuvre energy ≈ 0 with regenerative motors (0.04 kJ without).
- **Lateral gust (50 N, 1 s, in y).** Open loop drifts 6 m (no EDS lateral stiffness). With y controlled by roll tilt (quadcopter-style) it is held to ~0.24 m but recovers slowly (>10 s, −0.23 m overshoot). The EDS roll stiffness is so high that ±40 % rotor speed buys only ~0.8° of tilt, so **y authority via tilt is weak.**
- **Controllability.** Speed-only control of four wheels gives four wrench patterns: collective (lift), roll, pure x-thrust, and a pitch pattern that also produces yaw. **Independent yaw and y need more rotors or rotors with orthogonal or tiltable axes.**

## 3. Design takeaways (drag focus)
1. Hover at v ≈ 1–2 v_c: the drag power is the same (F_L·v_c) and control authority is highest. **Grounded (model).**
2. Keep counter-rotating pairs: thrust and angular momentum cancel, and the drag is a free steering reserve. **Grounded.**
3. Buy damping with fast rotor-speed control (≤ 10 ms) or add passive damping (eddy damper plate). **Grounded (model).**
4. Add orthogonal-axis rotor pairs for y and yaw. **Plausible-untested.**

**Follow-up (materials, switched coil zones):** [halbach_switched_arc_materials_check.md](halbach_switched_arc_materials_check.md).

## 4. Model limits
- 2-D first-harmonic EDS per rotor, quasi-static forces (no eddy-current time constant), and parametric inherent damping. Real EDW heave damping can be negative, which would make control harder.
- Small angles; no rotor-to-rotor field interaction, track edges, motor current/torque limits beyond a ±40 % speed clamp, or sensor noise.
- The power figures assume the 20 mm litz track. All hardware statements are **Plausible-untested** until a bench rotor is spun over a plate and litz ladder.

# Oscillator ratchet arrays: "one influencing another", from Brownian motors to hub motors and GEM (2026-10-25)

*License CC0. Requests (Channing, 2026-10-25, right after the GEM revisit): "Hmm, there might be a potential ratchet array.. essentially an oscillator acting as an ac current.. one influencing another" and "I think we touched on this when looking at hub motors". Labels: **Grounded**, **Plausible-untested**, **Speculative**, **Symbolic**. Citations were checked by web search on 2026-10-25 or carried from repo docs; anything else is [to verify]. Sim: [../sims/oscillator_ratchet_array_sim.py](../sims/oscillator_ratchet_array_sim.py) (illustration).*

**Linked:** [gravitoelectromagnetism_revisit.md](gravitoelectromagnetism_revisit.md) · [leaky_bound_state_family.md](leaky_bound_state_family.md) (its gating demo is a flashing ratchet on a leak) · [oloid_magnetic_track_motor.md](oloid_magnetic_track_motor.md) · [sumerian_noether_arnold_ratchet_review.md](sumerian_noether_arnold_ratchet_review.md).

## 0. Archive

| File : line | Channing (verbatim) | Concluded then |
|---|---|---|
| [grok_archive/2026-10-22_sumerian_history_and_noethers_theorem.md](grok_archive/2026-10-22_sumerian_history_and_noethers_theorem.md) : 828 (share #97, msg 11) | "Yes, impedance.. can we write the two-component groupoid geodesic + interface Lagrangian whose variation produces \tau\propto\sin\Delta\phi … Can we investigate magnetic ratchet motors?" | [sumerian_noether_arnold_ratchet_review.md](sumerian_noether_arnold_ratchet_review.md) lines 71–82: a ratchet needs broken symmetry plus a non-equilibrium drive (Feynman; Reimann 2002), **Grounded**. A ferrofluid thermal ratchet (Engel et al., *PRL* 91, 060602 (2003)) is **Grounded**; Grok's torque formula is [to verify]. Skyrmion/domain-wall ratchets are **Grounded** or Grok-reported. The τ ∝ sin Δφ sign was corrected. The two-ODE ratchet sweep was proposed but not run (H532). |
| [zeeman_muon_cavity_review.md](zeeman_muon_cavity_review.md) : 17, 18, 22 | "Simulate Zeeman splitting effects then, explore sympathetic coupling"; "Simulate coupled oscillators Tungsten and Muonic bismuth confinement"; "Simulate coupled oscillator dynamics" | Sympathetic coupling (pendulums on a shared beam) is correct classical physics, **Grounded** (line 39) |
| [oloid_magnetic_track_motor.md](oloid_magnetic_track_motor.md) : 5 | "It would ride the spine and be a magnetic track. But a frame may also work or an outside magnetic control system that switches which would end up being a motor, right?" | Yes: an electronically commutated (BLDC / switched-reluctance) linear motor, **Grounded**. Sensorless back-EMF commutation needs a kickstart (line 39). |
| [grassmann_ampere_pressure_sweep_review.md](grassmann_ampere_pressure_sweep_review.md) : 22, 128 | — | Regenerative braking recovers at most the potential energy lost, **Plausible-untested** (bounded) |

**Hub-motor thread.** I searched for 'hub motor', 'hub-motor', 'in-wheel', 'outrunner', 'regen', 'back-EMF' and 'BLDC' across docs/, grok_archive and the /workspace grok_share_* files, and **found no hub-motor thread**. The only back-EMF and regen hits are the oloid track motor, the Grassmann/pressure-sweep review, and Grok-side lines in two archives (fuller_golden_geodesic … :682 "harvested back-EMF"; resonant_future_blueprint_rgrf :3695 "Regenerative braking/turning"). His hub-motor words are **[Channing to supply]**. The closest captured thread is the oloid magnetic track motor, which is the same machine unrolled.

**Does the proposed link match?** It fits that captured thread, but I can't check it against the hub-motor conversation itself. In a hub motor (an outrunner BLDC), each coil phase is driven by an AC source. The phases are offset 120° so that together they make a travelling field, and the magnet rotor turns that sequenced AC into one-way torque. This is the deterministic cousin of a flashing/travelling-wave ratchet. Regenerative braking is the same machine run backwards: the rotor's motion induces AC back-EMF in each phase, which the inverter rectifies to DC. **Grounded** (standard machine physics). The ratchet parallel is **Plausible-untested** as a teaching frame. It is a useful lens, not a new mechanism.

## 1. Ratchets

| Claim | Label | Source |
|---|---|---|
| Feynman ratchet and pawl: at a single temperature it extracts no work, because the pawl fluctuates too (second law) | **Grounded** | Feynman Lectures Vol. I ch. 46 (1963) |
| Rocking ratchet: an asymmetric periodic potential plus a zero-mean AC force (with noise) gives directed drift; the energy comes from the drive | **Grounded** | M. O. Magnasco, "Forced thermal ratchets", *PRL* 71, 1477 (1993) |
| Flashing ratchets and Brownian-motor thermodynamics | **Grounded** | R. D. Astumian, *Science* 276, 917 (1997); R. D. Astumian, M. Bier, *PRL* 72, 1766 (1994) |
| Reviews | **Grounded** | P. Reimann, *Phys. Rep.* 361, 57 (2002); P. Hänggi, F. Marchesoni, "Artificial Brownian motors", *RMP* 81, 387 (2009) |
| Superconducting vortex (flux-quantum) ratchet: AC current → DC vortex flow on triangular pinning arrays, with polarity reversal | **Grounded** | J. E. Villegas, …, F. Nori, J. L. Vicent, *Science* 302, 1188 (2003). Fluxon ratchets in Josephson arrays and SQUID ratchets (Zapata, Ustinov, Sterck et al.) [to verify refs]. Links to [flux_attachment_review.md](flux_attachment_review.md): the "particles" being rectified are h/2e flux quanta |
| Biological motors (kinesin, myosin, F₀F₁-ATPase) are ATP-driven ratchets with ~50–100 % thermodynamic efficiency in some steps | **Grounded** (the concept); the efficiency figures are [to verify] | |

## 2. Coupled oscillators ("one influencing another")

- **Huygens's pendulum clocks.** Two clocks on a shared beam lock in antiphase. **Grounded** (Huygens 1665; modern re-analysis by Bennett et al., *Proc. R. Soc. A* 458, 563 (2002) [to verify]).
- **Kuramoto model.** dθᵢ/dt = ωᵢ + K Σ sin(θⱼ − θᵢ). Above a critical K the oscillators lock. **Grounded** (Y. Kuramoto 1975 [to verify ref]; Strogatz, *Physica D* 143, 1 (2000) [to verify]).
- **Coherent summation.** N in-phase sources give a field ∝ N and power ∝ N². Random phases give ∝ √N and ∝ N. **Grounded.** This redistributes power in angle; it is not extra energy.
- **Parametric pumping.** Modulating a parameter at 2ω pumps energy from the modulator. **Grounded.**
- **Electrical analogue.** A chain of magnetically coupled LC resonators carries magneto-inductive waves, each loop driving the next. **Grounded** (Shamonina, Kalinin, Ringhofer, Solymar, *Electron. Lett.* 38, 371 (2002) [to verify]). A time-varying (commutated) chain of this kind is a motor stator.

## 3. Applied to GEM: an array of phase-locked rotors

Gravitomagnetic fields add linearly, so N coherent rotors give at most N × Ω₁, and only if they all sit at the same distance, which is geometrically impossible. A ratchet can rectify an AC gravitomagnetic force on a test mass, but its output cannot exceed the drive's input energy. **Grounded.**

| Quantity (sim) | Value |
|---|---|
| One 10 kg steel disk, r = 0.15 m, 10,000 rpm, at 0.2 m on axis | Ω₁ = 2.2×10⁻²³ rad/s |
| Naive N to reach a GP-B-level 7 mas/yr (1.1×10⁻¹⁵ rad/s) | 4.9×10⁷ rotors (4.9×10⁸ kg), all at 0.2 m (impossible) |
| Naive N for Earth's 39 mas/yr | 2.7×10⁸ rotors (2.7×10⁹ kg; Earth is 5.97×10²⁴ kg) |
| **Packing limit.** A solid ball of such rotors gives Ω at its centre ≈ (8π/3)Gρ(½ r v_tip)/c² = 5.8×10⁻²² rad/s, **independent of size** | It never reaches 1.1×10⁻¹⁵. That would need ρ·r·v_tip about 2×10⁶ times larger, beyond any material's strength |

So no number of lab rotors reaches detectable frame dragging. Earth succeeds because it is a 6,371 km body, not because it is many rotors. **Grounded** (scaling). A GEM ratchet array for propulsion or power is **not supported**.

## 4. Where the idea is strong (EM)

| Application | Label |
|---|---|
| Vibration energy harvesting: rectifying ambient AC motion with piezo or electromagnetic transducers. µW–mW from Hz–kHz vibration; the output is bounded by the vibration power available | **Grounded** (C. B. Williams, R. B. Yates, *Sens. Actuators A* 52, 8 (1996) [to verify]) |
| Arrays of coupled piezo or Halbach harvesters, locked for broadband or coherent output | **Plausible-untested** (an active research area) |
| Commutated stators: hub motors, the oloid track motor, linear synchronous motors. A phase-sequenced coil array ratchets a magnet one way; regen reverses it | **Grounded** ([oloid_magnetic_track_motor.md](oloid_magnetic_track_motor.md)) |
| Craft gating as a flashing ratchet on a leak ([leaky_bound_state_family.md §3](leaky_bound_state_family.md)) | **Plausible-untested**; the energy ledger holds |
| Fluxon and vortex ratchets as rectifiers and logic | **Grounded** in the lab |

## 5. Sim (illustration)

`sims/oscillator_ratchet_array_sim.py`.
- **(i) Rocking ratchet.** Overdamped motion in a sawtooth (asymmetry 0.8, V₀ = 1, noise D = 0.05, ω = 0.1, 100 particles).
  - Drive off: drift 1×10⁻⁴ (zero within noise).
  - A = 1.8: drift 0.14 L per unit time.
  - Maximum 0.52 at A = 3.
  - Ledger (Sekimoto path bookkeeping): W_in = Q_bath + ΔU to ~10⁻¹³. At A = 1.8, W_in = 139.0, Q_bath = 139.0, ΔU = 0.07. All the drive work ends up as heat while it carries particles downhill-on-average; nothing is extracted from the bath.
- **(ii) Chain of 20 oscillators, nearest-neighbour coupled, ω spread 10 %.** Order parameter r rises from about 0.3–0.5 (unlocked) to 0.80 at K = 0.6 and about 0.87 at K ≥ 0.8. The coherent field ∝ rN.
- **(iii) GEM array numbers** as in §3.

Plot: `/workspace/oscillator_ratchet_array_plot.png` (box only).

## 6. Gaps
- The hub-motor thread and Channing's words from it [Channing to supply].
- [to verify]: fluxon/SQUID ratchet refs; Bennett 2002 Huygens; Kuramoto 1975, Strogatz 2000; Shamonina 2002; Williams & Yates 1996; motor-protein efficiency figures; Engel 2003 torque formula (carried over).

- **See also (2026-10-25):** [stator_review.md](stator_review.md): stator topologies, windings, losses, cogging and the track as an unrolled stator.

- **See also: shifting phase order = the phase relationship between coupled oscillators** (Channing's definition, 2026-10-25): [shifting_phase_order_coupled_oscillators.md](shifting_phase_order_coupled_oscillators.md).

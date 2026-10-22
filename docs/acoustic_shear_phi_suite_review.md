# Review: Acoustic wave equation with background shear flow, φ-modulated resonant B, and the toroidal φ-winding / particle trace / Bluetooth EMI suite (share #106)

- **Archive:** [grok_archive/2026-10-22_acoustic_wave_equation_with_background_flow_experiment.md](grok_archive/2026-10-22_acoustic_wave_equation_with_background_flow_experiment.md) (share `f70eec2f`, 10 messages: 5 Channing, 5 Grok).
- **Grok code (saved, labeled):** [sims/legacy_grok/toroidal_phi_bluetooth_suite.py](../sims/legacy_grok/toroidal_phi_bluetooth_suite.py). This is the complete version of the truncated [suite_element3_toroidal_phi_trace_bt.py](../sims/legacy_grok/suite_element3_toroidal_phi_trace_bt.py); Grok's saved output is [suite_element3_results.npz](../sims/legacy_grok/suite_element3_results.npz).
- **Related:** [tesla_davinci_threads.md §3e.1](tesla_davinci_threads.md#3e1-plasma-particle-tracing-and-bluetooth-packet-transmission-reference-dynamics) (earlier review of this code; Boris companion [sims/toroidal_particle_trace_boris.py](../sims/toroidal_particle_trace_boris.py)), [acoustic_streaming_and_centrifugal.md](acoustic_streaming_and_centrifugal.md), [dusty_plasma_bench.md](dusty_plasma_bench.md), [supercooled_electrons_rotation_review.md](supercooled_electrons_rotation_review.md) (#98).
- **Labels:** Grounded; Plausible-untested; Speculative; Symbolic (φ unless tested). "Grok-reported" = not rerun here.

## 1. Acoustic–shear model (msg 2)
| Claim | Label | Note |
|---|---|---|
| Linearized acoustics convected by a shear flow U_x(y), with the (v·∇)U term | **Grounded** | Standard linearized Euler / Pridmore-Brown-type system. |
| Shear stretches and can damp some instabilities; acoustic sources re-build compression | **Plausible** | Shear also *drives* instabilities (Kelvin–Helmholtz); "shear damps" holds only for some modes (e.g. flow-shear suppression of turbulence, Biglari–Diamond–Terry 1990). |
| Real experiments use gas injection and electrode modulation (Channing's pasted note) | **Grounded** in general | |
| Recreated run, `acoustic_shear_sim.npz` | **Grok-reported** | Code and file not captured. |

## 2. φ-modulated resonant B (msg 4)
| Claim | Label | Note |
|---|---|---|
| Earlier result "final max \|B\| = 1.0399", coherence rising under φ-modulated drive | **Grok-reported** | Grok's recreation did not reproduce 1.0399 and says the value depends on drive, filter and saturation knobs. |
| "Demonstrates dynamo self-organization and tokamak shear stabilization" (Channing's pasted summary) | **Symbolic** | Prescribed drive + high-k filter + soft saturation produce low-mode coherence by construction. No induction equation, so it is not a dynamo test. φ is not tested against other drive ratios. |

## 3. Suite element 3 (msgs 6–10), rerun here
| Claim | Label | Note |
|---|---|---|
| Rerun output: confinement 1.00, mean max r 0.197, EMI 0.101, Bluetooth 96.5 %, 1.3 ms | **Grounded as a rerun** | Matches Grok's numbers and the saved .npz exactly (seed 7). |
| "The φ-wound field kept particles well confined" | **Corrected** | Confinement is built in. The radial step is v⊥·0.01·dt·sin(φt) ≈ 2×10⁻⁵ per step, so r changes by <0.006 over 300 steps. `B_pol` (the φ-modulated part) is computed but never used. Only B_tor sets the poloidal rotation. Changing φ cannot change confinement. |
| "Mild EMI so Bluetooth stayed high" | **Corrected** | emi_level = 0.25(1 − confinement) + 0.15\|sin(2π/φ)\| = 0 + 0.101. That is a constant, not derived from plasma currents. Success = 0.98 − 0.4·0.101 = 0.94 probability, so 96.5 % is sampling luck over 200 packets. |
| `sin(n_poloidal·θ·φ)` | **Bug** | A non-integer multiple of θ is discontinuous at θ = ±π, so the "field" is not single-valued. |
| Bluetooth "1 ms slots" | **Corrected (minor)** | Classic Bluetooth slots are 625 µs. |
| Guiding-centre style tracing | **Corrected** | No gyration, drifts or mirror force are modelled. See the Boris companion in §3e.1 for an honest trace: rotational transform confines and φ is not special. |
| Reduced models are illustrative, not predictive | **Grounded** | Grok says so. |

## Key findings
1. The full Grok code was recovered. It closes the "[Channing to supply code]" gap in §3e.1 and reproduces the saved .npz.
2. The reported confinement and Bluetooth numbers are fixed by constants in the code, not by φ or by the plasma.
3. The 1.0399 φ-resonant B value is not reproducible from what was captured.

## Open questions for Channing
- Do you still have the code for `acoustic_shear_sim.npz` and `phi_resonant_B_sim.npz` (or the 1.0399 run)?
- Should the suite be rebuilt with a Boris pusher and an EMI term that actually depends on the plasma current?

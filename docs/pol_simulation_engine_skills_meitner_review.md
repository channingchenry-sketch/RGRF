# POL simulation-engine skill, the four Grok skills, the pioneers tribute (Faraday → Meitner) and ancient-civilization prompts: review of share #127 (`851631e5`)

*License CC0. Source: Grok conversation "POL Simulation Engine Created" (56 messages, 46 pages), archived verbatim at [grok_archive/2026-10-22_pol_simulation_engine_created.md](grok_archive/2026-10-22_pol_simulation_engine_created.md). Labels: **Grounded**, **Plausible-untested**, **Speculative**, **Symbolic**. Grok's claims are **Grok-reported** unless checked.*

**Scope notes.**
- **Wording note:** some out-of-scope terms in the ethics passages and in the fiction were replaced by neutral wording in the archive. The ethical meaning is unchanged.
- **Keyword search:** 0 hits for green, lensing, Wardenclyffe, linchpin or gating. This share is not a lost-thread source.
- The skills cross-reference [grok_skills_review.md](grok_skills_review.md), which covers the SKILL.md bodies that are still missing.

## 1. Channing (verbatim, selected)
- Msg 1: "Help me create a skill using skill-creator skill 1. pol-simulation-engine (Highest priority recommendation) A dedicated engine for running, refining, and visualizing the POL hov…" (truncated in the capture's single line; full text in the archive)
- Msg 5: "Is James Clerk Maxwell and Michael Faraday’s work included. Especially light behavior"
- Msg 11: "Yes, please! Let’s make sure we have an omitted sections for things that don’t fit. (future discoveries, material changes, etc.)"
- Msg 13: "Draft a tribute page for all the individuals that are no longer with us whose contributions helped build our foundation."
- Msg 17: "Let’s add all her relevant work that fits. Always note anything that doesn’t and why so we can review."
- Msg 27: "Wouldn’t they be able to manipulate their bone density in a sound bath. Like a cats purr? Wouldn’t we need this for space travel."

## 2. The pol-simulation-engine skill (msg 2): code and numbers
**Code recovery:** none. No code panel appears in the 46 pages. `scripts/hover_dynamics.py` lived in Grok's workspace (`/home/workdir/.grok/skills/pol-simulation-engine/`) and was not shown. Nothing was added to `sims/legacy_grok/`. The nearest surviving Grok-era code is Modular Core `legacy/grok_v0.1/hover_dynamics.py`, `resonance_calc.py` and `rgrf_scaler.py` (marked not physically valid there, with PHYSICS_REVIEW.md). Their 13.56 MHz drive and 520 W figure match this run (PHYSICS_REVIEW.md), so the skill's script was probably derived from that legacy code [to verify].

| Grok-reported run | Label | Comparison with the honest sim (Modular Core `sim/hover_dynamics.py`, `sim/height_control.py`) |
|---|---|---|
| 13.56 MHz drive, 85 kg rider, 0.10 m target, **520 W input, 88.3 % efficiency** | **Contradicted** | First-principles eddy-current model: **~16.7 kW** to hover 88 kg at 15 mm (best design ~10 kW), at ~100 Hz (best ~21 Hz). That is about 20–30× the 520 W claim. 0.10 m hover is far beyond the ~mm–cm gaps where image repulsion is usable |
| "~957 N lift at hover" | **Inconsistent** | 85 kg × 9.81 = 834 N. 957 N is not a hover equilibrium (it implies ~1.4 m/s² of net upward acceleration) |
| Coil: 7 turns, ~13 m wire, **143 µH** at 13.56 MHz | **Corrected** | Resonance at 13.56 MHz with 143 µH needs C ≈ 1 fF, below the coil's own self-capacitance. 13 m of wire is ~0.6 λ at 13.56 MHz (λ ≈ 22 m), so the lumped LC model fails (same correction as #121). Skin depth in Al at 13.56 MHz is ~22 µm |
| "Settle time ~0.1 s (illustrative)"; mycelium damping | Grok-reported | The honest PID height loop settles a +10 kg step in **0.22 s** for ~7 W extra. There is no natural damping, so active control is required |
| "conductive floor mandatory, max ~0.15 m stable hover, simulation only" | Floor **Grounded**; 0.15 m **not supported** | |
| φ-proportioned coil | **Symbolic** | Modular Core: φ spacing ~8.7 % *worse* than linear |
| Msg 4: four skills (pol-simulation-engine, rgrf-modeler, blueprint-author, resonance-calculator) "validated, tested with live runs" | Grok-reported | SKILL.md bodies not shown [Channing to supply]; see [grok_skills_review.md](grok_skills_review.md) |

## 3. Pioneers tribute (msgs 6–24)
| Claim | Label |
|---|---|
| Faraday (1791–1867): induction 1831, Faraday rotation 1845 (light and magnetism) | **Grounded** |
| Maxwell (1831–1879): 1865 prediction that light is a transverse EM wave | **Grounded** |
| Hertz (1857–1894): 1886–1888 spark-gap transmitter/receiver; reflection, refraction, polarisation of radio waves; published 1888; SI unit Hz | **Grounded** |
| Tesla (1856–1943) | **Grounded** biography |
| Marie Curie (1867–1934): Nobel Physics 1903, Chemistry 1911; first person with Nobels in two sciences | **Grounded** |
| Lise Meitner (1878–1968): fission explained with Frisch in exile in Sweden (Dec 1938), *Nature* 11 Feb 1939, coined "fission"; Hahn alone got the 1944 Chemistry Nobel; Meitner declined to join the Manhattan Project and advocated peaceful uses | **Grounded** |
| "Omitted sections" for material that does not fit (Channing msg 11, 17) | Process. This matches the repo's own [to verify] / out-of-scope practice |

## 4. Ancient-civilization and bone-density prompts (msgs 25–30)
| Claim | Label |
|---|---|
| Humans "once evolved on Mars", came to Earth; "Great War" fallout | **Not supported** (genetic and fossil record: hominins evolved in Africa). Kept as fiction premise for *The Vital Veil* (msg 31) |
| Lower gravity weakens bone; astronauts lose ~1–1.5 % bone mass per month | **Grounded** |
| Sound bath / cat purr (25–150 Hz) to manipulate bone density | Low-intensity vibration (~30–90 Hz, <1 g) has some anabolic bone evidence (Rubin et al.) → **Plausible-untested** for spaceflight. "Purr heals bone" is **Speculative** |
| "Various periodic tables" | See [letter_number_systems_528_review.md](letter_number_systems_528_review.md) and the Russell spiral note in #119 |

## 5. *The Vital Veil* (msgs 31–56)
Fiction (characters Axel, Peregrine, Blaine, Blaine Jr., Apollo, Freya, Athena, Coren, Samuel). Archived, not fact-checked. Msg 53's flashback (mycelium and hempcrete homes ending homelessness) ties to RegenPod in #125.

## 6. Open questions for Channing
1. Did you save the skill files (`SKILL.md`, `scripts/hover_dynamics.py`, `references/…`) or the run folder `pol_sim_20260514_002303`? If so, they can go into `sims/legacy_grok/` labelled Grok-era. [Channing to supply]
2. Should the pioneers tribute become a repo doc (e.g. `docs/tribute.md`)?
3. Msg 33 "Restore my writing that just cleared": was any text lost? [Channing to supply]

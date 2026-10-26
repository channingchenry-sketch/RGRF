# Review: "Biefeld-Brown Effect Investigation" (share #152, 2026-10-25)

- **Archive:** [grok_archive/2026-10-25_biefeld_brown_effect_investigation.md](grok_archive/2026-10-25_biefeld_brown_effect_investigation.md) (14 messages: 7 Channing, 7 Grok).
- **Share URL:** <https://grok.com/share/bGVnYWN5_33eb3e6f-3aa4-4ea2-9696-9d6d51a08395> (`33eb3e6f`; matches all 20 page footers).
- **Labels:** **Grounded** · **Plausible-untested** · **Speculative** · **Symbolic**. Citations are [to verify] unless marked. All numbers in the archive are Grok-reported.
- **Duplicate check:** the id was new. Earlier Biefeld–Brown / ion-wind mentions sit inside other reviews ([electric_distillation_glaphene_hertz_review.md](electric_distillation_glaphene_hertz_review.md), [plasma_shielding_patents_review.md](plasma_shielding_patents_review.md), [marklund_convection_review.md](marklund_convection_review.md)); none is this conversation. Grok mentions "August BSI Mark 2 notes" that are not in the repo [Channing to supply].
- **Figures:** 5 third-party web images (a rotating asymmetric-capacitor rig on a PVC frame; a "BSI Mark II" multi-stage thruster thumbnail; three more on pp. 5, 6 and 9). They are described in the archive header, not copied.
- **Scope:** one source-programme name is `[omitted: out of scope]`. No personal content.

## 0. Gap check

| Open thread | Verdict |
|---|---|
| **H285i hub-motor thread** ([oscillator_ratchet_array_review.md](oscillator_ratchet_array_review.md)) | **Recovered (a hub-motor thread).** Msgs 3–6 cover the outer-rotor BLDC hub motor: teardown, the 27N30P hoverboard class, Hall sensors at 120°, commutation, regen, and case heat → condensate. Whether this is the exact chat Channing remembered ("I think we touched on this when looking at hub motors") is [Channing to confirm]. |
| **H285j lost stator thread** ([stator_review.md](stator_review.md)) | **Partly recovered.** The teardown (msg 6) is a stator walk-through: a laminated silicon-steel stack with 27 teeth, star winding, Halls in the slots, and magnet-to-stator clamping. Channing's own words don't mention stators, so it may not be the remembered stator chat [Channing to confirm]. |
| **H285p tuning geometry and frequency to the plasma** | **Neighbour, not resolved.** In the DBD lattice (msg 12), drive voltage (~2.6–4.7 kV), frequency (~50 kHz) and electrode geometry (hexagonal vs square) select which plasma cells light. That is geometry-and-frequency tuning of a plasma, but not the phi-for-nature vs plasma-tuning conversation. Cross-link [plasma_tuning_sim](../sims/plasma_tuning_sim.py). |
| H722 "pong" (magnetic confinement + static E-field) | Not present. Plasmoids (Bostick 1956; compact toroids) are discussed, but there is no pong dynamic. |
| Sonoluminescence; helium opacity; F19/F20 green lensing; Na/K pumping | Not present ("green" appears only as copper corrosion). |
| Section C | Hub motor recovered as above; stator partly. |

## 1. Channing's questions (verbatim)

- Msg 1 ([L15](grok_archive/2026-10-25_biefeld_brown_effect_investigation.md#L15)): "Can we investigate the Biefied-Brown effect?"
- Msg 3 ([L145](grok_archive/2026-10-25_biefeld_brown_effect_investigation.md#L145)): "I’d like to explore a few things can we look at a hub motor?"
- Msg 5 ([L262](grok_archive/2026-10-25_biefeld_brown_effect_investigation.md#L262)): "Can we take it apart and look at the mechanics? Can we also look at the condensate?"
- Msg 7 ([L416](grok_archive/2026-10-25_biefeld_brown_effect_investigation.md#L416)): "We will leave it out for now may make for a good generator add or stacked flow loops.. can we take a turn and look at galvanotaxis?"
- Msg 9 ([L558](grok_archive/2026-10-25_biefeld_brown_effect_investigation.md#L558)): "Thank you, that will inform on grow techniques/ selective nodes. Can we look at plasmoids and voxels?"
- Msg 11 ([L673](grok_archive/2026-10-25_biefeld_brown_effect_investigation.md#L673)): "Yeah we already sort of speculate this.. can we look at the DBD lattice?"
- Msg 13 ([L779](grok_archive/2026-10-25_biefeld_brown_effect_investigation.md#L779)): "We brought up screening the ion wind before and our Tesla valves, just wondering if we should design loops or if that will unintentionally create back channels.."

## 2. Labelled findings

| Topic | Label | Note |
|---|---|---|
| Asymmetric-capacitor thrust in air = EHD ion wind (corona → ion drift → momentum transfer to neutrals; same direction for both polarities) | **Grounded** | Credit: Thomas Townsend Brown, who studied and patented the effect from the 1920s, and Paul Alfred Biefeld, his physics mentor at Denison, whose name was attached to it. |
| Brown's "electrogravitics" (electricity–gravity coupling) and vacuum or antigravity readings | **Speculative / unsupported** | Vacuum tests (Talley ~1988; Tajmar 2004) found no usable thrust once gas and breakdown were removed [to verify]. Any anomaly is ≥10⁵ below ion wind (Grok-reported). |
| Thrust/power ~20–70 N/kW; ~73 N/kW peak (2014 *AIP Advances* geometry sweep) | **Grounded** range [to verify paper] | Steady solid-state flight: Xu et al., *Nature* 563, 532 (2018) [to verify]. |
| Multi-stage stacking (BSI Mark II style) | **Grounded** (stacking raises airflow and thrust at some efficiency cost) | Third-party build; image described only. |
| Hub motor: outer-rotor BLDC, 27N30P, 15 pole pairs, Halls 120°, ~16 Kv, regen | **Grounded** | |
| Hub-motor case heat → condensate recovery | **Plausible-untested** (low-grade heat) | |
| Galvanotaxis / electrotaxis: keratinocytes and fibroblasts migrate toward the cathode; epithelial thresholds ~8–25 mV/mm | **Grounded** (Zhao et al., *Nature* 2006 [to verify]) | Ties to #149 fibroblast hyperpolarization. |
| Plasmoids (Bostick 1956), compact toroids, plasmoid thrusters | **Grounded** (lab objects); thruster readiness Grok-reported | |
| "Voxels": PIC/FDTD grids, dusty-plasma crystals, DBD pattern cells, mycelium voxel beds | Computation and dusty plasma **Grounded**; mycelium voxels **Plausible-untested** | |
| DBD lattice: ~2.6–4.7 kV, ~50 kHz; patterns (hexagon, honeycomb, superlattice) switch with voltage and frequency; plasma-activated water | **Grounded** (DBD pattern formation) [to verify figures] | Not galvanotaxis-scale: never put kV fields across living tissue. |
| Ion-wind loops with Tesla valves: an open propulsive jet plus a small closed regenerative loop; a closed thrust loop cancels net momentum and creates back-channels | **Grounded** (momentum accounting); Tesla-valve diodicity **Grounded** (best at higher Re / pulsatile flow) | Grok's "two loops, two jobs" design is **Plausible-untested**. |

## 3. High-voltage safety caveats

- EHD and DBD rigs run at kilovolts (10–50+ kV for ion wind; ~3–5 kV DBD). The supply, insulation, creepage and discharge of stored charge are lethal-hazard engineering. Use current-limited supplies, interlocks and bleed resistors, and work one hand only.
- Corona and DBD make **ozone and NOx**, so ventilate and monitor.
- Wet plumes and damp hemp or mycelium make surface-leakage back-channels (msg 14), and breakdown can follow them.
- Keep kV discharges off living mats and tissue (Grok msg 12: "Do not drop this across a…").

## 4. Researchers credited

Thomas Townsend Brown; Paul Alfred Biefeld; Winston H. Bostick (plasmoids); Martin Tajmar; the MIT EHD-aircraft team (Steven Barrett and colleagues) [to verify]; Min Zhao and the electrotaxis community [to verify].

## 5. Open items

- Grok's "August BSI Mark 2 notes" [Channing to supply].
- Confirm whether msgs 3–6 are the hub-motor and stator chats Channing remembered (H285i, H285j) [Channing to confirm].
- A single-stage screened duct with inlet and outlet Tesla valves (Grok's next drawing).

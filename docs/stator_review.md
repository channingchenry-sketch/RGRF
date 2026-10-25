# Stators: the stationary half of every motor, generator and track (2026-10-25)

*License CC0. Request (Channing, 2026-10-25): "Can we explore stators(I thought I had a thread but couldn’t find it)." Labels: **Grounded**, **Plausible-untested**, **Speculative**, **Symbolic**. Citations were checked by web search on 2026-10-25; anything else is [to verify]. Sim: [../sims/stator_design_sim.py](../sims/stator_design_sim.py) (illustration; every machine parameter is assumed).*

**Linked:** [oscillator_ratchet_array_review.md](oscillator_ratchet_array_review.md) · [oloid_magnetic_track_motor.md](oloid_magnetic_track_motor.md) · [oloid_spine_lorentz_drive.md](oloid_spine_lorentz_drive.md) · [halbach_switched_arc_materials_check.md](halbach_switched_arc_materials_check.md) · [halbach_litz_drag_reduction.md](halbach_litz_drag_reduction.md) · [halbach_rotor_control_vs_perturbation_sections.md](halbach_rotor_control_vs_perturbation_sections.md).

## 0. The lost stator thread: search record

I searched for stator, armature, winding, slot, lamination, cogging, axial/radial flux, coreless, Halbach stator, hub motor and commutat in these places:
- docs/ and docs/grok_archive;
- all /workspace grok_share_*.txt files;
- /workspace/browser-pdfs (pdftotext);
- /workspace/capture_queue.txt;
- /workspace/private (read-only);
- the user's Gmail (read-only search: 0 results).

**No stator thread was found, and none of Channing's turns in the archive mention stators.** Every hit is Grok-side text inside other threads:

| Where | Grok text (verbatim) |
|---|---|
| grok_share_ecd34446.txt : 1402 / 1438 (pyramid-node thread) | "Tungsten-quartz resonators in Grand Gallery or shafts act as stators." / "Acoustic piezoelectric motors rely on standing or traveling waves creating elliptical motion at the stator-rotor interface." |
| grok_share_d98ed125.txt : 2840 / 2985 (archived as grok_archive/2026-10-17_quantum_biology_natures_coherent_secrets.md) | "…moving magnets sweep past stationary coil windings (or vice versa)… This produces clean, vortex-structured AC with reduced cogging and smoother waveforms" |
| browser-pdfs/grok_share_7cf75c45.pdf : 62 (Holt/Hau/Searl thread, [holt_hau_searl_fput_jitterbug_review.md](holt_hau_searl_fput_jitterbug_review.md)) | "Concentric stator rings with cylindrical magnetic rollers that orbit without contact." (the Searl SEG, unverified claim) |
| grok_share_373a0a5b.txt : 29–75 (Newman machine thread) | "low-current pulsed commutation of a large permanent-magnet rotor"; "A mechanical commutator that switched polarity…" |
| [oloid_magnetic_track_motor.md](oloid_magnetic_track_motor.md) (doc) | The spine as a "switched stator"; Channing's line 5 quote is about the track becoming a motor |

The stator thread and the hub-motor thread (H285i) are therefore **[Channing to supply]**, logged as H285j. They may be in a share that was never captured.

## 1. What a stator does

The stator is the stationary structure of coils (and usually iron) that carries current and sets up a field. Polyphase currents in its windings, each phase an AC source offset in time and space, make a rotating or travelling field. The rotor (magnets, or a cage or reluctance rotor) locks to that field and turns it into one-way torque. That is the "phase-sequenced oscillator array rectified by the rotor" picture in [oscillator_ratchet_array_review.md](oscillator_ratchet_array_review.md). **Grounded** (standard machine theory, e.g. Hendershot & Miller, *Design of Brushless Permanent-Magnet Machines* [to verify edition]). Run backwards, the rotor induces back-EMF in the stator: generation and regenerative braking. **Grounded.**

## 2. Topologies

| Type | Notes | Label |
|---|---|---|
| Radial flux (the most common) | Flux crosses a cylindrical gap; slotted laminated iron stator | **Grounded** |
| Axial flux (pancake, yokeless and segmented armature) | Flux along the axis, disc-shaped. High torque density in short, wide packages (e.g. YASA-type machines, in-wheel drives) | **Grounded** [specific torque densities to verify] |
| Transverse flux | Flux closes perpendicular to the motion. High torque per pole, low power factor, complex | **Grounded** |
| Coreless / ironless | Air-cored windings: no cogging and no iron loss, but a lower field, so more magnet is needed. Common in axial-flux Halbach-rotor machines | **Grounded** |
| Halbach-array rotors with ironless stators | Halbach magnets concentrate the field on one side, so a back iron is unnecessary (dual Halbach discs around an ironless stator) | **Grounded**; see [halbach_switched_arc_materials_check.md](halbach_switched_arc_materials_check.md) |
| Linear motors | The stator unrolled into a track (LSMs in maglev, linear BLDC); end effects at the track ends | **Grounded**; the oloid track is a curved, unrolled stator |

## 3. Slots, poles and windings

- **Winding factor** k_w = k_d·k_p sets how much of each coil's flux linkage adds to the fundamental.
- **Fractional-slot concentrated windings (FSCW, tooth coils).** They give short end turns, high fill, low cogging and fault tolerance, but extra space harmonics and rotor losses. **Grounded** (A. M. El-Refaie, *IEEE Trans. Ind. Electron.* 57, 107 (2010), doi:10.1109/TIE.2009.2030211).
- **Sim (star of slots, double layer):** 12s/14p and 12s/10p 0.933 · 9s/8p and 9s/10p 0.945 · 18s/16p 0.945 · 24s/22p 0.949 · 24s/20p 0.933 · 12s/8p and 6s/4p 0.866. These match standard tables. **Grounded.**

## 4. Losses and materials

| Item | Label | Note |
|---|---|---|
| Laminations (0.2–0.5 mm Si-steel) cut eddy currents ∝ (t f B)² | **Grounded** | |
| Hysteresis plus eddy: Steinmetz P = k f^α B^β | **Grounded** (C. P. Steinmetz, *Trans. AIEE* 9, 3 (1892) [to verify]) | Sim uses k so M270-35A-like steel gives ~2.7 W/kg at 50 Hz, 1.5 T (assumed) |
| SMC (soft magnetic composite) cores: isotropic, suit 3D flux (axial/transverse), lower permeability | **Grounded** [refs to verify] | |
| Amorphous and nanocrystalline ribbon: very low core loss at high frequency, brittle and hard to cut | **Grounded** | |
| Litz wire beats skin depth δ = √(2ρ/ωμ) (Cu: 9.3 mm at 50 Hz, ~0.2 mm at 100 kHz) and proximity effect; it helps above ~1–10 kHz or in ironless gaps exposed to the rotor field | **Grounded**; see [halbach_litz_drag_reduction.md](halbach_litz_drag_reduction.md) | |
| Thermal limits: winding insulation class (e.g. H = 180 °C), magnet demagnetisation (NdFeB above ~80–150 °C by grade), cooling (air, jacket, direct oil, potted) | **Grounded** | |

## 5. Cogging

Cogging comes from the magnets' attraction to slotted iron. Its fundamental order is LCM(Q, 2p), and a higher LCM means smaller cogging. A skew of one cogging period (360°/LCM: 15° for 12s/8p, 4.29° for 12s/14p) cancels the fundamental. Ironless and Halbach stators have essentially none. **Grounded** (Zhu & Howe, *IEEE Trans. Energy Convers.* 15, 407 (2000) [to verify]).

## 6. Sim (illustration, assumed bench machines)

| At 1500 rpm, 2 N·m (P_mech 314 W) | Kt (N·m/A) | Copper loss | Core loss | Litz eddy loss | η |
|---|---|---|---|---|---|
| Iron-core radial, 14 poles, 1.2 kg core | 0.50 | 4.8 W | 18.6 W | — | 93.1 % |
| Ironless axial Halbach + litz | 0.32 | 7.0 W | 0 | 2.4 W | 97.1 % |

- The ledger P_in = P_mech + P_cu + P_core + P_eddy is exact at every map point.
- No bearing, windage or inverter losses are modelled, so the light-load peaks (99.9 %) are optimistic.
- The iron machine has the higher Kt; the ironless one wins at high frequency.

Plot: `/workspace/stator_design_plot.png` (box only).

## 7. RGRF ties

| Link | Label |
|---|---|
| The oloid spine track is an unrolled, curved stator. The switched coils are its phases, and back-EMF sensing needs the kickstart ([oloid_magnetic_track_motor.md](oloid_magnetic_track_motor.md), [oloid_spine_lorentz_drive.md](oloid_spine_lorentz_drive.md)) | **Grounded** principle; the geometry is **Plausible-untested** |
| The craft's switched 60°/45° Halbach arcs with litz trim coils as a segmented ironless stator ([halbach_switched_arc_materials_check.md](halbach_switched_arc_materials_check.md)) | **Plausible-untested** |
| Nitinol kickstart / thermal actuation as the start aid | **Plausible-untested** |
| Impedance zone as the stator–rotor gap (field-energy coupling region) | **Symbolic** framing of a real gap-field concept |
| Drag reduction: litz or segmented tracks cut eddy drag on moving Halbach arrays ([halbach_litz_drag_reduction.md](halbach_litz_drag_reduction.md)) | **Grounded** (Inductrack-type physics) |
| Searl SEG "stator rings" | **Speculative**, unverified (see holt_hau_searl review) |

## 8. Gaps
- The lost stator thread and the hub-motor thread [Channing to supply] (H285j, H285i).
- Target machine: power, speed, size, and whether it is for the oloid, the craft arcs or a hub [Channing to supply].
- [to verify]: Hendershot & Miller edition; Steinmetz 1892; SMC refs; Zhu & Howe 2000; axial-flux torque-density figures.

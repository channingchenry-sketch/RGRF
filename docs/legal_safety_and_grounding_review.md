# Legal / safety guardrails, grounding split, Grok's hover-sim claims, mycelium deck and Tesla resonance: review (2026-10-17)

*License CC0. Source: the Grok conversation "Open Source Regenerative Infrastructure Blueprint" (shared by Channing, captured 2026-10-17), archived verbatim at [grok_archive/2026-10-17_open_source_regenerative_infrastructure_blueprint.md](grok_archive/2026-10-17_open_source_regenerative_infrastructure_blueprint.md). Reviewed by Resona, 2026-10-17. Companion check script: [`sims/moving_magnet_eddy_lift_check.py`](../sims/moving_magnet_eddy_lift_check.py).*

**Labels:** **Grounded** · **Plausible-untested** · **Speculative** · **Symbolic**. φ is **Symbolic** unless tested. Unverified citations are marked **[to verify]**; gaps are marked **[Channing to supply]**.

> **Not legal advice.** Section 1 is general information about publicly available U.S. federal rules and international exposure guidelines, checked against the regulation texts on 2026-10-17. It is not legal advice. State and local rules (electrical codes, permits, noise, use of sidewalks and roads) also apply and vary by place. Where Channing builds and tests decides which rules apply **[Channing to confirm jurisdiction]**. If a build moves beyond a personal garage experiment (selling kits, public demos, carrying a person outside private property), check with the relevant authority or a qualified professional.

**Contents**
1. [Legal and safety guardrails, checked](#1-legal-and-safety-guardrails-checked)
2. [Buildable today vs visionary: Grok's split, labelled](#2-buildable-today-vs-visionary-groks-split-labelled)
3. [The "human-powered levitator" and eddy-current lift](#3-the-human-powered-levitator-and-eddy-current-lift)
4. [Grok's reported hover simulation (message 6): not reproducible, compared with our sims](#4-groks-reported-hover-simulation-message-6-not-reproducible-compared-with-our-sims)
5. [Mycelium deck material properties](#5-mycelium-deck-material-properties)
6. [Tesla double-resonant transformer theory (message 8)](#6-tesla-double-resonant-transformer-theory-message-8)
7. [Labels summary](#7-labels-summary)
8. [Open questions for Channing](#8-open-questions-for-channing)

---

## 1. Legal and safety guardrails, checked

Channing's opening request (verbatim, message 1): "Make sure are not breaking laws." Grok answered with a list of guardrails. Its spirit is right: experimental, documented, no public-road or flight use, honest limits. Below, each guardrail is matched to the actual rule. All rule texts are from eCFR (current as of 2026-10-15), fetched 2026-10-17.

### 1.1 Radio-frequency emissions (FCC)

| Situation | What the rule says | Applies to POL? | Label |
|---|---|---|---|
| **Lift coils at ~100 Hz** (the sister-repo hover sim default) | FCC Part 18 defines RF energy as "Electromagnetic energy at any frequency in the radio spectrum from 9 kHz to 3 THz" (47 CFR 18.107(a)). Part 15 emission limits also start at 9 kHz (47 CFR 15.209 table begins at 0.009 MHz). | **Below 9 kHz the FCC RF-emission rules do not reach the drive frequency itself.** Harmonics from a switching driver can reach above 9 kHz, so the general no-interference duty still matters (next rows). | **Grounded** |
| **Resonant / Tesla-coil drive at 50 kHz–1 MHz** (message 8 range) | A device that generates RF "for industrial, scientific, medical, domestic or similar purposes, excluding applications in the field of telecommunication" is ISM equipment (47 CFR 18.107(c); its examples include "ionization of gases"). Outside the assigned ISM bands, "Any non-ISM frequency, Below 500 W": **15 µV/m at 300 m** (47 CFR 18.305(b)). The assigned ISM frequencies (47 CFR 18.301) start at 6.78 MHz, so **50 kHz–1 MHz is non-ISM**, and 530–1,700 kHz overlaps the AM broadcast band. | A hobby Tesla coil is very likely to exceed 15 µV/m at 300 m when arcing (broadband spark noise). Which Part (15 or 18) the FCC would apply to a hobby coil is not spelled out in the text read here **[to verify with FCC guidance, e.g. KDB 680106 for wireless power]**. Either way the interference duty below applies. | **Grounded** (rule text); classification **[to verify]** |
| **Interference duty** | Part 18: "the operator of ISM equipment that causes harmful interference to any authorized radio service shall promptly take whatever steps may be necessary to eliminate the interference" (47 CFR 18.111(b)). Part 15: operation is subject to "the conditions that no harmful interference is caused", and the operator must "cease operating the device upon notification by a Commission representative" (47 CFR 15.5(b), (c)). Part 15 also says: "Intentional radiators that produce Class B emissions (damped wave) are prohibited" (15.5(d)); a spark-gap coil produces damped waves, but it is not built to communicate, so Part 18 is the more natural fit **[to verify]**. | Yes. Practical reading: short runs, shielded or screened test area, check AM radio and neighbours' devices, stop if interference is reported. | **Grounded** |
| **Home-built equipment** | "Equipment authorization is not required for devices that are not marketed, are not constructed from a kit, and are built in quantities of five or less for personal use." The builder "is expected to employ good engineering practices to meet the specified technical standards to the greatest extent practicable" (47 CFR 15.23). | Yes for a garage POL built by Channing for personal use. **Selling kits or boards changes this** (authorization and testing may be needed). Note that 15.23 is in Part 15; Part 18 has no matching home-built clause in the sections read here **[to verify]**. | **Grounded** |

### 1.2 Flight (FAA): only if it ever leaves the floor

Grok (message 2): "We never imply operational craft that would violate FAA, FCC, or aviation regs." A floor-bound board hovering ~10 mm over a conductive plate is not an aircraft in any normal sense, so FAA rules do not come into play for v0.1. If a future craft were "used or intended to be used for manned operation in the air by a single occupant" for "recreation or sport purposes only", 14 CFR Part 103 (ultralight vehicles) would be the first rule to read. Its limits for a powered ultralight (14 CFR 103.1(e), verbatim): "Weighs less than 254 pounds empty weight", "fuel capacity not exceeding 5 U.S. gallons", "Is not capable of more than 55 knots calibrated airspeed at full power in level flight", "power-off stall speed which does not exceed 24 knots calibrated airspeed". Also: daylight only (103.11), and "No person may operate an ultralight vehicle over any congested area of a city, town, or settlement, or over any open air assembly of persons" (103.15). Whether a hovering craft with no wing (no "stall speed") fits Part 103 at all is unclear **[to verify with FAA if it ever applies]**. **Grounded** (rule text); applicability to POL: **not applicable to v0.1**.

### 1.3 Electrical, high-voltage and field-exposure safety

| Hazard | Guidance | Label |
|---|---|---|
| **Mains-scale power draw** | The sister-repo hover sim needs **~16.7 kW** (default) or **~10 kW** (best geometry) to hover 88 kg. A U.S. 240 V / 50 A branch circuit gives 12 kW, and only ~9.6 kW for continuous loads under the common 80% rule (NEC 210.20(A) [to verify edition wording]). Full eddy hover therefore exceeds a normal household circuit; that is a wiring, permit and fire question, not just a physics one. | **Grounded** (arithmetic); code cite **[to verify]** |
| **Exposed live parts** | U.S. workplace rules treat ~50 V as the threshold for guarding live parts (OSHA 29 CFR 1910.303(g)(2) [to verify exact paragraph]). Not binding on a home hobbyist, but a sensible line: guard anything ≥ 50 V; discharge capacitor banks with a bleeder resistor before touching; one hand rule; isolation transformer. | **Grounded** (as general practice) |
| **Tesla-coil HV/RF** | RF burns at "low" current; ozone/NOx and UV from arcs; fire from streamers; RF interference (above). Already listed in [geometric_unity_review.md §3](geometric_unity_review.md#3-tesla-coil-physics-msg-6-checks-and-corrections) and the R-damp soft-start rule in [tesla_davinci_threads.md §1b](tesla_davinci_threads.md#1b-declassified-and-official-records-2026-10-15). Not repeated here. | **Grounded** |
| **Low-frequency magnetic-field exposure** (new; Grok did not mention it) | ICNIRP 2010 general-public **reference level for 50–400 Hz is B = 2 × 10⁻⁴ T (200 µT)** (ICNIRP, *Health Physics* 99(6):818–836 (2010), Table 4; https://icnirp.org/cms/upload/publications/ICNIRPLFgdl.pdf). The POL lift coils at 100 Hz produce fields of order **0.1 T** near the coils (the sister repo's crude on-axis estimate overshoots ~2×). That is ~500× the reference level at the rider's feet and lower legs. Reference levels are conservative screening values; localised exposure is judged against the basic restrictions (induced electric field in tissue), which needs a calculation. The question is real, and the book should flag it. | **Grounded** (guideline); POL exposure **Plausible-untested** concern, needs an induced-field estimate |
| **Implants and magnetic media** | Pacemakers and implanted devices are commonly protected by keeping the public out of zones above **0.5 mT** (static) **[to verify source, e.g. ICNIRP 2009 static-field guidance / IEC 60601 / ACGIH]**. Both the static Halbach option (§4) and the AC coils exceed this near the board. Signage and keep-out distance for demos. | **Grounded** practice; threshold **[to verify]** |
| **Heat** | Sister repo: coil heating ~2.25 K/s adiabatic, floor ~0.56 K/s under a parked board, at full hover current. Thermal cut-outs and duty limits are needed at any meaningful lift. | **Grounded** (sim) |

### 1.4 Grok's guardrails, one by one

| Grok guardrail (message 2, verbatim) | Check | Label |
|---|---|---|
| "POL v0.1 Levitator: Human-powered hoverboard prototype ... stays within hobby/experimental use ... No claims of flight or unregulated vehicle use." | Hobby/experimental framing fits 47 CFR 15.23 (home-built, ≤5 units, personal use). "Human-powered" is physically wrong for the lift (§3). | Legal framing **Grounded**; "human-powered" **corrected** |
| "We never imply operational craft that would violate FAA, FCC, or aviation regs." | FAA: not applicable to a floor-bound board (§1.2). FCC: the duty is not about "implying"; the operator must actually avoid harmful interference (§1.1). | **Grounded**, made specific |
| "Any practical steps ... stay in backyard/garage/experimental research territory with proper disclaimers." | Disclaimers do not change electrical, RF or exposure obligations. Add: power-circuit limits, guarding, field keep-out (§1.3). | **Grounded**, extended |
| "We include honest limitations sections and encourage readers to check local regulations." | Good practice. This file is a draft of that section. | **Grounded** |
| (message 6) "Safety — Low voltage, no high-speed runs until stable. Stay well below any vehicle regs." / "This is 100% legal garage tinkering" | "Low voltage" is consistent with the sister-repo coil (~10 V rms per coil) but **not** with its current (~763 A rms per coil) or power (~16.7 kW). Low voltage does not mean low hazard at those currents (burns, fire, arc flash at the bus). "100% legal" is too strong as a blanket statement; "likely within home-built rules if kept private and interference-free" is the honest version. | **Corrected** |
| Weapons / harm | Grok: "never for harm, evasion, or misuse". Nothing in the POL / RGRF material is weapons-related, and this repo keeps it that way. | **Grounded** (project policy) |

---

## 2. Buildable today vs visionary: Grok's split, labelled

Grok's split (message 2, verbatim): "We proactively separate buildable today (mycelium panels, Python hover simulations, phi-spiral coil winding guides) from inspirational future (ley-line docking, filament riders, pyramid node craft)." Message 4 expands it into three tiers. The split is sound; the labels within it need tightening.

| Item | Grok's tier | Repo label | Note |
|---|---|---|---|
| Mycelium composite panels (*T. versicolor* on hemp) | Strongly grounded | **Grounded** (as insulation / low-load panels) | Load-bearing deck needs skins or densification (§5). |
| Eddy-current lift over a conductive floor | Strongly grounded | **Grounded** physics; **cost ~10–17 kW** for a rider | Grok's own limitation list is right; its message 6 sim numbers are not (§4). |
| φ-spiral coils | Strongly grounded ("No overwhelming evidence they outperform") | **Symbolic** | Tested: φ spiral **+8.7 % more power** than linear (sister repo); also null in [sims/resonant_drive_phi_test.py](../sims/resonant_drive_phi_test.py). "Similar to known fractal antennas" is an analogy only. Grok's honest note is right; "Strongly Grounded" as a tier heading is not. |
| Tesla-style resonant wireless power | Partially grounded | **Grounded** (near field) | See §6 and [em_topo L6](em_topological_gravity_review.md#l6-wireless-energy-transfer-northern-europe-focus-noted). |
| Python hover simulations | Buildable today | **Grounded** (our sister repo and this repo's scripts exist and run) | Grok's own sim code: **not available** (§4). |
| Integrated POL → docking stations → filament riders → pyramid nodes → cosmic craft | Visionary | **Speculative** | See [book_blueprint_structure.md §4.3](book_blueprint_structure.md#43-cosmic-filaments-and-the-filament-rider). |
| Cosmic plasma filaments as real phenomena | Visionary tier, stated as real | **Grounded** (they exist) | Grok says "straight, magnetically confined plasma structures observed in radio astronomy". That fits Galactic Centre radio filaments; cosmic-web filaments are mostly gravitational (see [em_topo §5](em_topological_gravity_review.md#5-plasma-filaments--birkeland-currents-as-highways)). |
| Ley lines as "earth energies" | Visionary ("regarded as pseudoscience") | **Symbolic** | Grok's verdict matches [tesla_and_ancient_alignments.md: Ley lines](tesla_and_ancient_alignments.md#ley-lines). |
| "informed universe ideas from Kaku et al." | Visionary | **Symbolic** | Attribution not checked **[to verify]**; see [em_topo L5d](em_topological_gravity_review.md#l5d-cosmic-ley-lines-as-fractals-cosmic-web-vs-neural-networks-informed-universe-and-entangled-neutrinos) (informed universe Symbolic). |
| Net human-powered or ambient-resonant sustained hover | Visionary ("Thermodynamics and efficiency limits bite hard") | **Not feasible** with known physics at rider scale (§3) | Grok is right here, and this contradicts its own message 6 optimism (§4). |

Grok's answer to "Is it just prototyping?" (message 4, verbatim): "The core answer is no, it’s not just prototyping — there are places where current physics and materials impose real limits". **Grounded**, and the repo agrees: the 520 W vs ~16.7 kW gap is a physics bill (copper and floor losses), not a prototyping shortfall ([transistor_drive_stages.md §6](transistor_drive_stages.md#6-power-budget-note-does-transistor-efficiency-close-520-w-vs-1017-kw)).

---

## 3. The "human-powered levitator" and eddy-current lift

- **Eddy-current repulsion over a conductor: Grounded.** A changing field (AC coil, or a magnet moving relative to the sheet) induces currents in the sheet whose field repels the source. Thin-sheet theory: Reitz, "Forces on moving magnets due to eddy currents", *J. Appl. Phys.* 41, 2067 (1970) [to verify page]; finite-plate AC model in the sister repo uses Dodd & Deeds (1968).
- **Human-scale demonstrations: Grounded.** The Hendo hoverboard (Arx Pax, 2014) carried an adult about 2.5 cm above copper or aluminium using four battery-powered rotating-magnet "hover engines", with ~7 minutes of battery in demonstrations (phys.org / AFP, Nov 2014; Associated Press via CBC, 12 Nov 2014, quoted "about 15 minutes" and a 40 kg board). That shows the physics works at rider scale **with an onboard battery pack**, briefly, on a metal floor. It does not show human power.
- **"Human-powered": not feasible for the lift.** Human sustained output is ~100–250 W (bursts ~400 W). The sister-repo sim gives **16.7 kW** at default settings (**67×** a strong cyclist) and **~10 kW** for the best design found (**~40×**). To reach 250 W with this mechanism it estimates "~19 cm of solid copper in floor AND in winding". A moving-magnet board (§4) needs ≥ ~3.6–7 kW of drag power at rider weight. Grok itself says in message 4: "Human-powered alone struggles against drag and losses — we’d need mechanical amplification or hybrid input." "Mechanical amplification" cannot add energy; only an external power source (battery, mains, tether) can. **Correction:** the book should call POL a *battery- or mains-powered* eddy-current board, or (Channing's design intent) a **buoyant body with EM trim** ([lift §1a](lift_and_equilibrium_systems.md#1a-design-intent-buoyant-stability-not-levitation)), where a few hundred watts could run trim coils, control and sensors (**Plausible-untested**).
- **Human input as a minor contribution** (e.g. pushing for propulsion, a pedal generator topping up a battery): **Grounded**, at ~100–250 W. It can propel a board that is already levitated by another source; it cannot hold up 80 kg.

---

## 4. Grok's reported hover simulation (message 6): not reproducible, compared with our sims

> **Status: Grok-reported, not reproducible.** Grok wrote (verbatim): "I just ran a refined Python hover dynamics simulation for our v0.1 parameters (simple order-of-magnitude eddy model). It shows the power/efficiency behavior clearly." **No code, inputs file or output data were shown** in the conversation, and none exists in the share capture. The results below are Grok's statements only. **[Channing to supply the script if it was ever saved; otherwise treat these as unverified.]**

### 4.1 What Grok reported (verbatim)

1. "At realistic B ~0.2 T and effective area ~0.8 m² over a 5 mm Al plate, lift can overcome 80 kg weight even at low walking speeds in this idealized model."
2. "Efficiency is poor — most energy goes to heat in the plate + coil resistance + drag."
3. "Sustained human-powered (100–300 W) hover requires optimized coils, minimal gap, and a very flat conductive track."
4. "Full untethered human-carrying? Hits the wall fast due to scaling (power ~ velocity³ in many losses, plus stability)."
5. "small decks hover nicely; human payload demands hybrid input or better materials."

### 4.2 Independent check: moving magnets over a sheet

Grok's scenario is a board **moving** over a plate ("lift ... at low walking speeds"), so the relevant grounded model is a magnet moving over a thin conducting sheet. In the Reitz thin-sheet model (the same w = 2/(μ₀σd) the sister repo prints), lift/drag = v/w. To hold a lift F_L the drag power is exactly **P = F_L · w**, whatever the speed. [`sims/moving_magnet_eddy_lift_check.py`](../sims/moving_magnet_eddy_lift_check.py) takes Grok's own inputs (0.2 T, 0.8 m², 80 kg, 5 mm Al), with the field allowed to act at full magnetic pressure over the whole area, which is generous. Output (run 2026-10-17):

| Plate | w (m/s) | Lift at 1.0 / 1.5 m/s (walking) | Speed for lift = 785 N | Drag power to hold 80 kg (= m g w) |
|---|---|---|---|---|
| Al 5 mm (Grok's case) | 9.09 | 152 N / 337 N | **2.33 m/s** | **7.1 kW** (29× 250 W) |
| Cu 5 mm | 5.34 | 431 N / 931 N | 1.37 m/s | 4.2 kW (17×) |
| Al 10 mm | 4.55 | 587 N / 1,249 N | 1.17 m/s | 3.6 kW (14×) |

Thin-sheet validity: for a 10 cm pole pitch at walking speed the skin depth in Al is ~22–27 mm, larger than 5 mm, so the model applies. The 10 mm Al value of w (4.55 m/s) matches the sister repo's printed "Reitz w" for its 10 mm plate, so the two models agree.

### 4.3 Comparison and contradictions

| Grok claim | Our result | Verdict |
|---|---|---|
| (1) 80 kg lift "even at low walking speeds" over 5 mm Al | Walking speed (1–1.5 m/s) gives only **~150–340 N**, under half of the 785 N weight. Lift reaches 80 kg at ~2.3 m/s (a jog), and only if 0.2 T really fills 0.8 m². | **Contradicted** (optimistic by ~2–5× at walking speed) |
| (1) as a power statement | Grok gives no power number. At lift = weight, the board must be pushed against **~3.1 kN of eddy drag** at 2.3 m/s = **7.1 kW**. | **Missing the key number** |
| (3) "human-powered (100–300 W) hover requires optimized coils, minimal gap, and a very flat conductive track" | Implies that optimisation could close the gap. Our sims: 7.1 kW (Grok's case), ≥ 3.6 kW (10 mm Al); stationary AC hover **16.7 kW** default, **~10 kW** best searched design, with **~2.4 kW** floor loss even for a zero-resistance coil (sister repo). | **Contradicted**: optimisation narrows the gap by ~2×, not the needed ~15–70× |
| (4) "power ~ velocity³ in many losses" | For eddy drag at fixed lift, power is **constant** (m g w), not ∝ v³. Aerodynamic drag power is ∝ v³ but is tiny at walking speed (~½ ρ C_d A v³ ≈ 1–2 W at 1.5 m/s for a standing rider, C_d A ≈ 0.7 m² [to verify]). | **Incorrect** for the dominant loss |
| (2), (5) poor efficiency; small decks hover | Agrees with all repo sims and with Hendo (battery-powered, minutes). | **Grounded** |
| Coil array that is "Human-powered forward motion ... induces eddy currents" | A moving **passive coil** array makes no field of its own; motion-induced lift needs **permanent magnets** on the board (e.g. Halbach arrays, as in LLNL's Inductrack maglev concept, R. F. Post & D. D. Ryutov, *IEEE Trans. Appl. Supercond.* 10, 901 (2000) [to verify]). With electromagnets, the coils need a power source and the AC-hover numbers (10–17 kW) apply. | **Correction**: the design must choose magnets (motion lift) or powered coils (stationary lift) |
| "Human-scale needs forward velocity + strong B-field (~0.1–0.5 T locally)" | 0.1–0.5 T at the plate is achievable with NdFeB Halbach arrays (several kg of magnet; mass and cost not estimated here) **[to verify mass]**. | **Plausible** |

**Relation to the 520 W budget.** All of this sits on the same side of the documented gap: the sister repo (16.7 kW / ~10 kW), [transistor_drive_stages.md §1.3 and §6](transistor_drive_stages.md#13-fitness-of-the-named-parts-for-the-pol-lift-coil-grounded-numbers-from-the-sister-repo-sim) (driver efficiency cannot close 520 W vs ~16.7 kW; ~32× even at 99%), [lift_and_equilibrium_systems.md power ledger](lift_and_equilibrium_systems.md#power-ledger-summary), and now the moving-magnet bound (3.6–7.1 kW). Grok's message 6 is the outlier, and since its code is missing, the repo's reproducible numbers take precedence.

**Message 8 claim:** "Tune primary driver to match coil + deck effective LC. This boosts efficiency of magnetic field generation for lift, reducing input power needs." **Partly wrong.** Resonant tuning cancels the coil's *reactive* power, so the driver and supply carry far less current (sister repo: 29.7 kVA reactive at 100 Hz, needing ~125,000 µF of capacitance per coil). It does **not** reduce the *real* power (copper I²R plus floor eddy heating, 16.7 kW), which is the physics cost of lift. Same point as [transistor_drive_stages.md §6](transistor_drive_stages.md#6-power-budget-note-does-transistor-efficiency-close-520-w-vs-1017-kw).

---

## 5. Mycelium deck material properties

Repo reference: [mycelium_uses.md](mycelium_uses.md) (Jones et al. 2020 review; Channing's comparison table; Bath OSB insulation data).

| Grok claim | Check | Label |
|---|---|---|
| (msg 4) densities "~94–135 kg/m³" | Within the insulation-grade range (Jones et al. 2020: 57–99 kg/m³ for straw/hemp insulation; as-grown composites 87–552 kg/m³). | **Grounded** (for insulation grades) |
| (msg 4) "λ ≈ 0.040–0.058 W/m·K" | Matches Jones et al. 2020 (0.04–0.08) and Bath OSB (0.0415). | **Grounded** |
| (msg 4) "Compressive strengths typically 0.1–0.5 MPa"; (msg 6) "~0.2–1+ MPa" | Jones et al. 2020: as-grown composites **~0.2–1.1 MPa** (wheat straw 0.17, white-oak sawdust 1.1). Grok's two ranges disagree with each other but both sit inside the literature range; 0.1–0.5 fits low-density insulation grades, 0.2–1.1 the full span. | **Grounded** |
| (msg 6) "densities of ~100–250 kg/m³" | Within range. | **Grounded** |
| (msg 6) "up to wood-like in optimized hot-pressed forms" | Appels et al., *Materials & Design* 161, 64–71 (2019), doi:10.1016/j.matdes.2018.11.027: hot-pressed *Trametes multicolor* composites reached density **0.35 g/cm³**, flexural strength **0.86 MPa**, flexural modulus **80 MPa**. The abstract (verbatim): "heat pressing improves homogeneity, strength and stiffness of the materials shifting their performance from foam-like to cork- and wood-like". That is wood-like in **density and stiffness class (cork / soft wood)**. Strength is still far below structural timber (tens of MPa). | **Grounded** with a qualifier; "wood-like" strength **overstated** |
| (msg 6) "A 1m × 0.8m deck can be kept under 8–12 kg while supporting distributed loads." | Mass: 1 × 0.8 m × 30 mm at 250–350 kg/m³ = **6–8.4 kg**. Fine. **Bending is the real limit.** Treat the rider as a central point load of 785 N on a 0.6 m span (coils near the ends): M = FL/4 ≈ 118 N·m, section modulus b h²/6 = 0.8 × 0.03²/6 = 1.2 × 10⁻⁴ m³, so stress ≈ **1.0 MPa**. That exceeds non-pressed flexural strength (0.05–0.29 MPa, Appels 2019) and is ~equal to the hot-pressed 0.86 MPa, before any safety factor or dynamic load (jumps ~2–3× [to verify]). **A bare mycelium deck will crack.** A sandwich panel (mycelium core + hemp/flax-fibre or wood-veneer skins) is the standard fix; its strength then comes mainly from the skins. | Mass **Grounded**; load claim **not supported for a bare deck**; sandwich deck **Plausible-untested** (needs coupon tests) |
| (msg 6) "Fire-resistant" | Mycelium composites char rather than melt and perform better than polystyrene foams in fire tests (Jones et al. 2020 notes good fire performance); the Bath "fire-resistant" wording is a press release. "Fire-resistant" should read "better fire behaviour than synthetic foams, not fireproof". | **Grounded** (qualified) |
| (msg 4) "Water absorption can be high, so sealing or hybrid designs matter" | Agrees with Jones et al. 2020 and Appels 2019. | **Grounded** |
| (msg 6) "Grow ... 2–3 weeks growth, hot-press for strength" | Typical colonisation times are 1–4 weeks depending on substrate and mould size; hot pressing at ~150 °C for 20 min in Appels 2019. | **Grounded** |
| Channing's POL target (420–480 kg/m³, 2.1–2.8 MPa, up to ~3.6) from [mycelium_uses.md comparison table](mycelium_uses.md) | Above the top of as-grown literature values. Unchanged by this conversation: still needs a source or coupon tests. | **Plausible-untested** |

---

## 6. Tesla double-resonant transformer theory (message 8)

The Tesla-coil physics was checked in detail in [geometric_unity_review.md §3](geometric_unity_review.md#3-tesla-coil-physics-msg-6-checks-and-corrections) (tuning condition, C2 as distributed self-capacitance plus top load, k ranges, energy sloshing vs "swing", quarter-wave myth, split modes f± = f₀/√(1 ± k), DRSSTC vs SSTC, near-field fall-off ~1/d³ in M and ~1/d⁶ in efficiency, φ turn spacing Symbolic). History and records: [tesla_davinci_threads.md §1](tesla_davinci_threads.md#1-nikola-tesla), [§1a](tesla_davinci_threads.md#1a-mechanical-oscillator-earthquake-machine) (mechanical oscillator), [§1b](tesla_davinci_threads.md#1b-declassified-and-official-records-2026-10-15) (Babat 1949, Goldstone 1975, R-damp). Only what message 8 adds is checked here.

| Message 8 statement | Check | Label |
|---|---|---|
| "A Tesla coil is a resonant transformer invented by Nikola Tesla in 1891." | US 454,622 (23 June 1891); see GU review §3. | **Grounded** |
| f1 = 1/(2π√(L1C1)), f2 = 1/(2π√(L2C2)); L1C1 = L2C2 ⇒ f1 = f2 | Standard LC resonance and tuning condition. C2 is distributed (self-capacitance + top load), so tune by measurement. | **Grounded** |
| M = k√(L1L2), "k ... typically 0.1–0.6" | Definition of k: **Grounded**. Range: spark-gap coils typically k ≈ 0.1–0.2; DRSSTCs somewhat tighter. **0.6 is unusually tight** for a Tesla coil (risk of primary-to-secondary flashover); such values belong to ordinary transformers or tightly coupled WPT pads. | Definition **Grounded**; upper end **corrected** |
| "amplifying voltage by √(C1/C2) or √(L2/L1)" | **Correct as the ideal lossless bound.** If all primary energy moves to the secondary: ½C1V1² = ½C2V2², so **V2/V1 = √(C1/C2)**. With L1C1 = L2C2, C1/C2 = L2/L1, so this also equals **√(L2/L1)**. It is an **energy-transfer** ratio, not the turns ratio N2/N1 of an ordinary tightly coupled transformer. Real coils reach only part of it, because of losses (spark gap, wire and corona), incomplete transfer, and the gap failing to quench at the first primary-current minimum. Complete transfer occurs only at particular k values for a given mode pair [to verify the "magic k" series]. Real gain fraction **[to verify typical %]**. | **Grounded** (ideal); real gain lower |
| "high-frequency (50 kHz – 1 MHz), high-voltage, low-current output" | Typical range; see GU review §3. | **Grounded** |
| "Modern reproductions (MIT resonant coupling, solid-state DRSSTC) achieve 40%+ efficiency over ~2m" | **Mixes two things.** Kurs et al., *Science* 317, 83–86 (2007), doi:10.1126/science.1143254, verbatim abstract: "We were able to transfer 60 watts with ∼40% efficiency over distances in excess of 2 meters." That is coil-to-coil efficiency; Kurs's MIT thesis notes 400 W from the wall for 60 W at the load (~15% end to end). **A DRSSTC is an arc generator, not a power-transfer system**, and has no such efficiency figure. Message 4's "40–90%+ efficiency over ~2m" overstates: ~40% at 2 m is the published figure; higher efficiencies occur at shorter range **[90% figure to verify]**. | MIT figure **Grounded** (corrected); DRSSTC part **incorrect** |
| "Real applications in EV charging exist" (msg 4) | SAE J2954 wireless charging standard [to verify edition]; Tesla Cybercab shown with inductive charging (Oct 2024; see [book_blueprint_structure.md §3.1](book_blueprint_structure.md#31-wording-fixes-for-groks-drafts)). | **Grounded** |
| "Tesla’s grand Wardenclyffe-scale global vision hit this wall hard — not realized due to physics + economics." | Agrees with [tesla_and_ancient_alignments.md §A](tesla_and_ancient_alignments.md#claims-vs-evidence). | **Grounded** |
| "wind phi-spiral geometries (golden-ratio for field harmony)" | **Symbolic**; tested worse (+8.7 % power) in the sister repo. | **Symbolic** |
| "Extending to planetary “ley-line” or cosmic plasma filament resonance remains inspirational" | Grok's own label agrees. | **Speculative / Symbolic** |

---

## 7. Labels summary

| Item | Label |
|---|---|
| FCC: RF rules start at 9 kHz; 100 Hz lift drive below that | Grounded |
| FCC: Tesla coil at 50 kHz–1 MHz is non-ISM; 15 µV/m at 300 m (<500 W, Part 18); interference duty (18.111, 15.5) | Grounded (rule text); Part 15 vs 18 classification [to verify] |
| FCC 15.23 home-built exemption (≤5, personal, not marketed, not a kit) | Grounded |
| FAA Part 103 | Grounded (text); not applicable to a floor-bound v0.1 |
| ICNIRP 2010: 200 µT at 50–400 Hz (public); POL coils ~0.1 T near the board | Grounded guideline; POL exposure needs an induced-field estimate |
| Household circuit vs 10–17 kW draw | Grounded arithmetic; NEC cite [to verify] |
| Buildable vs visionary split | Sound; "φ coils" moved from "strongly grounded" to Symbolic |
| Eddy-current lift; Hendo as rider-scale demo (battery, minutes) | Grounded |
| "Human-powered levitator" | Not feasible for lift (≥15–70× short); human input as minor propulsion Grounded |
| Grok's message 6 sim results | **Grok-reported, not reproducible (no code)**; walking-speed lift claim contradicted; power claim missing; "power ~ v³" incorrect for eddy drag |
| Resonant tuning "reducing input power needs" | Partly wrong: reduces reactive power only |
| Mycelium density, λ, compressive strength ranges | Grounded |
| "Wood-like" hot-pressed mycelium | Grounded for density and stiffness class; strength overstated |
| Bare mycelium deck carrying a rider | Not supported (bending ~1 MPa vs 0.05–0.86 MPa); sandwich deck Plausible-untested |
| Tesla resonance equations, V2/V1 = √(C1/C2) = √(L2/L1) | Grounded (ideal lossless bound) |
| k up to 0.6 | Corrected (typical 0.1–0.2 for spark-gap coils) |
| "40%+ over ~2 m" | Grounded for Kurs et al. 2007 WPT (coil to coil); not a DRSSTC property |

---

## 8. Open questions for Channing

1. **Grok's hover script (message 6):** was it ever saved or exported? If so, add it to `sims/legacy_grok/` so its results can be rerun. **[Channing to supply]**
2. **Jurisdiction:** where are tests planned (country / state)? Section 1 covers U.S. federal rules only. **[Channing to confirm]**
3. **Lift mode for v0.1:** permanent magnets moving over a track (motion lift, needs speed; Inductrack/Hendo-style), powered AC coils (stationary lift, 10–17 kW), or buoyant body with EM trim (your design intent)? The safety and legal picture differs for each.
4. **Tesla-coil drive frequency and power** for the resonant branch, if one is planned: this decides the FCC limit row in §1.1 and the exposure calculation.
5. **Deck build:** are hemp/flax-fibre or veneer skins acceptable on the mycelium core? A few coupon bending tests (3-point bend, 30 mm thick) would settle §5.
6. **Selling or sharing kits:** is that ever planned? It would move the project out of the 47 CFR 15.23 home-built exemption.

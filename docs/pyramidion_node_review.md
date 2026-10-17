# Pyramidion Node: the Electric Universe ley-line docking station, reviewed (2026-10-17)

*License CC0. Labels: **Grounded** / **Plausible-untested** / **Speculative** / **Symbolic**. Citations were checked by Crossref / web search on 2026-10-17. Unverified items are marked [to verify]. Gaps are marked [Channing to supply]. Health statements are hedged on purpose: nothing here is medical advice.*

- **Source conversation:** Grok, "Electric Universe Ley Line Docking Station", shared by Channing. The verbatim archive is [grok_archive/2026-10-17_electric_universe_ley_line_docking_station.md](grok_archive/2026-10-17_electric_universe_ley_line_docking_station.md) (54 messages; no code visible). Quotes are marked "(Grok, msg n)".
- **Not captured:** `electric_universe_summary.md` and `pyramidion_node_full_blueprint.md`, the files Grok says it created. **[Channing to supply]**
- **New sim:** [`sims/pyramid_piezo_estimate.py`](../sims/pyramid_piezo_estimate.py), an honest piezo voltage/power estimate (results in §3).
- **Not duplicated here** (cross-linked instead):
  - Birkeland currents and filaments: [em_topo §5](em_topological_gravity_review.md#5-plasma-filaments--birkeland-currents-as-highways), [L5d](em_topological_gravity_review.md#l5d-cosmic-ley-lines-as-fractals-cosmic-web-vs-neural-networks-informed-universe-and-entangled-neutrinos), [book_blueprint_structure.md §4](book_blueprint_structure.md#4-plasma-filament-propulsion-review-of-groks-message-8);
  - Z-pinch and sheared flow: [tungsten_bismuth_core.md §3](tungsten_bismuth_core.md#3-z-pinch-with-sheared-flow-stabilization--grounded);
  - sonic pinching: [tungsten_bismuth_core.md §3a](tungsten_bismuth_core.md#3a-sonic-pinching-grok-excerpt--lost-sim-description-2026-10-15) and [transistor_drive_stages.md §8.3](transistor_drive_stages.md#83-sonic-pinch-as-a-secondary-earth-shuttle);
  - Tesla history and ley lines: [tesla_and_ancient_alignments.md](tesla_and_ancient_alignments.md#ley-lines);
  - Da Vinci: [tesla_davinci_threads.md §2](tesla_davinci_threads.md#2-leonardo-da-vinci) and [§3e](tesla_davinci_threads.md#3e-toroidal-flows-and-vortices);
  - lift methods: [lift_and_equilibrium_systems.md](lift_and_equilibrium_systems.md).

## 0. Channing's starting idea (verbatim, msg 1)
> "If you were to make a docking station on earth. You would obviously place it on intersecting lay lines, right? Also, you would want gold at the top of the platform to gather energy or charge. Then to propel it upward, out of our atmosphere or perhaps just around the magnetic sphere until oriented. Using earths natural exhaust vents some resonance maybe even chemical reactions.. Maybe that’s one of the pyramids. Another for healing. Connecting across the cosmos. Maybe?"

**Overall label: Speculative / Symbolic.** It is a creative concept for the Blueprint and *Entanglements*. Grok's own bottom line is fair (msg 2): "mainstream archaeology sees pyramids as tombs/mausoleums … No hard evidence of ancient power plants or docking … EU itself is fringe."

## 1. The Electric Universe framing, stated plainly
The Electric Universe (EU) idea holds that electric currents, not gravity and fusion, shape and power stars and galaxies. Its plasma physics building blocks are real: Birkeland currents, double layers and Z-pinches are measured in the lab and in space. EU's cosmological claims, however, are **contradicted by mainstream astrophysics**:
- the Sun is fusion-powered, as its neutrinos show directly: Borexino, *Nature* 512, 383–386 (2014) (pp chain) and *Nature* 587, 577–582 (2020) (CNO cycle);
- large-scale structure and the CMB are fitted by gravity plus dark matter;
- the measured intergalactic fields are weak (see [em_topo context](em_topological_gravity_review.md)).

The respectful way to use EU in RGRF is as **inspiration**, keeping the physics we can test: plasma circuits, field-aligned currents and pinches. **Label: EU cosmology Speculative / fringe; its plasma components Grounded.**

## 2. Site, capstone and the "Earth circuit"

| Claim | Label | Check |
|---|---|---|
| Intersecting ley lines as "telluric current nodes" where "Earth's magnetic and electric fields concentrate" (msg 2) | **Symbolic / not supported** | Ley alignments test as chance (Broadbent 1980; [tesla_and_ancient_alignments.md](tesla_and_ancient_alignments.md#ley-lines)). Telluric currents are real (fields of ~mV/km, much larger in geomagnetic storms [to verify typical range]). They follow conductivity structure, not leys. |
| "Earth's crust acts like a giant capacitor or battery" | **Grounded (as the global electric circuit)** | Earth's surface and the ionosphere form a leaky capacitor at ~250 kV, with ~1 kA of fair-weather current worldwide, charged by thunderstorms [figures to verify]. The *crust* as a battery under pyramids ("conductive limestone aquifer … galvanic cell") is **Speculative**. |
| Gold capstone "gathers energy or charge", "ionizes the air", "lightning rod for the ionosphere" | **Partly Grounded, mostly Speculative** | Gold is the third-best common conductor (after silver and copper) and does not corrode (**Grounded**). Corona and charge gathering depend on **height and tip curvature, not on gold**. A 146 m peak in the ~100 V/m fair-weather field sits in ~10⁴ V of ambient potential and draws point-discharge currents of µA–mA only under storm fields. This is lightning-rod physics ([franklin_lightning_rod.md](franklin_lightning_rod.md)), not a power source. No gold capstone of the Great Pyramid is attested [to verify]. |
| "Recent physics modeling … shows the Great Pyramid can focus electromagnetic energy in its chambers and base … like radio waves or microwaves" (msg 2) | **Grounded paper, corrected scope** | M. Balezin, K. V. Baryshnikova, P. Kapitanova & A. B. Evlyukhin, "Electromagnetic properties of the Great Pyramid: First multipole resonances and energy concentration," *J. Appl. Phys.* 124, 034903 (2018), doi:10.1063/1.5026556. It is a **numerical** scattering study for **200–600 m radio wavelengths** (≈0.5–1.5 MHz, AM band), with dipole and quadrupole resonances and field concentration in the chambers and the substrate. There are **no microwaves**, no measurement, no gold cap and no power claim. It does not concern Schumann (λ ≈ 38,000 km). |
| Dunn, *The Giza Power Plant* (1998) | **Speculative (not peer-reviewed)** | Book-length hypothesis. Its chemical-residue and hydrogen claims are **[to verify]**; the usual explanation for salt deposits is efflorescence from limestone [to verify]. |
| Pyramids as tombs | **Grounded** (archaeological consensus) | |

## 3. Oscillations, materials and the piezo numbers

### 3.1 Sound speeds (msg 8 table)

| Material | Grok (m/s) | Check (longitudinal) | Label |
|---|---|---|---|
| Air | 343 | 343 m/s at 20 °C | **Grounded** |
| Limestone | 5,500 | Very variable, ~3,000–6,000 m/s depending on porosity. The porous Tura/Mokattam limestones are at the low end [range to verify] | **Grounded (range)** |
| Granite | 6,000 | ~5,000–6,200 m/s typical | **Grounded** |
| Quartz | 5,900 | Single crystal ~5,700–6,300 m/s depending on axis; fused silica 5,900 | **Grounded** |
| Gold | 3,240 | 3,240 m/s; density 19,300 kg/m³ | **Grounded** |

Wavelengths: λ = c/f is correct (granite 375 m at 16 Hz, 766 m at 7.83 Hz). **Note:** "the whole 146 m structure vibrates coherently" (msg 14) needs a mechanical drive at that frequency. See §3.3: Schumann waves do not provide one.

### 3.2 King's Chamber acoustics
- **Room modes: Grounded.** For a rigid box, f = (c/2)·√((n_x/L)² + (n_y/W)² + (n_z/H)²). With ~10.45 × 5.2 × 5.8 m this gives **16.4 Hz** (length), **33.0 Hz** (width) and **29.6 Hz** (height), matching Grok (msg 8). The "16 Hz resonance" is ordinary room acoustics.
- **Measurements: reported, not peer-reviewed.** The acoustic engineer **Tom Danley** made the 1990s King's Chamber measurements (for a Boris Said documentary; described in Dunn 1998, on Art Bell 11 Nov 1997, and in Danley's own ProSoundWeb article). He reported room modes below 20 Hz, sarcophagus modes coinciding with room modes, ambient infrasound from a few Hz to ~20 Hz (which he attributed to wind exciting the shafts as Helmholtz resonators), and a pattern a musicologist read as roughly an **F-sharp chord**. **Label: Plausible (an expert's measurements, consistent with room acoustics) but non-peer-reviewed.** No raw data are public [to verify]. Grok's "F# noted in acoustic tests" (msg 4) traces to this.
- **528 Hz "standing wave" (msg 48): corrected.**
  - λ = 343/528 = 0.65 m is right. But 528 Hz is **not** an axial mode of 10.45 m: n = 32 gives 525.2 Hz and n = 33 gives 541.6 Hz.
  - At 528 Hz the 3D mode density is high (hundreds to thousands of modes overlap), so "a standing wave" is a 1D idealisation.
  - "Without decay (ideal lossless case)" is Grok's own caveat.

### 3.3 Schumann resonance: Grounded as EM, wrongly used as a vibration source
- **Grounded:** the Earth–ionosphere cavity modes are ~7.8, 14.3, 20.8, 27.3 and 33.8 Hz, excited by lightning. They are very weak: ~pT magnetic and ~mV/m electric [amplitudes to verify]. The cavity is low-Q (~4–5; [tesla_davinci_threads.md §1](tesla_davinci_threads.md#1-nikola-tesla), [tungsten_bismuth_core §7b-alfven.1](tungsten_bismuth_core.md#7b-alfven1-schumann-resonance-as-a-coupling-guide)).
- **Correction:** Schumann resonances are **electromagnetic**. They do not shake rock, so they cannot drive a "displacement-driven" piezo model. Grok's "acoustic tests … show strong responses near 16 Hz (a Schumann harmonic)" (msg 14) is wrong twice: 16 Hz is not a Schumann mode, and the 16 Hz is the room's acoustic mode.
- "The gold capstone + entire structure becomes a massive Schumann antenna" is **not supported**: a 146 m structure is ~4×10⁻⁶ of the 38,000 km wavelength.

### 3.4 Piezoelectric voltage and power: corrected (`sims/pyramid_piezo_estimate.py`)
Grok's formula (msg 16, plain-text reading): V = g × t × σ, σ = Y × ε, ε = ΔL/t, with ΔL = 5 µm, t = 1 m, Y = 78.7 GPa, g = 0.057 V·m/N, giving σ ≈ 0.39 MPa and **V ≈ 22,430 V**. Then (msgs 12, 14) **~2.1–2.5 W per block at 100 MΩ**, "kilowatts" for the whole pyramid, and (msg 50) **45–280 V and 0.8–12 W per resonator at 528 Hz**.

| Issue | Correction | Label |
|---|---|---|
| "g₃₃" for quartz | Quartz (class 32) has **d₁₁ and d₁₄, no d₃₃**. The 0.057 V·m/N is g₁₁ = d₁₁/(ε₀ε_r), with d₁₁ = 2.3 pC/N and ε_r ≈ 4.5. | **Grounded** (value right, label wrong) |
| Granite as an aligned crystal | Grains are randomly oriented, so the net effect is a statistical residue.<ul><li>G. J. Tuck, F. D. Stacey & J. Starkey, *Tectonophysics* 39, T7–T11 (1977), doi:10.1016/0040-1951(77)90148-2: no reliable signal, upper limit ~100 mV.</li><li>B. Bishop, "Piezoelectric effects in quartz-rich rocks," *Tectonophysics* 77, 297–321 (1981), doi:10.1016/0040-1951(81)90268-7: mostly statistical effects, with a fabric effect in a few quartzites and mylonites, at most ~1 % of single crystal [percentage from a secondary summary, to verify].</li><li>T. Sasaoka, C. Yamanaka & M. Ikeya, *GRL* 25, 2225–2228 (1998), doi:10.1029/98GL51179: apparent granite coefficient ≈ 1.4×10⁻¹⁵ C/N, **~10⁻³ of single-crystal quartz**.</li></ul>Grok itself notes "randomly oriented" and "10–50× lower"; the data say ~100–1000× lower. | **Grounded** |
| Strain 5×10⁻⁶ from "Earth vibrations" | Ambient ground motion at ~8 Hz of ~0.1–1 µm/s [site-dependent, to verify] gives a strain v/c ≈ 2×10⁻¹¹ to 2×10⁻¹⁰, i.e. **10⁴–10⁵× smaller**. And Schumann provides no mechanical drive (§3.3). | **Grounded** (order of magnitude) |
| Power with an ideal voltage source | A 1 m³ quartz element has **C ≈ 40 pF**, so its source reactance is **≈ 510 MΩ at 7.83 Hz** (244 MΩ at 16.4 Hz). Matched power is P = V²ωC/4. On Grok's own inputs: **0.25 W at 7.83 Hz** (0.53 W at 16.4 Hz), and only **0.095 W into 100 MΩ**, not 2.5 W. Lower frequency gives **less** power, not "~12× higher". Grok's 0.43 W "matched" figure (msg 12) was right. Its 100 MΩ table (2.1 W) and its comparison table (0.21 W) contradict each other. | **Grounded** |
| Realistic output | Granite factor 10⁻³ with realistic ambient strain: **V ≈ 0.06–0.6 mV per m³ block, P ≈ 10⁻¹⁸–10⁻¹⁶ W**. Even 10⁴ m³ of granite gives **~10⁻¹² W**. Even on Grok's 5 µm strain, granite gives 23 V and ~2.5×10⁻⁷ W per block. | **Grounded** (estimate) |
| 528 Hz, 1–10 Pa → "45–280 V, 0.8–12 W per resonator" (msg 50) | Upper bound (aligned single crystal, σ ≈ p): **0.06–0.6 V, 10⁻¹⁰–10⁻⁸ W**. The incident acoustic intensity is only p²/2ρc ≈ **0.001–0.12 W/m²**, so Grok's watts **exceed the sound power available**. Air→quartz transmission is also only ~10⁻⁴. | **Grounded** (energy conservation) |
| "Thousands of blocks … kilowatts" | Not supported (see above). | **Not supported** |

**Bottom line:** quartz in granite is **not** a usable power source. The "micro- to millivolts" Grok mentions in its own realism check (msgs 8, 16) is the honest figure.

### 3.5 Rectifiers: silicon vs Schottky (msgs 18, 20)
- **Grounded:** forward drop ~0.6–0.7 V (Si) vs ~0.2–0.45 V (Schottky). Full-wave average = (2/π)·V_pk, so Grok's 14,351 V from 22,430 V is arithmetically fine.
- **Corrections:**
  - (1) At kV levels the issue is not V_f but **reverse voltage rating**. The SB540 Grok names is a **40 V** part. A 22 kV bridge would need series HV silicon stacks or SiC Schottky dice (≤ ~1.7–3.3 kV each [to verify]).
  - (2) Schottky diodes have **higher reverse leakage**, which matters at the nA–µA currents of a high-impedance piezo source.
  - (3) At the **realistic** sub-mV outputs (§3.4) no passive diode conducts at all. Harvesters use active/synchronous rectification or SSHI-type interfaces.
  - "Faster switching (good for 7.83–16 Hz)" is irrelevant at those frequencies.
- **Label:** diode physics Grounded; Grok's "~100 % efficiency" applies only to its unrealistic kV source.

## 4. Healing-field claims: hedged

| Claim | Label | Note |
|---|---|---|
| A "2025 review" linking Schumann resonance to bioelectricity, sleep and healing (msg 22) | **[to verify]**; claimed effects **not established** | The review was not identified. Proposed Schumann–biology links are mostly correlational or small studies. Natural Schumann fields are ~pT. |
| "Low-frequency EM fields … accelerate healing" / PEMF in medicine | **Grounded for specific, regulated PEMF uses** (e.g. bone-healing stimulators, at field strengths far above Schumann); other claims mixed | Not evidence for pyramid or Schumann "healing nodes". |
| Bosnian "pyramids" (Osmanagić) | **Not supported** | Archaeologists and geologists regard the hills as natural formations [specific statement to verify]. The `Jelsciences` chip is a low-tier source. |
| Bovis "pyramid power" (food, blades) | **Not supported** (anecdotal; controlled tests negative [to verify]) | |
| Solfeggio tones (396–852 Hz), 528 Hz "miracle tone", "linked to DNA repair" (msgs 46, 48) | **Not supported** | The set is a modern (late-20th-century) construction, not an ancient scale [origin to verify]. The one study often cited is K. Akimoto, A. Hu, T. Yamaguchi & H. Kobayashi, "Effect of 528 Hz Music on the Endocrine System and Autonomic Nervous System," *Health* 10, 1159–1170 (2018), doi:10.4236/health.2018.109088. It is a very small sample [n to verify], published in a low-impact journal, and compares 528 Hz with 440 Hz music for stress markers. It is weak evidence and says nothing about DNA. |
| Toroidal healing node at "~microtesla" (msg 24), then "~0.004 T for 1000 A and 100 turns" (msg 26) | **Arithmetic Grounded; source not supported** | B = μ₀NI/(2πR) = 4 mT at R = 5 m, which is correct. But 1000 A can't come from the piezo (§3.4: ≤10⁻¹² W), and "microtesla" vs "4 mT" is a 1000× inconsistency. "At 7.83 Hz, the torus acts as a resonant cavity" is **wrong**: a 10 m torus is ~10⁻⁶ λ, so any resonance would have to be a lumped LC. |

**Label for the healing node: Speculative**, with health effects **not established**. Any human-exposure test would need ethics review, and is out of scope here.

## 5. Field and plasma physics passages

| Topic (msg) | Label | Check / correction |
|---|---|---|
| Feynman diagrams, QED vertex, virtual photon → classical field (msg 26) | **Grounded** | Correct but not needed: at 7.83 Hz and lab fields, classical Maxwell/MHD is exact enough. |
| MHD equations, frozen-in flux, tokamak safety factor, kink/tearing (msg 26) | **Grounded** | Textbook. |
| EM vs gravity table (msg 28): "~10⁻³⁶ times weaker … between proton/electron" | **Corrected** | Coulomb/gravity is **2.27×10³⁹** for proton–electron, **1.24×10³⁶** for proton–proton and **4.17×10⁴²** for electron–electron (OpenStax *College Physics* §18.3). In relativity EM is the tensor F_μν, not two separate vector fields. The rest of the table is **Grounded**. |
| Plasma "cells", double layers, EM-driven cosmic web (msg 28) | Double layers **Grounded**; EM-driven cosmic web **Speculative / fringe** | See [book_blueprint_structure.md §4.3](book_blueprint_structure.md#43-cosmic-filaments-and-the-filament-rider). |
| Birkeland currents (msg 30): Birkeland 1908; Region 1/2; ~MA; Juno | **Grounded** | Field-aligned currents: Iijima & Potemra 1976 ([em_topo §5](em_topological_gravity_review.md#5-plasma-filaments--birkeland-currents-as-highways)). Juno: S. Kotsiaros et al., *Nat. Astron.* 3, 904–909 (2019), doi:10.1038/s41550-019-0819-7 (weaker than expected, as Grok says). "Up to ~1 TW" [to verify]. Galactic Birkeland currents: **Speculative** ([book_blueprint_structure.md §4.1](book_blueprint_structure.md#41-filament-basics), Peratt 10¹⁷–10¹⁹ A). |
| Bennett relation μ₀I²/(8π) = N k_B T, with 1 MA and 10 MK → N ≈ 1.81×10²⁰ m⁻¹ (msg 32) | **Grounded (checked)** | 0.05 J/m ÷ (k_B·2T) = 1.81×10²⁰ m⁻¹ for T_e = T_i. |
| Sausage (m=0) and kink (m=1); sheared-flow stabilisation; Zap Energy (msgs 32–36) | **Grounded** | U. Shumlak & C. W. Hartman, *PRL* 75, 3285 (1995), doi:10.1103/PhysRevLett.75.3285 (kink stabilised for dv_z/dr ≳ 0.1 k v_A); U. Shumlak et al., "Evidence of stabilization in the Z-pinch," *PRL* 87, 205005 (2001), doi:10.1103/PhysRevLett.87.205005 (ZaP); Y. Zhang et al., *PRL* 122, 135001 (2019), doi:10.1103/PhysRevLett.122.135001 (FuZE sustained neutrons). Repo detail: [tungsten_bismuth_core.md §3](tungsten_bismuth_core.md#3-z-pinch-with-sheared-flow-stabilization--grounded). |
| Grok's growth-rate "simulations" (γ reduced 36 %, 20 %, 4 %) (msgs 34–38) | **Unreproducible heuristics** | No code was shown and Grok calls them heuristic. The percentages are not physics results. |
| Kruskal–Shafranov "q = (2π r B_z) / (μ₀ I R) > 1" (msg 38) | **Corrected** | The stated form is not dimensionless. For a column of radius a and length L: q = 2πa B_z/(L B_θ) = 4π²a² B_z/(μ₀ I L) > 1. |
| Stabilised pinch at "~5 kA … from piezo-derived kW-scale power" (msg 40) | **Not supported** (power source) | The pinch physics is fine; the piezo power is not there (§3.4). |
| Hexagon of six EM sources: strong fields "minimal wobble", weak fields "visible wobble" (msg 40) | **Plausible-untested** (no model given) | Parallel currents **attract**. A free ring of six current filaments is not self-stable, so it needs external confinement or fixed mounts. A simple N-filament test would settle the "wobble" claim. See the locking passages in §7. |
| Mercury: diamagnetic χ "≈ −2.4×10⁻⁵"; conductive; MHD vortex (radial J + axial B) (msg 42) | **Grounded** (SI volume χ of Hg is closer to ≈ −2.8×10⁻⁵ [to verify]) | Gold ≈ −3.4×10⁻⁵ and copper ≈ −9.6×10⁻⁶ are diamagnetic; **aluminium is paramagnetic** (≈ +2.2×10⁻⁵) [values to verify]. **Correction:** "Gold/mercury combo: Both weakly diamagnetic → subtle repulsion" is wrong. Diamagnets are each pushed out of field gradients; they do not meaningfully repel each other. **Safety: Grounded.** Hg is toxic; use gallium alloys (Galinstan). Liquid mercury found under Teotihuacan (2015) is **Grounded** as an archaeological find [primary source to verify]. Energy use there is **Speculative**. |
| Ferrous "peaks/valleys" vs non-ferrous "equal flux" (msg 44) | **Grounded, with a nuance** | High-μ material concentrates flux (**Grounded**). Non-ferrous conductors barely distort **DC** fields, but they **exclude AC** fields (skin effect), which also distorts them. "Equal flux" therefore depends on frequency. |
| Tungsten for sustained resonance; tungsten-quartz (msg 44) | Properties **Grounded**; "high-Q tungsten" **corrected** | W: ρ ≈ 19.3 g/cm³, E ≈ 411 GPa, c_L ≈ 5.2 km/s, melting point 3,422 °C. Quartz is the high-Q material (crystal-resonator Q ~10⁴–10⁶). Bonded metal joints **lower** Q. W's acoustic impedance (~1.0×10⁸ Rayl) vs quartz (~1.5×10⁷) is a ~7× mismatch, which is useful as a heavy **backing / tail mass** in Langevin-type transducers. "Tungsten-bronze" piezo ceramics are named after a crystal **structure type** (e.g. SBN) and do not contain tungsten metal. |
| Solfeggio Lorentzian sim: harmonic config peaks at 528 Hz (msg 46) | **Symbolic** (circular) | The resonator was centred near 528 Hz in the "harmonic" case, so its peak there is built in. |

## 6. Motors, locking and propulsion

| Topic | Label | Check |
|---|---|---|
| Ultrasonic piezo motors: elliptical stator motion, friction drive, holding torque, no magnetic field (msgs 50–52) | **Grounded** | Real example: **Shinsei USR60** drives at **40–45 kHz**, 130 Vrms; rated **0.5 N·m** (max/holding 1.0 N·m); 5 W rated output; 100 rpm; a non-magnetic variant exists. Shinsei's catalogue gives efficiency of "approximately 30 [%]" (shinsei-motor.com, catalogue 2022). |
| "528 Hz drive" for an ultrasonic motor; 0.002 N·m per element; "35–45 %" efficiency | **Corrected** | 528 Hz is audible, not ultrasonic. USM stators run at their tens-of-kHz flexural modes. Grok's torque is unsourced. Its 25–55 % range brackets reality, but ~30 % is the catalogue figure. |
| "Infrasound + Electromagnetic Locking … analogous to injection locking in oscillators" (msg 52) | **Grounded as a concept** (R. Adler, "A Study of Locking Phenomena in Oscillators," *Proc. IRE* 34, 351–357 (1946), doi:10.1109/JRPROC.1946.229930); the node application is **Speculative** | The Grounded embodiment of "mechanical vibration locks an electrical oscillation" is the **quartz crystal oscillator**. "Infrasound … excite[s] telluric currents" is **not supported**. Locking "plasma/charge distribution into coherent modes" is **Speculative**. |
| Acoustic levitation (msg 4) | **Grounded at mm scale** | A. Marzo et al., *Nat. Commun.* 6, 8661 (2015). It cannot lift craft. |
| Ion-wind / EHD thrust (msgs 4, 14) | **Grounded in air only** | H. Xu et al., "Flight of an aeroplane with solid-state propulsion," *Nature* 563, 532–535 (2018). It needs air, so it cannot work "out of our atmosphere". See [lift_and_equilibrium_systems.md §4](lift_and_equilibrium_systems.md#4-ionic-wind--electroaerodynamics-grounded). |
| Chemical/hydrogen "plasma kick" through the shafts; magnetosphere "tethering" | **Speculative** | |
| **Heavy-Lift Obelisk Array** ("magnetic-repulsion launch of larger vessels via synchronized EM pulses", msg 4) | **Speculative** | Recorded as a concept only, with no engineering detail. |
| Da Vinci vortices (msgs 44–52) | History **Grounded**; φ and "equal-flux" links **Symbolic** | See [tesla_davinci_threads.md §2](tesla_davinci_threads.md#2-leonardo-da-vinci) and [§3e](tesla_davinci_threads.md#3e-toroidal-flows-and-vortices). |

## 7. Locking / lock-pin passages (candidate source for the missing "electrostatic locking linch pins")

Channing says a section on **"electrostatic locking linch pins"** is missing. This conversation has **no passage** using "linchpin", "lock pin" or "electrostatic locking". The closest passages are below, verbatim. They are a **candidate source only, Channing to confirm**. Compare them with the "6 lock pins + Spin" in [rgrf_foundations_review.md §5](rgrf_foundations_review.md#5-the-6-lock-pins--spin-verbatim-with-labels): pin 2 "resonant frequency locking" and pin 4 "spin-induced coherence".

1. Msg 14: "Magnetic orientation: Schumann modulates the ionosphere, helping craft “lock on” to cosmic plasma filaments once above the atmosphere."
2. Msg 14: "The pyramid node essentially plugs into Earth’s plasma circuit and could phase-lock with incoming cosmic filaments."
3. Msg 40 (hexagon test): "Right (Weaker Fields): Lower intensity with small random perturbations (realistic noise from Schumann variations or material imperfections) → visible wobble/asymmetry. The hexagon deforms slightly; weaker pinning allows oscillatory motion or drift."
4. Msg 40: "Docking: Hexagonal resonator arrays at the apex/gold capstone could create a stable "reception grid" that locks onto incoming cosmic currents."
5. Msg 51 (Channing): "Can we explore infrasound and Electromagnetic locking?"
6. Msg 52: "EM Locking: Infrasound-modulated EM fields create phase-locked synchronization between acoustic pressure nodes and electromagnetic standing waves. This is analogous to injection locking in oscillators — the mechanical vibration “locks” the plasma/charge distribution into coherent modes."
7. Msg 52: "Locking: Infrasound + EM creates self-stabilizing “locked” modes for propulsion (stable Z-pinch exhaust) and healing (coherent bio-fields)."

**Labels:**
- phase / injection locking: **Grounded** (Adler 1946);
- the hexagonal "pinning" of field sources: **Plausible-untested**;
- locking onto cosmic filaments: **Speculative**.

**What an "electrostatic locking linch pin" could mean physically (Resona suggestion, not Channing's wording):** a fixed charged electrode or field node that holds a phase or position reference. Examples are electrostatic bearings and trapping in a quadrupole (Paul-trap-style) field, which escapes Earnshaw by using AC (cf. [lift_and_equilibrium_systems.md §9](lift_and_equilibrium_systems.md#9-levitation-methods-grounded)). **[Channing to supply the original section or wording.]**

## 8. Labels summary
- **Grounded:**
  - plasma components of EU (Birkeland currents, double layers, Bennett pinch, kink/sausage modes, sheared-flow stabilisation: Shumlak 1995/2001, Zhang 2019);
  - room modes (16.4 / 33 / 29.6 Hz);
  - sound speeds;
  - Schumann modes (as EM);
  - Balezin 2018 (numerical, 200–600 m radio);
  - EM vs gravity ratios;
  - Hg diamagnetism and MHD;
  - ferrous flux concentration;
  - tungsten properties;
  - rectifier physics;
  - injection locking;
  - ultrasonic motors (USR60);
  - acoustic levitation (mm scale) and EHD thrust in air;
  - Juno Birkeland currents;
  - the Borexino solar-fusion evidence.
- **Plausible / reported:** Danley's King's Chamber infrasound (non-peer-reviewed); the hexagonal-array wobble test.
- **Speculative:**
  - EU cosmology;
  - the Pyramidion Node and docking/launch;
  - capstone charge collection as power;
  - the hydrogen "plasma kick";
  - the heavy-lift obelisk array;
  - the healing node;
  - locking onto cosmic filaments;
  - the Dunn power-plant hypothesis.
- **Symbolic:** ley-line siting; Solfeggio "harmonic" configurations; Da Vinci φ / equal-flux links.
- **Not supported:**
  - kW from piezo granite;
  - Schumann as a mechanical drive or as something a 146 m antenna can collect;
  - 528 Hz healing / DNA repair;
  - Bosnian pyramids and Bovis pyramid power;
  - infrasound exciting telluric currents.
- **Corrected:**
  - g₃₃ → g₁₁;
  - ideal-source power (2.5 W → 0.095 W at 100 MΩ even on Grok's inputs; real ≤10⁻¹⁶ W per m³);
  - 528 Hz piezo watts exceeding the acoustic power available;
  - "16 Hz Schumann harmonic";
  - "microwaves" in Balezin;
  - SB540 (40 V) at 22 kV;
  - the 10⁻³⁶ "proton/electron" ratio;
  - the Kruskal–Shafranov form;
  - "diamagnets repel each other";
  - "high-Q tungsten";
  - "528 Hz ultrasonic motor";
  - "torus as a 7.83 Hz cavity".

## 9. Open questions for Channing
1. **"Electrostatic locking linch pins":** what did the missing section say, and where was it (which month or thread)? Are any of the §7 passages part of it?
2. Do you have `electric_universe_summary.md` or `pyramidion_node_full_blueprint.md` downloaded?
3. **Earlier EU conversation:** msg 2 refers to a "previous conversation about the electric universe" covering cyclotron/magnetron riding and quantum links. Is that the L5b excerpt ([em_topo L5b](em_topological_gravity_review.md#l5b-filament-riding-casimir-resonance-chamber--quartz-tuning-grok-excerpt-recovered-2026-10-15)) or another thread? [Channing to supply]
4. Should the Pyramidion Node live in the Blueprint (Part I Ancient / Part III Future) or in *Entanglements* as narrative?
5. Is the hexagonal "wobble" test worth a small sim (6 current filaments, strong vs weak, with mounts)?

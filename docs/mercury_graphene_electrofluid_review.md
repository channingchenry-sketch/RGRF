# Mercury under resonance, perforated graphene, ionic wind, liquid metals, bismuthene, CNT/BNNT, and the bubble→well gate: review of Grok share `604dca24` (2026-10-17)

**Source:** [grok_archive/2026-10-17_mercury_resonance_perforated_graphene_screens.md](grok_archive/2026-10-17_mercury_resonance_perforated_graphene_screens.md). This is share #79: 12 messages, rebuilt from the PDF capture. No images or code.

**Rerun / check:** [sims/s70_80_claim_checks.py §8–§9](../sims/s70_80_claim_checks.py) (Minnaert bubble resonance; mercury saturated-vapour concentration). Output: [sims/s70_80_claim_checks_output.txt](../sims/s70_80_claim_checks_output.txt).

**Related:**
- [lorentz_larmor_boron_nitride_review.md](lorentz_larmor_boron_nitride_review.md): h-BN, the Larmor correction and Lorentz "gaps".
- [drill_bit_density_gradient_review.md](drill_bit_density_gradient_review.md): hot/cold zones and adiabatic cooling.
- [butterfly_node.md](butterfly_node.md): foci and the free egg.
- [tungsten_bismuth_core.md](tungsten_bismuth_core.md): bismuth diamagnetism.

**Labels:** Grounded · Plausible-untested · Speculative · Symbolic.

## ⚠ Mercury safety (read first)

Grok mentions mercury's toxicity but understates it. The repo's position is: **do not use elemental mercury in any build or experiment in this project.** Grok itself pivots away from mercury in msg 4.

- **Vapour is the main hazard.** Liquid mercury evaporates at room temperature. Saturated air over open mercury holds ~14 mg/m³ at 20 °C and ~60 mg/m³ at 40 °C ([sim §9](../sims/s70_80_claim_checks_output.txt)). Exposure guidelines are ~0.025–0.05 mg/m³ averaged over 8 h (NIOSH REL 0.05 mg/m³; OSHA ceiling 0.1 mg/m³). Open mercury therefore exceeds them by ~300–500× in a still room. Vapour is odourless, and chronic exposure damages the nervous system and kidneys.
- **Never heat, vibrate, ultrasonicate or spray mercury.** Each one raises vapour or aerosol release sharply. That is exactly the "resonance / cavitation / sonochemistry" regime discussed in msg 2. The vibrating-drop and beating-heart experiments in the literature are run under controlled lab ventilation.
- **Amalgamation.** Mercury dissolves into or attacks aluminium, copper, zinc, gold and silver. On aluminium (the repo's inner sheath) it breaks the oxide skin and drives rapid corrosion. Keep Hg away from all Al parts.
- **Organic mercury is worse.** Methylmercury (the Minamata disease agent) forms from inorganic mercury in the environment and bioaccumulates. Mercury waste must never go to drains or soil.
- **Spills.** Never vacuum or sweep. Follow the EPA guidance for small spills, ventilate, and keep children and pregnant people away. For anything larger than a thermometer, call the local health or environmental agency.
  - EPA: https://www.epa.gov/mercury
  - EPA spill guide: https://www.epa.gov/mercury/what-do-if-mercury-thermometer-breaks
  - OSHA: https://www.osha.gov/mercury
- **The graphene "non-toxic sandwich" (msg 2) is overstated.** A capping layer can suppress outgassing in a lab electrode. Graphene has grain boundaries, pinholes and tears, and the device is still mercury waste. It does not make mercury safe to handle.
- **Other metals Channing listed:**
  - **Cadmium** is a known human carcinogen and is toxic by inhalation of dust or fume. Grok rightly sets it aside.
  - **Gallium** is far less toxic than Hg and is not volatile, but it **embrittles and penetrates aluminium** (liquid-metal embrittlement). Ga or Galinstan must not touch the Al sheath.
  - **Chromium(VI)** compounds (e.g. from some plating or electrolytes) are carcinogenic. Use only Cr(III) or metallic Cr.
- Corona / ionic-wind rigs (msg 4) use kV supplies and produce ozone. Use current-limited supplies and ventilation.

## Channing (verbatim)

| Msg | Prompt |
|---|---|
| 1 | "Can we look at mercury under resonance and graphene.. also can we look at our perforated graphene screens again?" |
| 3 | "Can we look at what happens in electrostatic winds again just with the graphene sheets let's remove the mercury and look at just electrolytes.. actually let's look at Gallium, Manganese, Magnesium, Zinc, Copper, chromium and cadmium some of them are again with are last discussion as well.." |
| 5 | "Ok now let's explore boron, bismuth, ferrofluids that work best with graphene.. also, look at graphene spikes or nodules in our cavity type set up can we create further pinning and transfer it in and out through capacitors or like Lorenz type relay kind of like the gaps we talked about earlier, also let's say there are different channels could we switch kind of like a train track.. also in the membrane it there is a bound between the materials does this allow for flexibility" |
| 7 | "Can we explore bismuthene's Hall effects also can we bring in CNT, BNNT's and transistors.. can we examine electro fluid behavior" |
| 9 | "Can we explore the density relation.. hot cold path will have different effects on each(condensation, strengthening, damping, spinning) also, I'm picturing balanced waves at a set frequency and then like another frequency that creates a bubble but also if a gate opens it becomes a well can we explore that concept?" |
| 11 | "Can we pause here and save.. to be continued" |

## A. Mercury and graphene; perforated graphene (msg 2)

| Claim | Label | Check |
|---|---|---|
| Vibrated Hg drops show subharmonic (Faraday) oscillation, rotation, ejection | Grounded | Lab literature; see the safety section. |
| The mercury beating heart is electrocapillary/redox-driven, not pure mechanical resonance | Grounded | Grok gives the right framing. |
| Hg adatoms bind weakly to graphene (~0.1–0.2 eV) | Plausible / **[to verify]** | DFT values vary with functional and dispersion correction. |
| Hg²⁺ binds functionalised graphene / graphene–Au; sub-ppb sensors | Grounded (sensor literature) | Specific limit **[to verify]**. |
| Graphene–Hg–graphene sandwich electrode, "non-toxic" | Plausible (device exists) / **overstated** | See the safety section. Paper **[to verify]**. |
| Solid crystalline Hg nanoparticles on rGO at room temperature by sonochemistry | **[to verify]** | An unusual claim. Hg melts at −38.8 °C. |
| Perforated graphene: FIB/laser perforation, composites on porous supports (Lockheed Perforene), gas separation, ultrafiltration | Grounded | Commercial scale-up has been slow; Grok's caveats are fair. |
| Nanoperforated graphene THz edge-state absorption; valley selectivity with circular polarisation | Plausible / **[to verify]** | |
| Graphene's diamagnetism used in light-driven levitating/spinning discs | Grounded | Pyrolytic graphite levitation and photothermal rotation. "Tesla-style engines" means the Tesla-turbine analogy. |

## B. Ionic wind with graphene; the metals (msg 4)

| Claim | Label | Check |
|---|---|---|
| Graphene-coated emitters lower corona inception and raise ionic-wind volume velocity by 41 % at a 10 mm gap | **Verified** | J. Wang et al., *Int. J. Energy Res.* (2019), doi:10.1002/er.4532. Grok's 41 % is that paper's 41.3 %. |
| Vertical graphene on wires: lower power, less ozone | Plausible / **[to verify]** | |
| Flow over graphene induces electronic current (Coulomb-drag / phonon coupling) | Grounded | Small currents (µA-scale), not a power source. |
| Ga/Galinstan continuous-electrowetting pump, no moving parts, < 15 mW | **Verified** | S.-Y. Tang et al., *PNAS* 111, 3304 (2014): up to 5,400 µL/min at ~13 mW. |
| FEEP with Ga or Ga alloys | Partly correct / **[to verify]** | Flight FEEP thrusters mostly use indium or caesium. Ga is the standard liquid-metal ion source for focused-ion-beam tools. |
| Graphene stabilises Ga contact; Ga intercalation under graphene | Plausible / **[to verify]** | |
| Cu, Cu–Cr–Zr, Zn, Mg electrode roles; MnCl₂ flow-battery electrolytes | Grounded | |
| Cd "non-preferred" on toxicity grounds | Grounded | See the safety section: carcinogen. |

## C. Boron, bismuth, graphene ferrofluids, spikes, switching, membranes (msg 6)

| Claim | Label | Check |
|---|---|---|
| Borophene metallic and anisotropic; h-BN lattice-matched to graphene (~1.8 % mismatch) and the standard graphene dielectric | Grounded | |
| Graphene-stabilised Fe₃O₄ / MnFe₂O₄ suspensions: less sedimentation, higher field yield stress | Grounded (MR-fluid literature) | Grok mixes up ferrofluids (nanoparticle, colloidal) and magnetorheological fluids (micron particles). The "5–30 wt %" graphene loading is **[to verify]**. |
| Graphene edges/spikes are good field emitters (turn-on < 3 V/µm, enhancement factors 10³) | Grounded | |
| Spikes at the cavity foci "pin" charge or ferrofluid; release through capacitors or a "Lorentz relay" | Plausible-untested | Field-gradient trapping (dielectrophoresis, magnetophoresis) is real. In a conducting fluid, field emission into the liquid becomes electrolysis or breakdown. "Lorentz relay" links to [lorentz_larmor_boron_nitride_review.md §A](lorentz_larmor_boron_nitride_review.md). |
| "Train-track" switching of channels by field pulses, ferrofluid plugs and MR valves | Plausible-untested | Ferrofluid-plug valves and MR valves are demonstrated in microfluidics. Routing at the foci is untested. |
| Bonded 2D-layer membranes stay flexible; local covalent links where stiffness is needed | Grounded (qualitative) | |

## D. Bismuthene Hall effects, CNT/BNNT transistors, electrofluids (msg 8)

| Claim | Label | Check |
|---|---|---|
| Bismuthene on SiC: QSH candidate with a ~0.8 eV gap and edge states | Grounded | F. Reis et al., *Science* 357, 287 (2017). Quantised conductance at room temperature in devices is not yet shown, as Grok notes. |
| α-bismuthene "doubled QSHE" (C_S = 2); β-bismuthene spin-charge separation under flux tubes; AHE in thin Bi flakes | **[to verify]** (theory/recent) | |
| CNT FETs near-ideal subthreshold swing; CNT@BNNT coaxial heterostructures as clean dielectric | Grounded / **[to verify]** specific paper | |
| Field-aligned CNTs in ferrofluid; BNNT nanofluids raising κ; electroferrofluids; CNT single-file water and slip flow | Grounded / Plausible | |

## E. Hot/cold paths; bubble → well gate (msg 10)

| Claim | Label | Check |
|---|---|---|
| Hot: lower density and viscosity, less damping, evaporation; cold: the reverse, condensation, stronger magnetisation; baroclinic torque | Grounded | Water below 4 °C is an exception (density falls). |
| Cold zones from "adiabatic expansion" | **Correction** | Needs heat rejection ([drill_bit_density_gradient_review.md §B](drill_bit_density_gradient_review.md)). |
| Standing wave f₁ parks bubbles (primary Bjerknes); f₂ near Minnaert resonance nucleates or grows a bubble | Grounded | f_M·R ≈ 3.3 m/s in water at 1 atm. 0.1 mm bubbles resonate near 33 kHz, 1 mm near 3.3 kHz ([sim §8](../sims/s70_80_claim_checks_output.txt)). Nucleating new vapour bubbles needs cavitation-threshold pressures (~0.1–1 MPa or more) unless nuclei are present. |
| Opening a gate turns the confined bubble into an open "density well"; reversible | Plausible-untested | A coherent concept. Gate time must be short versus the acoustic period (µs at tens of kHz), which rules out ferrofluid plugs (ms) for fast switching. The "density memory" framing is Speculative. |

## Contradictions with the repo
- None with the lift ledger. Nothing here addresses lift; the ~10–17 kW vs 520 W gap stands.
- **Material conflict:** both Hg and Ga attack aluminium. Neither may contact the Al sheath.

## Items [to verify]
- Hg-adatom binding energies.
- The graphene–Hg–graphene sandwich paper.
- Solid Hg nanoparticles on rGO.
- Nanoperforated-graphene THz edge absorption.
- Vertical-graphene low-ozone corona.
- FEEP propellant claim.
- Ga intercalation under graphene.
- Graphene loading of 5–30 wt %.
- α/β-bismuthene and the Bi-flake AHE papers.
- CNT@BNNT transistor arrays.

## Open questions for Channing
1. Is mercury here only a comparison or thought experiment? The review assumes no physical mercury work is planned. If any is, it needs a lab with mercury handling procedures.
2. For the bubble→well gate, what gate time and bubble size do you picture? That decides which gate (electrostatic, CNT FET, ferrofluid plug) can work.

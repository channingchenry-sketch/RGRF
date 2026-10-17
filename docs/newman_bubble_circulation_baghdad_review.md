# Newman's energy machine, spark bubbles, circulation cells and the Baghdad jar: review of Grok share `373a0a5b` (2026-10-17)

*License: CC0-1.0. Labels: **Grounded** (established physics or a checked source), **Plausible-untested** (consistent with known physics, never built or measured here), **Speculative** (beyond current evidence), **Symbolic** (meaning or aesthetics, not a physical claim). Numbers Grok gave without a rerun are marked **Grok-reported**. Unchecked citations are marked [to verify]; gaps are marked [Channing to supply]. Channing's words are quoted verbatim.*

- **Archive:** [grok_archive/2026-10-17_joseph_newman_energy_machine_investigation.md](grok_archive/2026-10-17_joseph_newman_energy_machine_investigation.md) (26 messages, all public; nothing withheld).
- **Claim checks:** [sims/grok_s81_85_claim_checks.py](../sims/grok_s81_85_claim_checks.py), output in [sims/grok_s81_85_claim_checks_output.txt](../sims/grok_s81_85_claim_checks_output.txt) (sections A–C).
- **Related docs (not repeated here):** [bubbles_arcs_frc.md](bubbles_arcs_frc.md) (bubble buoyancy and arcs), [em_topological_gravity_review.md](em_topological_gravity_review.md) (momentum bookkeeping for EM drives), [electrostatic_locking_pins.md §4](electrostatic_locking_pins.md#4-cross-links-every-other-lock-pin-in-the-repo-and-captured-shares) ("lock" vocabulary), [materials_electronics.md](materials_electronics.md) (BN, graphene), [ANALYSIS_2026-10-12.md](ANALYSIS_2026-10-12.md) (power budget and φ results).

## 0. Summary

| Topic (msgs) | Verdict | Label |
|---|---|---|
| Newman's energy machine (1–2) | Failed independent testing: the 1986 NBS tests found input power greater than output power in every condition. **Not supported as over-unity.** Grok says this plainly and correctly. | Grounded (the test result); Newman's theory **not supported** |
| Tesla-coil driver for bubble dynamics (3–4) | A pulsed HV source can make spark bubbles; the "Larmor precession locking as master clock" framing is not a measured mechanism. | Grounded (spark bubbles) / Speculative (Larmor lock of a ferrofluid flow) |
| Spark-bubble numbers (6) | ~8 mm / 1.7 ms and ~13–14 mm / ~3 ms match the Rayleigh collapse time to within ~20 % (section A). 3.5–7.5 % hydraulic efficiency is in line with the literature [to verify the specific source]. | Grounded (order of magnitude); exact pairs Grok-reported |
| Material-tuned circulation, hot/cold zones (7–10) | Ferrohydrodynamics and heat-pipe physics are real; "self-sustaining circulatory oscillation" (msg 10) is **not supported**: a dissipative loop needs a continuous heat or power input. | Plausible-untested (thermomagnetic convection) / not supported (self-sustaining) |
| Golden-ratio or 3-6-9 twist pitch (10) | No physical reason given; no test. | Symbolic |
| BN "cyclotron", Cu–BN–graphene chain (11–14) | Material properties are right (h-BN insulating and thermally conductive; graphene and Cu conductive). A "cyclotron" here is a swirl chamber, not a particle accelerator. | Grounded (materials) / Speculative (device) |
| Four-ellipse "thruster" (14) | "Smooth rearward momentum flux" without propellant tanks is only possible if working fluid leaves the craft. A closed internal circulation gives zero net thrust (momentum conservation). Grok concedes this in msg 16. | Contradicts momentum conservation as first worded; corrected in msg 16 |
| Central hot core, cold boundary (15–18) | A reasonable spacecraft thermal-control layout (hot core, radiating shell). | Plausible-untested |
| Vinegar (19–20) | Weak acid, attacks Cu in air, changes surface tension and ferrofluid stability: correct. | Grounded |
| Baghdad jar (21–22) | It works as a weak galvanic cell when acid is added (Grounded). That it **was** a battery is contested; the mainstream reading is a scroll or sacred-text container. | Mainstream vs contested, see §3 |
| Electroplating (23–24) | No archaeological evidence of ancient electroplating; ancient gilding was mechanical, diffusion or fire (mercury) gilding. | Mainstream: unsupported for antiquity |
| Carboxyl CNT–BNNT bonding, plasma "3D printer" (25–26) | Carboxyl-CNT / BNNT H-bonding in composites is reported in the literature [to verify specific paper]; a plasma welder that keeps these bonds intact is untested (plasma would break them). | Plausible-untested / Speculative |

## 1. Newman's energy machine (msgs 1–2)

Channing: "Can we explore Joseph Newmans work?"

Grok gives a fair account. Checked facts:

- **NBS test, Grounded.** National Bureau of Standards, *NBSIR 86-3405*, "Report of Tests on Joseph Newman's Device" (R. E. Hebner, G. N. Stenbakken, D. L. Hillhouse; tests March–June 1986). At every test condition the input power from the batteries exceeded the output power. The report's efficiencies run from about 27 % to 67 %. Government document, linked only: <https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nbsir86-3405.pdf> (doi:10.6028/NBS.IR.86-3405).
- **Courts, Grounded.** *Newman v. Quigg*, 681 F. Supp. 16 (D.D.C. 1988), affirmed 877 F.2d 1575 (Fed. Cir. 1989). The patent was refused for lack of utility and enablement. Grok's "Later court rulings upheld the rejection" is correct.
- **Newman's theory (gyroscopic particles; copper mass converting to energy via E = mc²), not supported.** The energy involved in any coil is many orders of magnitude below a mass change that could be measured, and the tests showed ordinary motor losses.

**Verdict:** Newman's machine is **not supported as over-unity**. It is an inefficient high-voltage pulsed DC motor. Grok's own conclusion ("conservation of energy is not optional") matches the repo's position in [ANALYSIS_2026-10-12.md](ANALYSIS_2026-10-12.md).

## 2. Bubble dynamics, circulation and the thruster thought experiment (msgs 3–18)

Channing (msg 3): "Luckily, we are working with equilibrium and angular momentum.. can we use Tesla coils for the bubble dynamics.. where we left off earlier"

Here "Tesla coil" means the resonant high-voltage transformer used as a pulse source. It is in scope.

- **"Larmor precession locking … as the master clock" (msgs 4, 6, 8).** Speculative. Larmor precession concerns magnetic moments (nuclear or electron spins, or single-domain particles). A bulk ferrofluid vortex has no Larmor-locked angular momentum of its own: the particle moments relax in microseconds (Néel/Brown relaxation), and the flow is set by viscosity and body forces. No data or sim is given. The earlier "wave-gate" thread it refers to is [Channing to supply].
- **Electrohydraulic spark bubbles (msg 6), Grounded in order of magnitude.** The Rayleigh collapse time t_c = 0.915 R √(ρ/Δp) gives an oscillation period ≈ 2 t_c of 1.45 ms for R = 8 mm and 2.45 ms for R = 13.5 mm (section A). Grok's 1.7 ms and ~3 ms are consistent (real bubbles in a vapour/gas mix run longer than the ideal Rayleigh bubble). The specific voltage–radius pairs and the 3.5–7.5 % efficiency range are Grok-reported [to verify the source]. Grok's parallel/perpendicular "energy window" table (msg 6) is a qualitative design guess: Plausible-untested.
- **Material-tuned thresholds, hot/cold transition zones (msg 8).** Thermomagnetic convection is Grounded: ferrofluid magnetisation falls with temperature, so a field gradient drives hot fluid one way and cold fluid the other. It still needs a continuous heat source.
- **Precessing funnel (msgs 9–10).** Channing (msg 9): "Let’s do a thought experiment.. let’s say we have our ellipse cavity an inward to outward funnel should work with our system this is our foci procession this alone creates our pulse if we have two intermittent channel(also same on the bottom) weaker magnetic(hot zone)twisted channels outside a similar vortex well to the cold zone what would this do?"
  - Grok (msg 10): "Once primed, the system could sustain a low-input or self-sustaining circulatory oscillation". **Not supported** as "self-sustaining": viscous and thermal losses stop any free circulation unless energy is supplied. "Low-input" is fine if the heat input is counted.
  - "Set the twist pitch … near a golden-ratio or 3-6-9 related multiple": **Symbolic** (no test; the repo's φ-coil sims show no φ advantage, see [ANALYSIS_2026-10-12.md](ANALYSIS_2026-10-12.md)).
- **Parallel pair, BN "cyclotron" (msgs 11–12).** h-BN is an electrical insulator with high in-plane thermal conductivity: Grounded. The "cyclotron orbit" is a swirl of fluid in a ring chamber; ordinary cyclotron motion applies to free charges, not to a neutral fluid. Speculative as a device.
- **Cu–BN–graphene chain (msgs 13–14).** Materials facts Grounded. Channing (msg 13): "…let’s imagine this looking almost like a rocket thruster".
  - **Contradiction (momentum).** Msg 14 says the four units produce "a relatively smooth rearward momentum flux … rather than continuous combustion or high-pressure propellant tanks". A closed loop cannot push the craft: internal circulation has zero net momentum. Thrust requires expelling mass (then the fluid **is** propellant) or pushing on an outside medium (air or water). Grok's msg 16 corrects this: "No claim of over-unity or propellant-free thrust is made; any directed momentum still comes from organized outflow of the working fluid". Taken with that correction, the design is a pulsed-jet concept that has not been tested.
- **Central hot core and cold radiating boundary in space (msgs 15–16).** Plausible-untested; this is how spacecraft thermal design works (heat sources inside, radiators outside).
- **Paramagnetic offsets, barbed/pitted surfaces, Tesla valves, drag-heat inlets (msgs 17–18).** Surface texture does pin bubble nucleation sites (Grounded). Tesla valves are real fixed-geometry diodes with modest diodicity at steady flow (Grounded). Everything about their combination is Plausible-untested. These "barbed/pitted" surfaces are bubble-nucleation texture, not the lock-pin hardware in [electrostatic_locking_pins.md](electrostatic_locking_pins.md).

## 3. Vinegar, the Baghdad jar and electroplating (msgs 19–24)

Channing (msg 21): "Hmm let’s explore an ancient battery or what appears to be its a sealed jar with copper, lead and either vinegar or whine"

Grok identifies the Baghdad (Khujut Rabu) jar and says the inner rod is iron. Channing accepts this (msg 23): "Yes, iron.. can we explore electroplating?"

**Mainstream vs contested labels:**

| Claim | Status |
|---|---|
| Ceramic jar (~13 cm) with a copper cylinder, an iron rod and bitumen/asphalt seal; from Khujut Rabu near Ctesiphon, 1936; published by W. König in 1938 | **Mainstream / Grounded** |
| A Cu/Fe pair in vinegar or wine generates a small voltage | **Grounded.** Ideal Fe/Cu²⁺ difference is 0.78 V (section B); replicas report ~0.5–0.9 V, matching Grok's "roughly 0.5–1 volt" |
| Date: Grok says "Parthian or early Sasanian (roughly 1st–3rd centuries CE)" | **Contested.** König assumed Parthian; St J. Simpson (British Museum) notes the pottery is Sasanian (224–640 CE) and the find context is poorly recorded |
| It **was** used as a battery | **Contested, minority view.** Mainstream archaeology reads it as a container for sacred scrolls (similar copper-tube jars from Seleucia held papyrus traces). P. T. Keyser, *J. Near Eastern Studies* 52 (1993) 81–98, proposed electro-analgesia: minority view. A Sino-Platonic Papers no. 377 reconstruction claims >1.4 V with a tin–air "outer cell": a minority view and not peer-reviewed in a physics journal [to verify] |
| Used for electroplating gold or silver in antiquity | **Unsupported (mainstream).** No electroplated ancient object is known; thin gilding of that period is explained by leaf, diffusion and fire (mercury-amalgam) gilding. Electroplating is a 19th-century technique (L. Brugnatelli 1805; Elkington patents 1840 [to verify]) |

Grok's own summary (msg 24) agrees: "there is no convincing evidence it was" used for plating. Scale check (section B): 1 µm of gold on 10 cm² is 19.3 mg. At 1 mA that takes ~2.6 h, and at a realistic 0.1 mA ~26 h per cell. That is possible in principle, but there is no evidence anyone did it.

Vinegar (msg 20): weak electrolyte; attacks copper in air; shifts ferrofluid surfactant stability with pH. All **Grounded**. Grok's advice to use it as a process/cleaning fluid rather than a working fluid is sensible.

## 4. Carboxyl CNT–BNNT bonding and a plasma "3D printer" (msgs 25–26)

Channing (msg 25): "Mmm sorry this kind of touches on an earlier thread when we discussed carboxyl groups and hydrogen bonding with BNNT’s and CNT’s would it be feasible for a sort of 3D printer(plasma welder).. or something hmm may need to pause here"

- COOH-functionalised CNTs bonding to BNNT surfaces in composites: Plausible-untested to Grounded [to verify a specific paper].
- Plasma deposition or welding keeping these hydrogen bonds: **Speculative**. Plasma temperatures break H-bonds and strip carboxyl groups. A cold atmospheric plasma for surface activation followed by low-temperature assembly is the more plausible route.
- The "earlier thread" on carboxyl / BNNT bonding: [Channing to supply].

## 5. Contradictions with the repo

- **Self-sustaining circulation (msg 10)** contradicts the repo's energy accounting ([ANALYSIS_2026-10-12.md](ANALYSIS_2026-10-12.md)): every loop here is dissipative.
- **Propellant-free thrust (msg 14)** contradicts momentum conservation (same issue as in [em_topological_gravity_review.md](em_topological_gravity_review.md)); Grok withdraws it in msg 16.
- **φ / 3-6-9 pitch** is Symbolic; the repo's φ-coil drives show no advantage.

## 6. Open items

- Source for the spark-bubble radius/voltage pairs and the 3.5–7.5 % efficiency range [to verify].
- The earlier "wave-gate / bubble dynamics" thread and the carboxyl/BNNT thread [Channing to supply].
- Full share URL [Channing to supply].

# Review: Poynting flux, vortex gravity ideas and MHD force balance (shares #65 and #66, 2026-10-17)

Share #66 picks up where #65 stops: its first prompt asks for the force balance, Poynting flux and restructuring that #65 offered next. The two are reviewed together.

- **Archives:**
  - §A: [grok_archive/2026-10-17_poyntings_theorem_electric_universe.md](grok_archive/2026-10-17_poyntings_theorem_electric_universe.md) (22 messages: 11 user, 11 Grok).
  - §B: [grok_archive/2026-10-17_mhd_force_balance_poynting_flux_uranates.md](grok_archive/2026-10-17_mhd_force_balance_poynting_flux_uranates.md) (8 messages: 4 user, 4 Grok).
- **Labels:** **Grounded** · **Plausible-untested** · **Speculative** · **Symbolic** (as in [REBUILD_INDEX.md](REBUILD_INDEX.md)). φ is Symbolic unless tested.
- **Sims:** no code shown in either share. Grok's offered force-balance ODE sweep was never run. The tension and pressure magnitudes were checked in [`sims/grok_claim_checks_shares_60_69.py`](../sims/grok_claim_checks_shares_60_69.py).
- **Lock pins:** none in these shares.
- **Found sources for the exploratory index.** Share #66 is a found source for the [shifting_phase_order_review.md §H9](shifting_phase_order_review.md#h9-exploratory-topic-index-channing-probably-just-exploratory) rows **Poynting flux**, **Multi-field equilibrium** and **Uranates**, and a candidate for **Lorentz force in reverse equilibrium**. The phrase "reverse equilibrium" does not occur in either share. The nearest passage is the radial balance in which J×B (magnetic pressure and tension) holds a rotating core against centrifugal force; this matches candidate (a) in §H9.
- **Already covered elsewhere (cross-links, not repeated):**
  - Early solar-system plasma spin and EU context: [em_topological_gravity_review.md L1](em_topological_gravity_review.md#l1-early-solar-system-plasma-spin-dynamics-mass-on-a-sink--gravity-well) and [L4](em_topological_gravity_review.md#l4-plasma-dynamics-around-an-em-field-the-isotropic-electrostatic-tensor-in-the-interstellar-medium).
  - Laplace resonances and solar-system chains: [three_body_living_universe_review.md §3](three_body_living_universe_review.md#3-celestial-mechanics-messages-212).
  - "Gravity behaves like a magnetic field / is EM": [cavendish_breathing_solids_review.md §9](cavendish_breathing_solids_review.md#9-gravity-grace-dipoles-dynamos-field-history-messages-89106).
  - Tokamak and Grad–Shafranov notes, reconnection: [tungsten_bismuth_core.md §7b-dyn](tungsten_bismuth_core.md).

## A. Share #65 (0e4fc6cb): Poynting's Theorem in Electric Universe

### A1. Channing's prompts (verbatim)

1. "Back to our concept of the universe the other day can we look at poyntigs theorem?"
2. "Early solar system vortex/planetary alignment concept"
3. "Strong force coupling.. in early solar system like we sort of discussed we were working up to the la grangiens"
4. "So the suns burning through space with plasma creating these cyclic, then, vortex fields once material is introduced(could the weaker hold of the strong force in a high energy state be gravity) the flow then can also create a place for a moon to reside locked in a balanced vortex(important to sustain for us, is it the same for other planets)? Can we look at vortex equations and what is happening at the tightest points"
5. "What if Gravity is the difference of strong forces weak hold and drag which also gives us time dilation..? Also, gas giants can probably produce their own moons that can eject into space as it fights through the thick atmosphere.. is this a possibility?"
6. "Can it be derived from vortex dynamic point our EM field our own dovetail"
7. "Is a vortex not curvature of spacetime"
8. "Right, ok I was just thinking of the scaled up perspective my idea of gravity as this boundary layer with angular pressure"
9. "What happens when mass accumulates, would the vortex core enlarge and become stable(given it had stable flow) the boundary layer would increase per each mass increase right?"
10. "Along with the EM field our" (cut off in the capture; rest [Channing to supply])
11. "We will continue later, we should have an investigations folder and save into that"

### A2. Claims

| Claim | Check | Label |
|---|---|---|
| Poynting's theorem −∂u/∂t = ∇·S + J·E, with u = ½(ε₀E² + B²/μ₀) and S = E×B/μ₀ (garbled in the capture) | Standard form (Poynting 1884). | **Grounded** |
| Anticyclonic vortices form in discs through the Rossby-wave instability and trap dust | Established disc physics (Lovelace et al. 1999; Li et al. 2000, *ApJ*) [to verify exact refs]. | **Grounded** |
| Alfvén's plasma cosmogony put electromagnetic processes at the centre of solar-system formation | H. Alfvén & G. Arrhenius, *Evolution of the Solar System*, NASA SP-345 (1976) (government document, link only: [NTRS 19770006016](https://ntrs.nasa.gov/citations/19770006016)). Historical; not the standard model. | **Grounded** (as history) |
| Laplace resonance of Io–Europa–Ganymede; tidal locking of the Moon | Standard. | **Grounded** |
| "Could the weaker hold of the strong force in a high energy state be gravity" / "gravity is the difference of strong forces weak hold and drag", giving time dilation | Grok answered correctly that this is **not supported**: the residual strong force saturates at nuclear range, drag is dissipative, and gravitational time dilation is geometric and measured. | **Speculative** (contradicted) |
| Gas giants make moons in circumplanetary discs; PDS 70c has a moon-forming disc | M. Benisty et al., *ApJL* 916, L2 (2021) (ALMA). | **Grounded** |
| Moons can be ejected by moon–moon scattering (runaways or recapture), not by "fighting through" the atmosphere | Scattering ejection is shown in simulations (e.g. "ploonet" papers, Sucerquia et al. 2019 *MNRAS*) [to verify]. Grok's correction of the atmosphere picture is right: drag circularises and decays orbits. | **Plausible-untested** (simulation result) |
| "A vortex is not curvature of spacetime"; a vortex's energy sources only a negligible curvature; analog-gravity draining vortices mimic horizons | Correct. Analog gravity: W. G. Unruh, *PRL* 46, 1351 (1981); rotational superradiance in a draining vortex, T. Torres et al., *Nat. Phys.* 13, 833 (2017). | **Grounded** |
| Gravity as "a boundary layer with angular pressure" at the largest scale | Grok kept this as an exploratory lens. Local angular-momentum-supported layers are real; promoting them to gravity has no model or prediction. | **Speculative** |
| Adding mass at fixed angular momentum compacts a vortex core rather than enlarging it; in dusty vortices the dust can collapse into a planetesimal | Qualitatively consistent with disc-vortex simulations; no numbers given. | **Plausible-untested** |
| Message 22: an investigations file "2026-07-27_vortex-em-boundary-layer-gravity-exploration.md" was saved | A Grok-side artefact; it is **not in this repo**. The date suggests the conversation was held in July 2026. Contents: [Channing to supply] if wanted. | open |

**Contradiction with the repo.** The repo's position is that gravity is not EM ([cavendish review §9](cavendish_breathing_solids_review.md#9-gravity-grace-dipoles-dynamos-field-history-messages-89106)). Grok's answers here agree with it.

## B. Share #66 (055440d2): MHD force balance, Poynting flux, restructuring, uranates

### B1. Channing's prompts (verbatim)

1. "Hey Resona, Can we look at the explicit force balance (centrifugal + gas pressure + magnetic pressure/tension) that sets the core radius, or examine how the Poynting flux behaves inside the magnetic boundary layer as mass is loaded? Also, investigate magnetic restructuring effects? Then, can we investigate sodium and potassium uranates?"
2. "Would heat transfer radial large scale equivalent to equator in a sink state.. gas giants, sun in source state..?? There are some potassium uranates that occur naturally though right is there a way to neutralize radiation by conversion in nature?"
3. "Just to clarify I was saying that the Sun is in source state as well as the gas giants mercury Venus earth mars in sink with and without EM fields(can we compare the differences) then, Uranus and Neptune reacting to the interference of Jupiter, Saturn, and the Suns vortex from field interactions… can we pause and pick up later?"
4. "Heat transfer isn’t different on earth day to night temperature changes? Or is that just attributed to atmosphere?"

### B2. Force balance, Poynting flux, restructuring (message 2)

| Claim | Check | Label |
|---|---|---|
| J×B = (B·∇)B/μ₀ − ∇(B²/2μ₀): tension of magnitude B²/(μ₀R_c) toward the centre of curvature, plus magnetic pressure | Standard identity. | **Grounded** |
| Radial balance of a rotating column: ρΩ²R ≃ ∂/∂R(p + B²/2μ₀) **−** B_θ²/(μ₀R) | **Sign error** (checked against the PDF, which shows "−"). From the radial momentum equation −ρΩ²R = −∂/∂R(p + B²/2μ₀) − B_θ²/(μ₀R), the correct form is **ρΩ²R = ∂/∂R(p + B²/2μ₀) + B_θ²/(μ₀R)**. The azimuthal-field tension pulls inward, on the same side as the inward pressure gradient. | **Corrected** |
| Centrifugal confinement in rotating mirrors gives large parallel density drops; rotation shifts the Grad–Shafranov axis | Established (rotating-mirror and rotating-tokamak equilibria). | **Grounded** |
| Magnetisation σ = B²/(4πγρc²) falls as mass is loaded; Poynting-dominated jets convert to kinetic flux | Gaussian-unit definition, standard in jet physics. | **Grounded** |
| Restructuring: reconnection, island coalescence, flux pumping, stochastic fields; sawtooth "core crash" | Standard. | **Grounded** |
| A "deliberately driven, low-level restructuring cycle" for controlled energy release in resonant nodes | No design or numbers. | **Speculative** |

### B3. Uranates (messages 2, 4): chemistry only

| Claim | Check | Label |
|---|---|---|
| Na₂U₂O₇ (α P2₁/a, β C2/m, γ hexagonal), K₂U₂O₇, Na₂UO₄, NaUO₃ (U(V)); uranyl O=U=O layers | Standard solid-state chemistry; the polymorphs match DFT and diffraction literature (e.g. *Phys. Chem. Chem. Phys.* 2023, [doi:10.1039/d3cp01222k](https://doi.org/10.1039/d3cp01222k)). | **Grounded** |
| Na₂U₂O₇ melts at "~1646 °C" | Commonly quoted, but the literature reports decomposition of γ-Na₂U₂O₇ near 1620 K, so a clean melting point is doubtful. [to verify] | **Plausible-untested** |
| Carnotite K₂(UO₂)₂(VO₄)₂·3H₂O, a secondary mineral of the Colorado Plateau | Standard (water content 1–3). | **Grounded** |
| Bacteria fed glycerol convert dissolved U into a persistent FeU(V)O₄ phase that survives air exposure | Mine-water study: ~95–99 % U(VI) removal over ~130 days, FeU(V)O₄ still detected after 4 weeks in oxygen (*Nat. Commun.* 2026, [doi:10.1038/s41467-026-72560-z](https://doi.org/10.1038/s41467-026-72560-z)). | **Grounded** |
| Chemistry cannot "neutralize" radioactivity; only decay (or rare natural fission, as at Oklo) changes nuclei | Correct. | **Grounded** |
| Uranates are not RGRF materials | Agreed. The repo keeps them as chemistry context only (§H9), and this review adds nothing on fuel-cycle use. | **Grounded** (scope) |

### B4. Planetary heat flow and source/sink (messages 4–8)

| Claim | Check | Label |
|---|---|---|
| Rapid rotation organises deep convection into columns, so gas-giant internal heat flux peaks at the poles with an equatorial minimum | A result of thin-shell rotating-convection models (e.g. Aurnou et al., *Icarus* 2008 [to verify]). Jupiter's and Saturn's observed emission is nearly uniform. | **Plausible-untested** (model result) |
| Sun: pure source; radiative zone then convection in the outer ~30 % | Standard (convection zone base at ~0.71 R☉). | **Grounded** |
| Jupiter, Saturn and Neptune emit more than they absorb | Standard. | **Grounded** |
| "Uranus: essentially zero detectable internal heat flux" | **Outdated.** A 2025 analysis over a full Uranian orbit finds 0.078 ± 0.018 W/m², an emitted/absorbed ratio of 1.13 ± 0.03 (X. Wang et al., *GRL* 52, e2025GL115660 (2025), [doi:10.1029/2025GL115660](https://doi.org/10.1029/2025GL115660)). It is still about ten times smaller than Neptune's. | **Corrected** |
| Magnetic fields barely change bulk thermal budgets; they shape escape, aurorae and upper-atmosphere heating (Mars vs Earth) | Standard. | **Grounded** |
| Uranus and Neptune "reacting to" Jupiter's, Saturn's and the Sun's vortex fields | Grok marked this as plasma-cosmology territory. No mechanism or data were given. | **Speculative** |
| Earth's day–night swing is moderated by atmosphere and ocean; airless bodies swing far more (the Moon ~100–390 K) | Standard (LRO Diviner). | **Grounded** |

## C. Open items

- The rest of message 19 in share #65 ("Along with the EM field our…"): [Channing to supply].
- What "Lorentz force in reverse equilibrium" meant (§H9 candidates a–c): [Channing to clarify].
- The Grok investigations file named in share #65 message 22: [Channing to supply] if it should be archived.

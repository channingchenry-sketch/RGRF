# Review: degrees of freedom and shifting phases — VO₂/vanadium, the NV centre, Fe³⁺ and magnetite

- **Request (Channing, verbatim, 2026-10-25):** "Let’s investigate the degrees of freedom and the shifting phases", then "Lets also look at Fe3". This answers H285m (the vanadium angle): **degrees of freedom and shifting phases**.
- **Builds on:** [vanadium_revisit_review.md](vanadium_revisit_review.md) (66e9566), [nv_center_spin_degrees_of_freedom_review.md](nv_center_spin_degrees_of_freedom_review.md) (30d3756) and [shifting_phase_order_review.md](shifting_phase_order_review.md).
- **Sim:** [sims/coupled_order_parameter_sim.py](../sims/coupled_order_parameter_sim.py) ([output](../sims/coupled_order_parameter_sim_output.txt)). It is a toy model and textbook illustration.
- **Labels:** **Grounded** / **Plausible-untested** / **Speculative** / **Symbolic**. License CC0.
- **Ledger rule:** phase transitions **move energy between degrees of freedom and between the system and its surroundings. They never create it.**

## 0. Channing's earlier words (archive, verbatim)

**"Shifting phase order":**
- [grok_archive/2026-10-15_exploring_miller_setterfield.md](grok_archive/2026-10-15_exploring_miller_setterfield.md) l. 129: "This is part of our foundation and we can say as much in our framework as well as shifting phase order. Now we can save and pause. We will expand later, thank you!" (also quoted in [shifting_phase_order_review.md](shifting_phase_order_review.md) l. 548).
- [grok_archive/2026-10-17_grassmann_vs_lorentz_force_laws.md](grok_archive/2026-10-17_grassmann_vs_lorentz_force_laws.md) l. 1141: "Can we explore magnetic sail dynamics? Also, shifting phase order keeps popping into my head"
- [grok_archive/2026-10-22_casimir_repulsion_discussion.md](grok_archive/2026-10-22_casimir_repulsion_discussion.md) l. 200: "Still nice to see that it matches our shifting phase order language" (Boyer π-phase repulsion; [shifting_phase_order_review.md §E](shifting_phase_order_review.md)).
- [shifting_phase_order_review.md](shifting_phase_order_review.md) l. 267: "can we explore floquet periodically driven topological phases?" (§F)
- l. 433–435: "We looked at heliums opaque features and black holes shortly after but there’s a gap in my notes" / "We went down a rabbit hole and bounced around from Pais effect in gravitoelectromagnetism in fractal spacetime to cathodoluminescence and imprinting techniques to Sonoluminescence."
- l. 505: "Not sure I can just say the chain of events it look like an extensive rabbit hole we went into pi flux pinning multi field equilibrium, poynting flux, ultrasonic waves and negentropy, Lorentz force in reverse equilibrium, uranates, Gödel Einstein Euler Lovelace memrisistors and RF bypass, micro modular reactors. It was probably just exploratory."
- l. 364: "Just a copy error it is w^2r"

**Degrees of freedom and phase shifting:**
- [grok_archive/2026-10-22_molecular_vibrations_schrodinger_dirac_wavelengths.md](grok_archive/2026-10-22_molecular_vibrations_schrodinger_dirac_wavelengths.md) l. 122: "I know we have touched on this before around the time we were discussing Plank’s constant. What came into my mind more recently was the degree of freedom can we dive deeper?" and l. 229: "…Also, can we look at what happens when the degrees of freedom grow? Then, can we look at fermi resonance?" (review: [molecular_vibration_schrodinger_dirac_review.md](molecular_vibration_schrodinger_dirac_review.md)).
- [grok_archive/2026-10-22_nist_materials_genome_initiative_insights.md](grok_archive/2026-10-22_nist_materials_genome_initiative_insights.md) l. 252–254: "Is there data for trying to separate bonds while there is a frequency match( let’s say we play waters frequency to water does this create a stronger bond or would it start phase shifting?"

**Earlier "order parameter" and "symmetry breaking" hits** (Grok text only, no Channing turns): pi-flux pinning, IT³, Casimir, Wick's theorem, altermagnets, Göbekli UV calcite.

**Fe³⁺ and iron-oxide hits** (`rg 'Fe3|ferric|magnetite|Verwey|magnetosome|Fe2O3|hematite'`). **None are Channing turns;** all are Grok text or RGRF reviews:
- Fe³⁺ colour centres in amethyst (lab-grown crystals, l. 151/296; corrected in [lab_grown_crystals_bom_review.md](lab_grown_crystals_bom_review.md)).
- "Mn²⁺ and Fe³⁺ are 3d⁵, five unpaired electrons, about 5.9 μB" and "Mn²⁺ and Fe³⁺ are the electronic clocks" (altermagnets share, l. 895/922; review [altermagnets_dna_hemp_charcoal_review.md](altermagnets_dna_hemp_charcoal_review.md)).
- Graphene-stabilised Fe₃O₄ ferrofluids (mercury/graphene share; [mercury_graphene_electrofluid_review.md](mercury_graphene_electrofluid_review.md)).
- "quantum compass + magnetite-based" hybrid models (quantum biology share, l. 193).
- Fe²⁺/Fe³⁺ in metallic fluid (prime lattice, l. 700); Fe₃O₄ nanofluid (ultrasonic share, l. 170); the Newman machine BOM (l. 377).
- No Verwey, magnetosome or hematite hits before this review.

## 1. What a degree of freedom is

- **Classical (Grounded):** each independent quadratic term in the energy holds ½k_BT (equipartition). A gas molecule has 3 translational degrees, plus 2 rotational (linear) or 3 (nonlinear), plus 2 per vibration mode, counting kinetic and potential energy.
- **Quantum (Grounded):** a mode holds ½k_BT only when k_BT ≫ ħω. Otherwise it **freezes out**. That is why H₂'s heat capacity steps from 3/2 R to 5/2 R to 7/2 R, and why Einstein and Debye solids fall to zero at low T. This is the "Planck's constant" link Channing recalled (l. 122).
- **In solids** the relevant degrees of freedom are **charge, spin, orbital, lattice (phonons), nuclear spin** and, for a whole particle, **centre-of-mass and rotation**. Ordered phases appear when interactions between these freeze them into a pattern.

## 2. Landau order parameters and symmetry breaking (Grounded)

- An **order parameter** is zero in the symmetric phase and nonzero in the broken-symmetry phase (magnetisation, dimerisation, charge order). Near T_c, F = a(T−T₀)η² + bη⁴ + cη⁶ (Landau 1937).
- **Second order** (b > 0): η grows continuously. There is no latent heat and no hysteresis; the heat-capacity jump and the susceptibility diverge.
- **First order** (an effective b < 0, stabilised by c): η jumps. There is **latent heat** L = T_cΔS, and **hysteresis** between superheating and supercooling spinodals.
- **Coupled order parameters:** a term −gη²u² lowers the effective quartic coefficient (b − g/2 on the symmetric path). **Strong enough coupling turns a continuous transition into a first-order one.** This is standard (Imry 1975; Bean–Rodbell 1962 for magnetoelastic coupling [to verify]).

## 3. VO₂ as the main example of coupled order

- **Phases:** M1 (monoclinic, V–V dimerised and tilted, insulating); R (rutile, metallic, above ~68 °C / 341 K); M2 (monoclinic, half the chains dimerised), stabilised by strain or Cr doping. **Grounded.**
- **Two coupled order parameters:** the **Peierls** lattice dimerisation (u) and **Mott–Hubbard** correlation and orbital ordering (η, the d∥ band gap). Which one drives the transition was debated for decades. Current consensus: a correlation-assisted Peierls ("Mott–Peierls") transition. Goodenough 1971; Zylbersztejn & Mott 1975; Biermann et al., PRL 94, 026404 (2005) (cluster DMFT) [to verify]. **Grounded** that both participate.
- **Ultrafast separation in time:**
  - Cavalleri et al., PRL 87, 237401 (2001): femtosecond optical switching, structural and electronic.
  - Cavalleri et al., PRB 70, 161102 (2004): an ~80 fs "structural bottleneck" tied to the 6 THz phonon.
  - Morrison et al., *Science* 346, 445 (2014): a metastable monoclinic **metal** after pumping (the electronic order melts while the lattice is still dimerised).
  - Wall et al., *Science* 362, 572 (2018): disordering of V–V dimers.
  - All [to verify the details]. **Grounded** that the electronic and lattice degrees of freedom can be separated in time.
- **Strain and doping:** W⁶⁺ lowers T_c by about 20–25 K per at. %. Epitaxial strain shifts T_c by tens of K. **Grounded.**
- **Latent heat** about 51 J/g (about 4.3 kJ/mol) [to verify]; hysteresis about 2–10 K, broader in films.

**Other vanadium phase shifts:**
- **V₂O₃:** the textbook Mott transition (McWhan et al. 1969–73). A paramagnetic metal becomes an antiferromagnetic insulator below ~150–160 K, with a large resistivity jump. Cr doping drives a paramagnetic metal-to-insulator line ending at a critical point (Limelette et al., *Science* 302, 89 (2003) [to verify]). **Grounded.**
- **Flow battery oxidation states** V²⁺ ↔ V³⁺ ↔ VO²⁺ ↔ VO₂⁺: these are **charge-degree switching** in solution, a redox "phase" (valence) shift driven electrochemically, not a thermodynamic phase transition. **Grounded** as chemistry; calling it a "phase" is a **Symbolic** use of the word.

## 4. The NV centre: degrees of freedom shifted out of equilibrium

- The degrees of freedom are electron spin, nuclear spin (¹⁴N/¹³C), the orbital/excited state, the NV⁻/NV⁰ charge state and phonons; in levitated particles also centre-of-mass and rotation ([nv_center_spin_degrees_of_freedom_review.md](nv_center_spin_degrees_of_freedom_review.md)). **Grounded.**
- **Optical pumping is non-equilibrium shifting of the spin populations.** Green light, through the intersystem crossing, drives ms = 0 to about 80–90 %, far from the thermal ≈ ⅓ each. The *photon's* energy pays for it, and the excess goes into phonons (heat) and red fluorescence. **Grounded.**
- **OIST 2026** (Nayak et al., *Sci. Adv.*, doi:10.1126/sciadv.aeh0566): the spin population (one degree of freedom) hands **momentum and energy to centre-of-mass motion** (another) through a field gradient. The magnet takes the reaction. **Grounded.** This is "one degree of freedom handing to another", and it is not a source of energy.

## 5. Fe³⁺ and magnetite (added at Channing's request "Lets also look at Fe3")

### 5a. Fe³⁺ (ferric) as a clean spin-only degree of freedom

- **Electronic structure (Grounded):** high-spin 3d⁵ (⁶S₅/₂). S = 5/2 and **L = 0**, so the orbital moment is quenched and the ion is close to "spin only" with g ≈ 2.00.
  - The saturation moment is gSμ_B = **5 μ_B**.
  - The effective (Curie) moment is g√(S(S+1))μ_B = **5.92 μ_B**. The archive's "about 5.9 μB" is this value, so it is correct.
  - EPR shows g ≈ 4.3 for rhombic Fe³⁺ and g ≈ 2 for axial Fe³⁺.
  - Because L = 0, spin–lattice relaxation is relatively weak.
- **Redox (Grounded):**
  - Fe²⁺/Fe³⁺ has E° = +0.77 V.
  - **Fenton chemistry:** Fe²⁺ + H₂O₂ → Fe³⁺ + •OH + OH⁻ (Fenton 1894; Haber–Weiss 1934). It is the source of oxidative damage and also of advanced-oxidation water treatment, which links to H₂O₂ in [living_habitat_life_support.md](living_habitat_life_support.md) and [hemp_oil_peroxide_economy_review.md](hemp_oil_peroxide_economy_review.md).
  - Biology holds iron as **Fe³⁺** in **transferrin** (transport) and **ferritin** (a store of ~4500 Fe as a ferrihydrite core), and cycles Fe²⁺/Fe³⁺ in **heme** (haemoglobin is Fe²⁺; methaemoglobin is Fe³⁺) and in cytochromes.
- **The iron–vanadium link (Grounded):**
  - **V-nitrogenase** uses the FeV cofactor in place of FeMo-co (Mo-nitrogenase: Fe₇MoS₉C). The V version makes more H₂ per N₂ and can reduce CO to hydrocarbons (Lee, Hu & Ribbe, *Science* 329, 642 (2010) [to verify]).
  - **Iron-based flow batteries:** the all-iron flow battery (Fe²⁺/Fe³⁺ positive, Fe/Fe²⁺ negative; Hruska & Savinell 1981 [to verify]; ESS Inc.) and the earlier **Fe/Cr** NASA redox battery (Thaller, NASA Lewis, 1974–) that preceded the all-vanadium cell. Iron is cheap and non-toxic but has a lower voltage (~1.2 V) and parasitic H₂ at the plating electrode. **Grounded**; a **Plausible** low-toxicity RGRF dock buffer.

### 5b. Magnetite Fe₃O₄: ferrimagnetism, the Curie point and the Verwey transition

- **Structure (Grounded):** an inverse spinel, (Fe³⁺)_A[Fe²⁺Fe³⁺]_B O₄.
  - The A (tetrahedral) Fe³⁺ moments are antiparallel to the B (octahedral) moments.
  - The Fe³⁺ moments cancel, leaving about **4 μ_B per formula unit** from Fe²⁺. This is **ferrimagnetism** (Néel 1948).
- **Curie point (Grounded):** T_C ≈ **858 K (585 °C)**. Above it the ordered moment vanishes, a continuous (second-order) magnetic phase shift. This is the physics behind thermoremanent magnetisation in rocks (palaeomagnetism).
- **Verwey transition (Grounded):** at **T_V ≈ 120–125 K** the conductivity drops by about 100× on cooling and the lattice distorts from cubic to monoclinic.
  - Verwey (1939) proposed Fe²⁺/Fe³⁺ **charge ordering** on the B sites.
  - Senn, Wright & Attfield, *Nature* 481, 173 (2012) [to verify], resolved the low-T structure as **"trimerons"**: linear Fe–Fe–Fe units in which an Fe²⁺ orbital electron is shared over three B sites. This couples **charge, orbital and lattice** order.
  - Ultrafast work shows the trimeron order melting in steps (de Jong et al., *Nat. Mater.* 12, 882 (2013) [to verify]).
  - **It parallels VO₂ directly:** a first-order transition with coupled electronic and lattice order parameters and hysteresis. **Grounded** analogy.

### 5c. Biomagnetite

- **Magnetotactic bacteria (Grounded):** chains of membrane-bound magnetite (or greigite) **magnetosomes**, about 35–120 nm. That is single-domain size, so each crystal is a permanent dipole. The chain acts as a compass needle that passively aligns the cell with Earth's field (Blakemore, *Science* 190, 377 (1975) [to verify]; Frankel; Komeili).
- **Magnetite magnetoreception in animals (Grounded that it is debated):**
  - Magnetite in fish olfactory cells and the "pigeon beak iron" hypothesis. Treiber et al., *Nature* 484, 367 (2012) [to verify] showed the pigeon-beak iron cells were **macrophages**, not receptors.
  - A magnetite-based *intensity/map* sense remains a candidate. The **cryptochrome radical pair** (Cry4) remains the leading *compass* hypothesis.
  - The hybrid "compass + magnetite map" model the archive mentioned (quantum biology share, l. 193) is **Plausible-untested**.

## 6. Other coupled degrees of freedom

- **Multiferroics and spin–lattice coupling (Grounded):**
  - BiFeO₃: ferroelectric order (T_C ≈ 1100 K) coexisting with antiferromagnetic order (T_N ≈ 640 K), with Fe³⁺ as the magnetic ion.
  - TbMnO₃: spiral magnetism *induces* ferroelectricity (Kimura et al., *Nature* 426, 55 (2003) [to verify]).
  - Magnetostriction and the magnetocaloric effect (Gd₅Si₂Ge₂, Pecharsky & Gschneidner 1997 [to verify]) are spin–lattice coupling in engineering form.
- **Einstein–de Haas and Barnett (Grounded):**
  - Einstein–de Haas (1915): flipping magnetisation rotates the body.
  - Barnett (1915): rotating a body magnetises it.
  - Both exchange angular momentum between spin and mechanical rotation; total L is conserved ([em_topological_gravity_review.md](em_topological_gravity_review.md) l. 269).
  - Ultrafast demagnetisation hands spin angular momentum to the lattice within about 200 fs (Dornes et al., *Nature* 565, 209 (2019) [to verify]).
- **Phase-locking as phase shifting in oscillator arrays (Grounded):** in the Kuramoto model, the order parameter r = |⟨e^{iθ}⟩| switches on above a critical coupling K_c = 2/(πg(0)). It is a synchronisation "phase transition" in phase space ([oscillator_ratchet_array_review.md](oscillator_ratchet_array_review.md)). Floquet driving ([shifting_phase_order_review.md §F](shifting_phase_order_review.md)) is the time-periodic version.

## 7. RGRF links (labelled)

| Link | Label |
|---|---|
| **A VO₂ skin as a phase-gated leaky boundary:** IR-transparent below ~68 °C and reflective/metallic above, i.e. a boundary whose leak rate Γ switches with temperature ([leaky_bound_state_family.md](leaky_bound_state_family.md), [vanadium_revisit_review.md](vanadium_revisit_review.md)) | **Plausible-untested** (Grounded physics; RGRF use untested) |
| **"Shifting phase order" read as order-parameter control:** which degree of freedom leads (electronic before lattice, spin before motion) is a controllable variable, as Grok framed it in the Miller–Setterfield share l. 144 | **Symbolic → Plausible** as a design vocabulary. The physics (pump-probe sequencing, Floquet driving, Kuramoto locking) is Grounded. |
| **Flux attachment as a reshuffle of degrees of freedom:** electrons plus vortices become composite fermions, and the "particle" degree of freedom is re-labelled ([flux_attachment_review.md](flux_attachment_review.md)) | **Grounded** (in the FQH); RGRF analogy **Symbolic** |
| **The Curie point as the thermal limit of Halbach and stator magnets:** NdFeB T_C ≈ 310–400 °C (583–673 K), with usable limits of about 80–200 °C depending on grade; SmCo T_C ≈ 700–800 °C; ferrite (Fe³⁺-based) ≈ 450 °C; magnetite 585 °C ([stator_review.md](stator_review.md)) | **Grounded**; design limit |
| **Iron and ferrite cores in the stator:** Fe–Si laminations (B_sat ≈ 2.0 T), V-Fe-Co (2.4 T), MnZn/NiZn ferrites (Fe³⁺-rich, low eddy loss at high frequency) | **Grounded** |
| **NV magnetometry imaging magnetosomes:** Le Sage et al., "Optical magnetic imaging of living cells", *Nature* 496, 486 (2013) [to verify], mapped magnetite chains in magnetotactic bacteria with an NV wide-field microscope | **Grounded**, and a real tool for a bench study of biomagnetite |
| **Water "frequency match" and phase shifting** (Channing, NIST share l. 252–254): resonant driving of a mode pumps energy into that degree of freedom; it does not form new ordered phases at audio frequencies ([nist_materials_genome_review.md](nist_materials_genome_review.md)) | **Grounded** caution |
| Colour, octave or "harmonic" reasons for any transition | **Symbolic** |

## 8. Sim results (toy model / textbook illustration)

`sims/coupled_order_parameter_sim.py`. F = a(T−T₀)(η² + u²) + b(η⁴ + u⁴) − gη²u² + c(η⁶ + u⁶), with a = b = 1, c = 0.5 and T₀ = 62 °C.

**(1) Coupling sweep:**

| g | Transition | Heating loses order at | Cooling regains at | Hysteresis |
|---|---|---|---|---|
| 1, 2 | second order | 62.0 °C | 62.0 °C | none |
| 5 | first order | 63.5 °C | 62.0 °C | 1.5 K |
| 8 | first order (VO₂-like) | **68.0 °C** | **62.0 °C** | **6.0 K** |

For g = 8 the equilibrium T_c is 66.5 °C.

**(3) Energy ledger, g = 8 closed cycle:**
- Heat in on heating = 3678.59 model units; heat out on cooling = 3678.59; net 0.000, which equals ΔU over the cycle. The first law closes and no work is extracted.
- **Entropy produced is 0.119 per cycle (> 0)**. The hysteresis loss (~40 model units of T·S_prod) is energy degraded to heat, never created.
- At VO₂ scale (L ≈ 51 J/g [to verify]), even an ideal 62/68 °C engine is limited by Carnot to 1.76 %, i.e. **< 0.90 J/g per cycle**.

**(2) Toy pump:** the electronic order η halves at **≈ 9 fs** and the lattice dimerisation u at **≈ 680 fs** (toy relaxation rates). The point is the order of events: electronic before lattice, as in the VO₂ and magnetite pump-probe experiments.

**(4) Fe³⁺ Brillouin S = 5/2:** M_sat = 5 μ_B and μ_eff = 5.92 μ_B. M/M_sat = **0.0052 at 1 T, 300 K** and **0.626 at 1 T, 2 K**. A paramagnet needs low T or high B to polarise, which is the same physics as the NV thermal moment at OIST.

**(5) Verwey toy:** a resistivity jump of about 200× across 123 K (real Fe₃O₄ ≈ 100× [to verify]).

**(6) Curie point:** a mean-field M(T) collapses at 858 K (magnetite), with the NdFeB Curie point (~583 K) marked.

Plot: `/workspace/dof_phases_plot.png` (6 panels), kept on the box and not committed.

## 9. [to verify] and an open question

- **Citations:**
  - Cavalleri 2001/2004; Morrison 2014; Wall 2018; Biermann 2005; Limelette 2003
  - Senn 2012; de Jong 2013; Le Sage 2013; Treiber 2012; Blakemore 1975
  - Lee–Hu–Ribbe 2010; Hruska–Savinell 1981; Kimura 2003; Pecharsky–Gschneidner 1997; Dornes 2019; Bean–Rodbell 1962
- **Numbers:** VO₂ latent heat (~51 J/g); the Verwey resistivity ratio; NdFeB grade-dependent Curie points.
- **Open question for Channing:** when "shifting phase order" pops into your head, is it closer to (a) **which degree of freedom leads in time** (electrons before lattice, spin before motion, as in VO₂, magnetite and OIST), or (b) **the phase relationship between coupled oscillators** (Kuramoto/Floquet locking in the Multi-Egg or magnetic-sail drives)? Or is it something else?

- **See also: shifting phase order = the phase relationship between coupled oscillators** (Channing's definition, 2026-10-25): [shifting_phase_order_coupled_oscillators.md](shifting_phase_order_coupled_oscillators.md).

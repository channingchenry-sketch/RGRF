# Tesla, Leonardo da Vinci and the Vitruvian Man: RGRF threads (2026-10-15)
*CC0 1.0. Labels: **Grounded** / **Plausible-untested** / **Speculative** / **Symbolic**. Citations checked by web search on 2026-10-15; unverified items are flagged.*

> Channing (verbatim, 2026-10-15): "We also explore Nikola Tesla and Leonardo Da Vinci at this time."
>
> Channing (verbatim, 2026-10-15): "We explored pretty much everything that wasn’t off limits."
>
> Channing (verbatim, 2026-10-15): "Took a turn at the Vetruvian man to go into concept of male and female energy and expanded consciousness."

"At this time" refers to the early phase described in [method_phi_and_natural_craft.md](method_phi_and_natural_craft.md): nature, sacred geometry, and Earth and the Sun as natural "craft". The same method applies here. Inspiration is **Symbolic**; specific claims are tested and labeled. The specific Tesla and Da Vinci threads, and any Grok text from them, are **[Channing to supply]**.

## 1. Nikola Tesla
The detailed history and claims table are in [tesla_and_ancient_alignments.md](tesla_and_ancient_alignments.md). Summary:

**Grounded**
- **Rotating magnetic field / AC induction motor.** US 381,968 "Electro-Magnetic Motor" and US 382,280 "Electrical Transmission of Power", both issued 1 May 1888. Polyphase currents produce a "progressive shifting" of the poles, which is the basis of every induction motor.
- **Resonant transformer (Tesla coil).** First patent: US 454,622 "System of Electric Lighting", 23 June 1891. It describes a capacitor and spark-gap primary driving a high-frequency, high-potential secondary. RGRF already uses Tesla coils (and Tesla valves, a separate invention) in [helium_water_circulation.md §9](helium_water_circulation.md).
- **Colorado Springs, 1899.** Large magnifying-transmitter experiments. Tesla's diary (published as *Colorado Springs Notes, 1899–1900*) records that, as a storm receded in July 1899, the disturbances it caused faded and returned periodically. He read this as **stationary waves in the Earth**. The lab was razed in 1904.
- **Wardenclyffe, Shoreham NY.** Built 1901–02. Funding ended and the plant never operated as intended; the tower was demolished in 1917.

**Speculative / unproven: global wireless power.** There is no documented measurement of useful power received at a distance. Why it fails:
1. **Losses.** Ground-wave and earth-return losses, and the energy spreads over the globe, so received power density is tiny.
2. **The Schumann cavity is low-Q.** The fundamental (~7.8 Hz) has Q ≈ 4–5. The Earth–ionosphere cavity is strongly damped, cannot store or bank much energy, and a ~38,000–40,000 km wavelength needs planetary-scale antennas. See [tungsten_bismuth_core §7b-alfven.1](tungsten_bismuth_core.md#7b-alfven1-schumann-resonance-as-a-coupling-guide).
- **The grounded descendant** is resonant inductive coupling: Kurs et al., "Wireless Power Transfer via Strongly Coupled Magnetic Resonances," *Science* 317, 83–86 (2007). That MIT work (60 W at ~40 % over ~2 m) led to WiTricity. It is near-field only: a few coil diameters, not global. See the Nordic and metasurface WPT material in [em_topo L6](em_topological_gravity_review.md#l6-wireless-energy-transfer-northern-europe-focus-noted).

### 1a. Mechanical oscillator ("earthquake machine")
> Channing (verbatim, 2026-10-15): "We can reference something that was noted which is a resonant device that made a building shake…" [trimmed]

- **The patent: Grounded.** N. Tesla, "Reciprocating Engine," US 514,169 (filed 19 Aug 1893, granted 6 Feb 1894). A steam- or gas-driven piston coupled to an air spring, arranged so that the restoring force is proportional to displacement, giving an **isochronous oscillation** whose period is set by the spring stiffness and moving mass. It was intended as a constant-frequency driver for generators.
- **The Houston Street building-shaking story: Unverified anecdote / Speculative.** The main source is Tesla's own account at his July 1935 birthday press interview (e.g. *New York World-Telegram*, 11 July 1935, reporter Earl Sparling), decades after the event. There he dates it to 1887 or 1888. Later retellings give 1896 or ~1898, and an earlier magazine retelling (~1912) is also cited. No contemporary police or press record has been identified. The dates and details vary between versions.
- **MythBusters, Episode 60 "Earthquake Machine" (aired 30 Aug 2006).** Tuned oscillators on metal bars and on a truss bridge produced **vibrations felt ~100 ft away, but nothing like an earthquake**. The myth was rated "busted". Small drivers can excite a structure's mode, but damping caps the amplitude well short of the dramatic version.

**Grounded resonance physics**
- **Driven damped oscillator:** m ẍ + c ẋ + k x = F₀ cos ωt. Steady amplitude X = (F₀/k) / √[(1 − r²)² + (2ζr)²], with r = ω/ω₀, ω₀ = √(k/m) and damping ratio ζ = c / (2√(km)).
- **Q factor:** Q ≈ 1/(2ζ). At resonance the amplitude is ~Q × the static deflection, and the build-up takes ~Q cycles. Real buildings have ζ of a few percent (Q ~ 10–50), so a small driver produces small motions. Energy input per cycle must exceed damping losses, and a tiny oscillator's power is far below what a large structure dissipates.
- **Millennium Bridge, London (June 2000).** Lateral sway came from **synchronous lateral excitation**: walkers fell into step with the sway, which fed it (a feedback loop, not a fixed external tone). It was fixed with viscous dampers and tuned mass dampers. P. Dallard et al., "The London Millennium Footbridge," *The Structural Engineer* 79(22), 17–33 (2001).
- **Tacoma Narrows (1940).** The collapse was **not** simple forced resonance or vortex-shedding resonance. It was aeroelastic **flutter**: torsional self-excitation ("negative damping") in which wind forces were coupled to the deck's own motion. K. Y. R. Billah & R. H. Scanlan, "Resonance, Tacoma Narrows bridge failure, and undergraduate physics textbooks," *Am. J. Phys.* 59(2), 118–124 (1991), doi:10.1119/1.16590.

**Stated design lesson.**
> Channing (verbatim, 2026-10-15): "Yes, and the lesson was to ensure dampening in our craft design."

**Design rule (R-damp): damping is required, in both the craft structure and the field drive.** Every structural mode and every driven field or plasma loop must have an identified damping path. It can be passive (viscous, tuned-mass, piezo shunt, helium gas spring) or active (feedback). Its damping ratio must be stated in the design ledger. No drive frequency may sit on an undamped mode. The damping hardware and loop are in [piezo_helium_feedback_loop.md](piezo_helium_feedback_loop.md). The rule is Grounded engineering practice; how well it works for RGRF's field and sheath loops is Plausible-untested.

**RGRF tie: Plausible-untested.** The design lesson is **resonance avoidance and damping**, in the craft's structure and in its field drive:
- keep the drive frequencies away from structural modes;
- add damping (viscous, tuned-mass, piezo shunt; cf. [piezo_helium_feedback_loop.md](piezo_helium_feedback_loop.md));
- watch for **self-excitation**, where a flow or plasma couples to the structure's own motion (the Tacoma lesson);
- spread or hop the drive spectrum so that no single mode is pumped ([§3e.1](#3e1-plasma-particle-tracing-and-bluetooth-packet-transmission-reference-dynamics), our extrapolation);
- if a low-frequency timing reference such as Schumann/IAR is used ([tungsten_bismuth_core §7b-alfven.1](tungsten_bismuth_core.md#7b-alfven1-schumann-resonance-as-a-coupling-guide)), check it against the structure's modal table.

## 2. Leonardo da Vinci
**Grounded**
- **Water, vortices and "turbulence."**
  - The **Codex Leicester** (c. 1504–1510) is a notebook on water, vortex motion and erosion.
  - The late **Deluge drawings** (c. 1517–18, Royal Collection, Windsor) show cascading, nested vortices.
  - Review: I. Marusic & S. Broomhall, "Leonardo da Vinci and Fluid Mechanics," *Annu. Rev. Fluid Mech.* 53, 1–25 (2021), doi:10.1146/annurev-fluid-022620-122816. It credits him with ideas suggestive of the no-slip condition, the hydraulic jump, cardiovascular vortices, volume conservation and "Leonardo's paradox" (the zig-zag path of rising bubbles). It also notes that "turbulence" has several meanings in his notes, and that his reasoning by analogy did not always reach modern conclusions.
  - RGRF link: the vortex and circulation threads ([recent_fluid_dynamics_2024_2026.md](recent_fluid_dynamics_2024_2026.md), [acoustic_streaming_and_centrifugal.md](acoustic_streaming_and_centrifugal.md)).
- **Codex on the Flight of Birds** (c. 1505; Biblioteca Reale, Turin, Ms. Varia 95). It treats the wing as a wedge, the tail as a rudder, and balance by the laws of equilibrium, along with air resistance and wind. This is a bio-inspired design method, as in the Manta-Butterfly form ([manta_butterfly_craft.md](manta_butterfly_craft.md)).
- **Polyhedra for Pacioli's *De Divina Proportione*** (written 1498, printed Venice 1509). Leonardo drew about 60 illustrations of regular and semiregular solids, including "skeletal" solids that show front and back at once. The book's title refers to the golden ratio. Leonardo's role was illustrating it, which is the main source of the "Leonardo used φ" claim (§3).

## 3. The Vitruvian Man
- **Grounded.** Leonardo's drawing (c. 1490, Gallerie dell'Accademia, Venice) illustrates Vitruvius, *De Architectura* **Book III**: a well-formed human body, standing with limbs outstretched, fits both a **circle** centred on the navel and a **square**. Leonardo doubled the limbs to fit both and offset the square's centre (the groin) from the circle's (the navel). The text on the sheet is from Vitruvius, whose proportions are simple ratios of body parts.
- **The φ claim is overstated.** The drawing is not constructed on the golden ratio. G. Markowsky, "Misconceptions about the golden ratio," *College Math. J.* 23(1), 2–19 (1992), doi:10.1080/07468342.1992.11973428, finds no credible evidence that Leonardo used φ in works outside Pacioli's book. Golden-rectangle overlays on his work are arbitrary. Pacioli himself advocated a Vitruvian system of simple proportions for art (Markowsky, citing Fischler). See also [method_phi_and_natural_craft.md](method_phi_and_natural_craft.md).
- **Male and female energy; expanded consciousness: Symbolic.** Many traditions describe complementary polarities that balance and generate: yin–yang in Chinese thought, Shiva–Shakti (consciousness and energy) in Hindu Tantra, the paired *nadis* of yoga. The Vitruvian figure, a body joining the circle (often read as heaven or spirit) and the square (earth or matter), is a natural image for that balance. These are respected contemplative frameworks, kept here as inspiration, not physics. Consciousness research is in [consciousness_fields.md](consciousness_fields.md).

### 3a. How male/female energy mapped to design
> Channing (verbatim, 2026-10-15): "Charge-balance concepts and expansion"

The **male/female framing stays Symbolic**. The physics it points to is real.

**Grounded hooks**
- **Quasi-neutrality.** A plasma keeps positive and negative charge densities nearly equal (n_e ≈ Σ Z n_i) on scales larger than the Debye length λ_D = √(ε₀ k T_e / n_e e²). Small charge imbalances create large restoring fields. This is the physical meaning of "charge balance", and it is why astrophysical bodies are close to neutral (see [em_topo](em_topological_gravity_review.md), opening section). Standard plasma textbooks (e.g. F. F. Chen, *Introduction to Plasma Physics and Controlled Fusion*).
- **Ambipolar diffusion and expansion.** Electrons are lighter and faster than ions and try to escape first. That builds an **ambipolar electric field** that slows the electrons and pulls the ions, so the two species **expand together**. The ambipolar diffusion coefficient is D_a ≈ D_i(1 + T_e/T_i) (textbook result). An expanding plasma plume or the solar wind works this way, with the balanced pair moving outward as one.
- **Double layers and charge separation.** Where balance breaks locally, a **double layer** forms: two adjacent sheets of opposite space charge with a potential jump that accelerates particles. Review: L. P. Block, "A double layer review," *Astrophys. Space Sci.* 55, 59–83 (1978), doi:10.1007/BF00642580, which includes auroral-zone double layers. In an **expanding** helicon plasma, a current-free double layer forms on its own at the expansion "neck" and accelerates ions outward: C. Charles & R. Boswell, *Appl. Phys. Lett.* 82, 1356–1358 (2003), doi:10.1063/1.1557319. This is the clearest grounded case of "charge balance + expansion → directed flow".
- **Existing RGRF sections:**
  - cation / charge separation: [em_topo R7](em_topological_gravity_review.md#r7-cation--charge-separation);
  - re-entry charge storage and sheath charging: [manta_butterfly_craft.md](manta_butterfly_craft.md#re-entry-energy-harvesting-and-charge-storage-overall-plausible-untested);
  - the on-demand sheath: [tungsten_bismuth_core §7b-reentry](tungsten_bismuth_core.md#7b-reentry-re-entry-as-a-control-method-that-we-create-2026-10-15);
  - anode double layers on the bench: [dusty_plasma_bench.md](dusty_plasma_bench.md).
- **RGRF use (Plausible-untested):** design for quasi-neutral, ambipolar expansion, for example a sheath or plume that is seeded, then allowed to expand with a controlled double layer. The [dusty plasma bench](dusty_plasma_bench.md) anode double layer is the testbed.

**Role mapping.** Asked whether male/female mapped to charges or species, Channing replied (verbatim, 2026-10-15): "Yes we also compared it to electromagnetism". The "Yes" confirms a charge mapping. Asked which role went to which, Channing replied (verbatim, 2026-10-15): "Yeah, it was about wavelength interactions. Then in plasma dynamics positive and negative charge. Then we got into lensing" and "And faradays work".
So the male/female pair mapped, in order, to:
1. **wavelength interactions**: E and B in waves (§3b, §3c);
2. **positive and negative charge** in plasma dynamics (this section);
3. **lensing** (§3c);
4. **Faraday's work** (§3d).

The mapping stays **Symbolic**. The physics each step points to is labeled in its own subsection.

**Speculative, separate from the physics above.** Ambipolar expansion, where opposite charges move outward together and stay balanced, can be read as a *metaphor* for "expanded consciousness" arising from balanced complementary energies. Nothing in plasma physics supports a physical link between the two.

### 3b. Electric/magnetic as a complementary pair
> Channing (verbatim, 2026-10-15): "Yes we also compared it to electromagnetism"

Reading E and B as a male/female pair is **Symbolic**. The physics of E and B as two aspects of one thing is **Grounded** (standard electrodynamics, e.g. J. D. Jackson, *Classical Electrodynamics*, 3rd ed., chs. 6, 7, 11):
- **One field, two faces.** E and B are the components of a single antisymmetric field tensor F_μν (E_i = F_{i0} in one common convention, B_i from the space–space components). Under a Lorentz boost they **mix**: a pure electric field in one frame has a magnetic part in another (E′_∥ = E_∥, E′_⊥ = γ(E + v×B)_⊥, B′_⊥ = γ(B − v×E/c²)_⊥). Neither is fundamental on its own.
- **Each regenerates the other.** Faraday's law, ∇×E = −∂B/∂t, and the Ampère–Maxwell law, ∇×B = μ₀J + μ₀ε₀∂E/∂t, mean that a changing B makes E and a changing E makes B. In a vacuum, this mutual regeneration *is* the electromagnetic wave. In a vacuum plane wave E and B are **in phase**, perpendicular to each other and to the propagation direction, with |E| = c|B|.
- **Equal shares of energy.** The energy density u = ½(ε₀E² + B²/μ₀). In a vacuum wave the electric and magnetic halves are equal: ε₀E²/2 = B²/(2μ₀). Neither partner carries more.
- **Duality symmetry.** Source-free Maxwell equations are unchanged under E → cB, cB → −E, and more generally under continuous rotations between E and cB. With sources the symmetry is broken, because there are electric charges but no magnetic ones. Restoring it exactly would need **magnetic monopoles**. P. A. M. Dirac, "Quantised singularities in the electromagnetic field," *Proc. R. Soc. Lond. A* 133, 60–72 (1931), doi:10.1098/rspa.1931.0130, showed that one monopole anywhere would explain why electric charge is quantised. No monopole has been observed, so exact E–B duality in nature is **Speculative**. (Emergent "monopole" quasiparticles in spin ice are a condensed-matter analog, not free monopoles; not cited here.)
- **RGRF links.** The colour-coded EM and geometry map ([em_geometry_map.md](em_geometry_map.md)) uses E/B-style pairings symbolically. The Electric Universe and EM-topological gravity review ([em_topological_gravity_review.md](em_topological_gravity_review.md)) covers where EM physics is real and where claims overreach. Charge balance and expansion (§3a) is the electric side. Fields, Alfvén waves and induction ([tungsten_bismuth_core §7b-alfven](tungsten_bismuth_core.md)) are the magnetic and coupled side.

### 3c. Wavelength interactions and lensing
> Channing (verbatim, 2026-10-15): "Yeah, it was about wavelength interactions. Then in plasma dynamics positive and negative charge. Then we got into lensing"

**Grounded**
- **Superposition and interference.** Maxwell's equations are linear in vacuum, so waves add. Equal-frequency waves interfere: constructively where in phase, destructively where in antiphase. This gives standing waves, beats and diffraction. The same rule underlies the drive superposition in the §7b-dyn.2 toy sims.
- **Plasma frequency and cutoff.** An unmagnetised plasma has refractive index n = √(1 − ω_p²/ω²), with ω_p = √(n_e e²/ε₀ m_e), or f_pe ≈ 8.98 √(n_e [m⁻³]) Hz. Waves **below ω_p are reflected** (evanescent). Waves above it pass, with phase speed > c and group speed < c. This is why the ionosphere reflects shortwave radio, and why re-entry blackout happens when the sheath's f_pe exceeds the link frequency ([tungsten_bismuth_core §7b-reentry](tungsten_bismuth_core.md#7b-reentry-re-entry-as-a-control-method-that-we-create-2026-10-15); numbers in [shifting_phase_order_review.md](shifting_phase_order_review.md)).
- **Plasma lensing.** Because n < 1 and depends on n_e, a plasma cloud refracts radio waves. An over-dense blob acts as a **diverging** lens, and the bending scales as λ².
  - A. W. Clegg, A. L. Fey & T. J. W. Lazio, "The Gaussian plasma lens in astrophysics: refraction," *ApJ* 496, 253–266 (1998), doi:10.1086/305344. They model interstellar "extreme scattering events": caustics, multiple images and position wander.
  - FRB lensing: J. M. Cordes et al., "Lensing of fast radio bursts by plasma structures in host galaxies," *ApJ* 842, 35 (2017), doi:10.3847/1538-4357/aa74da. Caustics can magnify bursts up to ~10² with narrow spectral peaks.
  - Pulsar scintillation and scattering are the same physics on smaller scales.
- **Gravitational lensing (a different mechanism).** Mass curves spacetime and bends all wavelengths equally (achromatic). Dyson, Eddington & Davidson, *Phil. Trans. R. Soc. A* 220, 291–333 (1920), doi:10.1098/rsta.1920.0009, measured the 1919 eclipse deflection consistent with GR's 1.75″ at the solar limb, against 0.87″ for the "Newtonian" value. Einstein rings and arcs are now routine in HST and JWST imaging, and weak lensing maps dark matter (see em_topo).
- **Engineered EM lensing (analogs).** Gradient-index (GRIN) lenses and Luneburg lenses bend waves with a graded refractive index. Metamaterials go further, to artificial magnetism and negative index: D. R. Smith, J. B. Pendry & M. C. K. Wiltshire, "Metamaterials and negative refractive index," *Science* 305, 788–792 (2004), doi:10.1126/science.1096796. A plasma with a shaped n_e profile is a tunable GRIN medium.

**Sheath or gravitational lensing?** Channing (verbatim, 2026-10-15): "Both our craft design relies on it own EM field creation which is why the buoyant stability was what we were trying to achieve versus actual levitation". So "lensing" covers **both**:
- the self-generated EM sheath, which is plasma lensing (Grounded physics; craft use Plausible-untested);
- the gravity-side lensing comparison (Grounded as gravitational lensing; any EM version Speculative, see below).

The design goal was stability on a buoyant body, not levitation. See [lift_and_equilibrium_systems.md §1a](lift_and_equilibrium_systems.md#1a-design-intent-buoyant-stability-not-levitation).

**RGRF use: Plausible-untested.** Treat the on-demand sheath as a **tunable plasma lens or window**. Shaping n_e (via the magnetic field, seeding and ambipolar expansion, §3a) would steer, focus or open radio links, i.e. blackout control. This is consistent with the magnetic-window studies cited in §7b-reentry. Power and shaping precision are unknown.

**Speculative.** "Gravity-like" lensing from EM fields. Plasma lensing is chromatic (∝ λ²) and needs free electrons. Gravitational lensing is achromatic and needs mass-energy. The electromagnetic field's own energy does gravitate, but by an immeasurably small amount at lab scales. EM cannot mimic gravitational lensing (see the em_topo "tiny gravity" review).

### 3d. Faraday's work
> Channing (verbatim, 2026-10-15): "And faradays work"

**Grounded**
- **Electromagnetic induction (1831).** A changing magnetic flux induces an EMF, ℰ = −dΦ_B/dt. M. Faraday, "Experimental researches in electricity" (First Series), *Phil. Trans. R. Soc.* 122, 125–162 (1832), doi:10.1098/rstl.1832.0006. This is the basis of every generator, transformer and induction coil in RGRF (Tesla coil §1, the induction equation in §7b-dyn).
- **The Faraday effect (1845).** A magnetic field along the beam rotates the plane of polarised light in a medium (Faraday used heavy lead-borate glass), by β = V B d, where V is the Verdet constant. This was the **first demonstrated link between light and magnetism**. M. Faraday, "Experimental researches in electricity, Nineteenth Series: On the magnetization of light and the illumination of magnetic lines of force," *Phil. Trans. R. Soc.* 136, 1–20 (1846), doi:10.1098/rstl.1846.0001. Faraday wrote that it established "a true, direct relation and dependence between light and the magnetic and electric forces".
- **Faraday rotation maps cosmic magnetic fields.** In a magnetised plasma the polarisation angle rotates by Δχ = RM λ², with RM ≈ 0.812 ∫ n_e B_∥ dl rad m⁻² (n_e in cm⁻³, B in μG, l in pc). Radio surveys use RMs to measure galactic, cluster and filament fields. For cosmic-web filaments, E. Carretti et al., "Magnetic field strength in cosmic web filaments," *MNRAS* 512, 945–959 (2022), doi:10.1093/mnras/stac384, used LOFAR RMs to infer B ≈ 32 ± 3 nG per filament. This agrees with the synchrotron-stacking result of Vernstrom et al. (2021) already cited in [em_topo L5b](em_topological_gravity_review.md#l5b-filament-riding-casimir-resonance-chamber--quartz-tuning-grok-excerpt-recovered-2026-10-15). (Vernstrom 2021 itself uses synchrotron and X-ray stacking, not Faraday rotation.)
- **Field lines.** Faraday's "lines of force" picture, which Maxwell later made mathematical, is the field-line language used throughout RGRF (magnetic arcs, flux ropes, Alfvén waves travelling along field lines in §7b-alfven).
- **The Faraday cage (1836).** A closed conductor screens its interior from external static fields, because charges rearrange on the surface. It screens time-varying fields when the openings are much smaller than the wavelength and the skin depth is small. This is the grounded basis of shielding and of the "leaky boundary" ideas (cf. the [Franklin lightning rod](franklin_lightning_rod.md)).
- **The homopolar (Faraday) disk (1831).** A conducting disk spinning in an axial field gives a steady DC EMF, ℰ = ½ B ω R², between axis and rim: the first electric generator. The same motional-EMF physics (v × B) drives Alfvén-wing and electrodynamic-tether coupling (§7b-alfven) and the Tesla-patent-era motors (§1).

#### 3d.1 Ulexite and the Faraday effect (2026-10-15)
> Channing (verbatim, 2026-10-15): "On another note something we started looking into was ulexite and faraday can we explore"
>
> Channing (verbatim): "Yeah exactly the idea, full rotation? Or unstudied?"

**The idea.** Faraday (magneto-optical) rotation of polarised light travelling along ulexite's natural optical fibres ("TV rock"), with the magnetic field along the fibres.

**Is there a measurement? Not that I found.**
- I found no published Verdet constant or magneto-optical measurement for ulexite, and none for other hydrated borate minerals.
- Measurements do exist for borate **glasses**:
  - "Faraday rotation in glasses," *J. Chem. Phys.* 41, 3289 (1964) (author believed to be N. F. Borrelli, **[to verify]**). It measured optical, diamagnetic and rare-earth glasses; Pr³⁺/Dy³⁺ silicate and borate glasses had the largest V.
  - Tb³⁺-rich borate glasses: F. Suzuki, F. Sato, H. Oshita, S. Yao, Y. Nakatsuka & K. Tanaka, "Large Faraday effect of borate glasses with high Tb³⁺ content prepared by containerless processing," *Opt. Mater.* 76, 174–177 (2018), doi:10.1016/j.optmat.2017.12.031. **V = 172–234 rad/(T·m) at 633 nm** for 45–60 mol% Tb₂O₃, against 134 rad/(T·m) for the TGG crystal.
  - A follow-up in *J. Am. Ceram. Soc.* (doi:10.1111/jace.20065; authors **[to verify]**) reports **−229 rad/(T·m)** for 58Tb₂O₃–42B₂O₃.
- **Answer to "full rotation? Or unstudied?":** the Faraday effect in ulexite appears **unstudied**. Full rotation is **not expected** at practical lab fields (see the estimate).
- Historical note: Faraday's own 1845 discovery used his heavy **lead borate** glass (see §3d), so borates and the Faraday effect share an origin story.

**Ulexite facts (Grounded).**
- **Composition and optics:** NaCaB₅O₆(OH)₆·5H₂O. Triclinic, biaxial (+), with n_α ≈ 1.491–1.496, n_β ≈ 1.504–1.506, n_γ ≈ 1.519–1.520 and birefringence ≈ 0.028–0.030 (Mindat).
- **Fibre optics:**
  - G. S. Baur, W. N. Larsen & L. B. Sand, "Image projection by fibrous minerals," *Am. Mineral.* 42, 697 (1957). They found that transverse sections project an image from face to face by reflections along twinned fibre interfaces. Fibre cross-sections are 0.06–0.75 mm², and twin widths 5–60 µm.
  - E. J. Weichel-Moore & R. J. Potter, "Fibre optical properties of ulexite," *Nature* 200, 1163–1165 (1963), doi:10.1038/2001163b0, explained it as core and cladding. The core is crystals aligned along c (n_γ ≈ 1.529 per Ghose et al.). The cladding comes from crystals randomly oriented about the fibre axis, giving an index difference of 0 to 0.038.
  - S. Ghose et al., "Ulexite, NaCaB₅O₆(OH)₆·5H₂O: structure refinement, polyanion configuration, hydrogen bonding, and fiber optics," *Am. Mineral.* 63, 160–171 (1978). SEM and X-ray work confirms the random orientation about the fibre axis and ~0.5 µm gaps between crystals.
  - **Correction:** the "Weichman et al. 1999 *Am J Phys*" reference was **not found**. The paper that matches the description is Weichel-Moore & Potter 1963 (*Nature*). There is also a teaching note: V. E. Henrich, "Fiber optic imaging: Nature beat us to it," *Phys. Teach.* 56, 128 (2018).

**Estimate: θ = V·B·L (computed).**
- **Diamagnetic V.** The proposed 0.01–0.02 min/(G·cm) converts to **2.9–5.8 rad/(T·m)**, since 1 min/(G·cm) = 290.9 rad/(T·m). That matches common diamagnetic glasses (fused silica ≈ 3.7 rad/(T·m) at 633 nm). Ulexite (n ≈ 1.5, hydrated borate) is plausibly in this range. That is an **analogy, not a measurement**.

| V (rad/T·m) | L | B = 0.5 T | B = 1 T |
|---|---|---|---|
| 2.9 | 2 cm | 1.7° | 3.3° |
| 2.9 | 5 cm | 4.2° | 8.3° |
| 3.7 | 2 cm | 2.1° | 4.2° |
| 3.7 | 5 cm | 5.3° | 10.6° |
| 5.8 | 2 cm | 3.3° | 6.6° |
| 5.8 | 5 cm | 8.3° | 16.6° |
| 234 (Tb-borate glass) | 2 cm | 134° | 268° |

- **Field needed (V = 3.7 rad/(T·m)):**
  - 45° (isolator): **10.6 T** at 2 cm, **4.2 T** at 5 cm.
  - Full 360°: **85 T** at 2 cm, **34 T** at 5 cm.
  - Full rotation in diamagnetic ulexite would therefore need pulsed-magnet or very long-path conditions.
- **Tb-borate glass (V = 234 rad/(T·m)):** 45° takes 0.17 T at 2 cm, and 360° takes **1.34 T** at 2 cm or 0.54 T at 5 cm. Full rotation is practical only with a rare-earth material.

**Key obstacle: polarisation scrambling (Grounded optics).**
- **Linear birefringence quenches Faraday rotation.** Along the fibre, each crystal has an in-plane birefringence of order Δn ~ 0.01–0.03. Over 2 cm at 633 nm that is a retardance of δ = 2πΔnL/λ ≈ **2,000–5,600 rad**, against a Faraday ρ ≈ 0.07 rad at 1 T. When δ ≫ ρ, the Faraday effect only slightly ellipticises the linear eigenmodes. The net azimuth rotation is of order ρ/δ (~10⁻⁵ rad) rather than ρ. This is the same problem that limits fibre-optic current sensors.
- **Random fibre orientation and many total-internal-reflection bounces** (the cladding *is* randomly oriented crystal) depolarise the output of a bundle. In the textbook sense, the "TV rock" image arrives largely depolarised. A bundle measurement may show no clean rotation at all.
- **Ulexite is soft and hydrated:** it dehydrates on heating and is water-soluble, so polishing and thermal control matter.

**Possible tests (Plausible-untested).**
1. **Polarimeter in a magnet.**
   - Setup: a 633 nm laser → polariser → ulexite slab (2–5 cm) inside a solenoid or between pole pieces → analyser (or a balanced polarimeter with a Wollaston prism) → photodiodes. Use an AC field (10–50 mT, ~100 Hz–1 kHz) and lock-in detection. Published lock-in Faraday setups resolve ~µrad.
   - Measure **along the fibres vs across the fibres**, and first measure the degree of polarisation transmitted with B = 0.
   - References: fused silica or BK7 and a water cell, for a known V.
   - Prediction: bundle measurements are quenched or depolarised, giving rotation ≪ VBL. A clear single crystal cut and aligned so that one of its two optic axes lies along the beam (biaxial) should give V of ~3–5 rad/(T·m). That would be a genuinely new (if modest) data point.
2. **Tb or rare-earth hybrid.**
   - Natural ulexite cannot simply be doped.
   - Option (a): a **synthetic fibre plate of Tb-borate glass** (V ~ 200 rad/(T·m)), drawn in the ulexite geometry. That gives full rotation at ~1 T over 2–3 cm. The fibres must be low-birefringence (glass, not crystal) to avoid quenching.
   - Option (b): impregnating ulexite's ~0.5 µm inter-crystal gaps with a paramagnetic (e.g. Tb³⁺ or Dy³⁺) solution. This is **Speculative**: water attacks ulexite, and the birefringent crystals would still quench the rotation.

**Links:** the Faraday effect in §3d; birefringence in macroscopic optics below; the borate cure for mycelium panels (borax-treated, BN-coated) in [living_habitat_life_support.md](living_habitat_life_support.md#living-vs-non-living-zones-petrified-tubes-as-designed-branches) and [open_grow_kit.md](open_grow_kit.md). The chemistry is related (borates), but the function is different (fungicide/fire retardant vs optics).

##### 3d.1a Macroscopic birefringence
> Channing (verbatim, 2026-10-15): "Yes we got into Birefrigent in a macroscopic idea as well let me see if I can track it down"

Channing's notes on the macroscopic birefringence idea: **[Channing to supply]**.

> Channing (verbatim, 2026-10-15), clarifying: "It was on sinusoidal torque"

**Sinusoidal torque on a birefringent body (Grounded).**
- **Optical torque on a waveplate.** Light changes polarisation in a birefringent plate, so it gives up spin angular momentum (ħ per photon per unit change of circular content). For linearly polarised light at angle θ to the fast axis, through a plate of retardance Δ:
  **τ = (P/ω)·sin Δ·sin 2θ.**
  - The torque is **sinusoidal in 2θ**. It pulls the plate axis toward the polarisation (alignment, with angular stiffness), and it spins the plate if the polarisation is rotated continuously.
  - Measured first by R. A. Beth, "Mechanical detection and measurement of the angular momentum of light," *Phys. Rev.* 50, 115–125 (1936), doi:10.1103/PhysRev.50.115. He used a quartz waveplate on a torsion pendulum. With circular input through a half-wave plate the spin reverses, so τ = 2P/ω.
- **Microscale.** M. E. J. Friese, T. A. Nieminen, N. R. Heckenberg & H. Rubinsztein-Dunlop, "Optical alignment and spinning of laser-trapped microscopic particles," *Nature* 394, 348–350 (1998), doi:10.1038/28566 (erratum *Nature* 395, 621). Calcite microparticles in optical tweezers either align with the polarisation or spin at >350 Hz.
- **Optical torque wrench.** A. La Porta & M. D. Wang, "Optical torque wrench: angular trapping, rotation, and torque detection of quartz microparticles," *Phys. Rev. Lett.* 92, 190801 (2004), doi:10.1103/PhysRevLett.92.190801. ~10 mW gives several hundred pN·nm (~10⁻¹⁹ N·m) on micron quartz particles, with feedback control.
- **Static-field analog.** An anisotropic dielectric in a DC field E feels a torque per volume τ/V = ½ ε₀ Δε E² sin 2θ, which is also sinusoidal in 2θ. This is the torque that reorients liquid crystals: the Fréedericksz transition and every LCD pixel. Standard liquid-crystal physics (e.g. de Gennes & Prost, *The Physics of Liquid Crystals*). The textbook was not re-checked here.

**Macroscopic scale (computed).**
- At 633 nm, ω = 2πc/λ = 2.98×10¹⁵ rad/s.
- **1 W on a quarter-wave plate, θ = 45°:** τ_max = P/ω ≈ **3.4×10⁻¹⁶ N·m**. A half-wave plate with circular input doubles it to 6.7×10⁻¹⁶ N·m. Torque scales linearly with power, so even 1 kW gives only ~3×10⁻¹³ N·m.
- **DC dielectric version (illustrative, Δε = 1, E = 1 MV/m, 1 cm³):** τ ≈ 4.4×10⁻⁶ N·m. That is ~10¹⁰ times the optical value, but still micro-newton-metres, and the field is near air breakdown (~3 MV/m).
- **Conclusion:** "sinusoidal torque" from birefringence is real and well measured. At macroscopic scale it is tiny: a useful **alignment, actuation or sensing** effect (torsion balances, optical wrenches, LC cells), not a drive torque for a craft.

**Damping link.** A sinusoidal torque drive on a suspended plate is a driven torsional oscillator. Its response near resonance is set by Q, so the **R-damp** rule in §1a applies: add damping, or drive off-resonance.


**Grounded context**
- **Calcite / Iceland spar double refraction.** E. Bartholin, *Experimenta crystalli Islandici disdiaclastici quibus mira & insolita refractio detegitur* (Copenhagen, 1669). A strongly birefringent uniaxial crystal (n_o ≈ 1.658, n_e ≈ 1.486, Δn ≈ 0.17; standard handbook values) gives two visibly separated images. Later work: Huygens (1678/1690), Malus (1808–1810, polarisation by reflection) and the Nicol prism (1828).
- **Viking sunstone (hypothesis).** G. Ropars, G. Gorre, A. Le Floch, J. Enoch & V. Lakshminarayanan, "A depolarizer as a possible precise sunstone for Viking navigation by polarized skylight," *Proc. R. Soc. A* 468, 671–684 (2012; published online 2 Nov 2011), doi:10.1098/rspa.2011.0369. Rotating Iceland spar to its isotropy point equalises the two beams and locates a hidden Sun to within a few degrees, even at twilight. The physics is Grounded (demonstrated). That Vikings actually used it is a **hypothesis**, supported by medieval texts and a calcite found on the 1592 Alderney wreck (Le Floch et al., *Proc. R. Soc. A* 469, 2013).
- **Waveplates plus Faraday rotation = optical isolators (Grounded engineering).**
  - A waveplate (a birefringent retarder) is **reciprocal**, while Faraday rotation is **non-reciprocal**: the rotation sense is fixed by B, not by the propagation direction.
  - A 45° Faraday rotator between polarisers passes light forward and blocks it backward.
  - Polarisation-independent fibre isolators combine birefringent walk-off crystals or wedges, a 45° Faraday rotator and a half-wave plate. Birefringence splits and recombines the polarisations, and the Faraday element makes the path one-way.
  - That is the grounded "birefringence + Faraday" pairing. The ulexite estimate above shows why the active element must be a high-V, low-birefringence material (Tb glass, TGG), with natural birefringent crystals only for the passive split/recombine role.

### 3e. Toroidal flows and vortices
> Channing (verbatim, 2026-10-15): "From there we got into toroidal flows and vortexes"

This follows buoyant stability, lensing and Faraday. Related material already in the repo:
- the Earth–Moon vortex thread ([em_topo R8](em_topological_gravity_review.md#r8-atmosphere-layers--earthmoon-vortex-spin--plasma-flow));
- the Saturn hexagon ([em_topo §3](em_topological_gravity_review.md#3-saturns-north-polar-hexagon));
- vortex mode theory ([acoustic_streaming_and_centrifugal.md §4](acoustic_streaming_and_centrifugal.md#4-vortex-mode-theory));
- FRC plasmoids ([bubbles_arcs_frc.md](bubbles_arcs_frc.md));
- the toroidal dynamo and the induction sims ([tungsten_bismuth_core.md §7b-dyn](tungsten_bismuth_core.md#7b-dyn-toroidal-dynamo--induction-equation-mhd-in-space-recovered-ocr-damaged-2026-10-15), [§7b-dyn.2](tungsten_bismuth_core.md#7b-dyn2-1d-periodic-toroidal-induction-model-with-schumannphi-drive-grok-excerpt));
- magnetic helicity as the "strongest grounded thread" ([em_topo §3](em_topological_gravity_review.md#3-topological-em-field-configurations-as-a-route-to-gravity-like-effects)).

**Grounded: fluid vortices**
- **Helmholtz vortex theorems (1858).** In an ideal (inviscid, barotropic) fluid:
  - vortex lines move with the fluid;
  - the strength (circulation) of a vortex tube is constant along it;
  - a vortex tube cannot end inside the fluid, so it closes on itself (a ring) or ends on boundaries.

  H. Helmholtz, "Über Integrale der hydrodynamischen Gleichungen, welche den Wirbelbewegungen entsprechen," *J. reine angew. Math.* 55, 25–55 (1858), doi:10.1515/crll.1858.55.25.
- **Vortex rings and Hill's spherical vortex.** A closed vortex ring is the natural toroidal flow (smoke rings, the jellyfish wake, the heart's left-ventricle filling vortex that Leonardo sketched, §2). Hill's spherical vortex is an exact steady solution: a sphere of rotational fluid carrying its own toroidal circulation through irrotational surroundings. M. J. M. Hill, "On a spherical vortex," *Phil. Trans. R. Soc. A* 185, 213–245 (1894), doi:10.1098/rsta.1894.0006.
- **Kelvin's vortex atom (1867): historical, and it failed.** Inspired by Helmholtz and Tait's smoke rings, W. Thomson proposed that atoms are knotted vortex rings in the ether ("On vortex atoms," *Proc. R. Soc. Edinb.* 6, 94–105, 1867). It could not produce spectra, stability or chemistry, and it was abandoned with the ether. It did leave knot theory, through Tait's knot tables. This is a cautionary example: elegant toroidal "universal" models can be wrong.
- **Leonardo's vortex drawings.** See §2 (Codex Leicester, Deluge series; Marusic & Broomhall 2021).
- **Taylor–Couette flow.** Fluid between rotating cylinders becomes unstable to stacked, counter-rotating **toroidal (Taylor) vortices**. G. I. Taylor, "Stability of a viscous liquid contained between two rotating cylinders," *Phil. Trans. R. Soc. A* 223, 289–343 (1923), doi:10.1098/rsta.1923.0008. Magnetised versions are used to study the magnetorotational instability.
- **Vortex lift and stability.** Hovering insects get extra lift from a stable **leading-edge vortex** (LEV) created by dynamic stall. Spanwise flow stabilises it, much like the conical LEV on a delta wing. C. P. Ellington et al., "Leading-edge vortices in insect flight," *Nature* 384, 626–630 (1996), doi:10.1038/384626a0. A controlled vortex can *add* lift and stability rather than only drag.

**Grounded: toroidal fields and plasma**
- **Toroidal / poloidal decomposition.** Any solenoidal field B = ∇×(T r̂) + ∇×∇×(P r̂) splits into toroidal and poloidal parts. In dynamos, differential rotation (Ω-effect) turns poloidal into toroidal field, and helical turbulence (α-effect) turns toroidal back into poloidal (see §7b-dyn). Tokamaks combine an external toroidal field with a plasma-current poloidal field, and they also carry toroidal and poloidal **flows**, whose shear suppresses turbulence (cf. §7b-dyn.1).
- **Spheromaks and FRCs: self-organised toroidal plasma.** A spheromak carries comparable toroidal and poloidal field, generated by its own currents with no toroidal coils. An FRC is almost purely poloidal with a field reversal ([bubbles_arcs_frc.md](bubbles_arcs_frc.md)).
- **Taylor relaxation (1974).** A turbulent plasma tends to relax to a minimum-energy, force-free state (∇×B = λB) while conserving total magnetic helicity. This explains the reversed-field pinch and spheromak states. J. B. Taylor, "Relaxation of toroidal plasma and generation of reverse magnetic fields," *Phys. Rev. Lett.* 33, 1139–1141 (1974), doi:10.1103/PhysRevLett.33.1139.
- **Magnetic helicity.** H = ∫ A·B dV measures how linked, twisted and knotted field lines are. It is nearly conserved in high-conductivity plasma, even during reconnection. Its fluid twin, kinetic helicity, measures the "knottedness" of vortex lines: H. K. Moffatt, "The degree of knottedness of tangled vortex lines," *J. Fluid Mech.* 35, 117–129 (1969), doi:10.1017/S0022112069000991.

**RGRF use: Plausible-untested.** A vortex-ring or toroidal plasma flow around the craft (a self-organised, helicity-carrying sheath like a small spheromak or FRC) could provide:
- **buoyant-body stability** (damping and righting moments; see [lift §1a](lift_and_equilibrium_systems.md#1a-design-intent-buoyant-stability-not-levitation));
- **sheath shaping** for the lens and window in §3c.

Open questions: formation power, lifetime against tilt and resistive decay, and operation in atmosphere rather than vacuum.

**Speculative / Symbolic.** "The torus as the universal shape" (cosmology, atoms, consciousness). Tori and vortex rings are common because of Helmholtz's theorems and helicity conservation, not because of a universal law of form. The vortex atom shows how such generalisations can fail.

#### 3e.1 Plasma particle tracing and Bluetooth packet transmission (reference dynamics)
> Channing (verbatim, 2026-10-15): "Plasma particle tracing and Bluetooth packet transmission"
>
> Channing (verbatim, 2026-10-15): "It was more about real dynamics as reference"

Both are used here as **grounded real-world reference dynamics**: benchmarks for how charged particles and packetized signals actually behave. They are **not design components**.

**Plasma particle tracing (Grounded).**
- **Single-particle motion.**
  - **Gyration:** ω_c = qB/m, r_L = v⊥/ω_c.
  - **Guiding-centre motion:** the orbit splits into fast gyration plus slow drift of its centre.
  - **Drifts:** E×B (v = E×B/B², independent of charge, so electrons and ions drift together) and grad-B (v ∝ μ B×∇B / qB², charge-dependent, so it separates charge and carries current).
  - **Magnetic mirrors:** the magnetic moment μ = mv⊥²/2B is an adiabatic invariant, so particles reflect where B rises, if their pitch angle is outside the loss cone. Examples: Van Allen belts, mirror machines.
- **The Boris pusher.** This is the standard numerical integrator: half electric kick, exact-norm magnetic rotation, half kick. It conserves energy in a pure magnetic field and has excellent long-term phase-space behaviour. J. P. Boris, "Relativistic plasma simulation—optimization of a hybrid code," *Proc. 4th Conf. Numerical Simulation of Plasmas*, NRL, Washington DC, pp. 3–67 (1970).
- **Particle-in-cell (PIC).** Many such particles are pushed through fields solved on a grid from their own charges and currents. This is the self-consistent kinetic method behind sheath, double-layer and thruster simulations (textbook: C. K. Birdsall & A. B. Langdon, *Plasma Physics via Computer Simulation*, 1985).
- **Role as reference:** any RGRF claim about sheaths, charge separation (§3a), drifts or mirrors should agree with what a Boris/PIC trace shows. See the archived Grok code and the Boris companion sim below.

**Archived Grok code: "Suite element 3" (toroidal φ-winding + particle trace + Bluetooth under EMI).**
- **Code:** saved verbatim as [`sims/legacy_grok/suite_element3_toroidal_phi_trace_bt.py`](../sims/legacy_grok/suite_element3_toroidal_phi_trace_bt.py). It was pasted 2026-10-15 and is **truncated** at `# --- Bluetooth packet transmission under EMI ---` / `# Model`. The Bluetooth part is **[Channing to supply code]**.
- **Grok's saved output:** [`sims/legacy_grok/suite_element3_results.npz`](../sims/legacy_grok/suite_element3_results.npz). It contains phi = 1.6180339887, confinement_frac = 1.0, success_rate = 0.965, avg_latency_ms = 1.28, emi_level = 0.1013, and R_p, Z_p and confined (40 particles, all True).
- **Rerun (2026-10-15):** the code prints `confinement fraction after 300 steps: 1.00` and `Mean max minor radius of confined particles: 0.197`. Its final R_p and Z_p **match the .npz exactly** (max difference 0.0, seed 7), and `confined` matches. The archived code is therefore the code that produced the saved particle results.
- **Bluetooth metrics (success_rate 0.965, latency 1.28 ms, EMI level 0.101) are Grok-reported and unverifiable.** They come from the missing Bluetooth code **[Channing to supply code]**.

**Code review (each point checked by running it):**
1. **B_pol is computed but never used.** `toroidal_B` returns it, but the update only uses `B_tor` (through `omega = 0.3 B_tor`). The "φ-modulated poloidal winding" has no effect on any orbit.
2. **`winding_phase` and `n_toroidal` are never used.**
3. **The radial step is negligible by construction.** Per step, dr = v_perp · 0.01 · dt · sin(φt), so the total excursion is v_perp · 0.01 · ∫sin(φt)dt. Over t ≤ 3, ∫sin(φt)dt ≤ 2/φ ≈ 1.24, so the excursion is ≤ ~0.003. Measured: max |Δr| = 0.0015. The particles start at r ≤ 0.276, and loss needs r > 1.1a = 0.385, so **confinement = 1.0 is guaranteed**. Correction to the pre-run estimate: the excursion is ~10⁻³, not "well under 0.001", but the conclusion is the same. The Grok-reported confinement_frac = 1.0 **matches this by-construction analysis**.
4. **No Lorentz force and no real drifts.** Positions just rotate in θ at a rate set by B_tor. There is no v × B, no gyration, and no grad-B or curvature drift (the vertical drift that rotational transform must cancel). It is not a particle trace in the physics sense.
5. **φ enters only as a frequency scale** in sin(φt), sin(8φθ) (unused) and sin(2πt/φ) (unused).

**Ablation (φ replaced, same code, seed 7).** Confined fraction and mean max r:
- φ: 1.00, 0.197 (max |Δr| 0.0015)
- 1.5: 1.00, 0.197 (0.0023)
- 2.0: 1.00, 0.196 (0.00006)
- √2: 1.00, 0.197 (0.0029)

**No difference: φ does nothing in this code.**

**Honest companion sim: [`sims/toroidal_particle_trace_boris.py`](../sims/toroidal_particle_trace_boris.py).** Dimensionless units (R0 = 1, B0 = 5, q/m = 1, minor radius a = 0.35).
- **A. Boris pusher.** 400 particles at v = 0.1 (gyroradius ~0.02), started at r = 0.05–0.2, isotropic pitch, T = 300, lost if r > a. The field is B_tor = B0R0/R plus a poloidal field from constant q. Energy is conserved to ~2×10⁻¹⁴.

  | Case | Confined at T = 300 |
  |---|---|
  | Pure toroidal (no B_pol) | **0.263**: vertical grad-B + curvature drift, median loss t ≈ 198 |
  | q = 3 | 0.860 (larger drift-orbit width ∝ q) |
  | q = 2 | 0.955 |
  | q = 1.5 | 0.985 |
  | q = √2 | 0.993 |
  | q = φ | 0.985 |

  **Rotational transform confines (Grounded):** 26 % confined without a poloidal field vs 86–99 % with one. Smaller q (more transform) means narrower drift orbits. **q = φ is not special.** It sits within counting noise (±~0.6 % for N = 400) of q = 1.5 and √2. With no perturbation, rational and irrational q behave alike.
- **B. Field-line Poincaré map with a resonant perturbation.** q(r) = 1.2 + 1.5(r/a)², with perturbation δb_r = ε sin(3θ − 2ζ), resonant at q = 3/2. The radial spread of the field lines (max over launch angles, in units of a):

  | ε | q = 1.5 (resonant) | q = √2 | q = φ |
  |---|---|---|---|
  | 0 | 0 | 0 | 0 |
  | 2×10⁻⁴ | **0.039** (island) | 0.0034 | 0.0028 |
  | 10⁻³ | **0.094** (island, ∝ √ε) | 0.019 | 0.015 |

  A 3-island chain forms **only at the rational surface q = m/n that matches the perturbation**. Its width grows ~√ε, as island theory predicts. The irrational surfaces (√2, φ) stay intact as KAM-like tori and only ripple, roughly linearly in ε. φ ripples slightly less than √2 here, mostly because it sits farther from the resonant q = 1.5 surface. This is consistent with KAM / Greene 1979 (golden tori are the most robust; see [method_phi_and_natural_craft.md](method_phi_and_natural_craft.md)). But it **only matters relative to the perturbations present**: with ε = 0, every surface is intact.
- **Plot:** [`docs/images/toroidal_particle_trace_boris.png`](images/toroidal_particle_trace_boris.png). It shows confinement vs time, confinement at T = 300, and the Poincaré section with the m = 3 islands at r/a ≈ 0.45.
- **Labels:**
  - Confinement via rotational transform: **Grounded** (reproduced).
  - Islands at rational q under resonant perturbation: **Grounded** (reproduced).
  - "φ-optimized windings improve confinement": **not supported** by the archived code (φ has no effect) or by the Boris run (no advantage without perturbation).
  - Robustness of irrational / golden-ratio q against a given resonant perturbation: **Grounded in principle (KAM)**. As an RGRF design rule ("avoid low-order rational q where perturbations exist") it is Plausible-untested.
- **Next steps:** add the actual RGRF coil perturbation spectrum (n_toroidal = 16 windings → n = 16 ripple) and test which q surfaces it breaks; and add E-fields (E×B) and collisions.

**Bluetooth packet transmission (Grounded; Bluetooth Core Specification / bluetooth.com).**
- **Band:** 2.4 GHz ISM (2.402–2.480 GHz).
- **Classic (BR/EDR):** 79 channels at 1 MHz spacing, **frequency-hopping spread spectrum at 1600 hops/s** in a pseudo-random sequence. Adaptive frequency hopping skips channels that have interference.
- **Bluetooth Low Energy:** 40 channels at 2 MHz spacing (3 primary advertising, 37 general-purpose), also hopping.
- **Modulation:** GFSK (BLE: BT = 0.5, modulation index ~0.5). Data travels in short **packets** with access codes and headers, in time slots (TDMA).
- **Role as reference:** a well-characterised example of how packetized, hopping RF signals behave in a crowded, lossy channel (interference, fading, coexistence). It is a benchmark for any RGRF wireless-feedback or sensing loop. This also corrects the "Bluetooth-enabled CNT" phrasing in [tungsten_bismuth_core.md](tungsten_bismuth_core.md): the link is a sensor radio, not the nanotube.

**Labels**
- Packets ↔ particle bunches, read as one "pulsed" dynamics: **Symbolic / analogy only.**
- **Our extrapolation, optional (Plausible-untested):** frequency-hopping-like modulation of the craft's own field to tune coupling or avoid resonances, i.e. hopping the drive among frequencies so that no single structural or plasma resonance is pumped. This connects to the timing ideas in [tungsten_bismuth_core.md §7b-alfven.1](tungsten_bismuth_core.md#7b-alfven1-schumann-resonance-as-a-coupling-guide) (Schumann / IAR timing). It is not something Channing stated as a design component.

**See also:** rotating electron columns, Landau/vortex beams and rotation-induced fields as reference dynamics in [shifting_phase_order_review.md §G](shifting_phase_order_review.md#g-rotating-electron-systems-and-rotation-induced-fields-reference-2026-10-15); driven (Floquet) edge modes in [§F](shifting_phase_order_review.md#f-floquet-periodically-driven-topological-phases-2026-10-15).

## Labels
| Claim | Label |
|---|---|
| Rotating-field induction motor (1888); Tesla coil (1891); Colorado Springs (1899); Wardenclyffe (abandoned, demolished 1917) | Grounded |
| Tesla global wireless power via the Earth / Schumann cavity | Speculative / unproven (losses, Q ≈ 4–5) |
| Resonant near-field wireless power (Kurs 2007, WiTricity) | Grounded |
| Tesla mechanical oscillator patent (US 514,169, 1894); driven-oscillator / Q / damping physics; Millennium Bridge synchronous lateral excitation; Tacoma Narrows flutter | Grounded |
| Houston Street building-shaking story | Unverified anecdote / Speculative (MythBusters 2006: not reproduced) |
| Design rule R-damp: damping required in structure and field drive (Channing's stated lesson) | Rule = Grounded practice; RGRF field/sheath effectiveness Plausible-untested |
| Resonance avoidance, damping and drive-spectrum spreading in craft structure and field drive | Plausible-untested |
| Leonardo's water/vortex studies, bird-flight codex, Pacioli polyhedra | Grounded |
| Vitruvian Man illustrates Vitruvius Book III (circle and square) | Grounded |
| Vitruvian Man constructed on φ | Not supported (Markowsky 1992) |
| Male/female energy; expanded consciousness | Symbolic |
| Quasi-neutrality, ambipolar expansion, double layers | Grounded |
| Designing RGRF sheaths and plumes around charge balance and expansion | Plausible-untested |
| Expansion ↔ "expanded consciousness" | Speculative (metaphor only) |
| E and B as one tensor; mutual regeneration; equal energy in a vacuum wave; source-free duality | Grounded |
| Exact E–B duality with sources (magnetic monopoles) | Speculative (unobserved) |
| E/B as male/female | Symbolic |
| Male/female mapped to wavelength interactions → ± charge → lensing → Faraday | Symbolic (mapping); each physics step labeled below |
| Superposition/interference; plasma cutoff below ω_p; plasma lensing (Clegg 1998, Cordes 2017); gravitational lensing (1919); GRIN/metamaterial lensing | Grounded |
| Sheath as a tunable plasma lens / blackout control | Plausible-untested |
| Gravity-like lensing from EM | Speculative |
| Faraday: induction (1831), Faraday effect (1845), Faraday rotation of cosmic fields (Carretti 2022), field lines, Faraday cage, homopolar disk | Grounded |
| Helmholtz theorems; vortex rings / Hill's vortex; Taylor–Couette vortices; leading-edge vortex lift; toroidal/poloidal dynamo decomposition; spheromaks/FRCs; Taylor relaxation; magnetic helicity | Grounded |
| Kelvin's vortex atom | Historical; failed |
| Vortex-ring / toroidal plasma flow around the craft for buoyant stability and sheath shaping | Plausible-untested |
| "Torus as universal shape" cosmology | Speculative / Symbolic |
| Boris pusher, guiding-centre drifts, mirrors, PIC; Bluetooth FHSS/GFSK packets, used as reference dynamics | Grounded |
| Packets ↔ particle bunches | Symbolic / analogy |
| Frequency-hopping modulation of the craft's field (our extrapolation) | Plausible-untested |
| Confinement via rotational transform (Boris sim: 26 % pure toroidal vs 86–99 % with q) | Grounded |
| Islands only at rational q matching a perturbation; irrational (√2, φ) surfaces survive | Grounded (KAM) |
| "φ-optimized windings" in Suite element 3 | Not supported (φ has no effect; confinement 1.0 by construction) |
| Suite element 3 Bluetooth metrics (0.965 success, 1.28 ms) | Grok-reported; unverifiable (code missing) |

| Ulexite fibre optics (core/cladding from crystal orientation) | Grounded |
| Faraday effect in ulexite | Likely unstudied; Plausible-untested (expected V ~3–5 rad/(T·m) by analogy) |
| Full 360° rotation in ulexite at practical lab fields (≤1–2 T, cm lengths) | Not expected (needs ~34–85 T); birefringence quenches it further |
| Tb-borate glass Faraday rotation (V ≈ 172–234 rad/(T·m)) | Grounded (measured) |
| Tb-borate glass fibre plate in the ulexite geometry | Plausible-untested |
| Tb/Dy solution impregnation of natural ulexite | Speculative |
| Calcite double refraction; waveplate + Faraday isolators | Grounded |
| Viking calcite sunstone | Physics Grounded (demonstrated); historical use a hypothesis |
| Birefringence → sinusoidal torque τ = (P/ω) sin Δ sin 2θ (Beth 1936; Friese 1998; La Porta & Wang 2004) | Grounded |
| Static anisotropic-dielectric torque ∝ sin 2θ (liquid crystals) | Grounded |
| Macroscopic birefringent torque as an RGRF actuator (≈3.4×10⁻¹⁶ N·m per W optical) | Plausible-untested; tiny |
| Sinusoidal torque drive on a suspended element | Needs damping (R-damp) |

## Open items
- The specific Tesla and Da Vinci threads explored, and any Grok text. **[Channing to supply]**
- Role mapping answered (§3a: wavelength interactions → ± charge → lensing → Faraday). Any Grok text from the lensing, Faraday, toroidal-flow and particle-tracing threads. **[Channing to supply]**
- Suite element 3 Bluetooth code (truncated) and the source of its reported BT metrics. **[Channing to supply code]**
- Channing's notes on the macroscopic birefringence idea (§3d.1a). **[Channing to supply]**
- Any earlier Grok text on ulexite and Faraday (§3d.1). **[Channing to supply]**

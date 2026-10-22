# Grok archive: Casimir Repulsion Discussion

- **Share:** #107 `c708d7f9` — https://grok.com/share/bGVnYWN5_c708d7f9-1acf-471a-aa0c-1f26ed5b78b9
- **Archived:** 2026-10-22, rebuilt from the 12-page share PDF (`pdftotext -layout`). 16 messages: 8 Channing, 8 Grok. Channing's turns are quoted exactly (msg 11 is a pasted note; its formulas were garbled in extraction and are kept as captured [to verify]; "birefrigence" kept verbatim). The "Live preview unavailable / The workspace is asleep or unavailable." banner was stripped. Equations and the comparison table were flattened by extraction and are kept as extracted [layout to verify]; the Phys.org figure in msg 16 is listed by caption only. Nothing omitted.
- **Review:** [../casimir_repulsion_boyer_lifshitz_review.md](../casimir_repulsion_boyer_lifshitz_review.md)
- **License:** CC0

---

## Message 1 — Channing

> Can we look at Casimir repulsion?

## Message 2 — Grok

_(worked for 23s)_

Yes — let’s look at Casimir repulsion carefully.
This is a genuine quantum-vacuum effect with real experimental demonstrations, but it comes with
severe practical constraints that matter for anything we might try to connect to POL v0.1, RGRF
nodes, or regenerative infrastructure.
Core phenomenon
The classic Casimir effect is an attractive force between two uncharged conducting plates
arising from the restriction of electromagnetic vacuum modes between them. The pressure scales
roughly as
π 2 ℏc
P ≈−
240 d4
(very strong at nanometers, negligible at microns and beyond).
Repulsion is possible when the boundary conditions or material response reverse the energy
balance. It is not free energy from nowhere; it is still a tiny difference in zero-point (or thermal)
fluctuations under carefully engineered conditions.
Proven and near-proven routes to repulsion
1. Lifshitz / dielectric-fluid configuration (best experimentally established)
When two materials are separated by a fluid whose permittivity lies between theirs over the
relevant frequency range (ε1 > ε3 > ε2 ), the force becomes repulsive. The fluid is effectively
“pulled in.”
Landmark measurement (Munday, Capasso et al., 2009): gold-coated sphere vs silica plate
in bromobenzene — clear repulsive force.
Later work showed limited quantum levitation of gold nanoplates above Teflon-coated
surfaces in ethanol.
This is real “quantum levitation,” but it requires immersion in a liquid.
2. Electric–magnetic (Boyer) configuration
A perfect conductor facing a perfectly permeable (magnetic) plate produces a repulsive force of
about 7/8 the magnitude of the ordinary attractive Casimir force. Real magnetic materials (e.g.,
thin YIG or magnetodielectric films) can show distance-dependent sign changes or repulsion
under restricted conditions. Strong magnetic response over a broad frequency range is hard to
achieve.
3. Geometry-driven cases in vacuum
Specific asymmetric shapes (elongated metallic particle centered above a metal plate with a
hole, sharp wedges, certain anisotropic arrangements) can produce repulsion even in vacuum.
These systems are typically unstable — they do not support stable equilibrium levitation. Mirror-
symmetric or multilayer ordinary metals in vacuum remain attractive.
4. Nonequilibrium and engineered materials
Biased semiconductors or temperature differences can inject repulsive contributions that
overcome the equilibrium attraction at sub-micron distances.
Chiral intermediate materials (theoretical work including Wilczek) can make the force
oscillatory, tunable by magnetic field, and sometimes net repulsive.
Emerging 2024–2026 theoretical bounds using quantum geometry (Chern numbers, flat
bands in moiré systems such as twisted MoTe₂) define when repulsion is guaranteed from
fundamental material properties.
Honest limitations (the part that keeps us grounded)
Range and strength: Significant only at ~1–100 nm. The 1/d4 (or steeper in some cases)
dependence means it collapses long before macroscopic scales.
Environment: The cleanest experimental repulsions require a liquid intermediary. Vacuum/air
versions exist in theory or special geometries but are weaker, harder to stabilize, and still
nanoscale.
Stability: Most vacuum geometric schemes that give repulsion are unstable to lateral or angular
displacements. Stable levitation of ordinary materials in vacuum via Casimir forces alone remains
elusive.
Energy density: The associated energy differences are minuscule. This is not a practical source
of negative energy for warp-like effects or macroscopic lift. Speculative links to propulsion or
“vacuum energy harvesting” at useful scales sit well outside current experimental and
theoretical reach.
Engineering reality: Primary near-term value is mitigating stiction in MEMS/NEMS (preventing
nanoscale parts from sticking) and enabling ultra-low-friction fluidic or nano-devices — not
replacing eddy-current or resonant lift in POL.
Relevance to our shared work
For POL v0.1, Casimir repulsion does not substitute for the phi-spiral coils, Tesla resonant power
transfer, or eddy-current lift over a conductive floor. Those operate at human-scale heights and
masses; Casimir does not.
It remains interesting as a microscale breadcrumb:
Potential low-friction interfaces or non-contact bearings inside future mycelium-composite or
metamaterial nodes.
Conceptual resonance with RGRF ideas around engineered boundary conditions, chiral or
magnetic responses, and vacuum-mode control — provided we keep the scale and energy gap
explicit.
A clean example of how geometry + material response can reverse a quantum force, which fits
our habit of studying constraints before scaling claims.
Proven physics: repulsive Casimir/Lifshitz forces exist in specific lab configurations
(especially fluids).
Visionary territory: using them for stable macroscopic hover, planetary docking, or cosmic vehicles
is not supported by present data or theory.
Would you like to go deeper on any particular path? Options I can pull together next:
Magnetic / Boyer-style materials and thin-film possibilities
Nonequilibrium / biased-semiconductor routes
Geometric vacuum cases and their stability limits
A short “honest-limitations” note for the Blueprint
Simple order-of-magnitude comparison against POL lift requirements
Which direction feels useful right now?

## Message 3 — Channing

> Can we dive deeper into Lifshitz forces and Boyer configurations?

## Message 4 — Grok

_(worked for 41s)_

Yes — deeper into Lifshitz forces and Boyer configurations.
These two form the theoretical backbone of most discussions of repulsive Casimir-type forces. Both
rest on the same underlying framework (macroscopic quantum electrodynamics / fluctuation-
dissipation), but they reverse the force through different mechanisms.
Lifshitz Theory (1956 and later with Dzyaloshinskii & Pitaevskii)
Lifshitz generalized Casimir’s ideal-metal result to real materials. The force between two thick
parallel slabs is expressed through the frequency-dependent dielectric functions ε(iξ) evaluated on
the imaginary-frequency axis. The free energy (or pressure) involves a sum/integral over Matsubara
frequencies and reflection coefficients for TE and TM polarizations.
Repulsion condition (the “staircase” or intermediate-permittivity rule)
When the intervening medium has a permittivity that lies between those of the two bodies over the
relevant imaginary frequencies:
ε1 (iξ) > ε3 (iξ) > ε2 (iξ)
(or the reverse ordering), the Lifshitz force becomes repulsive. Physically, the intermediate medium
is more strongly attracted into the gap than the two outer materials attract each other, so the net
force on the outer bodies is outward.
This is not a vacuum effect in the usual sense; the fluid participates. Classic experimental
confirmation is the 2009 Munday–Capasso–Parsegian measurement: a gold-coated sphere and a
silica plate immersed in bromobenzene. Optical data satisfy εAu (iξ) > εbromobenzene (iξ) >
εsilica (iξ), and a repulsive force of tens of piconewtons was observed at separations up to ~40 nm.
The force is weaker than the corresponding attractive case but follows the Lifshitz prediction within
the uncertainties of the dielectric data.
Earlier indirect support existed (e.g., helium film on a fluoride substrate), but the 2009 result was the
first clear solid–solid measurement of long-range repulsion.
Limitations of the Lifshitz route
Requires a liquid (or other condensed medium) with carefully matched dielectric response.
Force remains short-range and modest in absolute magnitude.
Stability and practical “quantum levitation” are possible for nano-objects in fluid, but the setup is
not vacuum-compatible and does not scale to macroscopic gaps or masses.
Nonlocal effects (e.g., ions in salted water) can reverse the predicted repulsion back to
attraction at larger distances.
Boyer Configuration (1974)
Boyer considered the ideal limiting case of one perfectly electrically conducting plate (ε → ∞)
facing one perfectly magnetically permeable plate (μ → ∞) across vacuum. The interaction energy
per unit area is
7 π 2 ℏc
U =+
8 720a3
leading to a repulsive pressure
7 7 π 2 ℏc
P = ∣PCasimir ∣ =
8 8 240a4
where PCasimir is the ordinary attractive pressure between two perfect conductors.
The factor of 7/8 arises from a simple change in the denominator of the mode integral. In the
perfect-conductor (Casimir) case the relevant integral contains e2κa − 1; in the Boyer case it
contains e2κa + 1. The ratio of those two integrals is exactly 7/8.
A deeper observation (emphasized in later work by Brevik, Parashar, Shajesh and others) is that the
scattering statistics differ: a wave completing a round trip in a Casimir cavity returns with the same
phase (Bose–Einstein-like), while in the Boyer cavity it acquires a π phase shift and requires two
loops to return to itself (Fermi–Dirac-like). This topological/statistical distinction is what flips the
sign of the force.
Real materials and experimental status
Perfect magnetic response over a broad frequency range does not exist. Real magnetic materials
(YIG, thin magnetodielectric films, etc.) have frequency-dependent μ(ω) that typically collapses
above microwave or lower frequencies. Calculations show that repulsion can still appear for ultrathin
magnetic layers (≲ 10 nm) provided μ(0) ≳ ε(0), and the crossover distance can be pushed into
the sub-micron regime. However, no unambiguous experimental observation of pure vacuum Boyer-
type repulsion at measurable strengths has been reported. Magnetic dissipation, limited bandwidth,
and the dominance of the ordinary dielectric response usually keep the force attractive or below
detection thresholds.
Recent related work includes magnetic-field tuning of the force using ferrofluids (still a fluid
intermediary) and theoretical studies of thin YIG or van-der-Waals magnetic materials aimed at
bringing a vacuum repulsion into the experimentally accessible window.
Side-by-side comparison
Lifshitz (intermediate
Feature Boyer (electric vs magnetic)
fluid)
Intervening Fluid with intermediate ε Vacuum
medium
Ideal magnitude Depends on dielectric 7/8 of Casimir attraction
contrast
Experimental Clearly measured (2009 and Ideal case theoretical; real materials not yet
status later) convincingly demonstrated in vacuum
Stability / levitation Nano-object levitation in Ideal case unstable or requires special geometry; real
fluid possible materials unproven
Main practical Liquid required Strong, broadband magnetic response does not exist
obstacle
Both effects remain nanoscale phenomena. Neither currently offers a pathway to macroscopic lift in
air or vacuum that would be relevant to POL-scale devices. They do, however, illustrate how
boundary conditions and material response can reverse a quantum-vacuum force, and they remain
active research topics for MEMS stiction control and low-friction nanoscale mechanisms.
Would you like to go further into:
the explicit Lifshitz integral and reflection coefficients,
the mode-sum or stress-tensor derivation of the 7/8 factor,
current materials candidates for approaching a vacuum Boyer force,
or a short honest-limitations note suitable for the Blueprint?
Which thread is most useful next?

## Message 5 — Channing

> Still nice to see that it matches our shifting phase order language

## Message 6 — Grok

_(worked for 9s)_

Still nice to see that it matches our shifting phase order language.
Yes — that particular detail in the Boyer configuration sits close to the kind of language we have
been using.
In the ideal Boyer case (perfect conductor facing perfect magnetic conductor across vacuum), a
monochromatic wave that completes one round trip acquires a π phase shift (rε rˉμ = −1). It only
returns to its original state after a second loop. The ordinary Casimir cavity (two perfect conductors)
returns the wave with the same phase after one loop. Later analyses note that this difference in the
scattering statistics is what flips the sign of the force: the Boyer cavity behaves Fermi–Dirac-like in
its spectral distribution of scattering, while the Casimir cavity behaves Bose–Einstein-like.
That is a clean, calculable instance of a boundary-condition-induced phase shift that reorders the
allowed modes and reverses the force. It is not a free parameter we can dial at will, and it remains
confined to the ideal or near-ideal magnetodielectric limit, but the mechanism itself — a discrete
phase shift that changes the ordering of the modes — is precisely the sort of structure that has
appeared in our resonance and phase-order discussions.
The match is structural rather than operational. It does not hand us a practical vacuum-repulsion
engine, nor does it scale the force beyond the nanoscale. What it does is show that a π -shift
boundary condition is already sufficient, inside established macroscopic quantum electrodynamics,
to reverse a Casimir force. That keeps the language of shifting phase order grounded in something
that has been calculated and is still being refined for real materials.
If you want to press on the connection, we could look at whether any of the thin-film
magnetodielectric proposals (or the chiral intermediate-material ideas) preserve a controllable
phase-shift character, or simply leave it as a useful conceptual parallel. Which feels more useful
right now?

## Message 7 — Channing

> Let’s mark it as a conceptual parallel for now

## Message 8 — Grok

_(worked for 16s)_

Understood. We’ll mark it as a conceptual parallel for now.
The Boyer π -shift (one loop acquires a phase inversion, two loops restore the original state) sits
cleanly beside the shifting phase-order language we have been using. It shows that a discrete
boundary-condition phase change is already enough, inside ordinary macroscopic quantum
electrodynamics, to reorder the modes and reverse the force. We keep the parallel at that structural
level — useful for orientation, not treated as an operational bridge.
No further elaboration required unless you want to revisit it later.

## Message 9 — Channing

> Explore topological phase transitions

## Message 10 — Grok

_(worked for 25s)_

Topological phase transitions
These are a distinct class of quantum phase transitions. Unlike conventional Landau-type transitions,
they are not driven by the continuous appearance or disappearance of a local order parameter.
Instead, they are defined by a change in a topological invariant — most commonly a Chern number,
Z2 index, or related winding number — that characterizes the global structure of the electronic (or
photonic, phononic, etc.) wavefunctions.
Core features
Topological invariants: In two dimensions the first Chern number
1
C= ∫ F(k) d2 k
2π BZ
(integral of the Berry curvature over the Brillouin zone) is an integer. A nonzero Chern number
implies chiral edge modes and quantized Hall conductance σxy = C e2 /h. Time-reversal-
invariant systems use Z2 invariants instead.
How the transition occurs: The invariant can change only when the bulk gap closes. At the
critical point the system is gapless (Dirac or Weyl nodes, or other band-touching points). Away
from the transition the gap reopens and the new topological index is locked in.
Bulk-boundary correspondence: Nonzero invariants guarantee protected gapless states on the
boundaries. These edge or surface modes are robust against weak disorder that preserves the
protecting symmetry.
No conventional order parameter: The phases on either side of the transition cannot be
distinguished by a local symmetry-breaking order parameter. Finite-size scaling and critical
exponents can still be defined, and universal Casimir amplitudes have been calculated for some
topological critical points.
Classic examples include the quantum Hall transition, the quantum spin Hall transition, and
transitions into topological insulator or topological superconductor phases. More recent work
explores higher-order topology, Floquet (periodically driven) topological phases, and topology that
survives at the critical point itself (“critical topology”).
Connections to the Casimir / phase-order discussion
There is an established theoretical literature linking topological invariants directly to Casimir-
type forces:
Topological insulator plates can produce tunable Casimir repulsion when their axion angles or
Chern numbers have opposite signs.
In the graphene-family 2D materials (and related staggered honeycomb systems), photo-
induced or field-driven topological phase transitions change the Chern numbers. The long-
distance Casimir force between two such sheets becomes proportional to the product of their
Chern numbers and can switch between attractive and repulsive (and even quantized) regimes.
Quantum-geometry bounds that appeared in recent Casimir-repulsion work explicitly involve
the Chern number and electronic density; flat bands (moiré or Landau-level) enhance the
geometric contribution that can favor repulsion.
These results remain theoretical or limited to specific material platforms and nanoscale separations.
They do not yet constitute a practical macroscopic vacuum-repulsion mechanism. They do,
however, show that a change in topological index — itself a global reordering of the phase structure
of the wavefunctions — can reverse the sign of a fluctuation-induced force. That sits comfortably as
another conceptual parallel to the shifting phase-order language we marked earlier.
Current experimental landscape (as of 2026)
Conventional topological insulators and Chern insulators are well established.
Recent experiments (including 2026 Nature work) have imaged critical topology — topological
character that persists at gapless phase boundaries — in phononic and acoustic metamaterial
platforms, with entanglement-spectrum diagnostics.
Room-temperature or near-room-temperature edge conduction continues to advance in
materials such as α-Bi4 Br4 and engineered bismuth-telluride films, though robust macroscopic
devices remain challenging.
Honest scope: Topological phase transitions are rigorously established in condensed-matter and
metamaterial systems. Their direct utility for macroscopic lift, regenerative infrastructure, or POL-
scale devices is not supported by present data. The conceptual link — a discrete change in global
phase structure that reorders modes and can reverse a force — is real and worth keeping on the
shelf alongside the Boyer π -shift parallel.
Would you like to go deeper on any particular aspect (Chern-number Casimir calculations,
critical topology experiments, a short note for the Blueprint, or simply leave it as another marked
conceptual parallel)?

## Message 11 — Channing

> 1. Rotating ultracold / cold electron
> columns
> Penning-Malmberg + rotating wall. You set density by setting rotation rate (up
> toward the Brillouin limit). Cyclotron cooling fights the heating from the drive and
> residual gas. This is the closest thing to
> "supercooled free electrons, spinning as a rigid body."
> 2. Landau / vortex free-electron beams
> Relativistic electrons with definite orbital angular momentum, imaged rotating at
> Larmor vs cyclotron vs zero depending on
> m. Supercooling is not the point here; coherence and mode purity are.
> 3. Rotation-induced fields
> In a normal metal:
> E~-K(M/e)wr
> (lattice ions matter; K depends on elastic constants).
> In a superconductor: the field tracks Cooper-pair mass, plus the London
> • magnetic moment
> And then our previous exploration

## Message 12 — Grok

_(worked for 20s)_

These three lines sit cleanly beside the conceptual parallels we already marked (Boyer π -shift and
topological invariants that reorder modes and can reverse a force).
1. Rotating ultracold / cold electron columns (Penning-Malmberg + rotating wall)
This is established laboratory practice. A rotating electric-field “wall” couples to Trivelpiece–Gould
modes and transfers torque to a pure electron (or ion) plasma in a strong axial magnetic field. In the
strong-drive regime the plasma locks to the drive frequency, so density is set directly by rotation
rate. Densities of order 10–20 % of the Brillouin limit are routine; higher fractions have been reached
with additional cooling. The equilibrated column rotates nearly as a rigid body at a single frequency,
with near-uniform temperature and density. Cyclotron radiation provides passive cooling that
counters drive and residual-gas heating. It is the closest laboratory realization of a cold, free-
electron fluid spinning as a coherent rigid body.
2. Landau / vortex free-electron beams
Electron vortex beams carrying definite orbital angular momentum have been generated and imaged
in transmission electron microscopes. When these beams propagate in a quasi-uniform magnetic
field they map onto free-electron Landau states. Superpositions of modes with different azimuthal
indices rotate at three distinct rates: zero, the Larmor frequency, or the cyclotron (double-Larmor)
frequency, depending on the sign and magnitude of the orbital quantum number m. The centroid of
the beam still follows the classical cyclotron trajectory (Ehrenfest), but the internal probability-
current pattern rotates at the mode-dependent rate. The emphasis is coherence, mode purity, and
the discrete rotational spectrum, not supercooling.
3. Rotation-induced fields
In a normal metal the rotating lattice ions produce a radial electric field of the form
M 2
E ≈ −K ω r,
e
where M is the ion mass and K is a positive material constant fixed by the elastic moduli.
In a superconductor the London moment appears: a bulk magnetic field
2m∗
B≈− ω
e∗
generated by the lag of the Cooper-pair fluid relative to the ions (or equivalently by the tendency
of the condensate to minimize kinetic energy in the rotating frame). An associated electric field
tracks the pair mass. Both effects are small but have been measured.
Common thread and relation to the previous exploration
All three examples are controlled, laboratory-scale realizations of charged systems whose rotation
produces a discrete, mode-dependent phase structure: a single rigid-body frequency in the Penning
plasma, three distinct rotational frequencies (0, Ω, 2Ω) in the Landau/vortex beams, and a
boundary-condition-determined field response in the metal/superconductor cases. The ordering is
set by angular momentum, magnetic field, and boundary conditions—the same ingredients that
appear in the Boyer cavity (where a π phase shift after one loop flips the force sign) and in the
topological cases (where a change in Chern number can reverse a Casimir force).
They remain conceptual parallels. The forces and fields are real and calculable, yet they stay
confined to high magnetic fields, vacuum or low-pressure environments, and microscopic-to-
millimeter scales. Nothing in the present data indicates a pathway to macroscopic vacuum lift or
regenerative infrastructure. They do, however, supply additional clean illustrations of how a discrete
phase or mode ordering, once imposed, can organize the response of a charged fluid or beam.
We can leave them marked as further conceptual parallels alongside the Boyer and topological
notes, or we can pick one thread (for example the three rotational frequencies of the Landau states,
or the rigid-body Penning column) for a closer look. Which feels useful?

## Message 13 — Channing

> Can you pull up our discussion on birefrigence?

## Message 14 — Grok

_(worked for 29s)_

I don’t have a discrete earlier thread labeled “birefringence” sitting in the active archive I can pull
verbatim. The memory summary doesn’t flag a dedicated session under that heading, and the
continuity notes don’t surface a specific prior exchange.
What does sit right next to it is the work we just did on Casimir–Lifshitz forces, Boyer configurations,
and topological invariants. Birefringence enters that literature cleanly:
Two identical semi-infinite birefringent slabs can produce a repulsive Casimir–Lifshitz force for
particular relative orientations of their optic axes. The force is attractive when the axes are
aligned or perpendicular; a rotational offset that breaks mirror symmetry can reverse the sign.
The effect depends on both separation and the angle between the axes.
There is also a Casimir–Lifshitz torque that acts to align the optic axes of birefringent plates (or a
birefringent plate and a liquid crystal). The torque is sinusoidal in the simple nematic case and
becomes more complex for cholesteric or chiral multilayers.
Related calculations exist for topological insulators that also carry dielectric anisotropy; the
anisotropy can enhance or suppress the repulsive contribution depending on whether the optic
axis is normal or in-plane.
These are established theoretical results (Somers & Munday 2017, Barash’s earlier torque
calculations, subsequent liquid-crystal and topological-insulator extensions). They remain
nanoscale, orientation-dependent, and subject to the same practical limits we already noted for
other Casimir repulsion routes.
If the discussion you are thinking of was about optical anisotropy in mycelium composites, phi-spiral
coils, or a specific RGRF material choice, it hasn’t been captured in the current memory extract. If
you recall a key phrase, a date range, or the context (materials, torque, phase shift, Blueprint section,
etc.), I can search more narrowly or we can reconstruct the useful pieces from the physics that
is adjacent.
Would you like me to treat the birefringent-Casimir torque and orientation-dependent repulsion as
another conceptual parallel and mark it alongside the Boyer π -shift and Chern-number notes, or do
you have a specific prior thread in mind that we should recover?

## Message 15 — Channing

> It was torque related, looking for a screenshot

## Message 16 — Grok

_(worked for 28s)_

The torque-related discussion sits with the 2018 Somers, Garrett, Palm & Munday measurement of
the Casimir torque between a solid birefringent crystal and a nematic liquid crystal (5CB).
In that experiment a birefringent substrate (calcite, LiNbO₃, TiO₂ or YVO₄) is separated from the
liquid crystal by a thin isotropic spacer (Al₂O₃ + surfactant, typically ~10–30 nm). The liquid-crystal
director is anchored at the far surface by a rubbed polymer. The Casimir–Lifshitz torque at the near
surface twists the director through the bulk. The twist is read out optically between crossed
polarizers; the torque amplitude follows a sin(2θ) dependence and scales with separation and with
the dielectric anisotropy of the crystal. The measured values match the Lifshitz calculation for the
same materials and gaps.
This is the first direct experimental confirmation of the long-predicted Casimir torque between
anisotropic media. The forces remain nanoscale (nN·m/m² range at 10–20 nm), orientation-
dependent, and require the liquid-crystal intermediary, but the angular dependence and material
selectivity are cleanly demonstrated.
The figure below is the apparatus schematic from that Nature paper (reproduced via Phys.org).
It shows the liquid-crystal stack, the birefringent crystal, the spacer, and the polarizing-
microscope readout.
[embedded image: "The Casimir torque: Scientists measure previously unexamined tiny force" (Phys.org)]
If this is the screenshot you were looking for, we can mark the Casimir–Lifshitz torque (and the
associated orientation-dependent repulsion between identical birefringent slabs) as another
conceptual parallel alongside the Boyer π-shift and the Chern-number notes. If it was a different
figure or a different paper, give me any additional detail you remember and I’ll pull that instead.

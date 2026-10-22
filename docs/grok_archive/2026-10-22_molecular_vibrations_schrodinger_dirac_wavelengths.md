# Grok conversation archive: "Data Linking Molecular Vibrations to Schrödinger and Dirac Wavelengths" (2026-10-22)

- **Source:** Grok-generated conversation, shared by Channing (share #93).
- **Share URL:** https://grok.com/share/bGVnYWN5_4e163fc7-fee7-4df7-b225-14a30f03a3e3 (share id `4e163fc7`).
- **Captured:** 2026-10-22. 28 messages (14 user, 14 Grok). Topics: vibrational Schrödinger equation and IR wavelengths, four-component Dirac–Coulomb shifts of hydride frequencies (Pb hydrides), degrees of freedom and the curse of dimensionality, neural-network vibrational solvers, Fermi and Darling–Dennison resonance, pressure/strain tuning, vibration–rotation coupling and the moment of inertia, Monte Carlo averaging of the inverse-inertia tensor, Klein-Gordon.
- **License:** CC0-1.0 (this archive file). The quoted text is Grok output, reproduced for the record.
- **Extraction cleanups.** The text below is verbatim except for these mechanical fixes:
  1. **Rebuilt from the PDF capture** (25 pages, `pdftotext -layout`). Channing's turns print right-indented and were re-joined onto one line each.
  2. Shredded display equations are replaced by one line `[MATH, reconstructed: …]`, an editorial reconstruction checked against the surrounding text. Two matrix-element prefactors were not legible and are marked so. Inline sub/superscripts flattened by the capture (e.g. "12 ℏωk" = ½ℏω_k, "Q2k" = Q_k²) are left as captured in prose.
  3. Page chrome removed: "Continue conversation" button text, "Grok & Channing" footer labels, form feeds, zero-width spaces. "Worked for …" timers are kept in parentheses. No other chat titles or account name appear in the text layer; Channing appears by first name only.
  4. Tables keep their captured column layout (some cells are split across lines by the capture).
  5. Speaker headers `==== [n] USER/GROK ====` added; messages numbered from 1. A personal-details scan was run.
  6. Nothing was omitted for scope: the share holds no out-of-scope or personal material.
- **Review:** see [molecular_vibration_schrodinger_dirac_review.md](../molecular_vibration_schrodinger_dirac_review.md).

---

```text
==== [1] USER ====
Is there any data linking molecular vibrations to wavelengths building of Schrödinger and Dirac?

==== [2] GROK ====
(Worked for 22s)

Yes — there is extensive, well-established data linking molecular vibrations to the Schrödinger
equation, and more specialized computational data connecting them to the Dirac equation
(primarily through relativistic effects on the potential energy surface).

Schrödinger Equation and Molecular Vibrations
The connection is foundational in quantum chemistry and spectroscopy. Under the Born–
Oppenheimer approximation, the nuclear motion (including vibrations) is described by the
vibrational Schrödinger equation. For a molecule, this is typically solved in normal coordinates after
expanding the potential about equilibrium.

In the harmonic-oscillator approximation (the standard starting point), each mode behaves as a one-
dimensional quantum harmonic oscillator:

[MATH, reconstructed: Ĥ_k = −(ℏ²/2) ∂²/∂Q_k² + (1/2) λ_k Q_k²]

with energy eigenvalues

[MATH, reconstructed: E_v = ℏω (v + 1/2),   ω = √(k/μ)]

(where v = 0, 1, 2, …, k is the force constant, and μ is the reduced mass). The corresponding
wavefunctions involve Hermite polynomials.

Wavelength/frequency link: Transitions between these levels absorb or emit photons whose energy

                                                                                        ~

matches ΔE = ℏω . These appear as infrared (IR) spectral bands, reported as wavenumbers ν
(cm⁻¹) or wavelengths (typically mid-IR, roughly 2.5–25 μm). Experimental IR spectra of thousands
of molecules match these predictions (with anharmonic corrections for better accuracy).

Examples of close theory–experiment agreement (fundamentals, in cm⁻¹):

    Water (H₂O): bend ~1595, symmetric stretch ~3657, asymmetric stretch ~3756.

    Carbon monoxide: ~2143.

    Many other diatomics and polyatomics show similar quantitative matches once anharmonicity
    (e.g., Morse potential or vibrational perturbation theory / VCI) is included. High-level
    calculations solving the vibrational Schrödinger equation routinely reach agreement within a few

    cm⁻¹ for small molecules.

Zero-point vibrational energy (from the v = 0 levels) is also routinely measured and calculated
this way.

Dirac Equation Connection
The Dirac equation is the relativistic wave equation for electrons (spin-½ particles). It does not
directly govern nuclear vibrations the way the Schrödinger equation does. However, there is clear
computational data linking the two:

Four-component relativistic density-functional theory (DFT) calculations that use the Dirac–
Coulomb Hamiltonian modify the electronic structure and thus the potential-energy surface.
Because vibrational frequencies come from the second derivatives of that surface (the Hessian),
relativity shifts the predicted frequencies.

A 2021 study (Jakubowska, Pecul, Ruud, J. Phys. Chem. A) computed harmonic frequencies for a
series of hydrides (H₂X, XH₃, XH₄) using four-component Dirac–Coulomb DFT. Key findings:

    Relativistic effects are small for light atoms but noticeable for heavier ones (fifth–sixth row).
    For H₂Po, shifts reach ~10% on the higher-frequency stretches; smaller but measurable for H₂Te,
    BiH₃, PbH₄, etc.

    Spin–orbit contributions are usually a minor fraction of the total relativistic effect (except in a
    few cases like H₂Te/H₂Po).
    Only modes involving significant heavy-atom motion are strongly affected.

These calculations provide quantitative “data” showing how the Dirac framework alters the
vibrational wavelengths that would be observed.

Summary of the Link
 Aspect               Schrödinger Equation                Dirac Equation

 Direct role          Governs nuclear vibrational         Governs relativistic electrons; affects PES

                      wavefunctions & energies            indirectly

 Wavelength           Energy spacings → IR photon         Shifts the calculated frequencies (especially
 connection           wavelengths                         heavy atoms)

 Experimental         Massive (IR spectra of countless    Computational benchmarks; important for
 support              molecules)                          accuracy in heavy-element chemistry

 Typical scale        Fundamental match after             Percent-level corrections for heaviest hydrides

                      anharmonicity

In short: the Schrödinger equation supplies the primary quantum description that “builds” the
vibrational energy levels and their associated IR wavelengths. The Dirac equation enters when
relativistic effects on the electronic structure must be included for quantitative accuracy, with
published numerical results demonstrating the magnitude of those shifts.

If you are thinking of a more specific resonance, frequency-matching, or speculative
geometric/wave interpretation (beyond standard quantum chemistry), feel free to clarify and we can
dig deeper into the literature or run a focused calculation/search. Next options could include looking
at particular molecules, anharmonic treatments, or relativistic examples in more detail.

==== [3] USER ====
I know we have touched on this before around the time we were discussing Plank’s constant. What came into my mind more recently was the degree of freedom can we dive deeper?

==== [4] GROK ====
(Worked for 40s)

Yes — we can go deeper on the degrees of freedom. This is the natural next layer after the Planck’s-
constant discussion and the vibrational Schrödinger/Dirac link.

Counting the Degrees of Freedom
A molecule of N atoms has 3N total classical degrees of freedom (three Cartesian coordinates
per nucleus).

       3 are pure translation of the center of mass.

       3 are overall rotation (or only 2 for a linear molecule, because rotation about the molecular axis
       does not change any nuclear positions).
       That leaves 3N − 6 (nonlinear) or 3N − 5 (linear) internal vibrational degrees of freedom.

These become the normal modes. In the harmonic approximation the multi-dimensional vibrational
Schrödinger equation separates exactly into that many independent one-dimensional harmonic-
oscillator equations — one per mode — after the coordinate transformation to normal coordinates

Qk .

Planck’s Constant Enters at the Quantization Step
Each of those one-dimensional Schrödinger equations is

[MATH, reconstructed: ( −(ℏ²/2) ∂²/∂Q_k² + (1/2) λ_k Q_k² ) ψ_{v_k}(Q_k) = ε_{v_k} ψ_{v_k}(Q_k)]

with eigenvalues

[MATH, reconstructed: ε_{v_k} = ℏω_k (v_k + 1/2),   ω_k = √λ_k]

The total vibrational energy is simply the sum over the 3N − 6 (or 3N − 5) modes. The zero-point
contribution from every mode is 12 ℏωk ; it cannot be removed even at absolute zero. The photon

wavelength (or wavenumber) that couples two levels of a given mode is fixed by the energy
difference Δε = ℏωk , so E = hν = hc/λ. Planck’s constant therefore both quantizes the motion

of each degree of freedom and sets the spectroscopic wavelength scale.

Quantum vs Classical Degrees of Freedom
Classically each vibrational mode has two quadratic energy reservoirs (kinetic + potential), so
equipartition would assign kT per mode. Quantum mechanically most modes are “frozen” at
ordinary temperatures because ℏωk ≫ kT . The vibrational partition function for each mode is

[MATH, reconstructed: q_k = e^{−ℏω_k/2kT} / (1 − e^{−ℏω_k/kT})]

and the total qvib is the product over all modes. This is why the heat-capacity contribution of

vibration is usually far below the classical R per mode until high temperature. The number of
degrees of freedom therefore controls both the spectroscopic complexity (how many fundamental
bands) and the thermodynamic behavior.

Dirac’s Role
The force constants λk (and therefore the frequencies ωk ) are second derivatives of the electronic

potential-energy surface. When that surface is computed with the four-component Dirac–Coulomb
Hamiltonian, relativity modifies the ωk in a mode-dependent way. The 2021 four-component DFT

study of the hydrides shows shifts of a few percent for Te/Sb/Sn compounds and up to ~10 % for the
high-frequency stretches of H₂Po and BiH₃; spin–orbit coupling is a smaller fraction except for the
heaviest cases. In other words, the Dirac framework changes the quantitative energy spacings —
and therefore the wavelengths — associated with each vibrational degree of freedom once heavy
atoms are present.

Summary Table

                                                                                          Relativistic correction

 Aspect                          Classical                   Quantum (Schrödinger)

                                                                                          (Dirac)

 Number of vibrational           3N − 6 (or 3N − 5)          Same number of independent   Same counting;
 DoF                             modes                       oscillators                  frequencies shift

 Energy per mode                 Continuous                  ℏω(v + 1/2)                  ω modified by relativistic

                                                                                          PES

                                                             1

 Zero-point                      None

                                                             2
                                                              ℏω per mode                Slightly altered ZPE

 Spectroscopic                   —                           Set by ΔE = ℏω               Wavelengths shift by the
 wavelength                                                                               same %

 Thermodynamic                   kT per quadratic            Often frozen (qk ≈ 1)

                                                                                          Minor secondary effect

 weight                          term                                                     on qvib

The degrees of freedom are the concrete channels through which the Schrödinger equation (and, for
heavy atoms, the Dirac-influenced electronic structure) builds the discrete vibrational energy ladder
and the associated infrared wavelengths.

If you want to push further we can look at a concrete molecule (H₂O, CO₂, or a heavy hydride), the
anharmonic mixing between modes, the vibrational partition function and heat capacity, or the
practical computational cost of solving the full multi-dimensional vibrational Schrödinger equation
once the number of degrees of freedom grows. Which direction feels most useful right now?

==== [5] USER ====
Yeah let’s look at a heavier hydride, let’s go with lead. Also, can we look at what happens when the degrees of freedom grow? Then, can we look at fermi resonance?

==== [6] GROK ====
(Worked for 45s)

Yes — let’s take all three.

1. Lead Hydride (PbH₄ and HC≡CPbH₃)
Lead is a classic heavy-atom case where the Dirac framework matters. PbH₄ is tetrahedral (Td
symmetry) and has 9 vibrational degrees of freedom (3N–6 for N=5).

From four-component Dirac–Coulomb DFT calculations (Jakubowska, Pecul, Ruud, J. Phys. Chem.
A 2021):

PbH₄ approximate harmonic frequencies (cm⁻¹)

 Mode       Symmetry             Relativistic   Non-relativistic   Notes

 ω₁         A₁ (sym. stretch)    ~1839          ~1847              Small shift

 ω₂         T₂ (asym. stretch)   ~1827          ~1839              Small shift

 ω₃         E (twist)            ~686           ~664               ~3% (text notes up to ~6% in one mode)

 ω₄         T₂ (scissor)         ~609           ~609               Negligible

Relativistic effects are modest for the stretches but visible on the lower-frequency modes.
Experimental gas-phase / matrix IR reports the asymmetric Pb–H stretch near 1815–1823 cm⁻¹,
which sits close to the relativistic calculation.

For the larger molecule HC≡CPbH₃ the picture is clearer: only modes with large Pb motion shift
significantly. Examples from the same study:

      C–Pb stretch: 384 (rel) vs 409 (nrel) cm⁻¹

      C–C–Pb bend: 187 (rel) vs 145 (nrel) cm⁻¹ (~29% shift)

      H–Pb–H scissor: 641 vs 597 cm⁻¹

Modes localized on the C≡C–H fragment are almost unchanged. This is the practical signature of the
Dirac-influenced potential-energy surface: the force constants (and therefore the wavelengths) of

the heavy-atom degrees of freedom are selectively modified.

2. What Happens When the Degrees of Freedom Grow
Once the number of vibrational degrees of freedom rises, two things become hard:

                                                                                          D

    Curse of dimensionality. In a direct-product basis the number of functions scales as Nbasis

                                                                                           12

    where D = 3N − 6. For 12 modes with 10 basis functions each you already have 10             functions
    — terabytes just to store one wavefunction. Integration grids scale the same way. Practical full-
    dimensional variational calculations (VCI, DVR, etc.) are routinely limited to roughly 6–12 modes
    for high accuracy; beyond that one needs pruning, contracted bases, Smolyak sparse grids,
    tensor-network methods, or neural-network representations of the wavefunction.

    Anharmonic coupling network. With more modes the number of possible cubic and quartic
    couplings grows rapidly. Most are weak, but a few near-resonances (see Fermi resonance below)
    become important. Methods such as vibrational self-consistent field (VSCF) + configuration
    interaction, or machine-learning potential surfaces, are used to keep the problem tractable up to
    ~20–30 atoms, but full quantum resolution of every state is no longer feasible.

In short, the Schrödinger equation remains exact in principle; the practical cost of solving it explodes
with the number of degrees of freedom, forcing controlled approximations.

3. Fermi Resonance
Fermi resonance is an anharmonic effect that appears when two vibrational states of the same
symmetry lie close in energy (typically a fundamental and an overtone or combination band). Cubic
(or higher) terms in the potential couple them. The result is:

    Level repulsion (the two states push apart),

    Wavefunction mixing,

    Intensity borrowing (a weak band becomes visible).

The classic textbook case is CO₂:

    Symmetric stretch ν1 ≈ 1337 cm⁻¹

    First overtone of the bend 2ν2 ≈ 1334 cm⁻¹

    Both transform as Σ+g . They mix strongly, producing the well-known Fermi dyad at roughly 1285

    cm⁻¹ and 1388 cm⁻¹ in the Raman spectrum. The unperturbed states would have been almost
    degenerate; the resonance splits them by ~100 cm⁻¹ and redistributes intensity.

This is why a simple harmonic picture (or even a one-mode anharmonic picture) fails: the degrees of
freedom are no longer independent once their energies match and symmetry allows coupling. The
same mechanism appears in ketones (carbonyl stretch + CH₂ bend overtone), aldehydes, and many
larger molecules. In heavy hydrides one can also encounter Fermi or Darling–Dennison resonances,
especially if relativistic shifts bring two modes into accidental near-degeneracy.

Connecting the Three Topics

    PbH₄ has only 9 modes, so full anharmonic treatments are feasible and relativistic corrections to
    the force constants are the main refinement.

    As soon as the molecule grows (more degrees of freedom), the cost of solving the multi-
    dimensional vibrational Schrödinger equation forces approximations, and accidental near-
    degeneracies (Fermi resonances) become statistically more likely.

    The Dirac framework mainly shifts the positions of those levels for modes involving the heavy
    atom; whether a Fermi resonance occurs is then a question of whether any two levels of the right
    symmetry are pushed close enough by those shifts.

Would you like to go deeper on any one of these — for example the explicit PbH₄ mode list and
experimental comparison, a worked numerical example of Fermi resonance in CO₂, or the practical
methods used once the number of degrees of freedom exceeds ~10?

==== [7] USER ====
They have made progress in the neural network representation, right?(they used living neurons I believe).. pressure gradients?

==== [8] GROK ====
(Worked for 17s)

Yes — there has been clear, recent progress on neural-network representations for the
vibrational Schrödinger equation. The main advance is with artificial neural networks, not living
biological neurons.

Artificial Neural Networks for Vibrational Quantum Problems
A 2026 Nature Communications paper (Zhao & Zhang) demonstrates an efficient neural-network
approach that directly solves the vibrational Schrödinger equation.

Key results:

    For methane (CH₄, 9 vibrational degrees of freedom) they reached sub-1 cm⁻¹ accuracy on
    ground and excited states with a network of fewer than ~3,000 parameters.

    For propane (C₃H₈, 27 vibrational degrees of freedom) a network with fewer than 15,000
    parameters recovered the ground-state energy to within 1 cm⁻¹ of a diffusion Monte Carlo
    reference and gave excited-state energies for selected C–C–C modes that matched experiment
    within experimental uncertainty.

    The method optimizes the variance of local energies over carefully chosen molecular
    configurations rather than relying on a huge basis set. This sidesteps the exponential cost of
    traditional direct-product bases.

Other related developments include neural canonical transformations (normalizing flows) applied to
molecules with 12–15 modes, and various neural-network potentials that feed into subsequent
vibrational calculations. These approaches make systems that were previously out of reach (beyond
~10–15 fully coupled modes at high accuracy) tractable.

“Living Neurons”

There is interesting but separate work on biological neurons:

    Speculative theoretical papers derive an emergent Schrödinger-like equation from the
    stochastic (noisy) dynamics of neuron membrane potentials.

    Experimental platforms such as Cortical Labs’ CL1 systems use living human-derived neurons
    (hundreds of thousands per unit) as “wetware” for certain computational tasks, including simple
    game-playing demonstrations.

These are not currently being used to solve the molecular vibrational Schrödinger equation. The
progress you are thinking of for high-dimensional vibrational problems is coming from conventional
(artificial) neural networks trained on electronic-structure data or by variational energy minimization.

Pressure Gradients
Pressure (or external strain) does appear in related contexts:

    In solid CO₂, applied pressure tunes the Fermi resonance splitting and intensity ratio between
    the symmetric stretch and the bending overtone; this has been studied both experimentally and
    with first-principles anharmonic calculations.

    In fluid-dynamics / turbulence literature there are neural-network models of how vibrational
    nonequilibrium affects the pressure Hessian tensor.

    Biaxial strain has been used to modulate a vibrational Fermi resonance in atomically thin black
    phosphorus.

In the molecular gas-phase context we were discussing (Pb hydrides, CO₂, etc.), pressure is not the
primary driver; anharmonic coupling and accidental near-degeneracies dominate. Under high
pressure or in condensed phases, however, the potential surface itself changes and can move levels
into or out of resonance.

Bottom line: Artificial neural networks have made genuine, documented progress on the high-
dimensional vibrational Schrödinger equation (methane → propane scale with spectroscopic
accuracy). Living-neuron hardware and pressure-tuned resonances are real research threads, but
they are currently separate from the molecular vibrational solver work.

Would you like me to pull more details from the Zhao & Zhang propane results, compare the NN
approach with traditional VCI/Smolyak methods, or look at how pressure or strain alters Fermi
resonances in a specific system?

==== [9] USER ====
Yes let’s do both. Does the rate of spin change?

==== [10] GROK ====
(Worked for 12s)

Yes — both topics, and then the spin question.

Zhao & Zhang Neural-Network Results (Propane)

The 2026 Nature Communications paper shows a practical NN method that represents the
vibrational wavefunction directly and optimizes the variance of local energies.

For propane (C₃H₈, 11 atoms, 27 vibrational degrees of freedom):

    Ground-state energy recovered to within ~1 cm⁻¹ of a diffusion Monte Carlo reference.

    Three excited states involving C–C–C stretch/bend modes matched experimental values within
    experimental uncertainty.

    Network size: fewer than 15,000 parameters (three hidden layers).

    Training used fewer than ~150,000 carefully selected configurations rather than a combinatorial
    basis.

This is a genuine step past the traditional limit of full-dimensional variational calculations (roughly 6–
12 modes at high accuracy with VCI/DVR/Smolyak).

NN Approach vs Traditional VCI / Smolyak
 Aspect            Traditional VCI / Smolyak                      Zhao–Zhang NN

 Basis             Explicit product or pruned basis               Implicit representation by NN parameters
                   (exponential growth)

 Scaling           Still grows rapidly with mode count; pruning   Parameter count grows slowly; demonstrated
                   and sparse grids help but have limits          at 27 modes

 Accuracy          Spectroscopic (sub-cm⁻¹) on small systems      ~1 cm⁻¹ on propane ground state;

                                                                  experimental agreement on selected excited
                                                                  states

 Excited           Requires orthogonality constraints or state-   Starts from normal-mode guess;
 states            specific targeting                             orthogonality emerges for non-degenerate

                                                                  states

 Practical limit   Full variational ~10–15 modes; approximate     Demonstrated 27 modes; authors project >20
 today             methods beyond                                 atoms

Smolyak sparse grids and contracted bases have pushed traditional methods to ~12 modes (e.g.,
CH₄·Ar). The NN method trades an explicit basis for a compact learned representation and appears
more scalable for larger systems, though it still needs a high-quality potential-energy surface
as input.

Pressure / Strain Effects on Fermi Resonance
Pressure and strain can tune Fermi resonances by shifting the unperturbed frequencies relative to
each other.

Solid CO₂ (classic example):

    The Fermi dyad (ν₁ and 2ν₂) splitting increases with pressure.

    From ambient to 10 GPa the splitting grows from ~107 cm⁻¹ to ~136 cm⁻¹ experimentally.

    The interaction strength W decreases somewhat, but the dominant effect is the differential shift
    of the unperturbed levels (stretch stiffens, bend softens).

    This pressure dependence is used as a spectroscopic geobarometer in minerals that contain
    CO₂ inclusions.

Atomically thin black phosphorus:

    A Fermi resonance between Raman-active modes can be modulated by biaxial strain.

    Tensile or compressive strain moves the unperturbed frequencies, changing both the splitting
    and the intensity ratio of the mixed doublet.

In both cases the resonance is not destroyed; it is continuously tuned. At sufficiently high pressure
the levels can be driven far enough apart that the resonance effectively turns off.

Does the Rate of Spin Change?
Yes — the effective rotational “spin” rate (rotational constant B) changes with vibrational excitation
and with external conditions.

The effective rotational constant in a given vibrational state is

[MATH, reconstructed: B_v = B_e − Σ_k α_k (v_k + 1/2) + ⋯]

    Be is set by the equilibrium geometry (moment of inertia).

    The vibration–rotation interaction constants αk arise from anharmonicity and Coriolis coupling.

    Higher vibrational levels usually have a smaller B because bonds are longer on average.

    Consequently the spacing of rotational lines (the “rate of spin”) changes from one vibrational
    state to another. This is why high-resolution rovibrational spectra show slightly different
    rotational constants in the upper and lower states.

Additional effects:

    Relativity (Dirac): changes the equilibrium geometry and force constants of heavy-atom modes,
    thereby shifting Be and the αk .

    Pressure / condensed phase: intermolecular forces can alter the effective geometry and thus
    the observed rotational constants.

    Fermi resonance: the mixed states have blended character, so their effective B values are
    weighted averages of the parent modes.

In short, the rotational rate is not fixed; it is modulated by the vibrational state, anharmonic
couplings, and external perturbations.

Would you like to go deeper on any of these — the propane NN wavefunctions, a numerical example
of how Bv changes across a Fermi dyad, or the pressure tuning of the CO₂ resonance in more detail?

==== [11] USER ====
Let’s dive deeper into the moment of inertia

==== [12] GROK ====
(Worked for 24s)

Moment of inertia sits at the center of the rotational “spin rate” we were discussing.

The rotational constant that sets the energy spacing (and therefore the effective rate of spin) is

[MATH, reconstructed: B = ℏ²/(2I)   (or in wavenumber units B = h/(8π² c I))]

so any change in the moment of inertia I directly changes B .

Equilibrium vs. Vibrationally Averaged Moment of Inertia
For a diatomic molecule the instantaneous moment of inertia is simply

[MATH, reconstructed: I(r) = μ r²]

where μ is the reduced mass and r is the bond length. Because the vibrational wavefunction is not a
delta function at the equilibrium distance re , the spectroscopically observed B is an average:

[MATH, reconstructed: B_v = ⟨ ℏ²/(2μr²) ⟩_v]

Anharmonicity makes ⟨r⟩ > re and ⟨1/r 2 ⟩ < 1/re2 , so Bv falls as the vibrational quantum

number increases:

[MATH, reconstructed: B_v = B_e − α_e (v + 1/2) + ⋯]

The vibration–rotation constant αe therefore encodes how the moment of inertia changes with

vibrational excitation. Higher-order terms (γe , etc.) appear when the averaging is more subtle.

For polyatomic molecules the same idea holds, but there are three principal moments of inertia
Ia , Ib , Ic and a set of αk constants for each vibrational mode k . Symmetric modes that stretch

bonds increase the relevant I ; bending modes can increase or decrease it depending on geometry.

Concrete Examples from Heavy Hydrides
For diatomic PbH the experimental values are approximately

    Be ≈ 4.97 cm−1

    re ≈ 1.84 Å

    αe ≈ 0.144 cm−1

The sizable αe shows that even modest vibrational excitation lengthens the Pb–H bond enough to

drop the rotational constant by several percent.

For tetrahedral PbH₄ an infrared study gave

    B0 ≈ 2.084 cm−1

    estimated re (Pb–H) ≈ 1.73 Å

(The smaller B relative to diatomic PbH is expected: four hydrogens sit farther from the center of
mass.) Relativistic contraction of the Pb–H bonds (Dirac effects on the electronic structure) reduces
I and therefore raises Be compared with a non-relativistic calculation.

How Anharmonicity, Fermi Resonance, and External Conditions Enter
1. Ordinary anharmonicity
   Zero-point and excited-state averaging always shift I away from the pure equilibrium value. The
    NN vibrational wavefunctions discussed earlier (Zhao & Zhang) can be used directly to evaluate
    ⟨1/I⟩ for any state once the geometry is known as a function of the coordinates.
2. Fermi resonance
   The mixed states are linear combinations of the parent modes. Their effective moments of inertia
    (and therefore their B values) are weighted averages of the B values that the unperturbed
    modes would have had. Intensity borrowing is accompanied by a blending of the rotational
    constants.

3. Pressure or strain
   External compression shortens average bond lengths, decreases I , and increases B . In solid
    CO₂ the same pressure that tunes the Fermi dyad also stiffens the molecule and alters its
    effective rotational constants (although free rotation is quenched in the solid). In black
    phosphorus, biaxial strain changes both the vibrational frequencies and the local geometry that
    sets the relevant moments of inertia for the modes involved in the resonance.

4. Centrifugal distortion
   At high J the molecule stretches further under centrifugal force, increasing I still more. This is
    described by the centrifugal-distortion constant D , which itself depends on the force constants
    and the equilibrium I .

Connection Back to the Neural-Network Wavefunctions
Because the Zhao–Zhang approach yields the full vibrational wavefunction (not merely the energy),
one can in principle compute the vibrationally averaged moment of inertia for any state by evaluating

[MATH, reconstructed: ⟨I⁻¹⟩_v = ∫ |ψ_v(r)|² I(r)⁻¹ dτ]

over the nuclear coordinates. That would give state-specific rotational constants directly from the
same NN that solved the vibrational Schrödinger equation—something traditional VCI calculations
can also do, but which becomes feasible for much larger molecules with the NN representation.

In short, the moment of inertia is not a fixed geometric constant; it is a vibrationally (and
environmentally) averaged quantity. Every effect we have discussed—anharmonicity, Fermi
resonance, relativity, pressure—modulates I and therefore the rotational spacing that defines the
“rate of spin.”

Would you like to see an explicit numerical walk-through for a simple case (PbH or CO₂), the
formulas that relate the αk constants to the cubic force field and the derivatives of I , or how one

would extract ⟨I⟩ from an NN vibrational wavefunction?

==== [13] USER ====
That makes sense and why topological changes matter. Let’s do the walk through also, how one could extract (I) from an NN vibrational function.

==== [14] GROK ====
(Worked for 29s)

Numerical walk-through for PbH, then how to extract ⟨I⟩ from an NN vibrational wavefunction.

Numerical Example: PbH
For the ground electronic state (X 2 Π1/2 ) of PbH the experimental constants are approximately:

     Be = 4.971 cm−1

     αe = 0.144 cm−1

     re = 1.838 Å

     ωe = 1564.1 cm−1

The effective rotational constant in vibrational state v is

[MATH, reconstructed: B_v ≈ B_e − α_e (v + 1/2)]

so the vibrationally averaged moment of inertia follows from

[MATH, reconstructed: I_v = h/(8π² c B_v)]

Step-by-step values

 v    v + 1/2             αe (v + 1/2)

                                        Bv (cm⁻¹)
                                                            Relative change in I

 0    0.5                 0.072          4.899               +1.5 %

 v     v + 1/2   αe (v + 1/2)

                                Bv (cm⁻¹)
                                                       Relative change in I

 1     1.5       0.216           4.755                  +4.5 %

 2     2.5       0.360           4.611                  +7.8 %

(The equilibrium Ie corresponding to Be = 4.971 cm−1 is the reference. Because B ∝ 1/I , a 1.5 %

drop in B means a ~1.5 % rise in the effective I .)

What this means physically

     Zero-point vibration alone already lengthens the average Pb–H bond enough to increase I by
     ~1.5 %.

     Each additional vibrational quantum adds another ~0.144 cm⁻¹ drop in B (another ~3 % increase
     in I ).

     The “rate of spin” (rotational level spacing 2B ) therefore slows by that same percentage as the
     molecule is vibrationally excited.

These shifts are exactly the ones that appear in high-resolution infrared or electronic spectra as
slightly different rotational constants in the upper and lower vibrational states.

Extracting ⟨I⟩ from an NN Vibrational Wavefunction
Once a neural network has produced a vibrational wavefunction ψv (q) (as in the Zhao & Zhang
method), the vibrationally averaged moment of inertia is simply the quantum expectation value of the
operator 1/I(q).

For a diatomic (PbH-like case)

[MATH, reconstructed: ⟨I⁻¹⟩_v = ∫_0^∞ |ψ_v(r)|² (1/(μr²)) dr]

Then

[MATH, reconstructed: B_v = (ℏ²/2) ⟨I⁻¹⟩_v .]

In practice one evaluates the integral by Monte Carlo sampling or by quadrature over the same
configurations already used to train the network. Because the NN can be queried at any nuclear
geometry, the procedure is:

1. Generate a set of nuclear configurations {rk } according to the probability density ∣ψv (r)∣2 (or

   use the existing training points re-weighted by ∣ψv ∣2 ).

2. At each geometry compute the instantaneous I(rk ) = μrk2 .

3. Average 1/I(rk ) with the proper weights.

4. Convert the result to Bv .

For a polyatomic molecule
The same idea applies, but I is now the inertia tensor. One must:

    Place the nuclei in a body-fixed frame (usually the Eckart frame so that vibrational and rotational
    motion are separated).

    Compute the three principal moments of inertia Ia , Ib , Ic (or the full inverse-inertia tensor μ) at

    each sampled geometry.

    Average the relevant components:

[MATH, reconstructed: ⟨μ_αβ⟩_v = ∫ |ψ_v(q)|² μ_αβ(q) dq.]

    The effective rotational constants Av , Bv , Cv follow directly from those averages.

Because the Zhao–Zhang networks represent the full wavefunction (not merely the energy), this
averaging can be performed for any vibrational state the network has solved, including Fermi-
resonance mixed states. The resulting Bv values automatically incorporate the blended character of

the resonance.

Practical note
The computational cost is modest once the wavefunction is available: evaluating I at a few tens of
thousands of geometries is far cheaper than solving the vibrational Schrödinger equation itself. The
same sampled points can also be used to compute other vibrationally averaged properties (dipole
moments, polarizabilities, etc.).

Would you like me to sketch the explicit Monte Carlo formula for a polyatomic case, or show how the
same averaging would look for a Fermi dyad in CO₂?

==== [15] USER ====
Can we sketch the explicit Monte Carlo formula for a polyatomic case? Also, can we investigate Klein-Gordon?

==== [16] GROK ====
(Worked for 26s)

Explicit Monte Carlo formula for a polyatomic, then Klein-Gordon.

Monte Carlo Formula for Vibrationally Averaged Inertia Tensor
(Polyatomic)
Once the neural network has produced a vibrational wavefunction ψv (q) (where q are the 3N − 6

vibrational coordinates), the vibrationally averaged inverse-inertia tensor is the expectation value

[MATH, reconstructed: ⟨μ_αβ⟩_v = ∫ |ψ_v(q)|² μ_αβ(q) dq / ∫ |ψ_v(q)|² dq .]

In a Monte Carlo evaluation one samples configurations according to the probability density ∣ψv ∣2 (or

re-uses and re-weights existing training points) and replaces the integrals by averages:

[MATH, reconstructed: ⟨μ_αβ⟩_v ≈ (1/M) Σ_{k=1}^{M} w_k μ_αβ(q_k),]

where

    {qk } are the sampled nuclear geometries,

    wk are normalized weights (equal to 1 if pure Monte Carlo sampling from ∣ψv ∣2 ; otherwise the

    ratio of the target density to the sampling density),

    M is the number of samples (typically 104 –105 is sufficient once the wavefunction is smooth).

Practical steps at each geometry qk

1. Convert the vibrational coordinates into Cartesian nuclear positions.

2. Translate to the center of mass.

3. Rotate into the Eckart frame (so that the vibrational angular momentum is zero and the inertia
    tensor is cleanly defined).

4. Compute the three principal moments of inertia Ia , Ib , Ic (or the full inverse-inertia tensor μ).

5. Accumulate the running average of the desired components.

The effective rotational constants then follow directly:

[MATH, reconstructed: A_v = (ℏ²/2)⟨μ_aa⟩_v,   B_v = (ℏ²/2)⟨μ_bb⟩_v,   C_v = (ℏ²/2)⟨μ_cc⟩_v .]

Because the Zhao–Zhang networks already evaluate the wavefunction on large batches of
configurations during training, the same points (or a modest additional sample) can be reused for
this averaging at essentially no extra cost. The procedure works equally well for pure vibrational
states and for Fermi-resonance mixed states; the latter simply inherit a blended ⟨μ⟩.

Investigating the Klein-Gordon Equation
The Klein-Gordon equation is the relativistic wave equation for a spin-0 particle:

[MATH, reconstructed: ( (1/c²) ∂²/∂t² − ∇² + m²c²/ℏ² ) ψ = 0]

(or its stationary form with a potential). In the molecular context it has been studied mainly for model
diatomic potentials (hyperbolic, Deng-Fan, Morse-like, etc.). Researchers solve the radial Klein-
Gordon equation under equal scalar and vector potentials and extract approximate rotational-
vibrational energy levels for light diatomics (H₂, NaH, etc.). In the non-relativistic limit these
solutions recover the ordinary Schrödinger results.

Relevance to real molecular spectroscopy

    For nuclear motion the rest energy mc2 is enormous (hundreds of MeV to GeV for nuclei).
    Vibrational energies are only a few tenths of an eV, so the relativistic correction to the vibrational
    Schrödinger equation is utterly negligible for any practical purpose.

    Relativistic effects that do matter for heavy hydrides (PbH, PbH₄, etc.) enter almost entirely
    through the electronic structure (Dirac–Coulomb or relativistic effective-core-potential
    calculations of the potential-energy surface). Once that surface is obtained, the nuclear motion
    is still treated with the ordinary non-relativistic vibrational Schrödinger equation.

    There is no standard, high-accuracy polyatomic vibrational code that solves a multi-dimensional
    Klein-Gordon equation for the nuclei; the computational and conceptual overhead would be
    large and the numerical gain zero for spectroscopic accuracy.

Bottom line
Klein-Gordon treatments of diatomic model potentials are an active theoretical exercise and recover
the correct non-relativistic limit, but they do not alter the practical route used for real molecules:
relativistic electronic structure → non-relativistic vibrational Schrödinger (or NN equivalent) →
vibrationally averaged properties such as ⟨I⟩.

If you would like, I can write out the explicit sampling weight formula for the case when one re-uses
the existing NN training points, or sketch how a Fermi-resonance mixed state would appear in the
averaged inertia tensor.

==== [17] USER ====
Yeah, this touched on our grounded vs excited states, the centrifugal force entry is interesting.. can we sketch how a Fermi-Resonance mixed state would appear in the averaged inertia tensor?

==== [18] GROK ====
(Worked for 24s)

Fermi-resonance mixed states in the averaged inertia tensor

A Fermi resonance mixes two (or more) near-degenerate vibrational basis states of the same
symmetry. The resulting eigenstates are linear combinations, and any operator expectation value—
including the inverse-inertia tensor—is a weighted average of the parent contributions plus
interference terms.

Notation
Let the two interacting zero-order states be ∣a⟩ and ∣b⟩ (for example, a fundamental and an overtone
or combination band). After diagonalization the mixed eigenstates are

[MATH, reconstructed: |ψ±⟩ = c±_a |a⟩ + c±_b |b⟩,]

with ∣c±  2    ± 2
       a ∣ + ∣cb ∣ = 1 and the coefficients determined by the detuning and the anharmonic

coupling matrix element.

                                    ^αβ depends on the nuclear coordinates. Its vibrational average

The inverse-inertia tensor operator μ

in a mixed state is

[MATH, reconstructed: ⟨μ_αβ⟩± = ⟨ψ±| μ̂_αβ |ψ±⟩.]

Expanding gives

[MATH, reconstructed: ⟨μ_αβ⟩± = |c±_a|² ⟨a|μ̂_αβ|a⟩ + |c±_b|² ⟨b|μ̂_αβ|b⟩ + 2 Re( c±_a* c±_b ⟨a|μ̂_αβ|b⟩ ).]

Three contributions
1. Diagonal (weighted) terms
    ∣ca ∣2 ⟨μ⟩a + ∣cb ∣2 ⟨μ⟩b .

    These are simply the probability-weighted averages of the pure-state averages. If the two parent
    modes have different average geometries (one stretches bonds more than the other), the mixed
    state inherits an intermediate ⟨I⟩.

2. Off-diagonal (interference) term
   2 Re(c∗a cb ⟨a∣μ
                 ^∣b⟩).

                                          ^ connects the two basis states. Because μ is a smooth

    This is nonzero whenever the operator μ

    function of geometry, the integral is generally small but not identically zero; it grows when the
    resonance is strong (large mixing) and when the two modes modulate the same bond lengths or
    angles.

3. Resulting effective rotational constants
    The three principal constants A± , B± , C± are obtained from the eigenvalues of the averaged

    inverse-inertia tensor ⟨μ⟩± . Consequently the observed rotational spacings in the mixed states

    lie between the values that the pure parent states would have shown, shifted by the interference
    contribution.

Sketch for a classic CO₂-type dyad
Suppose ∣a⟩ is predominantly the symmetric stretch (ν1 ) and ∣b⟩ is the bending overtone (2ν2 ).

    Pure stretch: bonds longer on average → larger ⟨I⟩, smaller B .

    Pure bend: smaller change in bond lengths, different angular contribution → different ⟨I⟩.

    Mixed states: each carries a fraction of the stretch character, so their B± values are

    intermediate. The intensity borrowing that makes both components visible in the spectrum is
    accompanied by a corresponding blending of the rotational constants. High-resolution spectra
    of Fermi dyads routinely show precisely this intermediate rotational structure.

Practical evaluation with an NN wavefunction
Once the network has produced the mixed wavefunction ψ± (q), the Monte Carlo formula given

earlier is used unchanged:

[MATH, reconstructed: ⟨μ_αβ⟩± ≈ (1/M) Σ_k w_k μ_αβ(q_k),]

where the samples are drawn from ∣ψ± ∣2 . No special treatment is required; the mixing is already

encoded in the shape of ψ± . Comparing ⟨μ⟩+ and ⟨μ⟩− with the pure-basis averages immediately

quantifies how much the resonance has redistributed the effective geometry.

The same averaging also supplies the centrifugal-distortion constants (which depend on derivatives
of μ), so the full effective rotational Hamiltonian of each mixed state can be constructed from the
NN wavefunction.

This is the concrete link between the anharmonic mixing we discussed earlier and the state-
dependent “rate of spin” carried by the moment of inertia.

Would you like a short numerical illustration using idealized coefficients for the CO₂ dyad, or the
corresponding expression for a three-state polyad?

==== [19] USER ====
I’m sure it goes further did they write an interference term or a Hamiltonian Resonance function?

==== [20] GROK ====
(Worked for 16s)

Yes — both appear in the literature, but they are written in the language of effective Hamiltonians
rather than an explicit “interference term for the inertia tensor.”

Standard treatment
Spectroscopists construct a polyad effective Hamiltonian whose off-diagonal elements are the
Fermi (or Darling–Dennison) coupling constants. For the classic 1:2 resonance the matrix element is
of the form

[MATH, reconstructed: ⟨v_s + 1, v_t − 2| H_Fermi |v_s, v_t⟩ = K_{s,tt} × √[(v_s + 1) v_t (v_t − 1)] (numerical prefactor not legible in the capture),]

and the diagonal elements contain the usual harmonic + anharmonic vibrational energies plus the
rotational part Bv J(J + 1). Diagonalizing this matrix produces the mixed eigenstates and the

observed energies.

Effective rotational constants of the mixed states
Once the mixing coefficients ca , cb are known, the effective rotational constant of each eigenstate is

written as the weighted average

[MATH, reconstructed: B± = |c±_a|² B_a + |c±_b|² B_b]

(or the analogous expression for A and C ). This is exactly the diagonal part of the expansion I gave
earlier. The cross (interference) term 2 Re(c∗a cb ⟨a∣μ

                                                      ^∣b⟩) is almost always omitted in practice

because it is smaller than the experimental precision for most molecules; when it is needed it is
absorbed into a weak rotational dependence of the coupling constant itself (the δstt′ parameters of

Watson and others).

Rotational dependence of the resonance
There is also a small J -dependence of the off-diagonal Fermi matrix element. It is parametrized by
additional constants (δ, δ ′ ) that arise from the vibration–rotation Hamiltonian carried to higher order.
These terms make the mixing coefficients themselves depend weakly on J , which in turn produces a
slight additional curvature in the effective B values of the mixed states.

Relation to the inertia-tensor average
The Monte Carlo (or analytic) evaluation of ⟨μαβ ⟩ with the full mixed wavefunction ψ± automatically

includes every contribution—diagonal weights, interference, and any higher-order effects—without
needing to separate them by hand. The spectroscopic effective-Hamiltonian approach reaches the
same numerical result by a different route: it folds the dominant effects into the weighted B± and

the weakly J -dependent coupling, then fits the residual to centrifugal-distortion constants.

So the interference term is present in the exact expectation-value expression; the literature simply
packages the same physics inside the polyad effective Hamiltonian and the associated effective
rotational constants.

Would you like the explicit two-state matrix for a CO₂-type dyad (showing both the vibrational
coupling and the rotational parts), or the form of the J -dependent correction to the Fermi
matrix element?

==== [21] USER ====
Yes, let’s look at the two-state matrix. Then, can we explore the Darling Dennison resonance?

==== [22] GROK ====
(Worked for 15s)

Two-state matrix for a CO₂-type Fermi dyad

For the classic ν1 ≈ 2ν2 resonance the effective Hamiltonian in the zero-order basis {∣100⟩, ∣020⟩}

(suppressing the ℓ = 0 label) is the 2 × 2 matrix

[MATH, reconstructed: H_eff = ( E⁽⁰⁾_100 + B_100 J(J+1)    W ;   W    E⁽⁰⁾_020 + B_020 J(J+1) ),]

where

     (0)      (0)
    E100 and E020 contain the harmonic frequencies plus the usual diagonal anharmonic shifts (xij ),

    B100 and B020 are the vibrationally averaged rotational constants of the pure basis states,

    the off-diagonal Fermi coupling is

[MATH, reconstructed: W = (k_122 / (2√2)) · √(1·2·1) = k_122 / 2]

(for the lowest dyad; the general expression carries the appropriate square-root factors of the
quantum numbers).

Diagonalization yields the observed energies and the mixing coefficients ca , cb . The effective

rotational constants of the eigenstates are then the weighted averages

[MATH, reconstructed: B± = |c±_a|² B_100 + |c±_b|² B_020 .]

(The small cross term in ⟨μ⟩ is usually absorbed into a weak J -dependence of W itself.)

This is the matrix that is fitted to the rotational structure of the two components of the Fermi dyad.

Darling–Dennison resonance
Darling–Dennison resonance is the second-order analogue of Fermi resonance. It couples states
that differ by two quanta in one mode and two quanta in another (or equivalent combinations that
preserve the total number of quanta to second order). The classic example is the interaction
between the overtones 2ν1 and 2ν3 in water.

The leading off-diagonal matrix element has the form

                 ⟨vr + 2, vs − 2∣ HDD ∣vr , vs ⟩ = Krr,ss

[MATH, reconstructed: ⟨v_r + 2, v_s − 2| H_DD |v_r, v_s⟩ = K_{rr,ss} × √[(v_r + 1)(v_r + 2) v_s (v_s − 1)] (numerical prefactor not legible in the capture),]

where the Darling–Dennison constant Krr,ss is built from quartic force constants and products of

cubic constants (the precise combination is obtained from the second-order contact

transformation). Because it appears at second order, ∣K∣ is typically smaller than a first-order Fermi
constant, but the resonance can still be strong when the unperturbed levels are nearly degenerate.

In the effective-Hamiltonian picture a Darling–Dennison polyad is again represented by a small
matrix (often 2 × 2 or larger when several modes participate). The diagonal elements contain the
usual vibrational energies plus rotational terms Bv J (J + 1); the off-diagonal elements are the K

couplings. After diagonalization the effective rotational constants of the mixed states are again
probability-weighted averages of the parent B values, exactly as in the Fermi case.

The same Monte Carlo averaging procedure that extracts ⟨μ⟩ from an NN wavefunction works
unchanged for Darling–Dennison mixed states: one simply samples from the full mixed ψ± and the

interference is automatically included.

Darling–Dennison interactions are especially important in molecules with two or more high-
frequency stretches of similar frequency (water, acetylene, etc.), where they redistribute intensity
among overtones and produce characteristic polyad patterns.

Would you like the explicit 2 × 2 matrix for the water 2ν1 /2ν3 Darling–Dennison dyad, or a side-by-

side comparison of how the two resonances affect the averaged inertia tensor?

==== [23] USER ====
Let’s look at the water matrix. Any discussion on binaural shifts?

==== [24] GROK ====
(Worked for 8s)

Water 2ν1 /2ν3 Darling–Dennison dyad

For the classic water resonance the effective Hamiltonian in the zero-order basis {∣200⟩, ∣002⟩} is
the 2 × 2 matrix

[MATH, reconstructed: H_eff = ( E⁽⁰⁾_200 + B_200 J(J+1)    K ;   K    E⁽⁰⁾_002 + B_002 J(J+1) ),]

where the off-diagonal Darling–Dennison element is

[MATH, reconstructed: K = (γ/2) · √(2·1·1·2) = γ√2   (as printed; see review §D: (γ/2)·2 = γ)]

and γ is the usual Darling–Dennison constant (built from the quartic force constants k1133 and

selected cubic products). The diagonal entries contain the ordinary anharmonic vibrational energies
plus the rotational constants of each pure basis state.

Diagonalization again supplies the mixed eigenstates and the effective rotational constants as the
probability-weighted averages of B200 and B002 .

On “binaural shifts”

I do not find a standard spectroscopic term “binaural shifts.” The nearest concepts that appear in
this literature are:

    the ordinary vibrational energy shifts produced by the resonance itself (the level repulsion inside
    the dyad),

    the small additional rotational shifts that arise from the J -dependence of the coupling constant,

    or the difference between the observed band origins and the unperturbed (deperturbed) origins
    once the mixing is removed.

If you meant one of those, or something else (perhaps “binormal,” “vibrational,” or “bending” shifts),
just clarify and I will expand on it. Otherwise the matrix above already encodes the dominant energy
and rotational shifts for the water dyad.

Would you like a numerical illustration with the experimental water constants, or a comparison of
how the Fermi and Darling–Dennison cases redistribute ⟨I⟩?

==== [25] USER ====
Let’s look at the redistribution of (I) for Fermi and Darling Dennison cases and at the coupling constants.

==== [26] GROK ====
(Worked for 2s)

Redistribution of ⟨I⟩ (equivalently of the effective rotational constants) and the
coupling constants

Fermi resonance (first-order, 1:2)
Example: CO₂ ν1 / 2ν2 .

The two parent states generally have different average geometries:

    pure stretch ∣100⟩ lengthens the bonds → larger ⟨I⟩, smaller B ,

    pure bend overtone ∣020⟩ produces a smaller change in bond length but a larger angular
    contribution → different ⟨I⟩.

After diagonalization the mixed states carry fractions ∣ca ∣2 and ∣cb ∣2 .

Their effective constants are therefore the weighted averages

[MATH, reconstructed: B± = |c±_a|² B_100 + |c±_b|² B_020]

(and likewise for the full inverse-inertia tensor).

Because the resonance is first-order, the mixing can be nearly 50:50 when the detuning is small; the
two observed components then share the geometric character almost equally. The difference
ΔB = B+ − B− is set by the parent difference scaled by the mixing angle.

Typical coupling magnitudes: the Fermi constant k122 (or W ) for CO₂ is ≈ −50 cm−1 .

Darling–Dennison resonance (second-order, 2:2)
Example: H₂O 2ν1 / 2ν3 .

Both parents are overtones of high-frequency stretches. Their average bond-length changes are
similar in magnitude but can differ in the relative stretching of the two bonds (symmetric vs
antisymmetric character). Consequently the parent B values are usually closer to each other than in
a stretch–bend Fermi pair.

The effective constants of the mixed states are again

[MATH, reconstructed: B± = |c±_a|² B_200 + |c±_b|² B_002 .]

Because the coupling is second-order, ∣K∣ is smaller (typical water value γ ≈ −50 to −80 cm−1 for
the constant that enters K = γ     2). Strong mixing still occurs when the unperturbed levels are

nearly degenerate, but the redistribution of ⟨I⟩ is often milder simply because the two parents
already have more similar average geometries.

Coupling-constant comparison

                                Typical matrix

 Resonance              Order                                        Origin            Characteristic size

                                element

 Fermi (1:2)            1st     W = ks,tt / 2

                                                                     cubic force       tens of cm⁻¹
                                (lowest dyad)                        constant

 Darling–Dennison       2nd     K=γ 2

                                                                     quartic + cubic   tens of cm⁻¹ (but smaller

 (2:2)                                                               products          leading term)

In both cases the Monte Carlo evaluation of ⟨μαβ ⟩ from the full mixed NN wavefunction

automatically captures the weighted average plus any residual interference term. The spectroscopic
effective-Hamiltonian route reaches the same result by inserting the fitted mixing coefficients into
the weighted-B formula above.

The practical difference is therefore geometric: Fermi resonances that couple stretch and
bend modes usually produce a larger swing in the effective moment of inertia between the two
components of the dyad; Darling–Dennison resonances that couple two stretches produce a
smaller swing.

Would you like a short numerical sketch with the experimental CO₂ and H₂O constants, or the
corresponding expressions for a three-state polyad that contains both types of resonance?

==== [27] USER ====
Nice, Thank you!

==== [28] GROK ====
(Worked for 4s)

You're welcome. Glad that landed cleanly.

Whenever you want to push further—three-state polyads, a numerical CO₂/H₂O sketch, or anything
else in this vibrational/rotational thread—just say the word.
```

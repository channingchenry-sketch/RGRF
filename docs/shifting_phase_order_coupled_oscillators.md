# Shifting phase order as the phase relationship between coupled oscillators

- **Definition (Channing, verbatim, H285n widget answer, 2026-10-25):** "The phase relationship between coupled oscillators". In RGRF, **"shifting phase order" means the phase relationship between coupled oscillators**: which one leads, by how much, and how that offset shifts.
- **Linked both ways:** [shifting_phase_order_review.md](shifting_phase_order_review.md) · [degrees_of_freedom_shifting_phases_review.md](degrees_of_freedom_shifting_phases_review.md) · [oscillator_ratchet_array_review.md](oscillator_ratchet_array_review.md)
- **Sim:** [sims/coupled_oscillator_phase_order_sim.py](../sims/coupled_oscillator_phase_order_sim.py) ([output](../sims/coupled_oscillator_phase_order_sim_output.txt)). Textbook illustrations.
- **Labels:** **Grounded** / **Plausible-untested** / **Speculative** / **Symbolic**. License CC0.
- **Ledger rule:** locking and synchrony *redistribute* energy between oscillators and in angle. They never create it.

## 0. Channing's recurring words

- **2026-10-15:** "This is part of our foundation and we can say as much in our framework as well as shifting phase order. Now we can save and pause. We will expand later, thank you!" ([grok_archive/2026-10-15_exploring_miller_setterfield.md](grok_archive/2026-10-15_exploring_miller_setterfield.md) l. 129). Grok's reply framed it as "the locked relationship itself is a controllable variable, not a fixed outcome" (l. 144). This definition confirms that reading.
- **2026-10-15:** "can we explore floquet periodically driven topological phases?" ([shifting_phase_order_review.md](shifting_phase_order_review.md) l. 267, §F).
- **2026-10-17:** "Can we explore magnetic sail dynamics? Also, shifting phase order keeps popping into my head" ([grok_archive/2026-10-17_grassmann_vs_lorentz_force_laws.md](grok_archive/2026-10-17_grassmann_vs_lorentz_force_laws.md) l. 1141). Grok there: "which subsystem leads (magnetic, fluidic, …)" (l. 1459).
- **2026-10-22:** "Still nice to see that it matches our shifting phase order language" ([grok_archive/2026-10-22_casimir_repulsion_discussion.md](grok_archive/2026-10-22_casimir_repulsion_discussion.md) l. 200). That was the Boyer π-phase boundary reversal, a phase-relationship sign flip.

## 1. Two coupled oscillators (Grounded)

- **Huygens (1665):** two pendulum clocks hung from a common beam fell into **anti-phase** synchrony within about 30 minutes and recovered it after being disturbed. He called it "an odd kind of sympathy". The coupling runs through tiny beam motions. C. Huygens, letter to the Royal Society, Feb 1665 (*Œuvres complètes* vol. 5 [to verify]). Modern analysis: Bennett, Schatz, Rockwood & Wiesenfeld, *Proc. R. Soc. A* 458, 563 (2002) [to verify].
- **Normal modes:**
  - Two identical oscillators (ω₀) coupled by a spring have an **in-phase** mode at ω₀ and an **anti-phase** mode at √(ω₀² + 2κ).
  - Exciting one oscillator excites both modes. The energy then **swaps back and forth** at the beat frequency Δω = ω_anti − ω_in.
  - The sim gives 1.000 and 1.095 rad/s, a beat (swap) period of **65.8 s**.
- **The Adler equation (self-sustained oscillators):** dφ/dt = Δω − K sin φ (R. Adler, *Proc. IRE* 34, 351 (1946)).
  - **Locked** for |Δω| < K, at the fixed offset **φ\* = arcsin(Δω/K)**. The phase difference *shifts* as the detuning changes, reaching ±90° at the edge of lock.
  - **Outside lock** it shows **phase slips** at the rate √(Δω² − K²)/2π.
  - This is shifting phase order in its simplest exact form.

## 2. Mode-locking: Arnold tongues and the devil's staircase (Grounded)

- The **circle map** θₙ₊₁ = θₙ + Ω − (K/2π) sin 2πθₙ (V. I. Arnold, 1961/1965 [to verify]) has, for each rational p:q, a **tongue** in (Ω, K) where the winding number locks to p/q, i.e. n:m locking.
- At K = 1 the tongues fill the Ω axis up to a set of measure zero. The winding number vs Ω is a **devil's staircase**: Jensen, Bak & Bohr, PRA 30, 1960 (1984) [to verify].
- Seen in: Josephson junctions under microwaves (**Shapiro steps**, V = n·hf/2e; S. Shapiro, PRL 11, 80 (1963)), driven pendula, cardiac rhythms and the onset of turbulence.

## 3. Many oscillators: Kuramoto, chimeras and collective phase (Grounded)

- **Kuramoto model** (Y. Kuramoto 1975, *Lecture Notes in Physics* 39, 420 [to verify]; review: S. H. Strogatz, *Physica D* 143, 1 (2000)):
  - dθᵢ/dt = ωᵢ + (K/N) Σⱼ sin(θⱼ − θᵢ).
  - The order parameter is **r e^{iψ} = (1/N) Σ e^{iθⱼ}**.
  - Synchrony switches on at **K_c = 2/(πg(0))**. For a Lorentzian of half-width γ, K_c = 2γ and r = √(1 − K_c/K).
  - Synchrony is a phase transition *in phase space* ([degrees_of_freedom_shifting_phases_review.md §6](degrees_of_freedom_shifting_phases_review.md)).
- **Chimera states:** identical, non-locally coupled oscillators split into a synchronised group and an incoherent group. Kuramoto & Battogtokh, *Nonlinear Phenom. Complex Syst.* 5, 380 (2002); Abrams & Strogatz, PRL 93, 174102 (2004). Seen experimentally in metronomes (Martens et al., PNAS 110, 10563 (2013) [to verify]).
- **Examples:**
  - **Metronomes on a moving platform** sync in phase (J. Pantaleone, *Am. J. Phys.* 70, 992 (2002)).
  - **London Millennium Bridge (2000):** pedestrians locked to the lateral sway above a critical crowd size (Strogatz, Abrams, McRobie, Eckhardt & Ott, *Nature* 438, 43 (2005)).
  - **Fireflies** (*Pteroptyx*; Buck 1988 [to verify]).
  - **Cardiac pacemaker cells** in the sinoatrial node (Peskin 1975; Michaels et al. 1987 [to verify]).
  - **Circadian clocks:** about 20,000 suprachiasmatic-nucleus neurons coupled, then entrained by light (Winfree 1967/1980 [to verify]).

## 4. Engineered phase control (Grounded)

- **Injection locking:** a free-running oscillator locks to a weak injected signal within the Adler range. Used for lasers (slave-laser locking), magnetrons and spin-torque oscillators.
- **Phase-locked loops (PLL):** phase detector, loop filter and VCO. These lock radio and clock phase (de Bellescize 1932 [to verify]).
- **Josephson junction arrays:** coherent phase-locked arrays (Shapiro steps) form the **voltage standard**, about 10⁴–10⁵ junctions locked to one microwave source.
- **Phased arrays and beam steering:**
  - A progressive phase step Δφ between elements steers the beam to sin θ = Δφ·λ/(2πd).
  - **Coherent peak intensity grows as N²**, incoherent as N. The *total* radiated power is still N × (element power). Coherence only **redistributes it in angle**.
  - The sim prints N = 10: 100 vs 10; N = 100: 10⁴ vs 10².
- **Floquet driving** (§F of the review, l. 267): periodic driving of a coupled lattice creates effective (quasi-energy) band structures and topological phases. The drive's phase relative to the system sets the outcome (Oka & Aoki 2009; Lindner, Refael & Galitski, *Nat. Phys.* 7, 490 (2011) [to verify]).
- **Geometric (Pancharatnam–Berry) phase:** taking a system around a closed loop in parameter space adds a phase that depends only on the loop's geometry (solid angle), not on its duration. S. Pancharatnam, *Proc. Indian Acad. Sci. A* 44, 247 (1956); M. V. Berry, *Proc. R. Soc. A* 392, 45 (1984). Example: Foucault's pendulum precession. **Grounded**: a phase shift from geometry alone.

## 5. RGRF links (labelled)

| System | Phase-order reading | Label |
|---|---|---|
| **Hub motor and stator phase sequence** ([stator_review.md](stator_review.md)) | Three windings 120° apart: ABC gives a field rotating one way, and **swapping any two phases (ACB) reverses it**. Sim: \|B\| = 1.5 constant, ABC counter-clockwise, ACB clockwise. This is literally a *shifting phase order*, and the cleanest RGRF example. | **Grounded** |
| **Oscillator ratchet array** ([oscillator_ratchet_array_review.md](oscillator_ratchet_array_review.md)) | Kuramoto coupling plus asymmetric potentials; the relative phase sets the net drift direction (flashing or rocking ratchets) | **Grounded** in model; directed transport needs a driven, out-of-equilibrium source |
| **Multi-Egg gyros** ([em_topological_gravity_review.md](em_topological_gravity_review.md), [tennis_racket_theorem_review.md](tennis_racket_theorem_review.md)) | Counter-rotating or precessing rotors as coupled oscillators: relative phase sets net angular momentum (zero for anti-phase pairs) and vibration cancellation | **Plausible-untested**; total L conserved |
| **Magnetic sail** ([grassmann_ampere_pressure_sweep_review.md](grassmann_ampere_pressure_sweep_review.md)) | The phase of loop currents relative to the plasma flow and any injected plasma shapes the magnetosphere (Grok's l. 1407 framing) | **Plausible-untested** (mag-sail physics Grounded; phase control untested) |
| **Oloid spine track** ([oloid_magnetic_track_motor.md](oloid_magnetic_track_motor.md), [oloid_spine_lorentz_drive.md](oloid_spine_lorentz_drive.md)) | Sequenced coils along a track form a travelling wave (a linear-motor phase order); the phase step sets speed and direction | **Grounded** (linear motors); oloid geometry **Plausible-untested** |
| **Leaky bound-state family** ([leaky_bound_state_family.md](leaky_bound_state_family.md)) | Coupled leaky cavities: locking bandwidth ~ coupling K, against linewidth Γ = 1/τ. Lock needs K > \|Δω\| and coupling stronger than loss (strong coupling: K > Γ/2). | **Grounded** |
| **Boyer π-phase Casimir** (§E) | A boundary phase of π flips the force sign: a phase relation as a control | **Grounded** at nm scale; **Symbolic** beyond |
| Golden-ratio frequency ratios | φ is the "most irrational" winding number, the *last* to lock (a KAM golden-mean torus). So φ-tuned oscillators *resist* locking. | **Grounded** fact; RGRF use **Symbolic** |

## 6. Sim results (textbook illustrations)

**(a) Adler locking (K = 1):** φ\* = 30.0° at Δω = 0.5, 60.0° at 0.866 and 81.9° at 0.99. At Δω = 1.2 (outside lock) there were 4.19 slips in 40 s, against a theory value of 4.22 (period 9.47 s).

**(b) Circle map:** at K = 1 the 0:1 and 1:1 tongues are about 0.16 wide in Ω and the 1:2 tongue about 0.073. About 51 % of the Ω grid sat on detected plateaus at this resolution. Theory gives 100 % up to a measure-zero set, so this is a coarse-grid estimate.

**(c) Kuramoto, N = 100, Lorentzian γ = 0.5, so K_c = 1.0:**

| K | r (sim) | r (theory) |
|---|---|---|
| 0.5 | 0.11 | 0 |
| 1.0 | 0.19 | 0 |
| 1.5 | 0.57 | 0.58 |
| 2.0 | 0.75 | 0.71 |
| 3.0 | 0.83 | 0.82 |

Below K_c the finite-N value of r ≈ 1/√N is noise.

**(d) Three-phase stator:** swapping two phases reverses the rotating field (counter-clockwise to clockwise) at constant |B| = 1.5.

**(e) Energy ledger, two coupled damped oscillators, one driven:** drive in **19.317**, dissipated **18.253**, stored change **1.065**. The residual is −4×10⁻⁴ (0.002 %, integrator error). **No over-unity**: locking and energy swapping move energy between modes and into damping.

Plot: `/workspace/coupled_oscillator_plot.png` (6 panels), kept on the box and not committed.

## 7. [to verify] and an open question

- Huygens' 1665 letter (Œuvres reference); Bennett et al. 2002; Arnold's circle map (1961/65); Jensen–Bak–Bohr 1984; Kuramoto 1975 (LNP 39); Martens 2013; Buck 1988; Peskin 1975; Winfree; de Bellescize 1932; Lindner 2011; Oka–Aoki 2009.
- **Open question for Channing:** which of your systems should we model first as coupled oscillators?
  - (a) the **hub-motor/stator** (phase sequence and Adler locking to the drive);
  - (b) the **Multi-Egg** counter-rotating gyros (phase relation and net L);
  - (c) the **magnetic sail** loop currents against the plasma;
  - (d) the **oloid track** travelling wave.

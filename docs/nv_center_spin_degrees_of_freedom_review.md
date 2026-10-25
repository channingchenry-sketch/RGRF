# Review: the NV-centre magnetic moment, its quantum degrees of freedom and OIST's spin-driven levitated diamond (2026)

- **Request (Channing, verbatim):** "Can we look at NV center magnetic moment and quantum degrees of freedom. Okinawa just did a demonstration on a diamond using a pulsed green laser. Touches something we discussed before."
- **Sim:** [sims/nv_center_odmr_sim.py](../sims/nv_center_odmr_sim.py) ([output](../sims/nv_center_odmr_sim_output.txt)). The plot is a textbook illustration, not data.
- **Labels:** **Grounded** / **Plausible-untested** / **Speculative** / **Symbolic**. License CC0.

## 1. The OIST demonstration (verified 2026-10-25)

**Paper:** A. Nayak, D. Kim, S. Tian and J. Twamley (Quantum Machines Unit, OIST; Twamley also at the Institute of Science Tokyo), "Spin force from a nitrogen-vacancy ensemble drives a 100-mg levitated resonator", *Science Advances*, published 7 Oct 2026 (OIST press release 8 Oct 2026). doi:[10.1126/sciadv.aeh0566](https://doi.org/10.1126/sciadv.aeh0566). Preprint arXiv:[2605.17750](https://arxiv.org/abs/2605.17750) (May 2026). Volume and article number [to verify].

**What was shown (Grounded; summarised in our own words):**
- **The setup:**
  - A commercial 3 × 3 × 0.5 mm single-crystal diamond with about 4.5 ppm NV centres hangs on a 5 cm carbon-fibre rod.
  - The rod runs from a **diamagnetically levitated pyrolytic-graphite plate**, which floats over a checkerboard of NdFeB magnets, with an iron shield in between.
  - The whole resonator is 128 mg, with a vertical frequency of 17.6 Hz and Q ≈ 55.
  - A small N52 cylinder magnet sits about 0.5 mm below the diamond and supplies a gradient of about 10–100 T/m (B₀ ≈ 0.63 T).
- **The drive:**
  - A 50 mW, 532 nm green laser is **pulsed at the mechanical frequency** (about 48 % duty).
  - Each pulse optically pumps the NV spins away from their thermal populations, so the ensemble's magnetic moment changes.
  - In the gradient this gives a periodic Stern–Gerlach-type force, f = m·∂B (about 5 nN at most), pulling the diamond toward the stronger field, so it acts as a paramagnet. Between pulses the spins relax back within T₁.
- **The result:**
  - Phase-coherent centre-of-mass oscillation of about 100 nm in air, against roughly 1 nm of lab noise. The authors' supplement reports about 1.5 µm in vacuum.
  - The resonance peak stands about four orders of magnitude above the Brownian noise.
- **Controls:**
  - With the gradient magnet removed, the peak disappears.
  - A 980 nm IR laser, which cannot polarise NVs, pulsed at 50 mW produces no peak.
  - The force tracks the **gradient, not |B|** (tested with two magnets).
  - A seven-level rate model fits the dependence on laser power and gap.
- **What it is *not*:** not a quantum superposition, not levitation by spin, and no new force. The authors call it a "classical mechanical response to a quantum force". It is a milestone toward macroscopic superposition and quantum-gravity tests. Their claim of eight to nine orders of magnitude more mass than earlier spin-mechanics experiments is author-reported.
- **My order-of-magnitude check (Plausible, my estimate):**
  - The slab holds about 3.6 × 10¹⁵ NVs.
  - Flipping every one would give at most N·μ_B·∂B ≈ 3.6 × 10¹⁵ × 9.3 × 10⁻²⁴ J/T × 100 T/m ≈ 3 µN.
  - The 5 nN measured therefore corresponds to about a 0.1 % net change in moment over the illuminated volume. This is consistent with the authors' "much smaller than a complete state transfer".

## 2. The NV⁻ centre in brief

| Item | Value / note | Label |
|---|---|---|
| Structure | A substitutional N next to a lattice vacancy; C₃ᵥ symmetry along one of four ⟨111⟩ axes; negative charge (6 electrons) | **Grounded** |
| Ground state | A ³A₂ spin-1 triplet. Zero-field splitting **D ≈ 2.870 GHz** between ms = 0 and ms = ±1 at room temperature, with dD/dT ≈ −74 kHz/K | **Grounded** |
| Magnetic moment | Electron spin with g ≈ 2.003, so **γ ≈ 28.0 GHz/T** and moment ≈ g μ_B per ms unit. The Zeeman term splits ms = ±1 by **2γB** along the axis. | **Grounded** |
| Nuclear spins | ¹⁴N (I = 1, hyperfine ≈ 2.2 MHz, quadrupole ≈ −5 MHz); ¹⁵N (I = ½, ≈ 3 MHz); a ¹³C bath (1.1 % natural abundance) that sets T₂* | **Grounded** |
| Optical cycle | A 532 nm phonon-sideband excitation into ³E (zero-phonon line 637 nm). ms = ±1 crosses preferentially through the singlet manifold (¹A₁ → ¹E, the 1042 nm IR line) back into ms = 0. **Result:** green light **pumps the spin into ms = 0** (about 80–90 %), and ms = ±1 fluoresces about 20–30 % less. Together these are the basis of ODMR. | **Grounded** |
| Level anticrossings | ESLAC ≈ 51 mT and GSLAC ≈ 102 mT; off-axis fields mix the spin states and reduce contrast. This is the "spin-mixing" effect OIST used at θ ≈ 54.7°. | **Grounded** |
| Coherence | T₁ ≈ ms at room temperature; T₂* ≈ 1 µs in natural ¹³C and up to about 100 µs in isotopically pure ¹²C; Hahn-echo T₂ ≈ 0.3–2 ms; dynamical decoupling > 1 ms (about 1 s at cryogenic temperatures) | **Grounded** (typical ranges) [to verify specific values] |
| Magnetometry | Single NV about 1–30 µT/√Hz (cw) and about 10 nT/√Hz (pulsed, AC). Best ensembles about 1 pT/√Hz (Wolf et al., PRX 2015 [to verify]). | **Grounded** |
| Pulsed protocols | Rabi (pulse length → π pulse); Ramsey (π/2–τ–π/2, which measures DC field and T₂*); Hahn echo (refocuses static ¹³C noise, gives T₂ and AC sensing); CPMG/XY8 dynamical decoupling (narrowband AC filters, used in NV-NMR) | **Grounded** |

**Quantum degrees of freedom in one diamond:**
1. Electron spin (ms = 0, ±1).
2. Nuclear spin (¹⁴N/¹⁵N, nearby ¹³C), used as quantum memory.
3. The orbital/excited state ³E, with strain and electric-field sensitivity and a temperature-dependent orbital doublet.
4. The charge state NV⁻ ↔ NV⁰ (photo-ionisation under green light; only NV⁻ is the useful qubit).
5. Lattice phonons, through strain coupling (Teissier 2014; Ovartchaiyapong 2014).
6. In levitated particles, **centre-of-mass motion** (Stern–Gerlach force; OIST 2026) and **rotation/libration**. For rotation: spin–rotation coupling and magnetic torque, with spin-cooling of a trapped diamond's libration (Delord et al., *Nature* 580, 56 (2020)); Barnett and Einstein–de Haas-type angular-momentum exchange; and the rotation-induced pseudo-field (Wood et al., Nat. Phys. 2017 [to verify]).

All of these are **Grounded** as physics. Each adds a channel that can be controlled and that causes decoherence.

**The OIST result in this frame:** it used electron spin (2) only *incoherently*, as an optically switched population, coupled to centre-of-mass motion (6) through a gradient. Coherent microwave control (Rabi, echo) and spin–motion entanglement are the next steps the authors name. They are **Plausible-untested** at the 100 mg scale.

## 3. The earlier thread this "touches" (archive search 2026-10-25)

I ran `rg` over docs/, grok_archive and the share txt files for NV/nitrogen-vacancy, diamond, 532/green laser, green lens, cryptochrome/radical pair, levitated, Barnett/Einstein–de Haas, degrees of freedom and qubit. The best matches, in order:

1. **The diamond crystal core / NV phonon coupling:** [grok_archive/2026-10-17_lab_grown_crystals_gemstones.md](grok_archive/2026-10-17_lab_grown_crystals_gemstones.md), line 667, msg 13. Channing: "Can we have a crystal lattice around a diamond, would this work like a capacitor would it be better in our feed back system?" Grok's replies proposed an "NV-doped diamond core" (l. 678), "Phonon / quantum-enhanced feedback… NV centers" (l. 715) and "NV-center phonon coupling" (l. 123). The review is [lab_grown_crystals_bom_review.md](lab_grown_crystals_bom_review.md): diamond is not piezoelectric, and NV is correct. **This is the closest prior NV thread.**
2. **A spinning tetrahedral crystal driven by 532 light:** [grok_archive/2026-10-17_earth_as_resonant_shuttle_core.md](grok_archive/2026-10-17_earth_as_resonant_shuttle_core.md), line 1683, msg 61. Channing: "Can we spin the tetrahedral only and redo simulation at 532hz with the light?" [earth_shuttle_core_review.md](earth_shuttle_core_review.md) flagged the Hz/nm mix-up: 532 **nm** is the green laser line. This is a direct "spin + green light + crystal" echo of the OIST setup. The link is **Symbolic**: the earlier sim was acoustic and phi-lattice, not NV physics.
3. **Diamagnetic levitation over NdFeB with pyrolytic graphite** (the OIST platform itself): [lift_and_equilibrium_systems.md](lift_and_equilibrium_systems.md), where diamagnetic levitation is passively stable and Grounded.
4. **Angular momentum exchange:** [em_topological_gravity_review.md](em_topological_gravity_review.md), l. 269 (Einstein–de Haas; total L conserved).
5. Others: Brewster/diamond NV mention ([brewster_fresnel_mycelium_optics_review.md](brewster_fresnel_mycelium_optics_review.md)), the NIST single-photon NV analog, and the discrete time crystal in NVs ([shifting_phase_order_review.md](shifting_phase_order_review.md)).

**The green-lensing / healing-light pods thread:** no hit links NV centres or green lasers to green lensing. The OIST result does **not** recover that lost thread. The colour map ([em_geometry_map.md](em_geometry_map.md): "Green = balanced centre", Symbolic; [CROSS_THREAD_MAP §6](CROSS_THREAD_MAP.md): blue = cryptochrome) is only a **Symbolic** echo: the NV's green is just an efficient pump band, and the useful output is red fluorescence at 637–800 nm. *If* green lensing involved green light acting on a spin system in a field, the NV centre is the cleanest Grounded example of "green light + magnetic field → spin state → readout". [Channing to confirm whether that was the shape of the idea.]

## 4. RGRF links (labelled)

- **Cryptochrome radical-pair magnetoreception:** a **Grounded** mechanism (blue light makes an FAD–Trp radical pair whose singlet–triplet mixing depends on field direction; Cry4 in birds; Xu et al., *Nature* 594, 535 (2021) [to verify]). The NV is the **solid-state analog**: light-driven, spin-selective intersystem crossing. As a design analog it is **Plausible**; as "the same thing" it is **Symbolic**. See [quantum_biology_regenerative_farm_review.md](quantum_biology_regenerative_farm_review.md) and [bioelectric_coupling.md](bioelectric_coupling.md).
- **Spin–rotation and spin–motion versus the oloid and spin threads** ([oloid_magnetic_track_motor.md](oloid_magnetic_track_motor.md), [oloid_spine_lorentz_drive.md](oloid_spine_lorentz_drive.md), [electrostatic_nodal_spin_dynamics_review.md](electrostatic_nodal_spin_dynamics_review.md)):
  - **Grounded:** spin forces and torques are real but tiny (nN on 128 mg). They need an **external gradient magnet**, which takes the equal and opposite reaction.
  - **Speculative / unsupported:** any propulsion reading. The momentum ledger holds, as in [nasa_1979_field_resonance_heaviside_primes_review.md](nasa_1979_field_resonance_heaviside_primes_review.md).
- **The NV as a bench magnetometer for Halbach and stator fields** ([stator_review.md](stator_review.md), [sims/halbach_switched_arc_check.py](../sims/halbach_switched_arc_check.py)): **Grounded, and a useful tool.** It gives a vector field map with no calibration, because the reading is set by γ. It needs an aligned bias field and the region below about 50–100 mT, which for this array means more than about 4 cm from the Halbach face (§5). Near the surface, use a Hall probe. Commercial NV magnetometers and imagers exist (QDTI, Qnami [to verify]).
- **The diamagnetic platform:** OIST's levitated graphite over a checkerboard of NdFeB is the Grounded mm-scale version of [lift_and_equilibrium_systems.md](lift_and_equilibrium_systems.md). It is passive, with µm–mm gaps, and has no payload capacity.
- **GEM / quantum gravity** ([gravitoelectromagnetism_revisit.md](gravitoelectromagnetism_revisit.md)): NV and levitated-diamond proposals target gravitationally induced entanglement (Bose et al. 2017; Marletto & Vedral 2017) and Stern–Gerlach interferometers. They are **Plausible-untested** as tests of whether gravity is quantum. **Speculative** as GEM or frame-dragging detectors: the field is about 10⁻¹⁴ rad/s in Earth's frame dragging, about 10¹⁰ below NV gyroscope sensitivity (about 10⁻⁴–10⁻⁵ rad/s/√Hz [to verify]). Nothing here generates gravity.
- **Green colour symbolism:** **Symbolic** only.

## 5. Sim results (textbook illustration)

`sims/nv_center_odmr_sim.py`, H = D S_z² + γ B·S (spin-1):
- **(a)** The ODMR lines are f± = D ± γB, so the splitting is 2γB (56 MHz/mT). The ms = −1 line reaches zero at the GSLAC, **102.4 mT**.
- **(b)** In cw-ODMR at 5 mT the dips sit at **2.730 / 3.010 GHz** (2 % contrast assumed).
- **(c)** Rabi at Ω/2π = 10 MHz, so the π pulse is 50 ns.
- **(d)** Ramsey with a 3 MHz detuning and T₂* = 1 µs.
- **Off-axis mixing at 50 mT:** on-axis the transitions are 1.469 / 4.271 GHz; at θ = 54.7° (the OIST orientation) they are 2.719 / 4.289 GHz, mixed and lower in contrast.
- **Shot-noise sensitivity, η ≈ (4/3√3)·Δν/(γ C √R):** a single NV (10⁵ cps) gives about **22 µT/√Hz**; a 4.5 ppm ensemble (about 10¹¹ cps) gives about **22 nT/√Hz** (Plausible model numbers).
- **Bench Halbach field:** B₀ = 0.96 T at the surface, λ = 10 cm, B(y) = B₀e^(−2πy/λ).

| Distance y | Field | Splitting 2γB | Ensemble resolution in 1 s (dB/B) |
|---|---|---|---|
| 2 cm | 273 mT | 15.3 GHz | 8 × 10⁻⁸ |
| 5 cm | 41.5 mT | 2.3 GHz | 5 × 10⁻⁷ |
| 10 cm | 1.79 mT | 100 MHz | 1.2 × 10⁻⁵ |
| 20 cm | 3.4 µT | 0.19 MHz | 7 × 10⁻³ |

**Required sensitivity:** to see the bench field you need only about **1 µT**, which any NV setup gives. Even a single NV at 22 µT/√Hz needs about 1 minute for 3 µT. The real limits are **too much field near the magnet** (the clean window is beyond about 3.6–4.7 cm, below the ESLAC/GSLAC) and **Earth's field (about 50 µT) at y > 15 cm**, which must be subtracted with a background scan. **Grounded** (model).

Plot: `/workspace/nv_center_plot.png`, kept on the box and not committed.

## 6. Gaps and [to verify]

- The *Sci. Adv.* volume and article number; the vacuum amplitude (~1.5 µm, from the preprint supplement).
- Coherence and sensitivity values (T₂*, T₂, Wolf 2015 pT/√Hz); Wood 2017 rotation; the Cry4 citation; the commercial NV magnetometer vendors; the NV gyroscope sensitivity.
- Whether "touches something we discussed before" means the diamond-core feedback thread (lab-grown crystals, msg 13), the spinning tetra at 532 (Earth-shuttle msg 61), or green lensing [Channing to confirm].
- An NV bench measurement of the Halbach array: diamond and bias-magnet sourcing [Channing to supply if wanted].

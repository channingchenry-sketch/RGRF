# Acoustic streaming, centrifugal buoyancy, dual torus & vortex modes (living doc)
*License CC0. Recovered from Channing's notes. **OCR damage:** some formulas were reconstructed, as marked; truncations are marked **[Channing to supply]**. Labels: **Grounded**, **Plausible-untested**, **Speculative**, **Symbolic/Fiction**.*

Links: [Butterfly-Node](butterfly_node.md), [muonic_hydrogen.md](muonic_hydrogen.md), `lift_and_equilibrium_systems.md` (chirp packets §8, levitation methods §9, Grounded loop mechanisms), `piezo_helium_feedback_loop.md`.

## 1. Acoustic streaming (Grounded)

**Rayleigh (boundary-driven) streaming.**
- In a standing wave with velocity amplitude U₁(x), a viscous boundary layer of thickness **δ = √(2ν/ω)** forms at the walls.
- Just outside that layer, the steady slip velocity is **U_s = −(3/(4ω)) U₁ dU₁/dx**.
- **Sources:**
  - Lord Rayleigh, "On the circulation of air observed in Kundt's tubes, and on some allied acoustical problems," *Phil. Trans. R. Soc. Lond.* 175, 1–21 (1884), doi 10.1098/rstl.1884.0002.
  - H. Schlichting, "Berechnung ebener periodischer Grenzschichtströmungen," *Phys. Z.* 33, 327–335 (1932).

**Eckart (bulk, attenuation-driven) streaming.**
- An attenuated beam deposits momentum in the fluid and drives a jet ("quartz wind").
- Order-of-magnitude scaling: **u ~ α I L² / (ρ c ν)**, where α is the attenuation, I the intensity and L the beam or vessel scale.
- Eckart showed the steady speed is proportional to the radiated power and to (4/3 + ν′/ν), where ν′ is the bulk viscosity.
- **Source:** C. Eckart, "Vortices and streams caused by sound waves," *Phys. Rev.* 73, 68–76 (1948), doi 10.1103/PhysRev.73.68.

**Unifying picture.** Streaming is forced by gradients of the **Reynolds stress** (the mean acoustic momentum flux) and resisted by viscosity. At high power it becomes jet-like and then turbulent.
- **Source:** J. Lighthill, "Acoustic streaming," *J. Sound Vib.* 61(3), 391–418 (1978), doi 10.1016/0022-460X(78)90388-7.

**Air-mode craft application (Plausible; small at flight speed).**
- **The idea:** high-frequency piezo vibration along a kirigami or polymorphic hull drives localized streaming. Uses would be:
  - boundary-layer control and drag reduction;
  - stabilizing or thinning an external water film;
  - gentle propulsion or attitude assist.
- **Caveat:** streaming speeds are mm/s to m/s. That is significant for films and boundary layers at low speed, and negligible against free-stream flow at flight speed.

*See also:* "sonic pinching" (acoustic / magnetosonic drivers on a sheared-flow Z-pinch) in [tungsten_bismuth_core.md §3a](tungsten_bismuth_core.md#3a-sonic-pinching-grok-excerpt--lost-sim-description-2026-10-15).

## 2. Centrifugal buoyancy (Grounded)

**The physics.**
- In a rotating frame, a_c = ω²r and dp/dr = ρω²r.
- Denser phases move outward and lighter phases (vapor) move inward. This is how centrifuges and rotating separators work.

**Spin throttling.** Changing ω modulates water distribution and how a film wraps the hull. **Grounded** physics; the application is **Plausible-untested**.

**Combined vibration + centrifugal** **[truncated, Channing to supply]**.

> **Bridge (Resona reconstruction, 2026-10-12; replace if original found):** Streaming body forces add to centrifugal stratification. Acoustic radiation force moves particles and droplets toward pressure nodes or antinodes depending on their contrast factor, competing with the ρω²r density sorting. Vibration can therefore fine-tune the layers that spin sets coarsely. **Grounded** physics; the combined control is **Plausible-untested.**


**Twisted toroidal geometry with a 60° twist.**
- g_eff = ω²r acts along the helical gradient, which gives a helical effective-gravity path.
- The kinematics are **Grounded**. Any functional benefit is **Plausible-untested**.

## 3. Dual torus & muon pathways

**Parallel vs perpendicular transport in magnetized plasma (Grounded).**
- **Along B:** field-aligned streaming, Alfvénic coupling, and angular-momentum export by magnetic stresses (magnetic braking).
  - E. J. Weber & L. Davis Jr., "The angular momentum of the solar wind," *ApJ* 148, 217–227 (1967), doi 10.1086/149138. Effective corotation extends out to the Alfvén radius, about 15–50 R☉.
- **Across B:** E×B drift, polarization drift, turbulent diffusion.
- "Controlled perpendicular shifting by **[truncated, Channing to supply]**".

> **Bridge (Resona reconstruction, 2026-10-12; replace if original found):** "…an imposed radial E-field (E×B drift), polarization drift from a time-varying E, or tailored turbulence (anomalous cross-field diffusion)." These are the standard cross-B transport routes. **Grounded.**


**Spin-sum and double-torus concept (Channing's text).**
- **Constructive addition:** L_total = L_water + S_muon + S_paramagnetic.
- **Paramagnetic enhancement.**
- **Two tori:** a primary torus with doubled angular momentum, and an inverted secondary.
- **The 60° twist** helicalizes precession into an "information-rich signal".
- **Planetary scanning, three channels:**
  - density from flux;
  - magnetic dynamics from wobble;
  - pathway coherence from buoyancy-guided flow.
- **"Buoyant lanes"** guide muon and pion cascades.

**Labels:**
- **Muography: Grounded.** K. Morishima et al., "Discovery of a big void in Khufu's Pyramid by observation of cosmic-ray muons," *Nature* 552, 386–390 (2017), doi 10.1038/nature24647 (ScanPyramids). Muon flux attenuation maps density.
- **Spin-sum coupling: Speculative.**
  - The sea-level cosmic-muon flux is about 1 per cm² per minute.
  - A muon crosses a metre-scale device in about 3 ns.
  - Its spin angular momentum (ħ/2) is negligible against any bulk L_water.
  - Paramagnetic spin contributions add vectorially, but they are not "doubled" by geometry.
- **Buoyant lanes guiding muons: Speculative.** At GeV energies, muons are unaffected by fluid buoyancy or flow. Only matter density, through energy loss, and strong B fields bend them.
- **Precession as an information signal: Plausible** in the sense of NMR / magnetometry. The 60° twist's role is untested.

**Tesla dialogue lines** in Channing's source: **Entanglements narrative / fiction, not a source.** (The repo mentions "Entanglements" in `em_geometry_map.md` and `C1-C12_seed_map.md`.)

### 3b. Light filtering & blue-light muon "capture" (quantum biology: not settled)

**Grounded: Cherenkov light.**
- A charged particle moving faster than light does in the medium (β > 1/n) emits Cherenkov radiation.
- In water, n ≈ 1.33, so the threshold is β > 0.75. For a muon that means a kinetic energy of roughly 160 MeV.
- The photon yield goes as dN/dλ ∝ 1/λ², so the light is weighted toward the blue and near-UV.
- **Sources:**
  - P. A. Cherenkov, "Visible luminescence of pure liquids under the influence of γ-radiation," *Dokl. Akad. Nauk SSSR* 2, 451–457 (1934).
  - I. M. Frank & I. E. Tamm, "Coherent visible radiation of fast electrons passing through matter," *Dokl. Akad. Nauk SSSR* 14, 107–112 (1937); also in *C. R. Acad. Sci. URSS* 14, 109–114.

**Grounded: detection.** Large water or ice Cherenkov detectors see muons through this light, using blue-sensitive photomultipliers.
- **Super-Kamiokande:** S. Fukuda et al., "The Super-Kamiokande detector," *Nucl. Instrum. Methods A* 501, 418–462 (2003), doi 10.1016/S0168-9002(03)00425-X. A 50 kt water detector.
- **IceCube:** M. G. Aartsen et al., "The IceCube Neutrino Observatory: instrumentation and online systems," *JINST* 12, P03012 (2017), doi 10.1088/1748-0221/12/03/P03012. A cubic kilometer of ice.
- Matching filters and photocathodes to the blue band improves signal-to-noise. Wavelength shifters are also used.

**Not possible: light capturing or slowing muons.**
- The light is a **product** of the muon's passage. It carries away only a tiny fraction of the muon's energy (roughly keV per cm, against about 2 MeV/cm ionization losses in water).
- Light does not trap, steer or slow muons. Filtering is **detection only**.

**Speculative: a cryptochrome or quantum-biology link.**
- Cryptochrome radical-pair magnetoreception is blue-light dependent. It is a serious but **unsettled** hypothesis for birds (see `bioelectric_coupling.md`, radical-pair).
- Linking it to cosmic-ray muons or to Cherenkov light has **no evidence**. Natural Cherenkov light in tissue from cosmic muons is extremely faint.

**See also:** `muonic_hydrogen.md`.

## 4. Vortex mode theory
*OCR-reconstructed where marked. Labels: the mathematics is **Grounded / standard**; the paramagnetic analogy and the device application are **Plausible-untested**.*

### (a) Cylindrical modes
- **Field expansion:** take a free scalar field in a cylinder of radius R and expand it as
  φ = Σ_m ∫ dk_z φ_ml(k_z, t) J_m(k_ml r) e^{imθ} e^{ik_z z}.
- **Boundary conditions:**
  - Dirichlet, J_m(k_ml R) = 0, gives k_ml = j_ml / R, where j_ml is the l-th zero of J_m.
  - The Neumann alternative uses the zeros of J′_m.
- **Dispersion:** ω² = k_z² + k_ml² + μ², where μ is the field mass.
  - The **centrifugal barrier** (the m²/r² term) is encoded in the Bessel zeros: higher m means larger j_ml.
- **Background vortex:** adds a position-dependent term, equivalent to minimal coupling to a circulatory vector potential **A_θ ∝ 1/r**.
  - That is the Aharonov–Bohm-like analog: waves on a "bathtub" vortex show AB wavefront dislocations.
  - M. V. Berry, R. G. Chambers, M. D. Large, C. Upstill & J. C. Walmsley, "Wavefront dislocations in the Aharonov–Bohm effect and its water wave analogue," *Eur. J. Phys.* 1, 154–162 (1980), doi 10.1088/0143-0807/1/3/008.

### (b) Tadpole self-energy (OCR-reconstructed)
- **Mode sum:** in the cylinder, the one-loop tadpole becomes a discrete mode sum:
  Σ(h) = Σ_m Σ_l ∫ dk_z/(2π) · g_m / (2 ω_ml(k_z, h)).
- **Degeneracy:** g_m = 1 for m = 0 and 2 for m ≥ 1 (±m).
- **Effect of the background field h:** it shifts the effective mass, μ² → μ² − a h², so ω_ml(h) ≈ ω_ml(0) − a h² (to leading order, with a absorbing the 1/(2ω) factor).
- **Which modes dominate:** low-m modes feel less centrifugal repulsion and contribute most.
- **Needs UV regularization.** The sum and integral diverge, so a cutoff, zeta function or dimensional regularization is required. Compare the Casimir checkpoint in `em_topological_gravity_review.md`.

### (c) Mode susceptibility (sign convention reconstructed)
- **Definition:** χ_ml = −(1/2) ∂²ω_ml/∂h² at h = 0.
- **Sign:** χ > 0 means the field lowers the mode frequency, stabilizing it. This is analogous to paramagnetism, but **only as an analogy**.
- **Robustness knob:** the vortex winding number selects which m dominates.
- **Connections:**
  - crystalline disk and phonon packets;
  - a static levitating field acting as h (§9 levitation methods);
  - for the chirp carrier you want χ > 0, so that it gets a restoring shift **[truncated, Channing to supply]** (chirp packets, `lift_and_equilibrium_systems.md` §8).

> **Bridge (Resona reconstruction, 2026-10-12; replace if original found):** "…that pulls the carrier frequency back toward the mode centre when h drifts, so the packet stays locked (negative feedback)." **Plausible-untested.**


### (d) Circumference as a design knob (OCR-reconstructed)
- **Phase around the loop:** for a toroidal or cyclic path of length L = 2πR, the round-trip phase is φ = kL = ωL / c_eff. Here c_eff includes medium or plasma dispersion.
- **Resonance condition:** L = nλ, which gives **f_n = n c_eff / L**. The free spectral range is c_eff / L.
- **Near a resonance:** the S-matrix poles move with L. The transmission is S₂₁ ≈ κ / (Δω + iγ/2), with κ the coupling and γ the total loss, and the linewidth gives Q = ω/γ.
- **What sets the design:** circumference fixes the discrete f_n, together with the material (c_eff), the coupling (κ) and the loss (γ) **[truncated, Channing to supply]**.

> **Bridge (Resona reconstruction, 2026-10-12; replace if original found):** "…alongside material dispersion and wall/coupling losses, which set linewidth and Q (Q ≈ ω/γ)." **Grounded** (ring-resonator theory).

- **Grounded:** ring resonators. W. Bogaerts et al., "Silicon microring resonators," *Laser Photonics Rev.* 6(1), 47–73 (2012), doi 10.1002/lpor.201100017. The same algebra applies to acoustic or fluidic rings, with c_eff the sound or wave speed.

# Review: Alan C. Holt, Lene Hau, John R. R. Searl, FPUT recurrence, vector equilibrium and the jitterbug (share #96)

- **Archive:** [grok_archive/2026-10-22_allen_holt_lene_hau_and_searl_experiments.md](grok_archive/2026-10-22_allen_holt_lene_hau_and_searl_experiments.md) (share `7cf75c45`, 6 messages: 3 Channing, 3 Grok).
- **Checks:** [sims/holt_hau_searl_fput_s96_checks.py](../sims/holt_hau_searl_fput_s96_checks.py) ([output](../sims/holt_hau_searl_fput_s96_checks_output.txt)).
- **Related:** [newman_bubble_circulation_baghdad_review.md](newman_bubble_circulation_baghdad_review.md) (Newman not over-unity), [ANALYSIS_2026-10-12.md](ANALYSIS_2026-10-12.md), [em_topological_gravity_review.md](em_topological_gravity_review.md), [platonic_breathing_craft_sketch_review.md](platonic_breathing_craft_sketch_review.md), [macroscopic_atom_topology_frequency_review.md](macroscopic_atom_topology_frequency_review.md), [electrostatic_isotropic_stress_review.md](electrostatic_isotropic_stress_review.md), [DESIGN_FORCE_FLOW_MAP.md](DESIGN_FORCE_FLOW_MAP.md).
- **Labels:** Grounded = established in peer-reviewed literature or rerun here; Plausible-untested; Speculative; Symbolic (φ and similar, unless tested).

## 1. Alan C. Holt (msg 2)

Channing wrote "Allen Holt"; the person meant is **Alan C. Holt**, NASA Johnson Space Center (Grok's identification, verified against NASA NTRS).

| Claim | Label | Note |
|---|---|---|
| Holt authored NASA-TM-80961 / JSC-16073, *Field Resonance Propulsion Concept*, August 1979 | **Grounded** | NTRS record 19800010907. The memo itself calls the concept dependent on "two unproven assumptions and currently unverified magnetohydrodynamic processes". |
| Resonance between pulsed EM waveforms and gravitational waveforms/metrics could propel a craft | **Speculative** | No demonstration exists. |
| NASA foreword: unofficial work, not UFO research | **Plausible-untested** | Grok-reported [to verify against the PDF foreword]. |
| Later AIAA talks; joint work with Eric W. Davis on EM-sensitive materials, Casimir, spinning-superconductor weight reduction | **Plausible-untested** | Grok-reported [to verify]. The spinning-superconductor weight-reduction claim (Podkletnov-type) has not been replicated (Speculative). |
| Underlying fields (reconnection, megagauss laser fields, Casimir force, superconducting magnets) | **Grounded** | Real research areas; none implies propulsion. |

## 2. Lene Hau (msg 2)

| Claim | Label | Note |
|---|---|---|
| Light slowed to 17 m/s (~38 mph) via EIT in ultracold sodium, BEC regime | **Grounded** | Hau, Harris, Dutton, Behroozi, *Nature* 397, 594 (1999). Rerun: 17 m/s = 38.0 mph. |
| Pulse stopped, stored as atomic coherence, revived on restoring the coupling laser | **Grounded** | Liu, Dutton, Behroozi, Hau, *Nature* 409, 490 (2001); storage up to ~1 ms. **Correction:** the 2001 stop was in a magnetically trapped *cold* sodium cloud, not stated as a BEC; Grok's "stop-and-store lives in the BEC" is imprecise. |
| Light converted to a travelling matter wave, carried to a second condensate, revived as light | **Grounded** | Ginsberg, Garner, Hau, *Nature* 445, 623 (2007) [to verify page]. |
| Hau as metaphor for mycelial/crystalline "coherence stores" | **Symbolic** | Grok itself says it is not a propulsion result. |

## 3. John R. R. Searl and the SEG (msg 2)

| Claim | Label | Note |
|---|---|---|
| Biography, 1946–1956 dating, ring/roller design, "Law of the Squares" | **Plausible-untested** | Searl's own account [to verify]. |
| Self-spin, excess output, cooling, weight reduction/lift, "Inverse Gravity Vehicle" | **Speculative / unverified** | No independent verified replication. Over-unity, free-energy and anti-gravity claims are unverified. |
| Roschin–Godin and other builder results show small apparent weight changes | **Speculative** | Grok-reported; not accepted; no calorimetry-grade evidence [to verify sources]. |
| Static magnets give no continuous torque without an energy input; ion wind/corona can mimic lift | **Grounded** | Matches the repo position. As already established for Newman ([review](newman_bubble_circulation_baghdad_review.md)): **Newman's machine is not over-unity**, and the same standard applies here. |

## 4. FPUT recurrence (msg 2)

| Claim | Label | Note |
|---|---|---|
| 1953–55 Los Alamos MANIAC I, Mary Tsingou wrote the code; near-return to mode 1 | **Grounded** | Fermi, Pasta, Ulam (LA-1940, 1955); Dauxois, *Physics Today* 2008 on Tsingou. Rerun (N=32 α-chain, α=0.25): mode-1 energy falls to 37 % and returns to 98 % (t≈19 500, units in script). |
| KdV continuum limit, solitons (Zabusky–Kruskal 1965); Toda proximity; slow thermalization by higher-order resonances | **Grounded** | Onorato et al., *PNAS* 2015 (four/six-wave). Exact scaling exponent Grok-reported. |
| Phi-spaced coil modes acting like q-breathers | **Plausible-untested** (φ part **Symbolic**) | Testable in the sim engine. |

## 5. Vector equilibrium and the jitterbug (msgs 4, 6)

| Claim | Label | Note |
|---|---|---|
| VE = cuboctahedron, 8+6 faces, 12 vertices, 24 edges, radius = edge | **Grounded** | Rerun: R/edge = 1.000. Correction: the cuboctahedron is the classic convex uniform polyhedron with circumradius = edge; Grok's "only convex polyhedron" is a strong form [to verify]. |
| Jitterbug stations: icosahedron at ±22.2°, Jessen at ±30°, octahedron at ±60° | **Grounded** | Rerun: 22.24°, 30.00°, 60.00°; icosa diamond diagonal = φ × edge (rerun). |
| Jessen "cubic-domain max ≈ 2√6/3" | **Grok-reported** | Rerun gives Jessen short diagonal √6/3 ≈ 0.816 × edge; Grok's quantity is unclear [to verify]. |
| DNA-origami jitterbug, ~fivefold volume change | **Plausible-untested** | Grok-reported [to verify citation]. Volume ratio octa/VE for fixed edge is ~0.42/2.36, i.e. about 5.6× — consistent. |
| Isotropic vector matrix "breathing", omnidirectional waves | **Grounded** as geometry; **Symbolic** as field/plasma model | Grok labels it the same way. |
| VE/jitterbug as planetary docking, filament-rider or consciousness pump | **Speculative / Symbolic** | Grok labels these visionary. |
| φ appears only at the icosahedral station | **Grounded** (geometry) | Any φ design benefit remains **Symbolic** unless tested. |

## 6. Gaps

- Holt NASA foreword quote, Holt–Davis papers [to verify].
- Searl replication reports Grok names [to verify]; any SEG measurement data [Channing to supply].
- POL v0.1 radius for the 12-around-1 coil layout [Channing to supply].

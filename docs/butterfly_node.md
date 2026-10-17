# Butterfly-Node (living doc)
*License CC0. Details are to be supplied by Channing. Only Channing's own words and existing repo material are used here; every gap is marked **[Channing to supply]**. Labels: **Grounded**, **Plausible-untested**, **Speculative**.*

**The concept as Channing named it:**
- figure-eight ferrofluid wings;
- a free-to-move egg cavity;
- copper half-tube control;
- an impedance cascade across the electrical, magnetic, acoustic, fluidic and mechanical domains;
- opposite-foci acoustic filtering.

Each element is mapped to existing POL / RGRF subsystems in the table at the end.

**Overall label:**
- The integrated node: **Plausible-untested.**
- Any lift or net-energy claim: **Speculative** (see the Power ledger section).

## 1. Figure-eight ferrofluid wings
- **Description:** ferrofluid held in a figure-eight (two-lobed) "wing" path. Geometry, volume, fluid type, field source and drive are **[Channing to supply]**.
- **Grounded basis:**
  - Ferrofluid moves toward stronger field and takes shapes set by magnetic body force (μ₀M·∇H), surface tension and gravity.
  - Field-guided ferrofluid paths, seals and pumps are established.
  - Source: R. E. Rosensweig, *Ferrohydrodynamics*, Cambridge University Press (1985); Dover reprint 2014.
- **Labels:**
  - Field-shaped ferrofluid path: **Grounded.**
  - Figure-eight circulation sustained by a moving or pulsed field: **Plausible-untested.** See Grounded loop mechanisms 1 and 6 (counter-rotating pairs) in `lift_and_equilibrium_systems.md`.

## 2. Free-to-move egg cavity
- **Description:** an egg (elliptical) cavity that is not rigidly fixed and can move or rotate within the node. Its constraint, its suspension, and whether it is a cavity in fluid or a solid shell are **[Channing to supply]**.
- **Grounded basis:**
  - Elliptical cavities reflect focus to focus (`em_topological_gravity_review.md`, Elliptical Eye).
  - A free body is stabilized either gyroscopically or by restoring forces. This is exactly C8's open question: gyro eggs or eddy springs?
- **Label:** **Plausible-untested.**

## 3. Copper half-tube control
- **Description:** copper half-tubes used for control. Their placement, their dimensions, and whether they are passive or actively driven are **[Channing to supply]**.
- **Grounded basis:**
  - A moving magnet or magnetized fluid near copper induces eddy currents that oppose the motion (Lenz's law). The result is velocity-proportional damping, the familiar magnet-in-copper-tube demonstration.
  - A half-tube gives one-sided or directional damping.
  - The POL sim's eddy-current EDS numbers (~52 N/kW) are in `lift_and_equilibrium_systems.md`.
- **Labels:**
  - Damping and centering: **Grounded.**
  - Use as a control law: **Plausible-untested.**

## 4. Impedance cascade (electrical → magnetic → acoustic → fluidic → mechanical)
- **Description:** energy is handed across domains through matched impedances. The stage order, the frequencies and the target impedances are **[Channing to supply]**.
- **Grounded basis:**
  - Lumped-element analogies (force ↔ voltage, velocity ↔ current; pressure ↔ voltage, flow ↔ current) are standard transducer and electroacoustic practice.
  - Power transfer between stages peaks when impedances are matched.
  - Every conversion stage has an efficiency below 1, and the losses multiply along the chain.
  - Fluidic R–L–C networks: Grounded loop mechanism 8 (Bruus 2008; the *Lab Chip* resonant-network papers).
- **Labels:**
  - The analogy and the matching principle: **Grounded.**
  - The specific five-domain cascade: **Plausible-untested.**

## 5. Opposite-foci acoustic filtering
- **Description:** acoustic energy is injected at one focus of the ellipse and collected or filtered at the opposite focus. The filter band and the transducers are **[Channing to supply]**.
- **Grounded basis:**
  - In an ellipse, any ray leaving one focus reflects to the other. Lithotripsy and whispering galleries use this (Elliptical Eye section).
  - Cavity modes act as band-pass filters.
  - Helium shifts the resonances because of its high sound speed (`piezo_helium_feedback_loop.md`, `helium_octave_table.md`).
- **Labels:**
  - Focusing: **Grounded.**
  - Using it as a selective filter inside a moving, free egg: **Plausible-untested.**

## Mapping to existing docs

| Butterfly-Node element | Existing doc / section | Relation |
|---|---|---|
| Egg cavity, gyro vs eddy stability | Multi-Egg / **C8** (`C1-C12_seed_map.md`, `em_topological_gravity_review.md`, `lift_and_equilibrium_systems.md` §7) | Same open question |
| Focus geometry, field-pressure loop | **Elliptical Eye / Multi-Egg core** and **Dive A (ponderomotive)** in `em_topological_gravity_review.md` | Geometry and force basis |
| Wings, copper control, cascade | **Grounded loop mechanisms 1–8** (Lorentz/Kelvin forces, Joule heating, vortex pairs, Tesla valves / RLC networks) in `lift_and_equilibrium_systems.md` | Mechanism menu |
| Two-fluid wings or interfaces | **Dual-Oil Module** (`lift_and_equilibrium_systems.md` §6b) | A possible fill |
| Wing form, craft-scale integration | **Manta-Butterfly craft** (`manta_butterfly_craft.md`) | Parent concept |
| Acoustic stage, helium medium | **Piezo-helium feedback loop** (`piezo_helium_feedback_loop.md`), `helium_octave_table.md` | Acoustic domain |
| Eddy-current numbers | **POL sim** results (`lift_and_equilibrium_systems.md`, power ledger; the README notes on the POL sim) | Quantitative limits |

## Power ledger
**Placeholder; [Channing to supply] drive powers.**

| Stage | Input (W) | Output / useful (W) | Loss path | Status |
|---|---|---|---|---|
| Electrical drive | ? | ? | Joule losses | to measure |
| Magnetic → ferrofluid | ? | ? | Viscous losses, relaxation | to measure |
| Copper control | ? | ? | Eddy heating (by design) | to measure |
| Acoustic stage | ? | ? | Wall and gas absorption | to measure |
| Fluidic / mechanical output | ? | ? | Friction, valve losses | to measure |

**Rule:** total out ≤ total in. Any claimed lift is compared against the ~0.05–0.1 N/W EDS baseline.

## Bench tests
1. **Figure-eight ferrofluid circulation.**
   - Build a sealed figure-eight channel with an off-the-shelf ferrofluid, driven by a rotating or phased magnet array.
   - Measure circulation speed (by particle tracking) against drive power and frequency.
   - Then add a copper half-tube along one lobe and measure the damping asymmetry.
2. **Opposite-foci filter.**
   - Make an acrylic or 3D-printed elliptical cavity with a piezo at one focus and a microphone at the other.
   - Sweep the frequency in air, then in helium.
   - Compare the transfer function at the foci with an off-focus position.
   - Then repeat with the egg free to move (suspended) and measure how the response degrades.
3. **Two-stage impedance cascade.**
   - Chain a piezo, an acoustic cavity and a fluidic RLC network with a Tesla valve.
   - Measure net flow per input watt with the stages matched and with them deliberately mismatched.
   - Expected result: matching improves transfer, and the end-to-end efficiency is well below 1.

## Gaps [Channing to supply]
- Dimensions and materials for every element.
- The figure-eight topology: whether it is a closed loop or two coupled lobes.
- How the egg is suspended, and its degrees of freedom.
- Copper half-tube placement, and whether it is active or passive.
- The stage order, frequencies and impedances of the cascade.
- The filter band.
- The intended function of the node: lift, stabilization, sensing or energy routing.
- How the node mounts on the Manta-Butterfly craft.

See also: [acoustic_streaming_and_centrifugal.md](acoustic_streaming_and_centrifugal.md) (streaming, centrifugal buoyancy, dual torus).

## See also (2026-10-17)

- [chern_simons_manta_butterfly_review.md](chern_simons_manta_butterfly_review.md): Grok share `6b85d507` proposes treating the figure-eight ferrofluid streams as a Chern–Simons fluid (Speculative: viscous helicity decay is expected) and adding a manta-style outer planform (hydrodynamics Grounded). Helicity-decay bench test suggested.

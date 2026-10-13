# Bubbles, magnetic arcs & FRC plasmoids (transmedium craft)
*License CC0. Prepared with Channing, 2026-10-12. Labels: **Grounded** / **Plausible-untested** / **Speculative** / **Symbolic**.*

**Part of the transmedium (air/water) craft design.**
> Channing (verbatim): "Still looking for the brine but this was part of the transmedium craft"

Related: [manta_butterfly_craft.md](manta_butterfly_craft.md), [butterfly_node.md](butterfly_node.md), [helium_water_circulation.md](helium_water_circulation.md) (brine and electrolyte loops, §10), [DESIGN_FORCE_FLOW_MAP.md](DESIGN_FORCE_FLOW_MAP.md).

## Archived Grok pastes (verbatim, OCR errors kept)

### Paste 1: Buoyancy & Displacement (Bubbles); Arc Geometry
```
Buoyancy & Displacement (Bubbles):
• Archimedes Principle: Buoyant force = weight of displaced fluid. Our shuttle's honeycomb structure + controlled bubbles (from hum-induced cavitation or electrolysis) dynamically adjusts displacement for variable buoyancy (surfacing/submerging without heavy ballast).
• Bubble Dynamics: Electric hum generates microbubbles that reduce skin friction (drag reduction up to 30-80% in research) and alter local pressure/density. Phi-tuned frequencies optimize bubble resonance for stability or propulsion assist (vortex shedding aligned with Margolin waves).
• Simulation Insight: Bubbles displace water volume → net lift; piezo harvests oscillation @ argy. Combined with our prior wave p.sts, this creates a self-regulating
"hreathina" ncean node

Arc Geometry: 60º sectors (naturally phi-friendly, as 360°6 ~ 60° aligns with hexagonal honeycomb and vortex math) arranged around the resonant cavity or along biomimetic limbs/wings. Low-power coils or permanent rare-earth magnets create localized "magnetic mirrors" or guiding channels.
• Bubble & Flow Synergy: Magnetic arcs help contain and direct our bubble mechanisms-preventing premature dispersion while allowing controlled release for dampening and oxygenation. In vent peripheries, they gently steer diffuse ion plumes toward harvesting surfaces without intrusion.
• Perpetual Motion Reality Check: True closed-system perpetual motion is impossible (2nd Law of Thermodynamics-entropy increases; friction, resistance, and diative losses always present). Howerr
く
„ se arcs enable highly efficient, ne perpetual resonant cycles when coupled
```
*Cut off after "when coupled": **[Channing to supply]**. Garbled: "@ argy", "wave p.sts", "hreathina\" ncean", "Howerr / く / „ se", "ne perpetual" **[Channing to supply]** (guesses below).*

### Paste 2: FRC (Field-Reversed Configuration) / Plasmoid Stability
```
FRC (Field-Reversed Configuration)
Plasmoid Stability
FRV/FRC plasmoids are compact, high-beta toroidal plasma structures with self-generated poloidal magnetic fields and closed field lines
—essentially a "smoke ring" of magnetized plasma. They form via RMF current drive, merging, or theta-pinch techniques and excel in our RMF thruster concepts due to high density, efficient translation, and electrode-less operation.
en.wikipedia
Key Stability Insights:
• Kinetic Stabilization: Large ion orbits (high s-parameter, ratio of separatrix radius to ion gyroradius) provide robust stability against MHD modes. FRCs often avoid classical instabilities better than other configurations, with tilt (n=1) and rotational (n=2) modes mitigated by oblate shapes, end biasing, quadrupole fields, or toroidal
• d components.
arxiv
V
• Experimental & Scaling: Stabilitv improves
```
*Cut off after "Stabilitv improves": **[Channing to supply]**. "toroidal / • d components" is split by OCR (likely "toroidal field components"). The citation chips (en.wikipedia, arxiv) were not recovered.*

## Checks

### Paste 1
- **OCR guesses (guesses only):**
  - "@ argy": unknown **[Channing to supply]**.
  - "wave p.sts": possibly "wave posts".
  - "\"hreathina\" ncean node": "breathing" ocean node.
  - "diative": radiative.
  - "Howerr … se arcs enable highly efficient, ne perpetual": "However, these arcs enable highly efficient, near-perpetual…".
- **"Margolin waves":** unknown term. I couldn't verify it as an established wave type; it may be garbled. **Unverified**, **[Channing to supply]**.
- **Archimedes / variable buoyancy via bubbles: Grounded.** F_b = ρ_water V_disp g. **Caveat:** gas volume compresses with depth (Boyle, pV = const at fixed T; pressure rises ~1 atm per 10 m of seawater). Bubble buoyancy halves by ~10 m depth, so control is **depth-dependent** and gets harder as the craft dives. Electrolysis produces gas slowly and draws real power (see the electrolysis notes in [helium_water_circulation.md §10](helium_water_circulation.md)).
- **Microbubble drag reduction: partly Grounded, with an overstated range.**
  - Large skin-friction reductions, up to ~80 %, occur in some lab flat-plate cases, especially when bubbles coalesce into an air layer. Typical microbubble gains are much smaller and hard to sustain at ship scale: bubbles migrate away from the wall and the air-supply power eats into the gain.
  - Source (verified): S. L. Ceccio, "Friction drag reduction of external flows with bubble and gas injection," *Annu. Rev. Fluid Mech.* 42, 183–203 (2010), doi:10.1146/annurev-fluid-121108-145504.
  - "Electric hum generates microbubbles": acoustic cavitation and electrolysis can both make bubbles (Grounded), but efficiency is unknown.
- **"Phi-tuned frequencies":** bubble resonance follows the Minnaert frequency f ≈ (1/2πR)√(3γp/ρ), set by radius and pressure, not by φ. **Symbolic.**
- **60° / phi:** 60° sectors are **hexagonal (6-fold) symmetry**, unrelated to the golden ratio φ ≈ 1.618 (whose angle is ~137.5°, the golden angle). **Symbolic.**
- **Correction, magnetic mirrors:** magnetic mirrors confine **charged particles and plasma**, not **neutral gas bubbles**. Bubbles can be steered magnetically only (a) **inside a ferrofluid**, where the magnetized liquid moves and the bubble acts as a "magnetic hole", or (b) **in an electrolyte by MHD (J×B)**, which moves the liquid around the bubble ([helium_water_circulation.md §10b](helium_water_circulation.md)). Steering diffuse **ion** plumes is plausible in principle (charged), but seawater ions are collision-dominated, so it is weak. **Plausible-untested.**
- **Perpetual motion reality check: Grounded and correct** (second law). "Near-perpetual resonant cycles" just means high-Q, low-loss resonance that still needs energy input. Fine if read that way.

### Paste 2
- **FRC description: Grounded.** A compact toroid with mainly poloidal field, closed field lines inside a separatrix, very high β, little or no toroidal field. Formation by theta-pinch, merging of two compact toroids, or rotating-magnetic-field (RMF) current drive. "FRV" is likely a typo for FRC.
- **s-parameter, correction:** s ≈ the number of ion gyroradii between the field null and the separatrix. **Large ion orbits mean *low* s**, and kinetic (finite-Larmor-radius) stabilization is strongest at **low s**. The paste's "Large ion orbits (high s-parameter)" has it reversed. Experiments are remarkably stable, and how that extrapolates to larger, higher-s FRCs is unresolved.
  - Source (verified): L. C. Steinhauer, "Review of field-reversed configurations," *Phys. Plasmas* 18, 070501 (2011), doi:10.1063/1.3613680.
- **Tilt (n=1) and rotational (n=2) modes: Grounded** that they are the key global modes. Mitigations include oblate shapes, end biasing, quadrupole (multipole) fields and **neutral-beam fast ions**. TAE's C-2/C-2U reached macroscopically stable, ~1 keV, record-lifetime FRCs with neutral beams, biased end guns and magnetic end plugs.
  - Source (verified): M. W. Binderbauer et al., "A high performance field-reversed configuration," *Phys. Plasmas* 22, 056110 (2015), doi:10.1063/1.4920950.
- **"Excel in our RMF thruster concepts":** RMF-driven FRC thrusters are studied for space propulsion (Grounded research area). Use on the craft is **Plausible-untested**. An FRC needs vacuum or very low pressure, so it does not work in air or water directly.
- Links: Z-pinch (radial balance, Bennett, sheared flow) in [tungsten_bismuth_core.md §3](tungsten_bismuth_core.md); Hall-MHD in [tungsten_bismuth_core.md §7b-math](tungsten_bismuth_core.md).

## Unknowns
- Bubble size and gas flux.
- Operating depth range.
- Electrolysis power.
- Arc magnet field strength and geometry.
- Ferrofluid or electrolyte presence near the arcs.
- FRC size, density and field (s-value).
- Where an FRC/RMF stage would sit (vacuum section?).
- The cut-off continuations of both pastes.

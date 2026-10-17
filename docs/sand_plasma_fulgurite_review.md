# Sand to plasma, fulgurites and the "frequency-locked arc": review of a Grok share (2026-10-17)
*CC0. Labels: **Grounded** / **Plausible-untested** / **Speculative** / **Symbolic**. Why φ appears, and how it is tested: [method_phi_and_natural_craft.md](method_phi_and_natural_craft.md).*

**Source (verbatim archive):** "Sand Becomes Plasma: Scientific Transformation", 6 messages: [grok_archive/2026-10-17_sand_becomes_plasma.md](grok_archive/2026-10-17_sand_becomes_plasma.md).

**Repo context (cross-links):**
- High-voltage safety: [legal_safety §1.3](legal_safety_and_grounding_review.md#13-electrical-high-voltage-and-field-exposure-safety).
- Lightning rods: [franklin_lightning_rod.md](franklin_lightning_rod.md).
- Quartz piezo properties: [feynman_metamaterial_piezo_review §2](feynman_metamaterial_piezo_review.md#2-quartz-and-metamaterials-message-4).
- Shear stabilization and cyclotron physics: [zpinch_tungsten_nodes_review §5](zpinch_tungsten_nodes_review.md#5-φ-spaced-nodes-ion-cyclotron-resonance-and-magnetron-shear-message-12).

**Channing's prompts (verbatim):**
1. "can sand become plasma"
2. "Explore fulgurite formation physics"
3. "Can we use our cyclotron shear stabilization to make an arc to hit sand that’s frequency locked? That doesn’t sound right.."

## 1. Sand to plasma (message 2)

| Claim | Check | Label |
|---|---|---|
| Sand is mostly SiO₂; arcs or torches melt it (>1,650–1,700 °C), then vaporize and ionize it | Quartz melts near 1,670–1,713 °C and boils near ~2,230 °C; a thermal plasma (~10⁴ K) dissociates and ionizes the vapour | Grounded |
| Lightning channel ~30,000 °C fuses sand into hollow tubes (fulgurites) | Peak channel temperature ~30,000 K | Grounded |
| Plasma torches make fused silica; RF or microwave plasmas fully vaporize silica particles; regolith vitrification | RF thermal-plasma synthesis of nano-silica is established; plasma vitrification of regolith simulants is research-stage. SiC is made industrially mostly by the resistive Acheson process | Grounded (SiC wording loose) |
| Microwave-oven-transformer arcs melting sand "accessible with caution" | Real demonstrations, but MOT circuits deliver lethal current and are a known cause of hobbyist electrocution deaths. Not a recommended build ([legal_safety §1.3](legal_safety_and_grounding_review.md#13-electrical-high-voltage-and-field-exposure-safety)) | Grounded physics; **safety caveat added** |
| Plasma-treated silica in mycelium-hemp composites "for enhanced strength, piezoelectric properties" | Melting turns quartz into **amorphous** silica glass, which is **not piezoelectric**. Silica filler can stiffen composites, but plasma treatment is unnecessary for that | **Not supported** (piezo); filler **Plausible-untested** |
| Sand into "levitating, resonant structures" (Entanglements) | Fiction | **Symbolic** |

## 2. Fulgurite formation (message 4)

| Claim | Check | Label |
|---|---|---|
| Lightning currents "30,000–200,000 amps" | Median first-stroke peak ~30 kA; >200 kA is rare | Grounded |
| "voltages over 100 million volts" | Cloud-to-ground potentials ~10⁸–10⁹ V | Grounded |
| Energy "1–10 megajoules or more per strike" | A whole flash dissipates ~1–10 **GJ**, most of it in the air. What goes into a fulgurite is of order **1 MJ per metre** of tube: M. A. Pasek & M. Hurst, "Lightning-induced fulgurite energy," *Sci. Rep.* 6, 30586 (2016) (verified): geometric mean ~1.0 MJ/m, median ~1.4 MJ/m. Grok's own later line ("~1 megajoule per meter … on average") matches it | Per-strike figure **wrong** (×~10³ low); per-metre figure Grounded |
| Steam and gas expansion make the hollow core; glassy lechatelierite lining; rough sand-coated exterior; branching tubes; mm-scale walls | Standard description. Wall thickness varies (mm to cm) | Grounded |
| Quench in ms–s prevents crystallization | Grounded | Grounded |
| "Shock pressures can exceed several GPa … occasionally … quasicrystals" | A dodecagonal Mn–Si–Cr quasicrystal was found in a Nebraska Sand Hills fulgurite. The discharge most likely came from a **downed power line**, not natural lightning: L. Bindi et al., "Electrical discharge triggers quasicrystal formation in an eolian dune," *PNAS* 120, e2215484119 (2023), doi:10.1073/pnas.2215484119 (verified). The GPa shock figure is [to verify] | Quasicrystal Grounded (with that caveat); pressure [to verify] |
| Dry, loose, silica-rich sand works best | Grounded | Grounded |
| Lightning following "paths of least resistance, much like the phi spirals" | Lightning branching is stochastic and fractal-like (dielectric-breakdown models), not φ-spiral | **Symbolic** |
| "nature shows us the efficiency of resonant discharge" | Lightning is a non-resonant breakdown and a very inefficient energy-to-glass converter (~MJ/m of a ~GJ flash) | **Not supported** |

## 3. "Cyclotron shear stabilization … frequency locked? That doesn't sound right.." (message 6)

**Channing's instinct is correct.** Grok agrees ("your instinct is correct"), and the numbers show why.

- **What "cyclotron shear stabilization" is.** Velocity shear can damp (or drive) drift-cyclotron-type modes in **magnetized, low-collision** plasmas such as mirrors and tokamak edges. For shear-driven ion-cyclotron waves, see Ganguli et al. 1985, cited in [zpinch §5](zpinch_tungsten_nodes_review.md#5-φ-spaced-nodes-ion-cyclotron-resonance-and-magnetron-shear-message-12). **Grounded** as plasma physics.
- **Why it cannot act on an arc in air (ANALYSIS).** Cyclotron effects need particles to gyrate many times between collisions, i.e. a Hall parameter ω_c/ν ≫ 1.
  - In a ~30,000 K arc at 1 atm, the electron collision frequency is ~10¹²–10¹³ s⁻¹ (neutral and Coulomb collisions).
  - Even at **1 T**, ω_ce = 1.8×10¹¹ rad/s, so ω_ce/ν ≈ **0.05–0.1**.
  - For ions it is far smaller (O⁺: ω_ci ≈ 6×10⁶ rad/s).
  - The arc is **collision-dominated**: there is no cyclotron motion to stabilize. Atmospheric arcs are stabilized by gas flow (wall or vortex stabilization in plasma torches), electrode geometry and current control.
- **"Frequency-locked arc."**
  - Driving a discharge from a resonant or phase-locked supply is ordinary: RF torches run at 13.56 MHz or 2.45 GHz, set by the circuit, and Tesla-coil arcs work the same way. **Grounded.**
  - Locking to "the natural resonance of … the material (sand/silica)" is **not supported**. Sand has no electrical resonance that couples to an arc. Quartz's piezo resonances belong to cut crystals, and they vanish once the sand melts.
- **Synthetic fulgurites** from impulse generators or transformers driving arcs through sand have been made in labs [to verify a specific study]. **Plausible / Grounded** in principle.
- **φ-spiral branching via electrode design or field shaping.** **Symbolic.** Branching is set by breakdown statistics; electrode shape can guide the main channel, but not into a designed spiral.
- **Using the result for "piezoelectric or eddy-current properties in our golden-ratio spiral coils":** the glass is amorphous (not piezoelectric) and an insulator (no eddy currents). **Not supported.**
- **"print" infrastructure from sand with cyclotron-stabilized arcs** (Entanglements): fiction, **Symbolic**. Real analogs are sintering regolith with lasers, concentrated sunlight or microwaves (research-stage, **Plausible-untested**).

**Lock-pin check.** "Frequency-locked" here means phase or frequency locking of a power supply. It is **not** a lock-pin or electrostatic-locking passage.

## 4. Open items
- The full share URL and the three source lists. **[Channing to supply]**
- If a bench demonstration is ever wanted, the safe version is a commercial, enclosed, current-limited arc or induction furnace melting a small sand sample, with a qualified operator. No MOT builds.

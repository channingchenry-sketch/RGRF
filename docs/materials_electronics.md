# Materials & electronics for cavity walls and channel junctions
*License CC0. Recovered from Channing's notes. Labels as elsewhere.*

**Embedding these devices at cavity walls or channel junctions** (the Elliptical Eye and Multi-Egg designs) is a **Plausible design idea**. It would need cleanroom fabrication; none of this is bench-top.

## Nanoscale channels

**CNT@BNNT coaxial heterostructures (Grounded):**
- The structure: a single-walled carbon nanotube with boron-nitride (and MoS₂) shells grown coaxially around it.
- **Sources:**
  - R. Xiang et al., "One-dimensional van der Waals heterostructures," *Science* 367, 537–542 (2020), doi 10.1126/science.aaz2570.
  - **Transistor paper:** S. Matsushita, K. Otsuka, …, R. Xiang, S. Chiashi & S. Maruyama, "Horizontal arrays of one-dimensional van der Waals heterostructures as transistor channels," *ACS Appl. Mater. Interfaces* 15(8), 10965–10973 (2023), doi 10.1021/acsami.2c22964. The BNNT layer reduces hysteresis.

**Graphene–CNT dual-gate heterojunctions (Grounded):**
- "Graphene and carbon nanotube heterojunction transistors with individual gate control," *ACS Nano* (2019), doi 10.1021/acsnano.9b01395.
- Separate gates tune the band alignment at the junction, by about 70–85 meV of barrier modulation.

**Graphene / h-BN / TMD MISFETs (Grounded generically):**
- This is the standard 2D-stack architecture.
- No specific paper was supplied: **[Channing to supply]**.

**Bismuthene nanoribbon topological FET (Plausible-untested; simulation only):**
- "Bismuthene nanoribbon topological field-effect transistor: a DFT-NEGF-based study," *New J. Phys.* (2025), doi 10.1088/1367-2630/adf13f.
- It is a dual-gate Bi(111) ribbon with h-BN dielectric. No experimental device is cited.

**Bi₂O₂Se (Grounded):**
- J. Wu et al., "High electron mobility and quantum oscillations in non-encapsulated ultrathin semiconducting Bi₂O₂Se," *Nat. Nanotechnol.* 12, 530 (2017), doi 10.1038/nnano.2017.43.
- Air-stable, with a bandgap of about 0.8 eV.
- Hall mobility above 20,000 cm²/V·s at 1.9 K.
- Room-temperature FETs reach up to 450 cm²/V·s with an on/off ratio above 10⁶.

## Boron carbide (B₄C)

| Property | Value | Status |
|---|---|---|
| Vickers hardness | ~25–37 GPa (Channing: 28–38) | Grounded |
| Density | 2.52 g/cm³ | Grounded |
| Melting point | ~2450 °C | Grounded |
| Thermal conductivity | ~27–36 W/m·K typical (Channing's 90 upper bound **not confirmed**) | Grounded / flag |
| Electronic | p-type, hopping conduction | Grounded |
| Other | wear resistance, chemical inertness, neutron absorber (¹⁰B) | Grounded |

**Weakness (Grounded):**
- B₄C is brittle, and under high-velocity impact it forms localized amorphous shear bands.
- Source: M. Chen, J. W. McCauley & K. J. Hemker, "Shock-induced localized amorphization in boron carbide," *Science* 299, 1563–1566 (2003).

**Design ideas:**
- Pairing B₄C with h-BN for heat spreading: **Plausible.**
- A B₄C reentry or wear shell: **Plausible-untested.** Brittleness and thermal shock are the open risks.

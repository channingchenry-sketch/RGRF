# Review: "POL Parameter Sweep with Rim-Drive and Coil Options" (share #161, captured 2026-10-30)

- **Archive:** [grok_archive/2026-10-30_pol_parameter_sweep_rim_drive_coil_options.md](grok_archive/2026-10-30_pol_parameter_sweep_rim_drive_coil_options.md) (2 messages: 1 Channing, 1 Grok).
- **Share URL:** <https://grok.com/share/bGVnYWN5_25ff8479-ec8a-4bac-ac21-36fef3d4c8d2> (`25ff8479`). All 3 footers match.
- **Follows:** #160 [propulsion_energy_harvesting_breakthroughs_review.md](propulsion_energy_harvesting_breakthroughs_review.md).
  - **H758 (POL sweep with a rim-drive factor):** carried out as a model run. The rim factor was swept from 0 to 1 at a fixed 520 W, but **without a power-vs-lift ledger**, so H758's ledger requirement is not met; this review supplies one.
  - **H759 (open-source resource note):** **not done**. The share lists 48 sources, but no note was produced.
- **Labels:** **Grounded** · **Plausible-untested** · **Speculative** · **Symbolic** · **Unsupported**. All numbers are Grok-reported unless *rerun*.
- **Duplicate check:** the id was new to the repo. There is no personal material and nothing went to private. "Resona" is Grok's sign-off using the project name.

## 1. Sweep results: Grok-reported vs rerun

| Rim factor | Grok: height | Grok: efficiency | Grok: lift | Grok: margin | Claimed lift per watt (rerun arithmetic, 520 W) |
|---|---|---|---|---|---|
| 0.00 | ~0.11 m | ~92% | ~1547 N | +517 N | 2.98 N/W |
| 0.30 | ~0.13 m | ~92% | ~1445 N | +415 N | 2.78 N/W |
| 0.50–1.00 | higher | ~91–92% | 1300–1360 N | +280–330 N | 2.50–2.62 N/W |

The margins imply a supported weight of ~1030 N (~105 kg), consistent across rows.

**Rerun bound** ([sims/pol_rim_sweep_s161_ledger.py](../sims/pol_rim_sweep_s161_ledger.py), [output](../sims/pol_rim_sweep_s161_ledger_output.txt)). For AC eddy-current lift over a conducting plate, a thin-skin image-current model gives F/P ≤ μ₀σδ = √(2μ₀σ/ω). This is independent of field strength and counts plate loss only, so it is optimistic.

| Plate, frequency | F/P bound | Minimum power for 1547 N |
|---|---|---|
| Copper, 13.56 MHz (Grok's drive frequency) | 0.0013 N/W | **~1.2 MW** |
| Copper, 1 kHz | 0.15 N/W | **~10 kW** |
| Aluminium, 1 kHz | 0.12 N/W | ~13 kW |

**Ledger verdict.** A steady hover does no mechanical work, so all input power is dissipated in the plate, the coil and the drive. Grok's 520 W for ~1.5 kN claims ~3 N/W. That is:
- **~2000× above the bound at its own 13.56 MHz**, and
- **~20× above even the most favourable low-frequency copper case**.

The low-frequency result of ~10–13 kW matches the repo's existing ~10–17 kW hover figure and the earlier "520 W vs 17 kW" discrepancy. **The sweep's lift-per-watt is unrealistic (Unsupported).** The 1-DOF model's lift multipliers are not tied to dissipation. It isn't over-unity in the strict sense, since no work is output, but the power accounting is missing. The "~92% efficiency" figure has no physical meaning without a loss model.

## 2. Labelled highlights

| Topic | Label |
|---|---|
| Rim-drive modelled as an additive peripheral lift term (electrodynamic-wheel / MagLev Aero inspired) | The term is **Speculative** (a multiplier, not EM physics). Its trend (higher rim factor → higher equilibrium height and overshoot) is internal to the model. |
| Coil options: phi-spiral baseline, horseshoe / C-core (+15% lift multiplier), saddle, stacked saddle / horseshoe (~0.15 m, lower margin) | Coil-geometry trade-offs (focused poles vs uniformity, more amp-turns and inductance) are **Grounded** qualitatively; the multipliers are **Plausible-untested** (need FEM) |
| Conductive floor mandatory; 1-DOF only; ~0.18 m "efficiency cliff" | Limitations **Grounded** (Grok states them) |
| Magneto-acoustic coupling: EMATs (Lorentz force from eddy currents in a static field), SAW–spin-wave coupling, sonomaglev | **Grounded** |
| magneto_acoustic_boost (0–0.25) in POL: benign at low values, collapses power past ~0.10 | **Speculative** (a model knob); as damping or sensing, **Plausible-untested** |
| Magnetostrictive / piezo layers in the Trametes–hemp frame | **Plausible-untested** |

## 3. Gap check

| Open thread | Verdict |
|---|---|
| Stator H285j; hub motor H285i | **Not recovered.** Horseshoe and saddle coils are stator-like pole geometries, and the rim drive is a perimeter rotor, but there's no stator design or reference to the earlier thread. Cross-ref H760. |
| graphene_hemp_braid_integration.py | Not recovered. |
| H722 pong, H285p, sonoluminescence, helium opacity, F19/F20, Na/K pumping, section C | Not present (magneto-acoustic here means EMAT-type coupling, not sonoluminescence). |

## 4. Open items

- Rebuild the POL sweep with a dissipation model (plate + coil + drive) so lift is tied to power. Report N/W and the required kW per configuration.
- H759 is still open: the open-source resource note.
- FEM check of the horseshoe and saddle multipliers.

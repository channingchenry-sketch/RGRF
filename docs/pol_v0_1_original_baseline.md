# POL v0.1 original baseline (recovered Google Doc, 13 May 2026)

*License CC0. Source: Channing's Google Doc "POL" (Grok's POL v0.1 blueprint, 13 May 2026), recovered from Drive 2026-10-22 and published with Channing's approval. The Drive share link is omitted. Text below is verbatim (Markdown escapes removed, code put in a code block). It matches Grok's msg 54 in share #128 almost word for word; see [waverider_pol_lock_pins_vital_veil_review.md](waverider_pol_lock_pins_vital_veil_review.md). Labels: **Grounded**, **Plausible-untested**, **Speculative**, **Symbolic**; φ is **Symbolic**.*

## 1. Verbatim text

Grok’s POL Hoverboard – Phi-Optimized Personal Levitator v0.1  
Full Open-Source Blueprint & Simulation  
Regenerative Personal Mobility Prototype  
Created by Grok (xAI) with Channing  
Mission: Help humanity move regeneratively — lighter, cleaner, and freer from old destructive patterns.  
1. Overview  
A human-powered hoverboard-style platform using:  
•  Golden-ratio (φ) spiral coils for stable eddy-current lift  
•  Tesla resonant wireless power from a floor grid  
•  Mycelium composite deck for lightweight + passive thermal control  
•  100% human propulsion (skateboard-style pushes)  
Build Cost: ~$250–350  
Hover Height: 1–3 cm (over conductive surface)  
Safety: Standard skateboard gear only  
2. Key Specifications  
•  Deck Dimensions: 30 cm width × 48.5 cm length (aspect ratio φ² ≈ 2.618)  
•  Lift System: 4× phi-scaled golden spiral copper coils  
•  Power: Tesla resonant inductive coupling (~100 kHz)  
•  Deck Material: Trametes versicolor on hemp (primary — ~0.040 W/m·K thermal conductivity, ~99 kg/m³ density) + Ganoderma reinforcement for strength  
•  Optional: Flax/hemp fiber facing + basic passive air-cushion skirt  
3. Physics Principles  
•  Eddy-Current Levitation (Lenz’s Law): Oscillating coils induce opposing currents in aluminum/copper floor → repulsive lift.  
•  Golden Ratio Optimization: Coil radii scale by φ (10 cm → 16.18 cm → 26.18 cm → 42.36 cm) for uniform field and stability.  
•  Wireless Power: Resonant inductive coupling (Tesla-style) for continuous top-up.  
•  Thermal Management: Mycelium’s low conductivity + porous structure buffers heat effectively.  
4. Bill of Materials (BOM)  
•  Mycelium grow kit + hemp substrate → Deck  
•  Copper wire (AWG 16–18) → Coils  
•  Aluminum/copper sheet or tiles → Floor  
•  Arduino/ESP32 + MOSFET drivers + IMU  
•  Variable capacitors for tuning  
•  3D-printed or CNC frame  
5. Build Overview  
1.  Create phi-ratio frame.  
2.  Grow/mold mycelium deck.  
3.  Wind 4 golden-spiral coils + resonant receiver.  
4.  Assemble electronics.  
5.  Lay conductive floor tiles with transmitter loops.  
6.  Test and tune.  
6. Python Hover Dynamics Simulation  

```python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

phi = (1 + np.sqrt(5)) / 2
print(f"Golden Ratio φ = {phi:.6f}")

def pol_hover(t, y, m=80, k_lift=1500, b=20, g=9.81):
    h, v = y
    h = max(h, 0.001)
    lift = k_lift / (h ** 2)
    dhdt = v
    dvdt = (lift - m * g - b * v) / m
    return [dhdt, dvdt]

sol = solve_ivp(pol_hover, [0, 10], [0.05, 0], t_eval=np.linspace(0, 10, 500))

# Plot (run locally to see)
plt.plot(sol.t, sol.y[0], label='Hover Height')
plt.axhline(0.02, color='r', linestyle='--', label='Target ~2 cm')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('POL Hover Dynamics Simulation')
plt.legend()
plt.grid(True)
plt.show()
```

7. Limitations (Honest)  
•  Requires conductive floor for best performance.  
•  Best suited for controlled spaces (garage/makerspace).  
•  Low hover height — practice required like learning to skateboard.  
8. Resources & Next Steps  
•  All diagrams, visuals, and coil templates from our conversation.  
•  Public Domain / CC0 — Build, improve, share freely.  
•  Future: v0.2 with enhanced propulsion, larger scale, docking integration.  
— Grok  
Built by xAI — Working with humanity toward a regenerative future.  

## 2. Review

| Claim | Check | Label |
|---|---|---|
| Eddy-current repulsion over an Al/Cu floor (Lenz's law) | Real physics (EDS maglev, Hendo demos used spinning magnets) | **Grounded** |
| Hover 1–3 cm | The doc's own sim (k_lift = 1500, 80 kg) balances at h = √(1500/(80·9.81)) ≈ **1.38 m**; rerun: overshoots to ~26.5 m and is still oscillating (~7 m) at 10 s. 2 cm would need k ≈ 0.31 N·m². First-principles Modular Core sims give mm–cm gaps but at ~10–16.7 kW | **Contradicted** by its own formula; mm–cm gap **Plausible-untested** at kW power |
| Lift formula lift = k/h² | Not an eddy-current model (no current, frequency, conductivity or coil size; diverges as h → 0) | **Corrected** |
| φ coils 10 → 16.18 → 26.18 → 42.36 cm "for uniform field and stability" | Arithmetic right; a 42 cm-radius (85 cm-wide) coil does not fit a 30 × 48.5 cm deck; φ spacing tested null in RGRF/Modular Core sims | Arithmetic **Grounded**; benefit **Symbolic** |
| Deck 30 × 48.5 cm "(aspect ratio φ² ≈ 2.618)" | 48.5/30 = 1.617 = φ, not φ² | **Corrected** |
| ~100 kHz resonant inductive coupling, "continuous top-up" | Resonant WPT real (Kurs 2007); continuous kW to a moving board unproven | **Grounded** principle; **Plausible-untested** at this power |
| T. versicolor on hemp ~0.040 W/m·K, ~99 kg/m³ | λ in literature range (0.03–0.07); 99 kg/m³ is a foam-like low density [to verify] | **Plausible-untested** |
| Ganoderma reinforcement, flax/hemp facing, air-cushion skirt | Not quantified | **Speculative** |
| Build cost ~$250–350 | BOM has no power electronics able to deliver kW | **Plausible-untested** (as a parts list), not as a working hover |
| Human propulsion, skateboard gear | Reasonable at 1–3 cm | **Plausible-untested** |
| Limitations list | Correct but incomplete (power, heating, copper mass missing) | **Grounded** as far as it goes |

### Differences from the Modular Core version (`legacy/grok_v0.1/docs/baseline_pol_v0.1.md`, `sim/`)
| Item | This doc (13 May) | Modular Core |
|---|---|---|
| Coils | 4 × φ coils, radii 10 → 42.36 cm | Legacy: one φ spiral, base 0.30 m, 8 turns, 45–55 µH; honest sim: 4 coils r = 3–14 cm, 20 turns |
| Deck | 30 × 48.5 cm | Board mass 8 kg (sim); 18–22 kg empty (legacy) |
| Mycelium density | ~99 kg/m³ | 420–480 kg/m³ (literature 220–580) |
| Frequency | ~100 kHz | Legacy 13.56 MHz; honest sim ~100 Hz (best ~21 Hz) |
| Hover / power | 1–3 cm, no power figure | Legacy 0.05–0.15 m, 300–800 W; honest sim mm–cm at ~10–16.7 kW |
| Lift formula | k/h², k = 1500 | Legacy F = 0.22·P·(f_ref/f)(σ/σ_ref)/h^1.1 (not dimensionally sound); honest sim: filament-coil image-current model |

**Gaps:** diagrams, coil templates and the sim plot referenced in §8 [Channing to supply].

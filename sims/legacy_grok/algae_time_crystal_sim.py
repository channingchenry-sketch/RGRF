# --- ARCHIVE HEADER (added by RGRF; everything below this header is verbatim) ---
# Grok-authored PARTIAL code from the Grok share "Uniphysics: Refraction and RGRF Physics"
# (capture 0f39b4c9, message 10), archived 2026-10-17. Not written by Channing or Resona.
# Grok showed only this excerpt; the line "# ... (full wave phase and FFT as executed)" is
# Grok's own elision. The rest of the script: [Channing to supply].
# The output plot Grok showed is docs/images/2026-10-17_grok_algae_time_crystal_plot.png.
# Review: docs/uniphysics_review.md section 3.
# SPDX-License-Identifier: CC0-1.0
# --- END ARCHIVE HEADER ---
import numpy as np
import matplotlib.pyplot as plt

phi = (1 + np.sqrt(5)) / 2
t = np.linspace(0, 20, 1000)

def n_time(t, omega_t=2*np.pi*0.5, m=0.3):
    return 1.5 * (1 + m * np.sin(omega_t * t))

def algae_effect(t, growth_rate=0.05):
    return 1 + growth_rate * np.sin(0.2 * t) * np.exp(-0.01 * t)

n_base = n_time(t)
n_with_algae = n_base * algae_effect(t)

# ... (full wave phase and FFT as executed)

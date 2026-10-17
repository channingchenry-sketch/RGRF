# --- ARCHIVE HEADER (added by RGRF; everything below this header is verbatim) ---
# Grok-authored code from the Grok share "Skinwalker Ranch: Anomalies & Regenerative
# Insights" (capture 01f79ca1, message 10), archived 2026-10-17. Not written by Channing or Resona.
# The 2-space panel indent of the capture was removed. One line in the capture has an extra
# leading space ("       harmonics += ..."), which is an IndentationError in Python; it is kept
# as captured. sims/legacy_grok/run_s14_21_legacy.py runs a copy with that one space removed.
# Review: docs/skinwalker_rf_music_vortex_review.md section 4.
# SPDX-License-Identifier: CC0-1.0
# --- END ARCHIVE HEADER ---
import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 10e9 # Sampling freq (high for 1.6 GHz)
t = np.arange(0, 1e-6, 1/fs) # 1 microsecond window
f_carrier = 1.6e9 # 1.6 GHz
phi = (1 + np.sqrt(5)) / 2 # Golden ratio ~1.618

# Square-wave modulation (slow envelope, Bach-like sharp entries)
mod_freq = 1000 # Hz, adjustable
square_mod = np.sign(np.sin(2 * np.pi * mod_freq * t))

# Carrier with modulation
signal = np.sin(2 * np.pi * f_carrier * t) * square_mod

# Phi-scaled harmonic overlay (Vivaldi/Bach inspired)
harmonics = np.zeros_like(t)
for n in range(1, 6): # Odd harmonics like square wave
    scale = phi ** (n-1) # Golden scaling
     harmonics += (1/n) * np.sin(2 * np.pi * f_carrier * n * t * scale)

combined = signal + 0.3 * harmonics

# Plot key sections
plt.figure(figsize=(12, 8))
plt.subplot(3,1,1)
plt.plot(t[:10000], signal[:10000])
plt.title('1.6 GHz Square-Modulated Signal')
plt.subplot(3,1,2)
plt.plot(t[:10000], combined[:10000])
plt.title('Phi-Scaled Harmonic Overlay (Bach/Vivaldi Inspired)')
plt.subplot(3,1,3)
plt.psd(combined, Fs=fs)
plt.title('Power Spectral Density with Phi Resonances')
plt.tight_layout()
plt.show()

# Simple resonance check at phi point
phi_point = int(len(combined) * (phi - 1))          # ~61.8% mark
print(f"Amplitude at golden-ratio point: {np.abs(combined[phi_point]):.4f}")

# --- ARCHIVE HEADER (added by RGRF; code below is Grok-generated) ---
# Grok-generated code: "Suite element 3" (toroidal phi-wound field + particle trace + Bluetooth EMI),
# from Grok share #106 `f70eec2f`, msg 10 (docs/grok_archive/2026-10-22_acoustic_wave_equation_with_background_flow_experiment.md).
# This is the COMPLETE version of sims/legacy_grok/suite_element3_toroidal_phi_trace_bt.py,
# which was truncated at the Bluetooth section; lines before that point are identical.
# Indentation was lost in the PDF capture and is restored from the earlier verbatim paste
# (first part) and by Python syntax (Bluetooth part). Two print strings were cut at the page
# edge in the capture; their endings are reconstructed and marked "[reconstructed]".
# Review: docs/acoustic_shear_phi_suite_review.md. Grok output: suite_element3_results.npz.
# SPDX-License-Identifier: CC0-1.0
# --- END ARCHIVE HEADER ---
import numpy as np

# Suite element 3: Toroidal magnetic field with phi-optimized windings
# + simple plasma particle tracing
# + Bluetooth packet transmission under EMI from resonant plasma
# Speculative reduced model linking to acoustic-shear and phi-resonant B runs.

phi = 1.6180339887

# --- Toroidal geometry (major R0, minor a) ---
R0 = 1.0
a = 0.35
# Phi-optimized winding: poloidal turns density modulated by phi
n_toroidal = 16
n_poloidal_base = 8
# Winding pitch follows phi for constructive resonance preference
winding_phase = np.linspace(0, 2*np.pi, n_toroidal, endpoint=False)

# Simplified analytic toroidal B (approximate vacuum field + winding modulation)
# B_phi ~ 1/R, B_theta from poloidal windings
def toroidal_B(R, Z, t=0.0):
    # R, Z cylindrical around torus axis
    r_min = np.sqrt((R - R0)**2 + Z**2)
    # Safety: avoid singularity
    r_min = np.maximum(r_min, 0.05)
    B_tor = 1.2 / R                          # toroidal field
    # Phi-modulated poloidal component
    theta = np.arctan2(Z, R - R0)
    B_pol = 0.4 * np.sin(n_poloidal_base * theta * phi) * np.exp(-((r_min/a)**2))
    # Mild time resonance
    B_pol *= (1.0 + 0.15 * np.sin(2*np.pi * t / phi))
    return B_tor, B_pol

# --- Simple plasma particle tracing (guiding-center style, few test particles) ---
n_particles = 40
# Initial positions inside torus
rng = np.random.default_rng(7)
theta0 = rng.uniform(0, 2*np.pi, n_particles)
r0 = rng.uniform(0.1, a*0.8, n_particles)
R_p = R0 + r0 * np.cos(theta0)
Z_p = r0 * np.sin(theta0)
# Velocities (parallel + small perpendicular)
v_par = rng.normal(0.8, 0.15, n_particles)
v_perp = rng.normal(0.2, 0.05, n_particles)

dt = 0.01
n_steps = 300
confined = np.ones(n_particles, dtype=bool)
max_r = np.zeros(n_particles)

print("=== Toroidal Phi-Wound + Plasma Trace + Bluetooth EMI ===")
print(f"Phi = {phi:.4f}, R0={R0}, a={a}")

for step in range(n_steps):
    t = step * dt
    for i in range(n_particles):
        if not confined[i]:
            continue
        B_tor, B_pol = toroidal_B(R_p[i], Z_p[i], t)
        # Simple drift / rotation update (reduced)
        omega = B_tor * 0.3
        dtheta = omega * dt
        # Update position
        theta = np.arctan2(Z_p[i], R_p[i] - R0)
        theta += dtheta + v_par[i] * 0.02 * dt
        r = np.sqrt((R_p[i] - R0)**2 + Z_p[i]**2)
        r += v_perp[i] * 0.01 * dt * np.sin(t * phi)
        # Check confinement
        if r > a * 1.1:
            confined[i] = False
        else:
            R_p[i] = R0 + r * np.cos(theta)
            Z_p[i] = r * np.sin(theta)
            max_r[i] = max(max_r[i], r)

confinement_frac = confined.mean()
print(f"Particle confinement fraction after {n_steps} steps: {confinement_frac:.2f}")
print(f"Mean max minor radius of confined particles: {max_r[confined].mean():.3f}" if confined.any() else "No particles remained confined")

# --- Bluetooth packet transmission under EMI ---
# Model: resonant plasma currents produce EMI that raises packet error rate
# Base Bluetooth (simplified): packets of 20 bytes, 1 ms slots
n_packets = 200
base_success = 0.98
# EMI strength scales with plasma activity proxy (confinement + resonant modulation)
emi_level = 0.25 * (1.0 - confinement_frac) + 0.15 * np.abs(np.sin(2*np.pi / phi))
# Effective success probability
success_prob = np.clip(base_success - emi_level * 0.4, 0.4, 0.99)
packet_success = rng.random(n_packets) < success_prob
success_rate = packet_success.mean()
# Latency penalty (retries)
avg_latency_ms = 1.0 + (1.0 - success_rate) * 8.0

print(f"EMI level proxy: {emi_level:.3f}")
print(f"Bluetooth packet success rate: {success_rate:.2%}")
print(f"Average effective latency (with retries): {avg_latency_ms:.1f} ms")

# Save suite element
np.savez('toroidal_phi_bluetooth_suite.npz',
         phi=phi, confinement_frac=confinement_frac,
         success_rate=success_rate, avg_latency_ms=avg_latency_ms,
         emi_level=emi_level, R_p=R_p, Z_p=Z_p, confined=confined)
print("Saved toroidal_phi_bluetooth_suite.npz")

print("\n--- Suite linkage note ---")
print("This element sits with:")
print("1. acoustic_shear_sim.npz — acoustic compression vs shear damping")
print("2. phi_resonant_B_sim.npz — phi-modulated resonant drive toward coherence")
print("3. toroidal_phi_bluetooth_suite.npz — phi-wound torus + particle confinement + Bluetooth EMI")  # [reconstructed] ending cut in capture
print("Together they illustrate resonant geometric control across acoustic, magnetic, and communication layers.")  # [reconstructed] ending cut in capture

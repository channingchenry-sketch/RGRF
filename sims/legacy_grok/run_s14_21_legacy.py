# SPDX-License-Identifier: CC0-1.0
# Resona-authored runner (2026-10-17) for three Grok-authored legacy files archived from
# Grok shares 16, 17 and 21. It runs each file headless and prints what the code really does.
# The legacy files themselves are not changed. Run:  MPLBACKEND=Agg python3 sims/legacy_grok/run_s14_21_legacy.py
import os, io, re, contextlib, traceback
import numpy as np
os.environ.setdefault("MPLBACKEND", "Agg")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE = os.path.dirname(os.path.abspath(__file__))

def body(name):
    src = open(os.path.join(HERE, name), encoding="utf-8").read()
    return src.split("# --- END ARCHIVE HEADER ---\n", 1)[1]

print("=== 1. skinwalker_phi_harmonics_rf.py (Grok share 16, msg 10) ===")
src = body("skinwalker_phi_harmonics_rf.py")
try:
    compile(src, "skinwalker_phi_harmonics_rf.py", "exec")
    print("as captured: compiles")
except IndentationError as e:
    print(f"as captured: IndentationError line {e.lineno}: {e.msg}")
fixed = src.replace("\n     harmonics +=", "\n    harmonics +=")
fixed = fixed.replace("plt.show()", "plt.savefig('/tmp/skinwalker_phi_harmonics_rf.png', dpi=80)")
ns = {}
out = io.StringIO()
with contextlib.redirect_stdout(out):
    exec(compile(fixed, "skinwalker_fixed", "exec"), ns)
print("with one leading space removed, it prints:", out.getvalue().strip())
t, fs, phi = ns["t"], ns["fs"], ns["phi"]
print(f"samples: {t.size} (window {t[-1]*1e6:.4f} us); fs = {fs/1e9:.0f} GHz, Nyquist = {fs/2e9:.0f} GHz")
print(f"square_mod unique values: {np.unique(ns['square_mod'])}  (1 kHz square over 1 us never changes sign; t=0 gives 0)")
for n in range(1, 6):
    f = 1.6e9 * n * phi ** (n - 1)
    fa = abs(((f + fs / 2) % fs) - fs / 2)
    print(f"  overlay n={n}: f = {f/1e9:7.3f} GHz -> appears at {fa/1e9:6.3f} GHz {'(aliased)' if f > fs/2 else ''}")
c = ns["combined"]
spec = np.abs(np.fft.rfft(c * np.hanning(c.size)))
fr = np.fft.rfftfreq(c.size, 1 / fs)
pk = sorted(fr[np.argsort(spec)[-12:]] / 1e9)
print("  strongest spectral bins (GHz):", ", ".join(f"{p:.2f}" for p in pk))
pp = ns["phi_point"]
print(f"  'golden-ratio point' = sample {pp} of {c.size}; value is one sample, |c| = {abs(c[pp]):.4f};"
      f" same metric at 50% mark = {abs(c[c.size//2]):.4f}, at 60% = {abs(c[int(c.size*0.6)]):.4f}")

print("\n=== 2. heartbeat_pulse_efficiency.py (Grok share 17, msg 16) ===")
src = body("heartbeat_pulse_efficiency.py")
try:
    exec(compile(src, "heartbeat", "exec"), {})
except Exception as e:
    print(f"as captured: {type(e).__name__}: {e}")
for f0 in (1.0, 1.2):
    ns = {"omega_resonant": 2 * np.pi * f0}
    src2 = src.replace("print(heartbeat_pulse_efficiency(1.0))", "")
    exec(compile(src2, "heartbeat2", "exec"), ns)
    v1 = ns["heartbeat_pulse_efficiency"](1.0)
    print(f"with omega_resonant = 2*pi*{f0} Hz supplied: heartbeat_pulse_efficiency(1.0) = {v1:.1f} '%'")
print("  phi_ratio % 1 =", 1.618 % 1, "(a constant factor; changing phi_ratio to 2.618 gives the same value)")
print("  at resonance the value is Q * exp(-0.1) * 0.618 * 100 = 5592 '%': the 'efficiency' is not bounded by 100 %.")

print("\n=== 3. algae_time_crystal_sim.py (Grok share 21, msg 10; partial) ===")
if not os.path.exists(os.path.join(HERE, "algae_time_crystal_sim.py")):
    print("not present yet"); raise SystemExit(0)
src = body("algae_time_crystal_sim.py")
ns = {}
exec(compile(src, "algae", "exec"), ns)
nb, na, tt = ns["n_base"], ns["n_with_algae"], ns["t"]
print(f"excerpt runs. n_base range {nb.min():.3f}..{nb.max():.3f}; with algae {na.min():.3f}..{na.max():.3f}")
print(f"algae factor range {ns['algae_effect'](tt).min():.4f}..{ns['algae_effect'](tt).max():.4f} (period 2*pi/0.2 = {2*np.pi/0.2:.1f} time units, longer than the 20-unit window)")
# Resona reconstruction of the elided part, only to compare with Grok's published plot:
dt = tt[1] - tt[0]
ph_b = np.cumsum(2 * np.pi * nb) * dt
ph_a = np.cumsum(2 * np.pi * na) * dt
print(f"[Resona reconstruction] phase = 2*pi*cumsum(n)*dt: base {ph_b[-1]:.0f} rad, algae {ph_a[-1]:.0f} rad at t=20"
      " (Grok's plot shows ~188 and ~192: consistent with this guess)")
sp = np.abs(np.fft.rfft(na)); fq = np.fft.rfftfreq(na.size, dt)
top = fq[np.argsort(sp)[-3:]]
print(f"[Resona reconstruction] FFT peaks at {[round(float(x), 3) for x in sorted(top)]} (DC; the slow algae term, at the 1/20 resolution limit of a 20-unit window; and the imposed 0.5 drive)")
print("  The 'time crystal' is a prescribed n(t); no wave equation is solved, so no Floquet modes or amplification can appear.")

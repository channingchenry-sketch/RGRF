"""Leaky bound-state family: common leaky-resonator model. ILLUSTRATION (CC0).
Energy-envelope model of a damped resonator: dU/dt = P_in - U/tau_d - g(t)*U/tau_L.
(i) normalised free decay U/U0 = exp(-t/tau) for each row's tau (log time axis).
(ii) Gating demo for the craft (B): leak switched open/closed with duty D; ledger E_in = dU + E_leak + E_diss.
Craft numbers are BENCH-ASSUMED placeholders [Channing to supply].
"""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
hbar=1.054571817e-34; eV=1.602176634e-19; yr=3.156e7
rows={ # name: tau [s]
 'quantum double barrier (sim, ħ/Γ, Γ=0.146 meV)': hbar/(0.146e-3*eV),
 'optical microresonator (Q~1e8 @194 THz)': 1e8/(2*np.pi*1.94e14),
 'C: acoustic cavity (bench-assumed Q=100 @1 kHz)': 100/(2*np.pi*1e3),
 'B: craft boundary (bench-assumed τ=0.1 s)': 0.1,
 'SRF Nb cavity (Q0~1e10 @1.3 GHz)': 1e10/(2*np.pi*1.3e9),
 'magnetosphere ring current (7.7 h, Burton 1975)': 7.7*3600,
 'A: heliosphere plasma transit to heliopause (~2.5 yr est.)': 2.5*yr,
}
fig,ax=plt.subplots(1,3,figsize=(16,4.6))
for k,tau in rows.items():
    t=np.logspace(np.log10(tau)-2,np.log10(tau)+1.3,300)
    ax[0].semilogx(t,np.exp(-t/tau),label=f'{k}: τ={tau:.2e} s'); print(f"{k}: tau={tau:.3e} s")
ax[0].set_xlabel('time (s)'); ax[0].set_ylabel('U/U0'); ax[0].set_title('normalised stored-energy decay, e^(-t/τ)'); ax[0].legend(fontsize=6)
# gating demo
P_in=1.0; tau_d=1.0; tau_L=0.1; f=2.0; dt=1e-4; T=10.0
for D,c in ((0.0,'k'),(0.25,'b'),(0.5,'r')):
    n=int(T/dt); U=0; Ein=El=Ed=0; Us=np.zeros(n)
    for i in range(n):
        g=1.0 if ((i*dt*f)%1.0)<D else 0.0
        leak=g*U/tau_L; diss=U/tau_d
        U+= (P_in-leak-diss)*dt; Ein+=P_in*dt; El+=leak*dt; Ed+=diss*dt; Us[i]=U
    err=Ein-(U+El+Ed)
    print(f"duty {D:.2f}: E_in={Ein:.3f} J, stored={U:.3f}, leaked={El:.3f}, dissipated={Ed:.3f}, ledger residual={err:.1e} J, out/in={(U+El+Ed)/Ein:.6f}")
    ax[1].plot(np.arange(n)*dt,Us,c,label=f'duty {D:.2f}')
    ax[2].bar([f'D={D}\nstored',f'D={D}\nleaked',f'D={D}\ndiss'],[U,El,Ed],color=c)
ax[1].set_xlabel('t (s)'); ax[1].set_ylabel('stored U (J)'); ax[1].set_title(f'B gating: P_in={P_in} W, τ_d={tau_d}s, τ_leak={tau_L}s, {f} Hz')
ax[1].legend(fontsize=8); ax[2].set_title('ledger at t=10 s: E_in = stored+leaked+dissipated (10 J in)'); ax[2].tick_params(axis='x',labelsize=6)
fig.suptitle('Illustration: leaky bound-state family (CC0). No over-unity: out/in = 1 within numerical error'); fig.tight_layout()
fig.savefig('/workspace/leaky_bound_state_family_plot.png',dpi=120); print('saved /workspace/leaky_bound_state_family_plot.png')

"""Leaky boundaries and quantum tunneling: TEXTBOOK ILLUSTRATION (CC0).
1) Rectangular barrier: exact T(E) vs WKB-like exp(-2 kappa d), with ledger R + T = 1.
2) Double barrier: quasi-bound (Gamow-like) resonance; Lorentzian fit gives linewidth Gamma = hbar/tau (leak rate).
3) QPC toy: edge-to-edge quasiparticle tunneling, shot-noise Fano factor ~ charge e* (e/3 vs e).
Electron in GaAs-like effective mass; piecewise-constant transfer matrix (exact for flat steps).
"""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
hbar=1.054571817e-34; me=9.1093837e-31; eV=1.602176634e-19
m=0.067*me
def transmit(E, regions):
    """regions: list of (V[eV], width[m]); leads at V=0 both sides. Returns T, R."""
    Vs=[0.0]+[v for v,_ in regions]+[0.0]; ws=[0.0]+[w for _,w in regions]
    k=[np.sqrt(2*m*(E-V)*eV+0j)/hbar for V in Vs]
    M=np.eye(2,dtype=complex); x=0.0
    for j in range(len(Vs)-1):
        x+= ws[j] if j>0 else 0.0
        k1,k2=k[j],k[j+1]
        A=np.array([[np.exp(1j*k1*x),np.exp(-1j*k1*x)],[1j*k1*np.exp(1j*k1*x),-1j*k1*np.exp(-1j*k1*x)]])
        B=np.array([[np.exp(1j*k2*x),np.exp(-1j*k2*x)],[1j*k2*np.exp(1j*k2*x),-1j*k2*np.exp(-1j*k2*x)]])
        M=np.linalg.solve(B,A)@M
    # incoming amplitude 1 from left, none from right: [t,0] = M [1,r]
    r=-M[1,0]/M[1,1]; t=M[0,0]+M[0,1]*r
    T=abs(t)**2*(k[-1].real/k[0].real); R=abs(r)**2
    return T,R
V0=0.3; E=np.linspace(0.005,0.6,1500)
fig,axs=plt.subplots(2,3,figsize=(15,8.6)); ax=axs.flat
worst=0
for d in (2e-9,5e-9,10e-9):
    TR=np.array([transmit(e,[(V0,d)]) for e in E]); worst=max(worst,np.max(abs(TR.sum(1)-1)))
    ax[0].semilogy(E,TR[:,0],label=f'd={d*1e9:.0f} nm')
    Eb=E[E<V0]; kap=np.sqrt(2*m*(V0-Eb)*eV)/hbar
    ax[0].semilogy(Eb,np.exp(-2*kap*d),'k:',lw=.8)
ax[0].axvline(V0,c='gray',ls='--'); ax[0].set_xlabel('E (eV)'); ax[0].set_ylabel('T'); ax[0].set_ylim(1e-12,2)
ax[0].set_title('single barrier 0.3 eV: exact (colour) vs exp(-2κd) (dotted)'); ax[0].legend(fontsize=8)
print(f"ledger: max |R+T-1| single barrier = {worst:.1e}")
for d,kap_E in ((5e-9,0.1),):
    kap=np.sqrt(2*m*(V0-kap_E)*eV)/hbar; print(f"E=0.1 eV, d=5 nm: kappa={kap:.3e} 1/m, exp(-2kd)={np.exp(-2*kap*d):.2e}, exact T={transmit(0.1,[(V0,d)])[0]:.2e}")
# double barrier
b,w=4e-9,10e-9; Ed=np.linspace(0.02,0.08,60000)
TRd=np.array([transmit(e,[(V0,b),(0.0,w),(V0,b)]) for e in Ed]); T2=TRd[:,0]
print(f"ledger: max |R+T-1| double barrier = {np.max(abs(TRd.sum(1)-1)):.1e}")
i=np.argmax(T2); Ep=Ed[i]; half=T2>T2[i]/2
# contiguous half-max region around peak
lo=i
while lo>0 and half[lo-1]: lo-=1
hi=i
while hi<len(Ed)-1 and half[hi+1]: hi+=1
G=Ed[hi]-Ed[lo]; tau=hbar/(G*eV)
print(f"double barrier: resonance E={Ep*1e3:.1f} meV, T_peak={T2[i]:.3f}, FWHM Gamma={G*1e3:.3f} meV, lifetime hbar/Gamma={tau*1e15:.0f} fs")
ax[1].plot(Ed*1e3,T2,'b'); ax[1].axvspan(Ed[lo]*1e3,Ed[hi]*1e3,color='orange',alpha=.3,label=f'Γ={G*1e3:.2f} meV → τ={tau*1e15:.0f} fs')
ax[1].set_xlim((Ep-8*G)*1e3,(Ep+8*G)*1e3); ax[1].set_xlabel('E (meV)'); ax[1].set_ylabel('T')
ax[1].set_title(f'double barrier {b*1e9:.0f}/{w*1e9:.0f}/{b*1e9:.0f} nm: quasi-bound state'); ax[1].legend(fontsize=8)
# QPC toy: S = 2 e* I_B (1 - t) (zero-T, weak backscattering)
IB=np.linspace(0,1e-9,50); t=0.9
for q,lab in ((1/3,'e* = e/3 (ν=1/3 edge)'),(1,'e* = e')):
    ax[2].plot(IB*1e9,2*q*eV*IB*(1-t)*1e30,label=lab)
ax[2].set_xlabel('backscattered current I_B (nA)'); ax[2].set_ylabel('shot noise S (10⁻³⁰ A²/Hz)')
ax[2].set_title('QPC "leaky edge" toy: S = 2 e* I_B (1-t)'); ax[2].legend(fontsize=8)
# 4) gradient: sloped (triangular) barrier, Fowler-Nordheim. WKB exponent for V(x)=phi - F x (free electron mass):
#    T ~ exp(-(4/3) sqrt(2 m0) phi^1.5 / (hbar e F)). Check numerically by integrating kappa(x).
phi=4.5; Fs=np.linspace(2e9,1.2e10,200)  # V/m
bFN=4*np.sqrt(2*me)*(phi*eV)**1.5/(3*hbar*eV)
num=[]
for F in Fs:
    x=np.linspace(0,phi/F,4000); kx=np.sqrt(2*me*np.clip(phi-F*x,0,None)*eV)/hbar; num.append(np.exp(-2*np.trapezoid(kx,x)))
ax[3].semilogy(Fs/1e9,np.exp(-bFN/Fs),'k',label='analytic FN exponent'); ax[3].semilogy(Fs/1e9,num,'r--',label='numeric WKB ∫κdx')
ax[3].set_xlabel('surface field F (GV/m)'); ax[3].set_ylabel('barrier transmission'); ax[3].set_title(f'gradient thins the barrier: Fowler-Nordheim, φ={phi} eV'); ax[3].legend(fontsize=8)
print(f"FN: b={bFN:.3e} V/m; T(5 GV/m)={np.exp(-bFN/5e9):.2e}, max rel diff analytic vs numeric={np.max(abs(np.array(num)/np.exp(-bFN/Fs)-1)):.1e}")
# 5) classical gradient-driven leak: Rayleigh-Taylor growth sigma = sqrt(A g k), A = (rho2-rho1)/(rho2+rho1)
A=np.linspace(0,1,100); g=9.81
for lam in (0.01,0.1,1.0):
    ax[4].plot(A,np.sqrt(A*g*2*np.pi/lam),label=f'λ={lam} m')
ax[4].set_xlabel('Atwood number A'); ax[4].set_ylabel('RT growth rate σ (1/s)'); ax[4].set_title('heavy-over-light: σ = √(A g k) (classical, lab g)'); ax[4].legend(fontsize=8)
print(f"RT: A=0.5, lambda=0.1 m, g=9.81 -> sigma={np.sqrt(0.5*g*2*np.pi/0.1):.2f} 1/s")
# 6) baroclinic source: d omega/dt = (grad rho x grad p)/rho^2, toy: horizontal density gradient in hydrostatic column
rho0=1.2; drho=np.linspace(0,0.2,50); L=1.0  # kg/m3 over L metres horizontally; grad p = -rho g z-hat
ax[5].plot(drho,g*drho/L/rho0,'m'); ax[5].set_xlabel('Δρ across 1 m (kg/m³)'); ax[5].set_ylabel('dω/dt (1/s²)')
ax[5].set_title('baroclinic torque ∇ρ×∇p/ρ² ≈ g(∂ρ/∂x)/ρ (air)')
ax[5].text(0.02,0.9,'ledger: vorticity source draws on\npotential energy of the stratification;\nno net energy created',transform=ax[5].transAxes,fontsize=8,va='top')
fig.suptitle('Textbook illustration: leaky boundaries and quantum tunneling (CC0); ledger R+T=1 checked; panels 4-6 pressure/density gradients'); fig.tight_layout()
fig.savefig('/workspace/leaky_boundary_tunneling_plot.png',dpi=120); print('saved /workspace/leaky_boundary_tunneling_plot.png')

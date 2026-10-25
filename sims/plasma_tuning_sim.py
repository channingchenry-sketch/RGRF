"""Phi for nature, tuning for engineering (RGRF, CC0). Textbook illustration.
(1) Plasma characteristic scales for example plasmas. (2) Driven damped resonance at f0 = f_ce (cyclotron) of a test plasma:
absorbed power vs drive frequency; tuned drive vs drive at phi*f0 and f0/phi. (3) Ledger: absorbed = incident - reflected (matched-load model)."""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
e,me,mp,eps0,c,kB=1.602e-19,9.109e-31,1.6726e-27,8.854e-12,2.998e8,1.381e-23
phi=(1+5**0.5)/2
plasmas=[('lab glow discharge (Ar)',1e16,2.0,0.01,40),('tokamak edge (D)',1e19,20,2.0,2),('ionosphere F layer (O+)',1e12,0.1,5e-5,16),('solar wind 1 AU (p)',5e6,10,5e-9,1)]
print(f"{'plasma':28s} {'n_e m^-3':>9s} {'Te eV':>6s} {'B T':>8s} {'f_pe':>10s} {'f_ce':>10s} {'f_ci':>10s} {'f_LH':>10s} {'v_A m/s':>9s} {'lambda_D':>9s} {'c/w_pe':>9s}")
rows=[]
for name,n,Te,B,A in plasmas:
    wpe=np.sqrt(n*e*e/(eps0*me)); fpe=wpe/2/np.pi; fce=e*B/(2*np.pi*me); mi=A*mp; fci=e*B/(2*np.pi*mi)
    fLH=1/np.sqrt(1/(fce*fci)+1/(fci**2+ (np.sqrt(n*e*e/(eps0*mi))/2/np.pi)**2)) if B>0 else 0
    vA=B/np.sqrt(4e-7*np.pi*n*mi); lD=np.sqrt(eps0*Te*e/(n*e*e)); sd=c/wpe
    f=lambda x: f'{x:.3g}'
    print(f"{name:28s} {n:9.2g} {Te:6.3g} {B:8.2g} {f(fpe)+' Hz':>10s} {f(fce)+' Hz':>10s} {f(fci)+' Hz':>10s} {f(fLH)+' Hz':>10s} {vA:9.3g} {lD:9.3g} {sd:9.3g}")
    rows.append((name,fpe,fce,fci))
print('check: f_pe = 8.98 kHz*sqrt(n_e/cm^-3):', f"{8980*np.sqrt(1e16/1e6):.3g} Hz for 1e10 cm^-3")
# (2) resonance absorption: Lorentzian with Q set by collisions; test plasma = lab glow discharge ECR at 0.0875 T (2.45 GHz)
B=0.0875; f0=e*B/(2*np.pi*me); Q=50; P_in=1000.0  # W incident
f=np.linspace(0.3*f0,2.2*f0,4000)
def absorbed_fraction(fd):  # matched-at-resonance load: |Gamma|^2 from a series RLC vs a matched source
    x=Q*(fd/f0-f0/fd); Z=1+1j*x; G=(Z-1)/(Z+1); return 1-np.abs(G)**2
A=absorbed_fraction(f)
for lab,fd in (('tuned f0',f0),('phi*f0',phi*f0),('f0/phi',f0/phi),('1% detuned',1.01*f0)):
    a=absorbed_fraction(fd); print(f'drive {lab:10s} {fd/1e9:6.3f} GHz: absorbed {a*P_in:8.2f} W, reflected {(1-a)*P_in:8.2f} W of {P_in:.0f} W (ledger: {a*P_in+(1-a)*P_in:.2f})')
print(f'ECR at B={B} T: f_ce = {f0/1e9:.3f} GHz (2.45 GHz magnetron); Q={Q}; half-power bandwidth {f0/Q/1e6:.0f} MHz')
fig,ax=plt.subplots(1,2,figsize=(13,4.8))
ax[0].plot(f/1e9,A*P_in,'b'); [ax[0].axvline(x/1e9,ls=':',c=cc,label=l) for x,cc,l in ((f0,'g','tuned f_ce'),(phi*f0,'r','phi*f_ce'),(f0/phi,'m','f_ce/phi'))]
ax[0].set(xlabel='drive frequency (GHz)',ylabel='absorbed power (W of 1000 W)',title='ECR-like resonance (Q=50): tuned vs phi-multiple drive'); ax[0].legend()
names=[r[0].split(' (')[0] for r in rows]; xs=np.arange(len(rows))
for k,(lab,col) in enumerate((('f_pe','b'),('f_ce','g'),('f_ci','r'))): ax[1].bar(xs+0.27*(k-1),[r[k+1] for r in rows],0.27,label=lab,color=col)
ax[1].set(yscale='log',xticks=xs,ylabel='Hz'); ax[1].set_xticklabels(names,rotation=15,fontsize=8); ax[1].set_title('characteristic frequencies: tune to the medium'); ax[1].legend()
fig.suptitle('Phi for nature, tuning for engineering: TEXTBOOK ILLUSTRATION'); fig.tight_layout(); fig.savefig('/workspace/plasma_tuning_plot.png',dpi=120)

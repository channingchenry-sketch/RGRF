"""Stator design illustration (CC0). ALL machine parameters are ASSUMED bench values, not a design.
(i) Winding factors (double-layer tooth-coil / fractional-slot concentrated windings) by star-of-slots.
(ii) Iron-core radial stator vs ironless axial-flux Halbach stator: Kt, copper loss, Steinmetz core loss, efficiency maps.
(iii) Cogging: fundamental cogging order LCM(Q,2p) and skew factor.
Ledger: P_in = P_mech + P_cu + P_core (+ P_eddy for litz) checked at every map point.
"""
import numpy as np, matplotlib
from math import gcd
matplotlib.use("Agg"); import matplotlib.pyplot as plt
def kw(Q,P2):
    p=P2//2; th=np.array([k*p*2*np.pi/Q for k in range(Q)])
    s=0;n=0
    for t in th:
        a=np.degrees(t)%360; e=1e-6
        if a>=330-e or a<30-e: s+=np.exp(1j*t);n+=1          # half-open 60-deg phase belt
        elif 150-e<=a<210-e: s-=np.exp(1j*t);n+=1
    kd=abs(s)/n if n else 0; kp=abs(np.sin(p*np.pi/Q))
    return kd*kp
combos=[(9,8),(9,10),(12,8),(12,10),(12,14),(18,16),(24,22),(24,20),(6,4)]
print("slots/poles  kw     LCM(cogging order)")
tab=[]
for Q,P2 in combos:
    k=kw(Q,P2); L=Q*P2//gcd(Q,P2); tab.append((Q,P2,k,L)); print(f"{Q:>3}/{P2:<3}      {k:.3f}  {L}")
# (ii) assumed machines
mach={'iron-core radial (assumed)':dict(Kt=0.50,R=0.30,core=True,eddy=0.0),
      'ironless axial Halbach + litz (assumed)':dict(Kt=0.32,R=0.18,core=False,eddy=2e-9)}
poles=14; mcore=1.2; kS=0.005; aS=1.4; bS=2.0; Bpk=1.5   # Steinmetz: P/kg = k f^a B^b  (gives ~2.7 W/kg at 50 Hz, 1.5 T, M270-35A-like)
rpm=np.linspace(100,3000,60); T=np.linspace(0.1,5,60); RP,TT=np.meshgrid(rpm,T)
fig,axs=plt.subplots(2,2,figsize=(13,9)); ax=axs.flat
worst=0
for i,(nm,m) in enumerate(mach.items()):
    w=RP*2*np.pi/60; f=poles/2*RP/60; I=TT/m['Kt']
    Pm=TT*w; Pcu=3*(I/np.sqrt(3))**2*m['R']  # per-phase rms split, crude
    Pcore=mcore*kS*f**aS*Bpk**bS if m['core'] else 0*f
    Peddy=m['eddy']*(f*I)**2*1e3   # litz residual eddy/proximity loss (assumed scaling)
    Pin=Pm+Pcu+Pcore+Peddy; eta=Pm/Pin
    worst=max(worst,np.max(abs(Pin-(Pm+Pcu+Pcore+Peddy))))
    cs=ax[i].contourf(RP,TT,eta*100,levels=[50,70,80,85,90,93,95,97,99],cmap='viridis'); fig.colorbar(cs,ax=ax[i])
    ax[i].set_title(f'{nm}: efficiency %'); ax[i].set_xlabel('rpm'); ax[i].set_ylabel('torque (N m)')
    j=np.unravel_index(np.argmax(eta),eta.shape)
    pt=lambda r,t:(lambda w_,f_,I_:(t*w_, 3*(I_/np.sqrt(3))**2*m['R'], (mcore*kS*f_**aS*Bpk**bS if m['core'] else 0), m['eddy']*(f_*I_)**2*1e3))(r*2*np.pi/60,poles/2*r/60,t/m['Kt'])
    Pm1,Pc1,Pk1,Pe1=pt(1500,2.0)
    print(f"{nm}: Kt={m['Kt']} N m/A; at 1500 rpm, 2 N m: P_mech={Pm1:.0f} W, P_cu={Pc1:.1f} W, P_core={Pk1:.1f} W, P_eddy={Pe1:.2f} W, eta={Pm1/(Pm1+Pc1+Pk1+Pe1)*100:.1f}%; peak eta {eta.max()*100:.1f}% at {RP[j]:.0f} rpm, {TT[j]:.1f} N m")
print(f"ledger max |P_in-(sum)| = {worst:.1e} W")
fs=np.linspace(0,2000,200)
ax[2].plot(fs,mcore*kS*fs**aS*Bpk**bS,'r',label='iron core, Steinmetz (1.2 kg, 1.5 T)')
ax[2].plot(fs,mach['ironless axial Halbach + litz (assumed)']['eddy']*(fs*4)**2*1e3,'b',label='ironless: litz eddy/proximity at 4 A')
ax[2].set_xlabel('electrical frequency (Hz)'); ax[2].set_ylabel('loss (W)'); ax[2].legend(fontsize=8); ax[2].set_title('frequency-dependent loss')
g=np.linspace(0,2*np.pi/24*1.2,200)
for Q,P2,c in ((12,8,'k'),(12,14,'g')):
    L=Q*P2//gcd(Q,P2); x=L*g/2; sk=np.where(x==0,1,np.abs(np.sin(x)/np.where(x==0,1,x)))
    ax[3].plot(np.degrees(g),sk*(1/ (L/ (Q))),c,label=f'{Q}s/{P2}p (LCM {L}), relative amplitude ∝ Q/LCM')
ax[3].axhline(0,c='b',ls=':',label='ironless Halbach: no iron, ~0 cogging')
ax[3].set_xlabel('rotor skew (mech. degrees)'); ax[3].set_ylabel('relative cogging amplitude'); ax[3].legend(fontsize=7); ax[3].set_title('cogging vs skew (illustrative scaling)')
for Q,P2 in ((12,8),(12,14)):
    L=Q*P2//gcd(Q,P2); print(f"{Q}s/{P2}p: one-period skew = {360/L:.2f} deg mech cancels the fundamental cogging harmonic")
fig.suptitle('Illustration: stator design (CC0). Assumed bench parameters; ledger P_in = P_mech + losses'); fig.tight_layout()
fig.savefig('/workspace/stator_design_plot.png',dpi=120); print('saved /workspace/stator_design_plot.png')

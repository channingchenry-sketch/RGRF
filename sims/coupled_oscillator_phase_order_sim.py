"""Shifting phase order as coupled-oscillator phase relationships (RGRF, CC0). Textbook illustrations.
(a) Adler: dphi/dt = dw - K sin phi; locked offset phi* = arcsin(dw/K); phase slips at rate sqrt(dw^2-K^2) outside lock.
(b) Circle map theta' = theta + Omega - K/(2pi) sin(2pi theta): winding number -> Arnold tongues / devil's staircase.
(c) Kuramoto N=100, Lorentzian g(w) (gamma=0.5): Kc = 2/(pi g(0)) = 2*gamma = 1.0.
(d) 3-phase stator toy: phase order ABC vs ACB reverses the rotating field.
(e) Energy ledger, two coupled damped driven oscillators: P_drive = P_damp + dE/dt."""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
rng=np.random.default_rng(1)
fig,ax=plt.subplots(2,3,figsize=(17,9.5)); ax=ax.ravel()
K=1.0; dws=np.linspace(-1.5,1.5,301)
phis=np.where(np.abs(dws)<K,np.degrees(np.arcsin(np.clip(dws/K,-1,1))),np.nan)
ax[0].plot(dws,phis,'b'); ax[0].set(xlabel='detuning dw / K',ylabel='locked phase offset phi* (deg)',title='(a) Adler: phi* = arcsin(dw/K); lock only |dw|<K')
for dw in (0.5,0.866,0.99): print(f'Adler K=1: dw={dw}: phi* = {np.degrees(np.arcsin(dw)):.1f} deg')
# phase slips at dw=1.2
dt=1e-3; t=np.arange(0,40,dt); phi=np.zeros_like(t); dw=1.2
for i in range(1,len(t)): phi[i]=phi[i-1]+dt*(dw-K*np.sin(phi[i-1]))
slips=phi[-1]/(2*np.pi); Tslip=2*np.pi/np.sqrt(dw**2-K**2)
print(f'dw=1.2 (outside lock): {slips:.2f} slips in 40 s, theory period {Tslip:.2f} s -> {40/Tslip:.2f} slips')
a2=ax[0].inset_axes([0.55,0.08,0.42,0.38]); a2.plot(t,np.mod(phi,2*np.pi),'r',lw=0.6); a2.set_title('dw=1.2: phase slips',fontsize=7); a2.tick_params(labelsize=6)
# (b) Arnold tongues
Om=np.linspace(0,1,300); Ks=np.linspace(0,1,120); W=np.zeros((len(Ks),len(Om)))
for i,k in enumerate(Ks):
    th=np.zeros_like(Om)
    for _ in range(200): th=th+Om-k/(2*np.pi)*np.sin(2*np.pi*th)
    th0=th.copy()
    for _ in range(400): th=th+Om-k/(2*np.pi)*np.sin(2*np.pi*th)
    W[i]=(th-th0)/400
ax[1].imshow(W,origin='lower',aspect='auto',extent=[0,1,0,1],cmap='twilight'); ax[1].set(xlabel='Omega (bare frequency ratio)',ylabel='K (coupling)',title='(b) circle map winding number: Arnold tongues')
w1=W[-1]; plateau=np.mean(np.abs(np.diff(w1))<1e-4)
print(f'circle map at K=1 (critical): fraction of Omega on locked plateaus ~ {plateau:.2f} (devil\'s staircase; theory -> 1, measure-zero gaps)')
w_half=np.mean(np.abs(w1-0.5)<1e-3)*1.0; print(f'width of 1:2 tongue at K=1: {w_half:.3f} in Omega; 0:1/1:1 tongues width {np.mean(np.abs(w1)<1e-3):.3f}')
ax[2].plot(Om,w1,'k'); ax[2].set(xlabel='Omega',ylabel='winding number',title="(b) K=1: devil's staircase")
# (c) Kuramoto
N=100; gam=0.5; w=gam*np.tan(np.pi*(rng.random(N)-0.5)); w=np.clip(w,-20,20)
Kc=2*gam; Kv=np.linspace(0,3,31); R=[]
for Kk in Kv:
    th=rng.random(N)*2*np.pi; h=0.01
    rs=[]
    for s in range(6000):
        z=np.mean(np.exp(1j*th)); th=th+h*(w+Kk*np.abs(z)*np.sin(np.angle(z)-th))
        if s>3000: rs.append(np.abs(z))
    R.append(np.mean(rs))
R=np.array(R); theo=np.where(Kv>Kc,np.sqrt(np.clip(1-Kc/np.maximum(Kv,1e-9),0,1)),0)
ax[3].plot(Kv,R,'bo',ms=4,label='N=100 sim'); ax[3].plot(Kv,theo,'r',label='r = sqrt(1-Kc/K) (N->inf)'); ax[3].axvline(Kc,ls=':',c='k'); ax[3].set(xlabel='K',ylabel='order parameter r',title=f'(c) Kuramoto, Lorentzian g(w): Kc = {Kc:.1f}'); ax[3].legend()
for Kk in (0.5,1.0,1.5,2.0,3.0): print(f'Kuramoto K={Kk}: r_sim={R[np.argmin(abs(Kv-Kk))]:.2f}, r_theory={np.sqrt(max(0,1-Kc/Kk)):.2f}')
# (d) 3-phase rotating field
tt=np.linspace(0,1,9)  # one electrical period
def field(order):
    off={'ABC':(0,-120,-240),'ACB':(0,-240,-120)}[order]; ang=np.radians([0,120,240])
    B=[sum(np.cos(2*np.pi*x+np.radians(o))*np.exp(1j*a) for o,a in zip(off,ang)) for x in tt]; return np.array(B)
for order,col in (('ABC','g'),('ACB','m')):
    B=field(order); ax[4].plot(B.real,B.imag,col+'o-',label=order)
    rot=np.sign(np.mean(np.diff(np.unwrap(np.angle(B)))))
    print(f'3-phase {order}: |B| = {np.abs(B).mean():.2f} (const 1.5), rotation {"CCW" if rot>0 else "CW"}')
ax[4].set(aspect='equal',title='(d) stator: swap two phases -> field reverses'); ax[4].legend()
# (e) energy ledger: two coupled damped oscillators, oscillator 1 driven
m=1.0; k0=1.0; kc=0.1; gdamp=0.05; F0=0.1; wd=1.0
x=np.zeros(2); v=np.zeros(2); h=1e-3; T=400; n=int(T/h)
Ein=0; Ed=0; E=lambda x,v: 0.5*m*(v**2).sum()+0.5*k0*(x**2).sum()+0.5*kc*(x[0]-x[1])**2
E0=E(x,v); hist=[]
for i in range(n):
    tm=i*h; F=np.array([F0*np.cos(wd*tm),0])
    a=(-k0*x-kc*(x-x[::-1])-gdamp*v+F)/m
    v_new=v+h*a; x_new=x+h*v_new
    vm=0.5*(v+v_new); Ein+=F[0]*vm[0]*h; Ed+=gdamp*(vm**2).sum()*h
    x,v=x_new,v_new
    if i%2000==0: hist.append((tm,x[0],x[1]))
Ef=E(x,v); err=Ein-Ed-(Ef-E0)
print(f'ledger: drive in {Ein:.4f}, dissipated {Ed:.4f}, stored change {Ef-E0:.4f}, residual {err:.2e} ({abs(err)/Ein*100:.3f} % of input, integrator error) -> no over-unity')
h_=np.array(hist); ax[5].plot(h_[:,0],h_[:,1],'b',label='x1 (driven)'); ax[5].plot(h_[:,0],h_[:,2],'r',label='x2 (coupled)'); ax[5].set(xlabel='t',title=f'(e) ledger: in {Ein:.3f} = loss {Ed:.3f} + stored {Ef-E0:.3f}'); ax[5].legend()
wn=(np.sqrt(k0/m),np.sqrt((k0+2*kc)/m)); print(f'normal modes: in-phase {wn[0]:.3f}, anti-phase {wn[1]:.3f} rad/s; beat (energy swap) period {2*np.pi/(wn[1]-wn[0]):.1f} s')
# phased array
for Nn in (1,10,100): print(f'phased array N={Nn}: coherent peak intensity ~N^2 = {Nn**2}, incoherent ~N = {Nn} (total power still N; coherence redistributes it in angle)')
fig.suptitle('Shifting phase order = phase relationships of coupled oscillators: TEXTBOOK ILLUSTRATIONS'); fig.tight_layout(); fig.savefig('/workspace/coupled_oscillator_plot.png',dpi=110)

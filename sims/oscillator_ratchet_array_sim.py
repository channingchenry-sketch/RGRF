"""Oscillator ratchet arrays. ILLUSTRATION (CC0).
(i) Rocking ratchet: overdamped particle, asymmetric sawtooth U(x), zero-mean AC drive F(t)=A cos(wt), with noise.
    Ledger: work in by drive = dissipated (gamma v^2 integrated, minus noise injection) + Delta U. Drive off -> zero drift.
(ii) Chain of N phase oscillators, each driven by its neighbour (Kuramoto nearest-neighbour), locking vs K; coherent sum ~N.
(iii) GEM: Omega of N coherent 10 kg rotors vs GP-B-detectable (~7 mas/yr) and Earth (39 mas/yr) levels, incl. packing limit.
"""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
rng=np.random.default_rng(1)
fig,ax=plt.subplots(1,3,figsize=(16,4.6))
# (i) rocking ratchet, dimensionless: gamma=1, period L=1, barrier V0=1, asymmetry a=0.8 (rise over 0.8, fall over 0.2)
L=1.0;V0=1.0;a=0.8;D=0.05;w=0.1;dt=5e-3;T=600
def F_U(x):
    y=x%L
    return np.where(y<a*L,-V0/(a*L),V0/((1-a)*L))
def U(x):
    y=x%L
    return np.where(y<a*L,V0*y/(a*L),V0*(L-y)/((1-a)*L))
amps=np.linspace(0,3,11); drifts=[]
n=int(T/dt); Np=100
for A in amps:
    x=np.zeros(Np); Win=np.zeros(Np); Wdiss=np.zeros(Np); x0=x.copy()
    for i in range(n):
        Fd=A*np.cos(w*i*dt)
        noise=np.sqrt(2*D*dt)*rng.standard_normal(Np)
        dx=(F_U(x)+Fd)*dt+noise
        xn=x+dx
        Win+=Fd*dx                       # drive work (Stratonovich: Fd at midpoint ~ same, smooth in t)
        Wdiss+=(U(x)-U(xn))+Fd*dx        # heat to bath, Sekimoto: -dU + dW (exact along path)
        x=xn
    v=np.mean(x-x0)/T; drifts.append(v)
    dU=np.mean(U(x)-U(x0))
    if A in (0,amps[6]): print(f"A={A:.2f}: drift v={v:.4f} L/time; <W_in>={Win.mean():.2f}, <Q_bath>={Wdiss.mean():.2f}, dU={dU:.3f}, ledger W_in-(Q+dU)={(Win.mean()-(Wdiss.mean()+dU)):.2e}")
ax[0].plot(amps,drifts,'o-'); ax[0].axhline(0,c='gray'); ax[0].set_xlabel('AC drive amplitude A (V0/L units)'); ax[0].set_ylabel('net drift (L per unit time)')
ax[0].set_title('rocking ratchet: zero-mean AC → directed drift'); print(f"max drift {max(drifts):.4f} at A={amps[int(np.argmax(drifts))]:.2f}")
# (ii) chain
N=20; om=1+0.1*rng.standard_normal(N); Ks=np.linspace(0,1,21); R=[]
for K in Ks:
    th=rng.uniform(0,2*np.pi,N); h=0.02
    for s in range(5000):
        c=np.zeros(N); c[1:]+=np.sin(th[:-1]-th[1:]); c[:-1]+=np.sin(th[1:]-th[:-1])
        th+=h*(om+K*c)
    vel=om+K*c; locked=np.std(vel)<1e-3
    R.append(abs(np.mean(np.exp(1j*th))))
ax[1].plot(Ks,R,'s-'); ax[1].set_xlabel('nearest-neighbour coupling K'); ax[1].set_ylabel('order parameter r (|sum|/N)')
ax[1].set_title(f'chain of {N} oscillators, each driving the next\ncoherent field ∝ rN, power ∝ (rN)²')
print("chain r vs K:", ", ".join(f"{k:.1f}:{r:.2f}" for k,r in zip(Ks[::4],R[::4])))
# (iii) GEM
G=6.674e-11;c_=2.998e8;yr=3.156e7;mas=np.pi/180/3600e3
J1=0.5*10*0.15**2*(10000*2*np.pi/60); Om1=2*G*J1/(c_**2*0.2**3)
Ndet=7*mas/yr/Om1; Nearth=39*mas/yr/Om1
rho=7850; vt=0.15*10000*2*np.pi/60
Om_pack=(8*np.pi/3)*G*rho*0.5*0.15*vt/c_**2  # dense sphere of such rotors, field at centre ~ independent of size
print(f"single rotor Omega={Om1:.2e} rad/s; naive N for GP-B-detectable 7 mas/yr: {Ndet:.1e} (mass {Ndet*10:.1e} kg); for Earth 39 mas/yr: {Nearth:.1e} (mass {Nearth*10:.1e} kg; Earth 5.97e24 kg)")
print(f"packing limit: a solid steel ball of such rotors gives Omega≈{Om_pack:.1e} rad/s at its centre, INDEPENDENT of size -> never reaches {7*mas/yr:.1e}; need rho*r*v_tip ~{7*mas/yr/Om_pack:.0e}x larger")
Ns=np.logspace(0,16,100)
ax[2].loglog(Ns,Om1*Ns,label='naive coherent sum N·Ω₁ (all at 0.2 m: impossible)')
ax[2].axhline(Om_pack,c='k',ls='--',label='packing limit (dense steel ball)')
ax[2].axhline(7*mas/yr,c='r',label='GP-B-level sensitivity ~7 mas/yr'); ax[2].axhline(39*mas/yr,c='g',label='Earth at GP-B orbit')
ax[2].set_xlabel('number of 10 kg rotors N'); ax[2].set_ylabel('Ω (rad/s)'); ax[2].legend(fontsize=7); ax[2].set_title('GEM array: linear gain, geometry-capped')
fig.suptitle('Illustration: oscillator ratchet arrays (CC0). Ratchets rectify drive energy; they never exceed it'); fig.tight_layout()
fig.savefig('/workspace/oscillator_ratchet_array_plot.png',dpi=120); print('saved /workspace/oscillator_ratchet_array_plot.png')

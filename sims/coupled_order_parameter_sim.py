"""Coupled Landau order parameters (RGRF, CC0). TOY MODEL / textbook illustration with VO2-like numbers.
F(eta,u;T) = a(T-T0)(eta^2+u^2) + b(eta^4+u^4) - g eta^2 u^2 + c(eta^6+u^6)
eta = electronic (Mott/gap) order, u = structural V-V dimerisation; ordered (insulating, M1-like) at low T.
On the symmetric path eta=u=x, y=x^2: F = A y + B y^2 + C y^3 with A=2a(T-T0), B=2b-g, C=2c.
 B>0 (weak g): second order at T0, no hysteresis.  B<0 (strong g): first order; ordered phase survives
 heating to T_sh = T0 + B^2/(6aC); disordered phase survives cooling to T0; equilibrium Tc = T0 + B^2/(8aC).
(1) g sweep with hysteresis; (2) toy pump: electronic order melts before the lattice; (3) energy ledger."""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
a,b,c,T0=1.0,1.0,0.5,62.0; C=2*c; K=273.15
def yeq(T,B):   # ordered local minimum y>0, or None
    A=2*a*(T-T0); disc=B*B-3*A*C
    if disc<0: return None
    y=(-B+np.sqrt(disc))/(3*C); return y if y>0 else None
def Fy(y,T,B): return 2*a*(T-T0)*y+B*y*y+C*y**3
def S(y): return -2*a*y          # S = -dF/dT (per unit volume, model units)
def sweep(B,Ts,ordered):
    ys=[]
    for T in Ts:
        if ordered:
            y=yeq(T,B)
            if y is None: ordered=False; y=0.0
        else:
            y=0.0
            if 2*a*(T-T0)<0: ordered=True; y=yeq(T,B) or 0.0   # disordered state goes unstable at T0
        ys.append(y)
    return np.array(ys)
Tup=np.linspace(50,75,2501); Tdn=Tup[::-1]
fig,AX=plt.subplots(2,3,figsize=(16,9)); ax=AX[0]
for g,col in ((1.0,'k'),(2.0,'b'),(5.0,'g'),(8.0,'r')):
    B=2*b-g; up=sweep(B,Tup,True); dn=sweep(B,Tdn,False)
    th=Tup[np.argmax(up==0)]; tc=Tdn[np.argmax(dn>0)]
    kind='2nd order' if B>=0 else '1st order'
    print(f'g={g}: B={B:+.1f} ({kind}); heating loses order at {th:.2f} C, cooling regains at {tc:.2f} C, hysteresis {th-tc:.2f} K' + (f'; equilibrium Tc {T0+B*B/(8*a*C):.2f} C' if B<0 else ''))
    ax[0].plot(Tup,np.sqrt(up),col+'-',label=f'g={g} ({kind})'); ax[0].plot(Tdn,np.sqrt(dn),col+'--')
ax[0].set(xlabel='T (C)',ylabel='order |eta| = |u|',title='(1) coupling g: 2nd -> 1st order; dashed = cooling'); ax[0].legend(fontsize=8)
# (3) ledger for g=8 (VO2-like 68 C up / 62 C down): integrate dQ = T dS on the smooth parts, dQ = dU at jumps
g=8.0; B=2*b-g
def ledger(Ts,ys):
    Q=0.0; Sprod=0.0
    for i in range(len(Ts)-1):
        T1,T2=Ts[i]+K,Ts[i+1]+K; y1,y2=ys[i],ys[i+1]
        if abs(y2-y1)>0.5:   # jump at T2: irreversible; heat = dU = dF + T dS ; entropy produced = -dF/T
            dF=Fy(y2,Ts[i+1],B)-Fy(y1,Ts[i+1],B); dS=S(y2)-S(y1); Q+=dF+T2*dS; Sprod+=-dF/T2
        else: Q+=0.5*(T1+T2)*(S(y2)-S(y1))
    return Q,Sprod
up=sweep(B,Tup,True); dn=sweep(B,Tdn,False)
Qh,Sh=ledger(Tup,up); Qc,Sc=ledger(Tdn,dn)
U=lambda y,T: Fy(y,T,B)+(T+K)*S(y)
print(f'ledger g=8: heat in on heating leg {Qh:.2f}, heat out on cooling leg {-Qc:.2f}; net {Qh+Qc:+.3f} (= U_end - U_start = {U(dn[-1],Tdn[-1])-U(up[0],Tup[0]):+.3f}) -> first law closes, no work extracted')
print(f'entropy produced per cycle {Sh+Sc:.4f} (>0, irreversible); hysteresis loss T*S_prod ~ {(Sh+Sc)*(65+K):.2f} model units of heat moved, never created')
Lg=51.0; print(f'VO2 scale [to verify L ~ 51 J/g]: a 62/68 C loop is bounded by Carnot 1-(335.15/341.15) = {(1-335.15/341.15)*100:.2f} % -> < {Lg*(1-335.15/341.15):.2f} J/g per cycle even as an ideal engine')
ax[1].plot(Tup,np.sqrt(up),'r',label='heating'); ax[1].plot(Tdn,np.sqrt(dn),'b',label='cooling'); ax[1].set(xlabel='T (C)',ylabel='order',title='(1) g=8: VO2-like loop 68 C up / 62 C down'); ax[1].legend()
# (2) toy pump: electrons hot instantly (decay 1.5 ps); lattice warms via e-ph coupling over ~1 ps; eta relaxes fast, u slow
t=np.arange(0,5000,0.5)  # fs
Te=lambda tt: 50+80*np.exp(-tt/1500)
Tl=lambda tt: 50+25*(1-np.exp(-tt/1000))
Ge,Gu=1/50.,1/600.   # relaxation rates (1/fs), toy
e=u=np.sqrt(yeq(50,B)); E=[];Uu=[]
for tt in t:
    ge=2*a*(Te(tt)-T0)*e+4*b*e**3-2*g*e*u*u+6*c*e**5
    gu=2*a*(Tl(tt)-T0)*u+4*b*u**3-2*g*e*e*u+6*c*u**5
    e-=0.5*Ge*ge*0.05; u-=0.5*Gu*gu*0.05; e=max(e,1e-6); u=max(u,1e-6); E.append(e); Uu.append(u)
E,Uu=np.array(E),np.array(Uu); e0=E[0]
te=t[np.argmax(E<0.5*e0)]; tu=t[np.argmax(Uu<0.5*e0)] if np.any(Uu<0.5*e0) else float('nan')
print(f'toy pump: electronic order halves at {te:.0f} fs, lattice dimerisation at {tu:.0f} fs (ordering, not exact times, is the point)')
ax[2].plot(t/1000,E/e0,'m',label='eta (electronic)'); ax[2].plot(t/1000,Uu/e0,'c',label='u (lattice)'); ax[2].set(xlabel='time (ps)',ylabel='normalised order',title='(2) toy pump: electronic order melts first'); ax[2].legend()
# (4) Fe3+ spin-only Brillouin S=5/2 (g=2, L=0): M/Msat vs B at several T; Msat = gS muB = 5 muB; mu_eff = g sqrt(S(S+1)) = 5.92 muB
muB,kB=9.274e-24,1.380649e-23
def BJ(J,x): return (2*J+1)/(2*J)/np.tanh((2*J+1)*x/(2*J))-1/(2*J)/np.tanh(x/(2*J))
Bf=np.linspace(1e-3,10,400)
for Tk,col in ((2,'b'),(4.2,'g'),(10,'r'),(300,'k')):
    x=2*2.5*muB*Bf/(kB*Tk); AX[1,0].plot(Bf,BJ(2.5,x),col,label=f'{Tk} K')
x1=2*2.5*muB*1/(kB*300); print(f'Fe3+ S=5/2: Msat 5 muB, mu_eff {2*np.sqrt(2.5*3.5):.2f} muB; at 1 T/300 K M/Msat = {BJ(2.5,x1):.4f}; at 2 K, 1 T: {BJ(2.5,2*2.5*muB/(kB*2)):.3f}')
AX[1,0].set(xlabel='B (T)',ylabel='M / Msat',title='(4) Fe3+ spin-only Brillouin, S=5/2'); AX[1,0].legend(fontsize=8)
# (5) Verwey-like resistivity: Fe3O4 jumps ~2 orders at Tv ~ 123 K on cooling (illustrative activated model)
Tv=np.linspace(60,200,700); Tvw=123.0
rho_hi=1e-2*np.exp(800*(1/Tv-1/Tvw)); rho_lo=4e-5*np.exp(150*(1/Tv-1/200))
w=1/(1+np.exp(-(Tv-Tvw)/1.0)); rho=10**((1-w)*np.log10(rho_hi)+w*np.log10(rho_lo))
AX[1,1].semilogy(Tv,rho,'brown'); AX[1,1].axvline(Tvw,ls=':',c='k'); AX[1,1].set(xlabel='T (K)',ylabel='rho (ohm m, illustrative)',title='(5) magnetite Verwey transition ~123 K (toy)')
print(f'Verwey toy: rho jump across Tv: {rho[np.argmin(abs(Tv-118))]/rho[np.argmin(abs(Tv-128))]:.0f}x (real Fe3O4 ~ 100x) [to verify]')
# (6) Curie point as a magnetic phase shift: mean-field M(T) for magnetite Tc ~ 858 K
Tm=np.linspace(1,900,900); m=np.ones_like(Tm)
for _ in range(200): m=np.tanh(np.where(Tm<858,m*858/Tm,0)); 
AX[1,2].plot(Tm,m,'k'); AX[1,2].axvline(858,ls=':',c='r'); AX[1,2].axvline(583,ls=':',c='gray'); AX[1,2].set(xlabel='T (K)',ylabel='M/M0 (mean field)',title='(6) Curie point: Fe3O4 858 K; NdFeB ~583 K (grey)')
fig.suptitle('Coupled order parameters: TOY MODEL / textbook illustration (VO2-like numbers, not data)'); fig.tight_layout(); fig.savefig('/workspace/dof_phases_plot.png',dpi=120)

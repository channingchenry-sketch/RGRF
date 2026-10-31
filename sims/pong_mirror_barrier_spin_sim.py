"""H722 'pong' reconstruction sim (2026-10-31). numpy only, deterministic.
Part A: guiding-centre particle on a field line in a frame rotating at Omega.
  Along-line coordinate z; mirror field B(z)=B0(1+(z/L)^2); mu = v_perp0^2/(2 B0) conserved (m=q=1).
  Electrostatic barrier q*Phi(z)=Phi0*exp(-(z-zb)^2/w^2) ... centred at the ends (|z|=zb).
  Centrifugal potential -1/2 Omega^2 rho(z)^2 with rho^2 = r0^2 + z^2 (line tilted away from axis).
  Jacobi constant J = 1/2 v_par^2 + mu B + Phi - 1/2 Omega^2 rho^2 is conserved (ledger).
Part B: 1D double well H = p^2/2 + lam (x^2-a^2)^2 (hbar=m=1); state oscillates between wells at
  the tunnel-splitting frequency (quantum 'pong'); norm and <H> conserved."""
import numpy as np
B0,L,zmax,r0=1.0,1.0,2.0,1.0
Rm=1+(zmax/L)**2
def U(z,mu,Om,Phi0):
    return mu*B0*(1+(z/L)**2)+Phi0*(np.exp(-((z-zmax*0.9)/0.15)**2)+np.exp(-((z+zmax*0.9)/0.15)**2))-0.5*Om**2*(r0**2+z**2)
def F(z,mu,Om,Phi0,h=1e-6): return -(U(z+h,mu,Om,Phi0)-U(z-h,mu,Om,Phi0))/(2*h)
def run(alpha,Om=0.0,Phi0=0.0,v=1.0,dt=2e-3,T=60.0):
    mu=(v*np.sin(alpha))**2/(2*B0); z=0.0; vz=v*np.cos(alpha)
    J0=0.5*vz**2+U(z,mu,Om,Phi0); Jmax=0; t=0; cross=[]; a=F(z,mu,Om,Phi0)
    while t<T:
        vz+=0.5*dt*a; z+=dt*vz; a=F(z,mu,Om,Phi0); vz+=0.5*dt*a; t+=dt
        Jmax=max(Jmax,abs(0.5*vz**2+U(z,mu,Om,Phi0)-J0))
        if abs(z)>zmax: return True,None,Jmax
        if len(cross)==0 or (t-cross[-1]>0.05 and np.sign(z)!=np.sign(z-dt*vz)): 
            if np.sign(z)!=np.sign(z-dt*vz): cross.append(t)
    per=2*np.mean(np.diff(cross)) if len(cross)>2 else None
    return False,per,Jmax
out=[]
p=lambda s: (print(s),out.append(s))
p("== Part A: mirror + barrier + rotation (m=q=v=1, B0=L=1, mirror ratio Rm=%.1f) =="%Rm)
p("Loss cone (no Phi, no Omega): sin^2(a_lc)=1/Rm -> a_lc=%.2f deg"%np.degrees(np.arcsin(np.sqrt(1/Rm))))
al=np.radians(60); e,per,J=run(al)
w=np.sqrt(2*(np.sin(al)**2/2)*B0/L**2); p("Bounce period, alpha=60deg: sim %.4f, analytic 2pi/sqrt(2 mu B0/L^2)=%.4f, |dJ|max=%.1e"%(per,2*np.pi/w,J))
e,per,J=run(al,Om=0.3); p("Bounce period with Omega=0.3: sim %.4f, analytic 2pi/sqrt(2muB0/L^2-Om^2)=%.4f, |dJ|max=%.1e"%(per,2*np.pi/np.sqrt(w**2-0.09),J))
alphas=np.radians(np.linspace(1,89,89))
for Om,Phi0,lab in [(0,0,'mirror only'),(0,0.3,'mirror + barrier Phi0=0.3'),(0.3,0,'mirror + rotation Om=0.3'),(0.3,0.3,'mirror + barrier + rotation')]:
    res=[run(a,Om,Phi0,T=40) for a in alphas]
    esc=np.array([r[0] for r in res]); Jm=max(r[2] for r in res)
    # isotropic weighting: fraction of solid angle (hemisphere), weight sin(alpha)
    wgt=np.sin(alphas); f=(esc*wgt).sum()/wgt.sum()
    edge=np.degrees(alphas[esc].max()) if esc.any() else float('nan')
    p(f"{lab:30s}: escape fraction (isotropic) {f:.3f}; largest escaping pitch angle {edge:.0f} deg; max |dJ| {Jm:.1e}")
p("Analytic isotropic loss fraction (mirror only) 1-cos(a_lc)=%.3f"%(1-np.sqrt(1-1/Rm)))
p("Ledger A: J (Jacobi constant) conserved to the residuals above; rotation energy comes from the frame (pinned), no source term, no over-unity.")
p("\n== Part B: double-well tunnelling (hbar=m=1, lam=1, a=1.5) ==")
N=1200; x=np.linspace(-4,4,N); dx=x[1]-x[0]; lam,a=1.0,1.5
V=lam*(x**2-a**2)**2
H=np.diag(V+1/dx**2)+np.diag(-0.5/dx**2*np.ones(N-1),1)+np.diag(-0.5/dx**2*np.ones(N-1),-1)
E,phi=np.linalg.eigh(H); phi/=np.sqrt(dx); dE=E[1]-E[0]; Tt=2*np.pi/dE
p("E0=%.6f E1=%.6f barrier V(0)=%.3f splitting dE=%.3e -> tunnelling ('pong') period T=2pi/dE=%.2f"%(E[0],E[1],lam*a**4,dE,Tt))
psi0=(phi[:,0]+phi[:,1])/np.sqrt(2)
if (psi0[x<0]**2).sum()<(psi0[x>0]**2).sum(): psi0=(phi[:,0]-phi[:,1])/np.sqrt(2)
c=phi.T@psi0*dx
ts=np.linspace(0,Tt,9); nerr=0; herr=0; E_ex=(np.abs(c)**2*E).sum()
for t in ts:
    psi=phi@(c*np.exp(-1j*E*t)); n=(abs(psi)**2).sum()*dx
    Hp=H@psi*1.0; eH=np.real(np.vdot(psi,Hp))*dx
    nerr=max(nerr,abs(n-1)); herr=max(herr,abs(eH-E_ex))
    p("t/T=%.3f  P(left well)=%.4f  norm=%.12f"%(t/Tt,(abs(psi[x<0])**2).sum()*dx,n))
p("Ledger B: max |norm-1|=%.1e, max |<H>(t)-<H>(0)|=%.1e; R+T style probability balance holds; no energy gained."%(nerr,herr))
open('sims/pong_mirror_barrier_spin_sim_output.txt','w').write('\n'.join(out)+'\n')

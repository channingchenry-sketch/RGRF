"""Checks for Grok share #99 (c0b832a5) 'Electrostatic Tensor and Nodal Spin Dynamics'. CC0. numpy only."""
import numpy as np
e0=8.8541878128e-12; mu0=4e-7*np.pi; c=299792458.0; G=6.674e-11; kB=1.380649e-23
print("1. Electrostatic Maxwell stress T=e0(EE-1/2 d E^2)")
E=np.array([0,0,1e6]); T=e0*(np.outer(E,E)-0.5*np.eye(3)*(E@E)); u=0.5*e0*E@E
ev=np.linalg.eigvalsh(T); print("  eig/u =",np.round(ev/u,6)," trace/u =",round(np.trace(T)/u,6))
iso=np.trace(T)/3; print("  true isotropic part (tr/3)/u =",round(iso/u,6),"-> -u/3 (trace = -u), NOT -u; the -1/2 e0E^2 d term is not the isotropic projection")
dev=T-iso*np.eye(3); print("  deviatoric eig/u =",np.round(np.linalg.eigvalsh(dev)/u,6))
print("2. When is T_ij purely isotropic? average EE over random directions:")
rng=np.random.default_rng(0); n=rng.normal(size=(200000,3)); n/=np.linalg.norm(n,axis=1)[:,None]
Tavg=e0*1e12*(np.einsum('ni,nj->ij',n,n)/len(n)-0.5*np.eye(3)); print("  <T>/u diag =",np.round(np.diag(Tavg)/u,3),"(-1/3: isotropic only for direction-averaged/random fields)")
print("  full EM plane wave E_|_B, |E|=c|B|: T = -u k^k (pure pressure along k, zero transverse):")
Ev=np.array([1e3,0,0]); Bv=np.array([0,1e3/c,0])
TE=e0*(np.outer(Ev,Ev)-0.5*np.eye(3)*(Ev@Ev))+(np.outer(Bv,Bv)-0.5*np.eye(3)*(Bv@Bv))/mu0
uu=0.5*e0*Ev@Ev+0.5*Bv@Bv/mu0; print("  diag/u =",np.round(np.diag(TE)/uu,6))
print("3. Standing wave nodes: E=E0 sin kx cos wt, B=(E0/c) cos kx sin wt")
x=np.linspace(0,1,9); k=2*np.pi
print("  E nodes at x/lambda=0,0.5; B nodes at 0.25,0.75 (quarter-wave offset). time-avg u(x)/(e0 E0^2/4):",np.round(np.sin(k*x)**2+np.cos(k*x)**2,3))
print("  -> time-averaged total u is uniform; nodes are E- or B-nodes, energy sloshes between them")
print("4. Nodal 'time dilation' scale dtau/tau ~ G/c^4 * int u/r dV (Grok-reported form, order-of-magnitude)")
for Ef,B,R,lab in [(1e6,1.0,1.0,"lab 1 MV/m + 1 T, R=1 m"),(1e-6,1e-9,1.5e11,"heliosphere-ish 1 uV/m,1 nT,R=1 AU")]:
    uu=0.5*e0*Ef**2+B**2/(2*mu0); val=G/c**4*uu*2*np.pi*R**2
    print(f"  {lab}: u={uu:.3g} J/m3 -> dtau/tau ~ {val:.2e}")
print("5. Plasma beta 2mu0 p/B^2 examples")
for n_,T_,B,lab in [(1e23,6000,0.15,"photosphere-ish n=1e23 m^-3,6000K,0.15T"),(5e6,1e5,1e-8,"1 AU wind n=5/cc,1e5K,10nT")]:
    p=2*n_*kB*T_; print(f"  {lab}: beta={2*mu0*p/B**2:.2f}")
print("6. Umbra deficit: photosphere 5772 K vs umbra 3900-4700 K (textbook range) ->",5772-4700,"to",5772-3900,"K; Grok's 1000-1900 K is consistent")
print("7. Io wing power Grok-reported 5e11-1.5e12 W; Voyager-era ~2e12 W: not rerun (needs conductance model) [to verify]")
print("8. Angular momentum: friction-coupled counter-rotating rotors conserve total L (share #97)")
I1,I2,w1,w2,kf,dt=1.0,2.0,3.0,-1.0,0.5,1e-3; L0=I1*w1+I2*w2
for _ in range(20000):
    tq=kf*(w2-w1); w1+=tq/I1*dt; w2-=tq/I2*dt
print(f"  L0={L0:.6f} L_end={I1*w1+I2*w2:.6f}; common w={w1:.4f}; KE lost to heat={0.5*(I1*3**2+I2*1)-0.5*(I1*w1**2+I2*w2**2):.4f} J")

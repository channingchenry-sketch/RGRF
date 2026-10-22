"""Share #92 checks (CC0). Reruns Grok's 1 AU pressures, ambipolar body force,
CGL invariants, Parker-spiral net magnetic force, anisotropic hoop sign,
Chapman-Ferraro standoff, ferrofluid force-density ratio."""
import numpy as np
mu0=4e-7*np.pi; kB=1.380649e-23; e=1.602177e-19; mp=1.67262e-27; eV=e
print("== 1. 1 AU pressures (n=5 cm^-3, v=400 km/s, B=5 nT, T=10 eV) ==")
n=5e6; v=4e5; B=5e-9
for T in (10,):
    print(f"p_proton = n kT = {n*T*eV:.2e} Pa (Grok 8e-12: matches, protons only, at 1 AU)")
print(f"p_p + p_e (Te=Tp) = {2*n*10*eV:.2e} Pa")
Tk=1e5; print(f"typical Tp~1e5 K (8.6 eV): p_p = {n*kB*Tk:.2e} Pa")
pB=B**2/(2*mu0); print(f"B^2/2mu0 = {pB:.2e} Pa (Grok ~1e-11)")
print(f"rho v^2 = {n*mp*v**2:.2e} Pa (Grok 1.3e-9)")
print(f"beta_p = {n*10*eV/pB:.2f}")
print("== 2. ambipolar body force n e E ==")
for E in (1e-9,3e-9,5e-9):
    print(f"E={E*1e9:.0f} nV/m -> n e E = {n*e*E:.1e} N/m^3 (Grok: ~1e-15 Pa/m; off by ~1e6)")
print(f"our sim E(1 AU)=0.13-0.16 nV/m -> n e E = {n*e*1.5e-10:.1e} N/m^3")
print(f"compare grad p_B ~ p_B/1AU = {pB/1.496e11:.1e} N/m^3")
print("== 3. CGL double-adiabatic 0.3 -> 1 AU (radial n~r^-2, |B| Parker) ==")
def Bmag(r): # r in AU, Br~r^-2, Bphi~r^-1, equal at 1 AU
    return np.hypot(1/r**2,1/r)
r0,r1=0.3,1.0; nr=(r0/r1)**2; Br=Bmag(r1)/Bmag(r0)
# p_perp/(n B) const -> T_perp ~ B ; p_par B^2/n^3 const -> T_par ~ n^2/B^2
Tperp_ratio=Br; Tpar_ratio=nr**2/Br**2
print(f"T_perp ratio {Tperp_ratio:.3f}, T_par ratio {Tpar_ratio:.3f}, anisotropy change x{Tperp_ratio/Tpar_ratio:.3f}")
print("(Pure CGL drives T_perp/T_par far from 1; observed stays near 1: Grok's 'over-predicts' is right)")
print("== 4. Parker spiral equatorial magnetic force, r>>1 AU ==")
r=np.linspace(5,50,4001)*1.496e11; Bphi=B*1.496e11/r
pres=-np.gradient(Bphi**2/(2*mu0),r); hoop=-Bphi**2/(mu0*r)
for a,b,c in list(zip(r/1.496e11,pres,hoop))[1000:4000:1000]: print(f"r={a:5.1f} AU  -dpB/dr={b:+.2e}  hoop={c:+.2e}  net={b+c:+.1e}")
print("(net ~0: tension alone is inward, but pressure gradient cancels it for B_phi~1/r)")
print("== 5. Anisotropic hoop term on a curved boundary, tangential b, radius R ==")
print("div[(p_par-p_perp) bb] normal part = -(p_par-p_perp)/R (toward centre if p_par>p_perp)")
print("=> p_par>p_perp ADDS inward pull (tension-like, firehose side); p_perp>p_par reduces it. Grok had it reversed.")
print("== 6. Chapman-Ferraro standoff ==")
B0=3.1e-5; RE=6.371e6
for pdyn in (1.0e-9,1.34e-9,2.0e-9):
    for f,lab in ((1,'plain dipole'),(2,'f=2 (Chapman-Ferraro image)')):
        Bs=f*B0
        rs=(Bs**2/(2*mu0*pdyn))**(1/6)
        print(f"pdyn={pdyn*1e9:.2f} nPa {lab}: r = {rs:.1f} R_E")
print("(observed ~10-11 R_E; f~2.4 incl. currents, Shue et al. 1998, Bz=0: 10.22*Pd^(-1/6.6) = 9.8 R_E at 1.34 nPa)")
print("== 7. Ferrofluid ==")
rho=1350; M=28e3; f=0.5e6
print(f"0.5 N/cm^3 / (rho g) = {f/(rho*9.81):.0f} x gravity; needs grad(mu0 H) = {f/M:.1f} T/m")

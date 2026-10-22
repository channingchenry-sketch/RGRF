"""Checks for share #95 (2012804d): Black Hole as Magnetic Nucleus. CC0.
Reruns the numbers Grok stated plus order-of-magnitude BH magnetosphere checks."""
import math
h=6.62607015e-34; c=2.99792458e8; e=1.602176634e-19; G=6.674e-11; Msun=1.989e30
me=9.1093837e-31; muB=9.2740100783e-24
def eV(nm): return h*c/(nm*1e-9)/e
print("1. Photon energies")
for nm in (390,443,450,460,500,660,730):
    print(f"   {nm} nm -> {eV(nm):.3f} eV")
print("   Grok: blue ~2.7-2.8 eV -> 443-459 nm (OK)")
print("2. 'few hundred uT ~ ten times Earth's field'")
for B in (300e-6,500e-6):
    print(f"   {B*1e6:.0f} uT / 50 uT = {B/50e-6:.0f}x (Earth 25-65 uT)")
print("3. Electron Larmor (radical-pair Zeeman) frequency g*muB*B/h")
for B in (50e-6,500e-6):
    f=2.0023*muB*B/h; print(f"   B={B*1e6:.0f} uT -> {f/1e6:.2f} MHz, period {1e9/f:.0f} ns")
print("   => needs pair coherence ~>100 ns-1 us at Earth field; consistent with ns-us pair lifetimes")
print("4. Zeeman energy vs kT at 300 K, 50 uT:", f"{muB*50e-6/(1.380649e-23*300):.1e}")
print("5. Black hole scales")
for name,M,B,a in (("M87*",6.5e9,10e-4*1,0.9),("Sgr A*",4.3e6,30e-4,0.9)):
    m=M*Msun; rg=G*m/c**2; Bt=B  # B in tesla (1-30 G horizon-scale, EHT polarimetry)
    # BZ jet power ~ (kappa/4pi c) Phi^2 Omega_H^2 ; SI form P = kappa/(mu0 c) * Phi^2 * Omega^2 ... use P ~ (1/(mu0)) * kappa * Phi^2 Omega^2 / c * 4pi /4pi
    rH=rg*(1+math.sqrt(1-a*a)); Om=a*c/(2*rH); Phi=math.pi*rH**2*Bt
    P=0.05*Phi**2*Om**2/(4*math.pi*1e-7*c)  # BZ, SI: kappa Phi^2 Omega_H^2/(mu0 c), kappa~0.05
    print(f"   {name}: r_g={rg:.2e} m, Omega_H={Om:.2e} rad/s, B~{Bt*1e4:.0f} G, P_BZ~{P:.1e} W")
    # Wald (1974) equilibrium charge, cgs: Q = 2 G B J / c^3, J = a G M^2 / c
    Gc=6.674e-8; cc=2.998e10; Mg=m*1e3; Bg=Bt*1e4
    J=a*Gc*Mg**2/cc; Qesu=2*Gc*Bg*J/cc**3; Q=Qesu/2.998e9
    Qext=math.sqrt(Gc)*Mg/2.998e9
    print(f"      Wald charge ~{Q:.1e} C vs extremal {Qext:.1e} C (ratio {Q/Qext:.1e})")
print("   M87* jet power measured ~1e35-1e37 W; this crude B~10 G estimate is 1-2 orders low, MAD-level flux (EHT 2021 polarimetry) closes the gap.")
print("6. Atom vs BH 'nucleus' size ratios")
print(f"   nucleus/atom ~ {1.75e-15/5.29e-11:.1e}; M87* r_g / Bondi radius(~0.1 kpc)~ {G*6.5e9*Msun/c**2/(0.12*3.086e19):.1e}")

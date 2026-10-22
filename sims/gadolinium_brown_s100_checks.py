"""Share #100 (Gerald V. Brown / gadolinium thread) — rerun of Grok-stated numbers.
CC0-1.0. Pure Python, standard library only."""
import math
e=1.602176634e-19; me=9.1093837e-31; mp=1.67262192e-27; c=2.99792458e8
RE=6.371e6; B0=3.11e-5  # equatorial surface dipole field, T
R=8.314; kB=1.380649e-23
print("== 1. Gadolinium magnetocaloric (Brown 1976: 14 K adiabatic, 4 kJ/kg isothermal at 7 T, Tc 293 K)")
print(f"  mean adiabatic dT/dB over 0-7 T = {14/7:.1f} K/T (low-field slope ~2.5-3 K/T; effect sub-linear in B)")
cp=236.0  # J/kg/K, Gd lattice+electronic near RT (approx, zero field)
print(f"  dT_ad ~ Q/cp = 4000/{cp:.0f} = {4000/cp:.0f} K (upper bound; cp is larger near Tc, so 14 K is consistent)")
print(f"  implied isothermal dS_M = 4000/293 = {4000/293:.1f} J/(kg K)")
print(f"  Brown 1976 regenerator span 46 C to -1 C = {46-(-1)} K after ~50 cycles  (span > single-shot 14 K because of regeneration)")
Th,Tc_=319.0,272.0
print(f"  Carnot COP (cooling) across that span = {Tc_/(Th-Tc_):.1f}  (ceiling; no over-unity: COP>1 is heat moved per work, not energy created)")
print("  permanent-magnet 1 T stage at ~2.5-3 K/T -> ~2.5-3 K single-shot lift (Grok: 'a few kelvin per stage' OK)")
print("\n== 2. Acoustic impedances (Grok: Ag ~38 MRayl, Sn ~24 MRayl)")
for n,rho,v in [("Ag",10490,3650),("Sn",7300,3320),("Au",19300,3240)]:
    print(f"  {n}: Z = {rho*v/1e6:.1f} MRayl")
print("\n== 3. Arrhenius factor for 10 kcal/mol at 298 K (Grok: ~1e-7)")
print(f"  exp(-Ea/RT) = {math.exp(-10*4184/(R*298)):.1e}")
print("\n== 4. Electron cyclotron frequency per gauss (Grok wrote 'f_ce ~ 28B kHz, B in gauss')")
fce_G=e*1e-4/(2*math.pi*me)
print(f"  f_ce = {fce_G/1e6:.2f} MHz per gauss = {fce_G/1e6*1e-2*1e3:.0f} kHz per uT = 28 Hz per nT  -> CORRECTION: 2.8 MHz/G, not 28 kHz/G")
print(f"  f_pe = 8.98 kHz * sqrt(n_e[cm^-3]) (Grok's 9 sqrt(n) kHz OK)")
Bsrc=300e3/(fce_G*1e4)
print(f"  AKR at 300 kHz needs B = {Bsrc*1e9:.0f} nT; with ~55,000 nT at the polar surface, r = {(55e-6/Bsrc)**(1/3):.2f} RE"
      f" -> altitude ~{((55e-6/Bsrc)**(1/3)-1)*6371:.0f} km (Grok: 'a few thousand km' OK)")
print("\n== 5. Three clocks, dipole, equatorial (Grok table: gyro / bounce(80 deg) / drift(90 deg))")
def clocks(L,WkeV,a_b=80,a_d=90):
    W=WkeV*1e3*e; g=1+W/(me*c*c); v=c*math.sqrt(1-1/g**2); p=g*me*v
    B=B0/L**3
    tg=2*math.pi*g*me/(e*B)
    sa=math.sin(math.radians(a_b))
    tb=4*L*RE/v*(1.30-0.56*sa)
    sd=math.sin(math.radians(a_d))
    wd=3*L*p*v/(2*e*B0*RE**2)*(0.7+0.3*sd)  # ~ (0.35+0.15 sin) * 2
    td=2*math.pi/wd
    return tg,tb,td
for L in (2,4,6):
    row=[]
    for W in (10,100,1000):
        tg,tb,td=clocks(L,W)
        row.append(f"{tg*1e6:7.1f} us / {tb:5.2f} s / {td/3600:6.2f} h")
    print(f"  L={L}: "+" | ".join(row))
tg,tb,td=clocks(6,10)
print(f"  L=6, 10 keV: gyrations per bounce = {tb/tg:.0f} (Grok ~7000); bounces per drift = {td/tb:.0f} (Grok ~20,000)")
print(f"  proton/electron at same energy: bounce ratio sqrt(mp/me) = {math.sqrt(mp/me):.1f}, gyro ratio mp/me = {mp/me:.0f}")
print("\n== 6. Cyclotron level spacing hbar*w_ce at 1 uT")
hbar=1.054571817e-34
print(f"  = {hbar*e*1e-6/me/e:.1e} eV (Grok '~1e-10 eV' is the right order for ~1-10 uT)")

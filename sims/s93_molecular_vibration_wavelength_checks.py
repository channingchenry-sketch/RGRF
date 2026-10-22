"""Share #93 checks: molecular vibrations vs Schrodinger/Dirac wavelength scales. CC0.
Reruns Grok's numbers from 'Data Linking Molecular Vibrations to Schrodinger and Dirac Wavelengths'."""
import numpy as np
h=6.62607015e-34; hbar=h/2/np.pi; c=2.99792458e8; kB=1.380649e-23
me=9.1093837e-31; u=1.66053907e-27; e=1.602176634e-19
mH=1.00782503*u; mPb=207.976652*u; mp=1.67262192e-27
def wn2Hz(w): return w*100*c
print("1. IR band 2.5-25 um <-> wavenumber / frequency")
for lam in (2.5e-6,25e-6): print(f"  {lam*1e6:5.1f} um = {1/lam/100:7.0f} cm^-1 = {c/lam:.3e} Hz")
for name,w in [("H2O bend",1595),("H2O sym",3657),("H2O asym",3756),("CO",2143),("PbH4 Pb-H asym",1823),("CO2 dyad lo",1285),("CO2 dyad hi",1388)]:
    print(f"  {name:15s} {w:5d} cm^-1 -> {wn2Hz(w):.3e} Hz, {1e4/w:6.2f} um, {h*wn2Hz(w)/e*1e3:6.1f} meV")
print("2. Mode counting 3N-6: PbH4 N=5 ->",3*5-6,"; CH4",9,"; C3H8 N=11 ->",3*11-6)
print("   direct-product basis 10^12 functions x 8 B =",10**12*8/1e12,"TB")
print("3. hbar*omega/kT at 300 K (frozen modes):")
for w in (1595,3657,2143,609): print(f"  {w} cm^-1: {h*wn2Hz(w)/(kB*300):.2f}")
print("4. PbH rotational constants")
mu=mH*mPb/(mH+mPb); Be=h/(8*np.pi**2*c*mu*(1.838e-10)**2)/100
print(f"  mu={mu/u:.4f} u; B_e from r_e=1.838 A: {Be:.3f} cm^-1 (Grok 4.971)")
B0=4.971; a=0.144
for v in range(3):
    Bv=B0-a*(v+.5); print(f"  v={v}: B_v={Bv:.3f}, I increase {100*(B0/Bv-1):.2f}%")
print("   PbH4 spherical top I=(8/3) m_H r^2 (Pb at centre):")
for r in (1.73,1.75):
    I=8/3*mH*(r*1e-10)**2; print(f"  r={r} A -> B={h/(8*np.pi**2*c*I)/100:.3f} cm^-1 (Grok B0 2.084)")
print("5. Grok's Dirac vs nonrel. frequency shifts (Grok-reported values)")
for n,r,nr in [("PbH4 w1",1839,1847),("PbH4 w2",1827,1839),("PbH4 w3",686,664),("C-Pb str",384,409),("C-C-Pb bend",187,145),("H-Pb-H sc",641,597)]:
    print(f"  {n:12s} {100*(r-nr)/nr:+6.1f}%")
print("6. CO2 Fermi dyad 2x2: unperturbed 1337/1334 (Grok) vs observed 1285/1388")
split=1388-1285; d=1337-1334; W=np.sqrt(split**2-d**2)/2
print(f"  observed splitting {split} cm^-1 -> |W| = {W:.1f} cm^-1 needed")
print(f"  mean check: (1337+1334)/2={1335.5} vs (1285+1388)/2={(1285+1388)/2}  (sum rule holds to ~1 cm^-1)")
E1,E2=1285,1388; m=(E1+E2)/2
for dd in (3,30,60):
    Wf=np.sqrt((split/2)**2-(dd/2)**2); H=np.array([[m+dd/2,Wf],[Wf,m-dd/2]]); ev,vec=np.linalg.eigh(H)
    print(f"  detuning {dd}: W={Wf:.1f}, mixing |c|^2={vec[0,0]**2:.3f}/{vec[1,0]**2:.3f}")
print("7. Water DD: <200|H|002> = (K/4)sqrt(2*1*1*2) = K/2 (Watson/standard convention); lit K ~ -155 cm^-1 [to verify] -> ~-78 cm^-1")
print("8. Context scales (not in chat): Compton, de Broglie, Zitterbewegung")
lc=h/(me*c); print(f"  electron Compton {lc:.4e} m; reduced {lc/2/np.pi:.4e} m")
print(f"  proton Compton {h/(mp*c):.4e} m")
fz=2*me*c**2/h; print(f"  Zitterbewegung 2mc^2/h = {fz:.4e} Hz (omega=2mc^2/hbar={2*me*c**2/hbar:.3e} rad/s)")
for T in (300,):
    for nm,m_ in (("e-",me),("H atom",mH),("H2",2*mH)):
        lam=h/np.sqrt(2*np.pi*m_*kB*T); print(f"  thermal de Broglie {nm} @300K: {lam:.3e} m")
fv=wn2Hz(3657); print(f"  ratio f_ZB / f(H2O 3657) = {fz/fv:.3e} = 2^{np.log2(fz/fv):.2f} 'octaves' (numerology, no physical link)")
print(f"  ratio IR lambda(2.73 um) / electron Compton = {1e-2/3657/lc:.3e} = 2^{np.log2(1e-2/3657/lc):.2f}")
print("9. Klein-Gordon for nuclei: E_vib/(m c^2)")
print(f"  H nucleus: {h*fv/(mp*c**2):.2e};  Pb: {h*wn2Hz(1564)/(mPb*c**2):.2e}")

"""Composite-fermion effective field and commensurability (geometric resonance) minima near nu = 1/2.
TEXTBOOK ILLUSTRATION (CC0). Not a fit to any dataset; parameters are typical GaAs values.
Model: B_eff = B - 2*phi0*n (two flux quanta per electron, HLR/Jain mean field).
Spin-polarized CF Fermi wavevector k_F* = sqrt(4*pi*n).
Weiss-type minima for a 1D density modulation of period a: 2 R_c*/a = i + 1/4,
R_c* = hbar k_F* / (e |B_eff|)  ->  |B_eff|_i = 2 hbar k_F* / (e a (i + 1/4)).
"""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
h=6.62607015e-34; e=1.602176634e-19; hbar=h/(2*np.pi); phi0=h/e
n=1.5e15          # m^-2  (1.5e11 cm^-2)
a=200e-9          # modulation period, m
B12=2*phi0*n
kF=np.sqrt(4*np.pi*n)
print(f"B(nu=1/2) = {B12:.3f} T, k_F* = {kF:.3e} 1/m")
mins=[]
for i in range(1,4):
    Bs=2*hbar*kF/(e*a*(i+0.25))
    mins.append(Bs); print(f"i={i}: |B_eff| = {Bs*1e3:.1f} mT -> B = {B12-Bs:.3f} T and {B12+Bs:.3f} T")
B=np.linspace(B12-0.9,B12+0.9,600); Beff=B-B12
fig,ax=plt.subplots(1,2,figsize=(11,4))
ax[0].plot(B,Beff,'k'); ax[0].axhline(0,c='gray',lw=.5); ax[0].axvline(B12,c='r',ls='--',label='nu=1/2')
ax[0].set_xlabel('applied B (T)'); ax[0].set_ylabel('B_eff = B - 2 phi0 n (T)'); ax[0].legend(); ax[0].set_title('CF effective field')
for Bs in mins:
    for s in (-1,1): ax[1].axvline(B12+s*Bs,c='b',ls=':')
ax[1].axvline(B12,c='r',ls='--'); ax[1].set_xlim(B12-0.9,B12+0.9); ax[1].set_yticks([])
ax[1].set_xlabel('applied B (T)'); ax[1].set_title(f'predicted CF geometric-resonance minima (a={a*1e9:.0f} nm), i=1..3')
fig.suptitle('Textbook illustration: composite-fermion Fermi sea near nu=1/2 (CC0)'); fig.tight_layout()
fig.savefig('/workspace/fractional_fermi_sea_plot.png',dpi=120); print("saved /workspace/fractional_fermi_sea_plot.png")

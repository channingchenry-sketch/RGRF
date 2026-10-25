"""NV- centre ODMR / Rabi / Ramsey textbook illustration (RGRF, CC0).
H = D Sz^2 + gamma_e B.S (spin-1, units GHz). Not a model of the OIST experiment.
Panels: (a) ODMR transition frequencies vs on-axis B (splitting 2*gamma*B), with GSLAC at ~102 mT;
(b) ODMR spectrum at B=5 mT (Lorentzian dips, contrast ~ 2%); (c) Rabi oscillation; (d) Ramsey with T2*.
Also: shot-noise sensitivity estimates and the bench Halbach / stator field check."""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
D=2.870; g=28.025  # GHz, GHz/T
Sz=np.diag([1,0,-1]).astype(complex); Sx=np.array([[0,1,0],[1,0,1],[0,1,0]])/np.sqrt(2)
def levels(B,theta=0.0):
    H=D*Sz@Sz+g*B*(np.cos(theta)*Sz+np.sin(theta)*Sx); return np.linalg.eigvalsh(H)
Bs=np.linspace(0,0.15,601); E=np.array([levels(b) for b in Bs])
# on-axis: ms=0 is level 0 at low field; transitions |E(+-1)-E(0)|
f_minus=np.abs(D-g*Bs); f_plus=D+g*Bs
fig,ax=plt.subplots(2,2,figsize=(11,8))
ax[0,0].plot(Bs*1e3,f_plus,'r',label='ms=0 -> +1'); ax[0,0].plot(Bs*1e3,f_minus,'b',label='ms=0 -> -1')
ax[0,0].axvline(D/g*1e3,c='k',ls=':',label=f'GSLAC {D/g*1e3:.1f} mT'); ax[0,0].set(xlabel='B along NV axis (mT)',ylabel='f (GHz)',title='(a) ODMR lines: splitting 2*gamma*B'); ax[0,0].legend(fontsize=8)
B0=5e-3; f=np.linspace(2.6,3.15,2000); w=0.005; C=0.02
spec=1-C*(w**2/((f-(D-g*B0))**2+w**2)+w**2/((f-(D+g*B0))**2+w**2))
ax[0,1].plot(f,spec,'g'); ax[0,1].set(xlabel='microwave f (GHz)',ylabel='norm. PL',title=f'(b) cw-ODMR at {B0*1e3:.0f} mT: dips at {D-g*B0:.3f}, {D+g*B0:.3f} GHz')
t=np.linspace(0,1,500); Om=10.0  # MHz Rabi, us
ax[1,0].plot(t*1e3,1-C*np.sin(np.pi*Om*t)**2*np.exp(-t/0.5),'m'); ax[1,0].set(xlabel='MW pulse length (ns)',ylabel='norm. PL',title='(c) Rabi, Omega/2pi = 10 MHz (pi pulse 50 ns)')
tau=np.linspace(0,3,800); T2s=1.0; det=3.0  # us, MHz
ax[1,1].plot(tau,0.5*(1+np.cos(2*np.pi*det*tau)*np.exp(-(tau/T2s)**2)),'k'); ax[1,1].set(xlabel='free precession tau (us)',ylabel='P(ms=0)',title='(d) Ramsey, detuning 3 MHz, T2* = 1 us')
fig.suptitle('NV- centre: TEXTBOOK ILLUSTRATION (not data, not the OIST experiment)'); fig.tight_layout(); fig.savefig('/workspace/nv_center_plot.png',dpi=120)
# off-axis check: at 50 mT, theta=54.7 deg (OIST-like orientation) the lines mix
for th in (0,np.deg2rad(54.7)):
    e=levels(0.05,th); print(f'B=50 mT theta={np.rad2deg(th):.1f} deg: transitions {e[1]-e[0]:.3f}, {e[2]-e[0]:.3f} GHz')
# sensitivity: cw-ODMR shot noise eta ~ (4/(3 sqrt3)) * w/(g*C*sqrt(R))
for name,R in (('single NV, R=1e5 cps',1e5),('ensemble 4.5 ppm, ~1e11 cps (1 mW-scale spot)',1e11)):
    eta=4/(3*np.sqrt(3))*(w*1e9)/(g*1e9*C*np.sqrt(R)); print(f'{name}: eta ~ {eta*1e9:.3g} nT/sqrtHz')
# bench Halbach field: RGRF halbach_switched_arc_check: B0 = 0.96 T surface, lambda = 10 cm; one-sided decay B(y) = B0 exp(-2 pi y / lambda)
B0h=0.96; lam=0.10; eta_ens=22e-9
print(f'Halbach surface {B0h} T -> on-axis line {D+g*B0h:.1f} GHz; far beyond GSLAC ({D/g*1e3:.0f} mT): near the surface use a Hall probe, NV for the far/stray field')
for y in (0.02,0.05,0.10,0.15,0.20):
    By=B0h*np.exp(-2*np.pi*y/lam); print(f'y={y*100:.0f} cm: B ~ {By*1e3:.3g} mT -> 2*gamma*B = {2*g*By*1e3:.4g} MHz splitting; ensemble (~22 nT/sqrtHz) resolves dB/B ~ {eta_ens/By:.1e} in 1 s')
print('Window where ODMR is clean (B < ~50-100 mT, below ESLAC 51 mT / GSLAC 102 mT, and aligned): y > ~3.6-4.7 cm for this array')

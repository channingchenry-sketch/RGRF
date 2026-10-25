"""Flux attachment: CF effective field vs filling, Jain fractions and CF Landau-level filling p.
TEXTBOOK ILLUSTRATION (CC0). Mean-field only; real gaps, disorder and spin are ignored.
nu = n*phi0/B. Attaching 2s flux quanta: B_eff = B - 2s*phi0*n  ->  B_eff/B = 1 - 2s*nu.
CF filling nu* = n*phi0/|B_eff| = p  gives  nu = p/(2s*p +- 1).
"""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from fractions import Fraction as F
nu=np.linspace(0.05,0.95,900)
fig,ax=plt.subplots(1,2,figsize=(12,4.5))
for s,c in ((1,'k'),(2,'g')):
    ax[0].plot(nu,1-2*s*nu,c,label=f'{2*s} flux quanta: B_eff/B = 1 - {2*s}ν')
ax[0].axhline(0,c='gray',lw=.5); ax[0].set_ylim(-1.2,1.05)
for s,c,mk in ((1,'b','o'),(2,'m','s')):
    for p in range(1,7):
        for sg in (1,-1):
            f=F(p,2*s*p+sg)
            if 0<f<1:
                x=float(f); ax[0].plot(x,1-2*s*x,mk,c=c,ms=4)
                ax[1].plot(x,sg*p,mk,c=c,ms=5)
                if p<=4: ax[1].annotate(str(f),(x,sg*p),fontsize=7,xytext=(3,3),textcoords='offset points')
                if s==1 and p<=3: print(f"2 flux, p={sg*p:+d}: nu={f}")
ax[0].set_xlabel('filling ν'); ax[0].set_ylabel('B_eff / B'); ax[0].legend(fontsize=8); ax[0].set_title('mean-field effective field')
ax[1].axvline(.5,c='r',ls='--',label='ν=1/2 (CF Fermi sea)'); ax[1].axvline(.25,c='orange',ls='--',label='ν=1/4 (4-flux CF sea)')
ax[1].set_xlabel('filling ν'); ax[1].set_ylabel('CF Landau levels filled, ±p (sign = B_eff direction)')
ax[1].legend(fontsize=8); ax[1].set_title('Jain sequences ν = p/(2sp ± 1): blue 2-flux, magenta 4-flux')
fig.suptitle('Textbook illustration: flux attachment and the Jain sequence (CC0)'); fig.tight_layout()
fig.savefig('/workspace/flux_attachment_plot.png',dpi=120); print('saved /workspace/flux_attachment_plot.png')

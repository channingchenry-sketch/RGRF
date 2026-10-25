"""Leucine dose vs muscle protein synthesis (MPS): ILLUSTRATION (CC0), general information, not medical advice.
Toy model: MPS stimulation = signal(leucine) x substrate(EAA availability).
 signal: Hill/Michaelis-Menten on leucine dose, half-max ~1 g, Hill n=2 (assumed; 'leucine threshold' idea).
 substrate: BCAA-only supplies 3 of 9 EAAs -> capped by EAA released from breakdown (Wolfe 2017 argues <=~30% ceiling).
 Complete protein: substrate not limiting. Jackman 2017: BCAA 5.6 g gave +22% MPS vs placebo, ~50% of a whey response.
"""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
L=np.linspace(0,5,200); K=1.0; n=2
sig=L**n/(K**n+L**n)
whey=100*sig            # % increase over baseline, complete protein (assumed max 100%)
bcaa=np.minimum(whey,30)*np.ones_like(L)  # substrate-capped (Wolfe ceiling ~30%)
bcaa=np.minimum(100*sig,30)
for d in (1,2.5,3):
    i=np.argmin(abs(L-d)); print(f"leucine {d} g: complete protein +{whey[i]:.0f}%, BCAA-only +{bcaa[i]:.0f}% (model)")
plt.figure(figsize=(7,4.5)); plt.plot(L,whey,label='complete protein / EAA (substrate not limiting)'); plt.plot(L,bcaa,label='BCAA only (capped by other EAAs from breakdown)')
plt.scatter([5.6*0.5],[22],c='r',zorder=5,label='Jackman 2017: 5.6 g BCAA (~2.8 g Leu, 2:1:1 assumed) → +22%')
plt.xlabel('leucine dose (g)'); plt.ylabel('MPS increase over baseline (%) — toy'); plt.legend(fontsize=8)
plt.title('Illustration: leucine signal vs substrate limit (not medical advice)'); plt.tight_layout(); plt.savefig('/workspace/bcaa_plot.png',dpi=120); print('saved /workspace/bcaa_plot.png')

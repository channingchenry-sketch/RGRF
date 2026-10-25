"""Vanadium revisit (RGRF, CC0). (a) VRFB Nernst OCV vs SOC + tank energy ledger; (b) VO2 hysteresis (textbook illustration).
Ledger rule: E_out = eta_RT * E_in, always < E_in. No over-unity."""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
R,F,T=8.314,96485,298.15; E0=1.26   # V, formal standard potential (VO2+/VO2+ 1.00 V; V3+/V2+ -0.26 V)
soc=np.linspace(0.02,0.98,300)
ocv_simple=E0+2*R*T/F*np.log(soc/(1-soc))            # two-electron-equivalent form, protons ignored
cH=4.0; ocv_H=ocv_simple+2*R*T/F*np.log(cH)            # + proton term (2 H+ at the positive side), ~4 M H+ (2 M H2SO4) assumed -> ~1.33 V at 50 %
# electrolyte: 1.6 M V; usable SOC 15-85 %; theoretical Wh per litre of TOTAL electrolyte (both tanks)
cV=1.6; Vavg=1.35; dSOC=0.70
Wh_per_L=cV*F*Vavg*dSOC/3600/2   # /2: each litre of energy needs a litre in each tank
rho=1.35  # kg/L
eta_lo,eta_hi=0.75,0.80
print(f'OCV at SOC 50% (simple) {E0:.3f} V; with proton term {np.interp(0.5,soc,ocv_H):.3f} V; SOC 10->90%: {np.interp(0.1,soc,ocv_H):.3f} -> {np.interp(0.9,soc,ocv_H):.3f} V')
print(f'Usable energy density (1.6 M, 15-85 % SOC, both tanks): {Wh_per_L:.1f} Wh/L electrolyte = {Wh_per_L/rho:.1f} Wh/kg (excl. stack, pumps, tanks)')
rows=[]
for name,P,hours in (('bench 520 W, 4 h',520,4),('hover 10 kW, 15 min',10e3,0.25),('hover 17 kW, 15 min',17e3,0.25),('hover 17 kW, 1 h',17e3,1)):
    Eout=P*hours; L=Eout/Wh_per_L; m=L*rho
    Ein_lo,Ein_hi=Eout/eta_hi,Eout/eta_lo
    rows.append((name,Eout,L,m,Ein_lo,Ein_hi))
    print(f'{name}: E_out {Eout/1e3:.2f} kWh -> electrolyte {L:.0f} L ({m:.0f} kg); recharge input {Ein_lo/1e3:.2f}-{Ein_hi/1e3:.2f} kWh (eta 75-80 %); loss {Ein_lo-Eout:.0f}-{Ein_hi-Eout:.0f} Wh; tau = E/P = {hours*60:.0f} min')
print('Compare Li-ion pack ~150-250 Wh/kg: VRFB is a ground/dock buffer, not a flight battery.')
# VO2 hysteresis: heating Tc 68 C, cooling ~62 C, width ~6 K; IR transmittance (2.5 um) 60% -> 5 %; resistance ratio ~1e4
Tt=np.linspace(30,100,400)
def frac(T,Tc,w=1.5): return 1/(1+np.exp(-(T-Tc)/w))
fh,fc=frac(Tt,68),frac(Tt,62)
Tr_h,Tr_c=0.60-0.55*fh,0.60-0.55*fc
logR_h,logR_c=5-4*fh,5-4*fc
fig,ax=plt.subplots(1,3,figsize=(15,4.5))
ax[0].plot(soc*100,ocv_simple,'b',label='Nernst, protons ignored'); ax[0].plot(soc*100,ocv_H,'r',label='with proton term (~4 M H+)'); ax[0].set(xlabel='state of charge (%)',ylabel='OCV (V)',title='(a) VRFB open-circuit voltage'); ax[0].legend()
names=[r[0] for r in rows]; ax[1].barh(names,[r[3] for r in rows],color='teal'); ax[1].set(xscale='log',xlabel='electrolyte mass (kg, log)',title=f'(a) tank sizing at {Wh_per_L:.0f} Wh/L; eta_RT 75-80 %')
ax[2].plot(Tt,Tr_h*100,'r',label='heating'); ax[2].plot(Tt,Tr_c*100,'b',label='cooling'); ax[2].set(xlabel='T (C)',ylabel='IR transmittance (%)',title='(b) VO2 film: insulator->metal ~68 C (hysteresis)')
a2=ax[2].twinx(); a2.plot(Tt,logR_h,'r:'); a2.plot(Tt,logR_c,'b:'); a2.set_ylabel('log10 R (ohm), dotted'); ax[2].legend(loc='center left')
fig.suptitle('Vanadium: TEXTBOOK ILLUSTRATION (model numbers; not measured data)'); fig.tight_layout(); fig.savefig('/workspace/vanadium_plot.png',dpi=120)
print('VO2 (illustrative): heating Tc 68 C, cooling 62 C, IR 2.5 um transmittance 60% -> 5%, resistance ratio 1e4')

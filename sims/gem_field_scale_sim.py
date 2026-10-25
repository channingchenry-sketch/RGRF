"""Gravitoelectromagnetism (GEM) field scales. ILLUSTRATION (CC0). Weak-field, slow-rotation GR.
Gyroscope (Lense-Thirring / Schiff) precession: Omega(r) = G/(c^2 r^3) [3 (J.rhat) rhat - J].
  On the spin axis: Omega = 2GJ/(c^2 r^3); equator: -GJ/(c^2 r^3); polar-orbit average: GJ/(2 c^2 a^3).
Gravitoelectric (Newtonian) acceleration a_GE = GM/r^2.
Gravitomagnetic acceleration on a test mass with speed v: a_GM ~ 2 v Omega  (order of magnitude;
  numerical prefactor depends on the GEM convention, factor 2 vs 4 in B_g).
Energy check: rotor kinetic energy vs gravitomagnetic spin-coupling energy U = S.Omega of a 1 kg, 1 m/s-scale test spinner.
"""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
G=6.674e-11; c=2.998e8; yr=3.156e7; mas=np.pi/180/3600e3; Msun=1.989e30
rows=[]
# (i) Earth, GP-B: polar orbit 642 km
M=5.972e24; I=8.034e37; w=7.2921e-5; a=6.371e6+642e3; J=I*w
Om=G*J/(2*c**2*a**3); v=np.sqrt(G*M/a)
print(f"GP-B frame dragging (polar-orbit average) = {Om*yr/mas:.1f} mas/yr  (GR with exact Earth model: 39.2; measured -37.2 +/- 7.2)")
rows.append(("Earth, GP-B orbit (642 km)",M,J,a,Om,v))
# (ii) lab rotor: 10 kg steel disk r=0.15 m at 10,000 rpm, field point 0.2 m on axis
m=10; R=0.15; w=10000*2*np.pi/60; J=0.5*m*R**2*w; r=0.2
Om=2*G*J/(c**2*r**3); rows.append(("10 kg disk, 10k rpm, 0.2 m on axis",m,J,r,Om,1.0))
KE=0.5*0.5*m*R**2*w**2
# oloid r=0.1 m, ~2 kg steel, 3000 rpm, crude I ~ 0.4 m r^2 [assumed]
m2=2; r2=0.1; w2=3000*2*np.pi/60; J2=0.4*m2*r2**2*w2
Om2=2*G*J2/(c**2*0.15**3); rows.append(("oloid ~2 kg, r=0.1 m, 3k rpm (assumed)",m2,J2,0.15,Om2,1.0))
# (iii) neutron star (1.4 Msun, R=12 km, I~1.3e38, P=1.5 ms) at 2R equator-ish; Kerr BH a*=0.9 10 Msun at 6 GM/c^2
Mn=1.4*Msun; In=1.3e38; Jn=In*2*np.pi/1.5e-3; rn=24e3
Omn=2*G*Jn/(c**2*rn**3); rows.append(("neutron star 1.4 Msun, P=1.5 ms, r=2R (axis)",Mn,Jn,rn,Omn,0.3*c))
Mb=10*Msun; Jb=0.9*G*Mb**2/c; rb=6*G*Mb/c**2
Omb=2*G*Jb/(c**2*rb**3); rows.append(("Kerr BH 10 Msun a*=0.9, r=6GM/c^2 (weak-field formula, indicative)",Mb,Jb,rb,Omb,0.4*c))
names=[];ge=[];gm=[];oms=[]
for nm,M_,J_,r_,O,v_ in rows:
    aGE=G*M_/r_**2; aGM=2*v_*O
    print(f"{nm}: J={J_:.3e} kg m^2/s, Omega={O:.3e} rad/s ({O*yr/mas:.3e} mas/yr), a_GE={aGE:.3e}, a_GM={aGM:.3e} m/s^2, ratio={aGM/aGE:.2e}")
    names.append(nm);ge.append(aGE);gm.append(aGM);oms.append(O)
print(f"energy check (lab disk): rotor KE = {KE:.3e} J; gravitomagnetic coupling of a 1 kg m^2/s test spin S*Omega = {1*rows[1][4]:.3e} J; ratio {rows[1][4]/KE:.1e}")
print(f"proton coupling ratio G m_p^2 / (e^2/4 pi eps0) = {G*(1.6726e-27)**2/(2.307e-28):.2e}")
fig,ax=plt.subplots(1,2,figsize=(14,4.8)); y=np.arange(len(names))
ax[0].barh(y,np.log10(oms),color='purple'); ax[0].set_yticks(y); ax[0].set_yticklabels(names,fontsize=7); ax[0].set_xlabel('log10 frame-dragging rate Ω (rad/s)'); ax[0].set_title('gravitomagnetic precession rate')
ax[1].barh(y-0.2,np.log10(ge),0.4,label='gravitoelectric GM/r²'); ax[1].barh(y+0.2,np.log10(gm),0.4,label='gravitomagnetic ~2vΩ')
ax[1].set_yticks(y); ax[1].set_yticklabels(['']*len(y)); ax[1].set_xlabel('log10 acceleration (m/s²)'); ax[1].legend(fontsize=8); ax[1].set_title('GE vs GM acceleration on a moving test mass')
fig.suptitle('Illustration: GEM field scales (CC0). Weak-field formulas; BH row indicative only'); fig.tight_layout()
fig.savefig('/workspace/gem_field_scale_plot.png',dpi=120); print('saved /workspace/gem_field_scale_plot.png')

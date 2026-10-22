"""Share #113 check: CIRE tank frequency, spiral ratios, wire length, and coherent vs jittered impulse ring-up (Q=600, kick every 4 cycles)."""
import numpy as np, math
L=33e-6;C=124e-12;f=1/(2*math.pi*math.sqrt(L*C));print('f0 MHz',f/1e6)
r=[8.0,10.7,14.3,19.0,25.4];print('radius ratios',[round(r[i+1]/r[i],3) for i in range(4)],'phi=1.618')
print('wire m',sum(2*math.pi*x/100 for x in r))
# coherent vs jittered impulse ring-up, Q=600, kick every 4 cycles
Q=600;w=2*math.pi;g=w/(2*Q);rng=np.random.default_rng(0)
def run(jit):
    z=0j
    for k in range(3000):
        dt=4+ (rng.normal(0,jit) if jit else 0)
        z=z*np.exp((1j*w-g)*dt)+1
    return abs(z)
coh=run(0);inc=np.mean([run(0.25) for _ in range(20)])
print('steady amplitude coherent',round(coh,1),'jitter 0.25 cycle',round(inc,1),'ratio',round(coh/inc,2),'energy ratio',round((coh/inc)**2,2))

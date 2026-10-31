"""Share #164 check: Euler-Heisenberg (EH) weak-field stress for pure B, and a rerun of Grok's w_eff tables.
Natural Heaviside-Lorentz units (hbar=c=1). L = X + c*4X^2 + 7c(E.B)^2, X=(E^2-B^2)/2, c=2 alpha^2/(45 m^4).
For a medium L(X) with pure B along z: p_par = L, p_perp = L - 2X L'(X), u = -L.
No energy is extracted; this is a stress bookkeeping check (ledger: closed system, no source/sink terms)."""
import math
a=1/137.036; e=math.sqrt(4*math.pi*a); Bc_T=4.414e9
def eh(Bn):  # B in units of m^2 (=e*B_c)
    c=2*a*a/45; X=-Bn*Bn/2; L=X+4*c*X*X; Lp=1+8*c*X
    u=-L; pp=L; pt=L-2*X*Lp
    return u,pp,pt
for Bc_mult in [1e-3,0.1,1.0]:
    Bn=Bc_mult/e  # B = mult*B_c = mult*m^2/e
    u,pp,pt=eh(Bn); m=Bn*Bn/2
    print(f"B={Bc_mult}Bc: du/u_M={(u-m)/m:.2e} dp_par/u_M={(pp+m)/m:.2e} dp_perp/u_M={(pt-m)/m:.2e} NEC u+p_perp={u+pt:.3e}>0, u+p_par={u+pp:.1e}")
print("EH = Maxwell crossover B/Bc =",math.sqrt(45)/2/a*e,"(~%.1e T, far outside weak-field validity)"%(math.sqrt(45)/2/a*e*Bc_T))
print("Grok table 1 rerun with Grok's own formula (P_par+2P_perp)/(3rho)-1:")
for r in [.1,.5,1,2,5,10]:
    pl,pp,ro=1-r,1+r,3+2*r; print(r,round((pl+2*pp)/(3*ro)-1,3))
print("Grok table 2 rerun (kappa=0.05): r, P_par, P_perp, rho, w_Grok_formula, w_physical=(P_par+2P_perp)/(3rho)")
for r in [.5,1,2,4,6,8,10]:
    k=.05;pl=1-r+2*k*r*r;pp=1+r-k*r*r;ro=3+2*r+k*r*r
    print(r,round(pl,3),round(pp,3),round(ro,3),round((pl+2*pp)/(3*ro)-1,3),round((pl+2*pp)/(3*ro),3))

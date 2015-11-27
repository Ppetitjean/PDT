from math import pi
rho16 = 998.9
rho0 = 999.8
mu = 8.9e-04
nu = mu/rho16
r = 0.033
d = 2*r
h = 0.11
w = 2*pi*1000/60
v = w*r
Re = (v*h)/nu
print("Re",Re)
Pr = nu/h
print("Prandt",Pr)
Nux = 0.029*(Pr**0.43)*(Re**0.8)
print("Nusselt x",Nux)
Nu = (1/0.8)*Nux
print("Nusselt",Nu)
kf = 0.5985
hx = kf*Nu/h
print("hx",hx)
hout = hx
hin = hx

BiotForced = hout/(hin+kf/(d/4))
print("BiotForced",BiotForced)

B=0.000214
g = 9.81
DeltaT = 16

Gr = (B*g*DeltaT*(h**3))/nu**2
print("Grashof",Gr)

Ra = Gr*Pr
print("Rayleigh",Ra)
NuD = 0.85*Ra**0.188
print("Nud",NuD)
hD = kf*NuD/h
print("HD",hD)
BiotNatural = hD/(hD+kf/(d/4))
print("BiotNatural",BiotNatural)
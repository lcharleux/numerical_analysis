import truss
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import patches
import copy

modulus = 210.e9     #Pa
rho = 2700.           #kg/m**3
surface = 1.e-4       #m**2
yield_stress = 400.e6 #Pa

m = truss.core.Model()
A = m.add_node((0.,0.), label = "A")
C = m.add_node((1.,0.), label = "C")
D = m.add_node((1.,1.), label = "D")
E = m.add_node((2.,0.), label = "E")
F = m.add_node((2.,1.), label = "F")
G = m.add_node((3.,0.), label = "G")
H = m.add_node((3.,1.), label = "H")


A.block[1] = True
G.block[0] = True
H.block[0] = True

G.force = np.array([0., -1.])*1.e4
#C.force[0] = .2
#C.force[1] = -0.




AC = m.add_bar(A, C, modulus = modulus, density = rho, section = surface)

CD = m.add_bar(C, D, modulus = modulus, density = rho, section = surface)
AD = m.add_bar(A, D, modulus = modulus, density = rho, section = surface)
CE = m.add_bar(C, E, modulus = modulus, density = rho, section = surface)
DF = m.add_bar(D, F, modulus = modulus, density = rho, section = surface)
DE = m.add_bar(D, E, modulus = modulus, density = rho, section = surface)
EF = m.add_bar(E, F, modulus = modulus, density = rho, section = surface)
EG = m.add_bar(E, G, modulus = modulus, density = rho, section = surface)
FH = m.add_bar(F, H, modulus = modulus, density = rho, section = surface)
FG = m.add_bar(F, G, modulus = modulus, density = rho, section = surface)
GH = m.add_bar(G, H, modulus = modulus, density = rho, section = surface)


#m.solve()
m0 = copy.deepcopy(m)


xlim, ylim = m.bbox(deformed = False)
fig = plt.figure(0)
plt.clf()
ax = fig.add_subplot(1,1,1)
ax.set_aspect("equal")
#ax.axis("off")
m.draw(ax, deformed = False, field = None, label = True, force_scale = 5.e-5, forces = True)
plt.xlim(xlim)
plt.ylim(ylim)
plt.grid()  
plt.xlabel("Axe $x$")
plt.ylabel("Axe $y$")

plt.savefig("treillis.png")

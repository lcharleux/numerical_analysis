# -*- coding: utf-8 -*-
"""
A Solar System class
"""

import ODE_solar_system
import numpy as np
import matplotlib.pyplot as plt
# from scipy.integrate import odeint # You may need this

def Euler(func, y0, t):
  dt = t[1] - t[0]
  nt = len(t)
  Y  = np.zeros([nt, len(y0)])
  Y[0] = y0
  for i in xrange(nt-1):
    Y[i+1] = Y[i] + func(Y[i], t[i]) * dt
  return Y

    
# Simulation settings    
G  = 1.               # Gravity constant
nm = 2                # Number of masses involved
m  = np.ones(nm)*1.e0 # Set all masses to 1. (except sun)
ms = 1.e5             # Mass of the sun
dt = 5.e-4     # time step duration 
nt = 50        # number of frames per step
solver = Euler # ODE solver


# Inputs 
theta = np.random.rand(nm) * 2. * np.pi # Starting
r = np.linspace(.01, 1., nm)
v = (G * ms / r)**.5 # orbital speed
v *= .75 # Decreasing initial velocity to produce elliptical orbits
x  =   r * np.cos(theta)
y  =   r * np.sin(theta)
vx = - v * np.sin(theta)
vy =   v * np.cos(theta)
P = np.array([x,   y]).transpose()
V = np.array([vx, vy]).transpose()
colors = "yrgbcmk"

# Centering the sun
m[0]  = ms
P[0] *= 0.
V[0] *= 0.    

nm = len(m)
s = ode_solar_system.System(m, P, V, G = G, nk = 5000)      



from matplotlib import animation
fig = plt.figure("Le systeme solaire")
plt.clf()
ax = fig.add_subplot(1,2,1)
ax.set_aspect("equal")
plt.xlim(-4., 4.)
plt.ylim(-4., 4.)
plt.grid()
planets = []



msize = 10. * (s.m / s.m.max())**(1./9.)
for i in xrange(nm):
  lc = len(colors)
  c = colors[i%lc]
  planet, = ax.plot([], [], "o"+c, markersize = msize[i])
  planets.append(planet)
  trail, = ax.plot([], [], "-"+c)
  planets.append(trail)


  
def init():
  for i in xrange(2 * nm):
    planets[i].set_data([], [])
    return planets 
    
def animate(i):
    s.solve(dt, nt, solver)
    x, y = s.position()
    for i in xrange(nm):
      planets[2*i].set_data(x[i:i+1], y[i:i+1])
      xt, yt = s.trail(i)
      planets[2*i+1].set_data(xt, yt)
    return planets 

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=2000, interval=20, blit=True)

plt.show()   

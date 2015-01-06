"""
Optimization of projectile trajectory

@author: ludovic.charleux@univ-savoie.fr
"""

# Packages
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

# Functions

def Wind(x, y):
  '''
  Returns the wind velocity at a given position.
  '''
  return -1.*y**.5, 0.  
  
def Trajectory(theta, v0):
  '''
  Computes the trajectory of the projectile
  '''
  Velocity = np.array([ [v0 * np.cos(np.radians(theta)), v0 * np.sin(np.radians(theta))]])
  Position = np.array([[0., 0.]])
  while True:
    last_position = Position[-1]
    last_velocity = Velocity[-1]
    new_position = Position[-1] + dt * Velocity[-1]
    Position = np.vstack((Position, new_position))
    wind = np.array(Wind(new_position[0], new_position[1]))
    new_velocity = last_velocity + dt * ( - g * ey -  k * ((last_velocity-wind)**2).sum()**.5 *(last_velocity - wind) )
    Velocity = np.vstack((Velocity, new_velocity))
    print new_position    
    if new_position[1] <= 0.: break
    #if len(Position) > 100: break
  return Position, Velocity

# Physical constants (SI Units)
m     =  1.   # Projectile mass
g     = 10.   # Gravity
theta = 45.   # Initial velocity angle versus horizontal direction in degrees
k     = 100.  # Drag coefficient
v0    = 1.    # Initial velocity
dt    = 0.001    # Time step

# Base vectors
ex = np.array([1., 0.])
ey = np.array([0., 1.])

# Putting it all together
Position, Velocity = Trajectory(theta, v0)
# Plots
fig = plt.figure(0)
plt.clf()
plt.gca().set_aspect('equal')
xmin = Position[:,0].min()
xmax = Position[:,0].max() 
ymin = Position[:,1].min()
ymax = Position[:,1].max()
x0, y0 = Position[0,0], Position[0,1]
xf, yf = Position[-1,0], Position[-1,1]
x = np.linspace(xmin, xmax, 10)
y = np.linspace(ymin, ymax, 10)
X, Y = np.meshgrid(x, y)
U, V = Wind(X, Y)
plt.contourf(X, Y, U, 100)
cbar = plt.colorbar()
cbar.set_label('Wind Velocity along x')
plt.plot(Position[:,0], Position[:,1], 'r-', label = 'Trajectoire', linewidth = 2.)
plt.plot(Position[0:1,0],Position[0:1,1],'ob',  label = 'Depart' )
plt.plot(Position[-1:,0],Position[-1:,1],'og',  label = 'Impact' )
#plt.quiver(X, Y, U, V,  width=0.0005)
plt.quiver(Position[:,0], Position[:,1], Velocity[:,0]/2., Velocity[:,1]/2.,  width=0.005)

plt.grid()
plt.xticks([x0, xf])
plt.yticks([y0, yf])
plt.legend()
plt.show()

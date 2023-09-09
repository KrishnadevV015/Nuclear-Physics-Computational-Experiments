import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm
import sys

theta=np.arange(0,np.pi,0.001)
phi=np.arange(0,2*np.pi,0.001)

(theta,phi)=np.meshgrid(theta,phi)


def to_plot(l,m):
    
    ylm =(sph_harm(m, l, phi,theta)) 

    
    if m<0:
        r=np.sqrt(2) * (-1) **m* ylm.imag 
    if m>0:
        r=np.sqrt(2) * (1) **m *ylm.real 

    if m==0:
        r=ylm
        
    #transforming to cartetian coordinates
    x=np.abs(r)*np.sin(phi)*np.sin(theta)
    y=np.abs(r)*np.cos(phi)*np.sin(theta)
    z=np.abs(r)*np.cos(theta)
    
    fig = plt.figure(figsize=plt.figaspect(1.))
    ax = fig.add_subplot( projection='3d')
    ax.set_title('Spherical Harmonics for l={},m={}'.format(l, m))
    ax_lim = 0.5
    ax.set_xlim(-ax_lim, ax_lim)
    ax.set_ylim(-ax_lim, ax_lim)
    ax.set_zlim(-ax_lim, ax_lim)

    ax.plot_surface(x,y,z,cmap='viridis')
    plt.savefig('axissphharm l={},m={}.png'.format(l,m))
    plt.show()

l_values=[0,1,2,3] #list containing l values

for l in l_values:
    for m in range(-l,l+1,1): #takes m vales corresponding to each l value

        to_plot(l,m)


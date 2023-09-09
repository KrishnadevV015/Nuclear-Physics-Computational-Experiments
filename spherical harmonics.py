from numpy import arange,pi,meshgrid,sqrt,abs,sin,cos
from matplotlib.pyplot import plot,title,show,savefig,figure,figaspect
from scipy.special import sph_harm
import sys

theta=arange(0,pi,0.001)
phi=arange(0,2*pi,0.001)

(theta,phi)=meshgrid(theta,phi)


def to_plot(l,m):
    
    ylm =(sph_harm(m, l, phi,theta)) 

    
    if m<0:
        r=sqrt(2) * (-1) **m* ylm.imag 
    if m>0:
        r=sqrt(2) * (1) **m *ylm.real 

    if m==0:
        r=ylm
        
    #transforming to cartetian coordinates
    x=abs(r)*sin(phi)*sin(theta)
    y=abs(r)*cos(phi)*sin(theta)
    z=abs(r)*cos(theta)
    
    fig = figure(figsize=figaspect(1.))
    ax = fig.add_subplot( projection='3d')
    ax.set_title('Spherical Harmonics for l={},m={}'.format(l, m))
    ax_lim = 0.5
    ax.set_xlim(-ax_lim, ax_lim)
    ax.set_ylim(-ax_lim, ax_lim)
    ax.set_zlim(-ax_lim, ax_lim)

    ax.plot_surface(x,y,z,cmap='viridis')
    savefig('axissphharm l={},m={}.png'.format(l,m))
    show()

l_values=[0,1,2,3] #list containing l values

for l in l_values:
    for m in range(-l,l+1,1): #takes m vales corresponding to each l value

        to_plot(l,m)


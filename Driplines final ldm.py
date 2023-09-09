from numpy import arange,exp
from matplotlib.pyplot import plot,xlabel,ylabel,show,title,legend,figure,savefig,grid
import sys
a_volume=14.1
a_surface=13.0
a_c=0.595
a_asym=19.0

def zmin(A): #to find z with maximum binding energy for a particular A
    return round((A/2)*(1/(1+0.25*(a_c/a_asym)*A**(2/3))))
def BE(A,z):
    N=A-z
    if z%2==0 and N%2==0: #to check if the nuclues is even-even
        a_parity=33.5
    if z%2==1 and N%2==1:#to check if the nuclues is odd-odd
        a_parity=-33.5
    if (z%2==0 and N%2==1) or (z%2==1 and N%2==0): #to check if the nucleus is even-odd or odd-even
        a_parity=0
    E_volume=a_volume*A
    E_surface=-a_surface*(A**(2/3))
    E_col=-a_c*(z*(z-1)/(A**(1/3)))
    E_sym=-a_asym*((A-2*z)**2)/A
    E_par=(a_parity/(A**(3/4)))
    be=(E_volume+E_surface+E_col+E_sym+E_par)
    return be

A=arange(3,300,1,dtype=int) #Array with A values
z_stability=[]#list to store proton number to draw beta stability curve
n_stability=[]#list to store proton number to draw beta stability curve

for a in A: #loop to generate N,Z to draw beta stability curve
    z=zmin(a)
    z_stability.append(z)
    n_stability.append(a-z)
    
def sp(a,z): #proton separation energy
    return BE(a,z)-BE(a-1,z-1)

def sn(a,z): #neutron separation energy
    return BE(a,z)-BE(a-1,z)

ndripp=[] #list to store proton number to draw neutron dripline
ndripn=[] #list to store neutron number to draw neutron dripline
pdripn=[] #list to store neutron number to draw proton dripline
pdripp=[] #list to store proton number to draw proton dripline

Z_values=arange(2,118,1)
N_values=arange(2,294,1)

for z in Z_values: #fixing z values and varying n values to generate data for proton dripline
    for n in N_values:
        a=n+z
        sne=sn(a,z)
        if sne<0:
            ndripn.append(n)
            ndripp.append(z)
            break
        
for n in N_values: #fixing n value and varying z value to generate data for neutron dripline
    for z in Z_values:
        a=n+z
        spe=sp(a,z)
        if spe<0:
            pdripn.append(n)
            pdripp.append(z)
            break

figure(figsize=(15,10))
plot(pdripn,pdripp,'g-',label='Proton Drip-line')
plot(ndripn,ndripp,'b-',label='Neutron Drip-line')
plot(n_stability,z_stability,'r-',label='Beta Stability')
plot(Z_values,Z_values,'k-',label='N=Z')
legend()   
ylabel('Proton number(Z)',size=12)
xlabel('Neutron number(N)',size=12)
title('Nuclear drip lines and Beta stability curve (Using Liquid drop model)',size=18)
grid()
savefig('Driplines (ldm).png',dpi=400)
show()                      

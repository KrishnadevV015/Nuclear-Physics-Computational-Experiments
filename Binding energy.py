#Binding Energy curve
from numpy import arange
from matplotlib.pyplot import plot,xlabel,ylabel,legend,title,grid,show,figure,savefig
import sys


#Defining the parameters
a_volume=14.1
a_surface=13.0
a_c=0.595
a_asym=19.0

def zmin(A): #to select the Z value with maximum BE for an A value
    z=round((A/2)*(1/(1+0.25*(a_c/a_asym)*A**(2/3))))
    return z

def BE(A): #To define Binding energy
    z=zmin(A)
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
    E=(E_volume+E_surface+E_col+E_sym+E_par)
    
    return E_volume,E_surface,E_col,E_sym,E_par, E #returns all 6 energy values

A_values=arange(1,294,1,dtype=int) #Array with A values

EVol=[]#List to store volume contribution
ESur=[]#List to store Surface contribution
ECol=[]#List to store coloumbic contribution
Esym=[]#List to store Asymmetric contribution
Epar=[] #list to store pairing contribution
be=[] #list to store binding energy
for A in A_values: #to find Each energy contribution per nucleon
    ev,es,ecol,esym,epar,ben=BE(A)/A
    be.append(ben)
    EVol.append(ev)
    ESur.append(es)
    ECol.append(ecol)
    Esym.append(esym)
    Epar.append(epar)
#to plot respective energy contributions against A
figure(figsize=(12,8))
plot(A_values,EVol)
plot(A_values,ESur)
plot(A_values,ECol)
plot(A_values,Esym)
plot(A_values,Epar)
plot(A_values,be)

legend(['$E_{Volume}$','$E_{Surface}$','$E_{Coulomb}$','$E_{Asymmetry}$','$E_{Pairing}$','Binding energy per nucleon'])
grid()
xlabel('A (Mass number)',size=12)
ylabel('Binding energy per nucleon (in MeV)',size=12)
title('Binding Energy Curve-Liquid Drop Model',size=18)
savefig('Binding energy curve.png')
show()

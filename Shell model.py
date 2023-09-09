#shell model
from numpy import arange,linspace,array
from matplotlib.pyplot import hlines, show,text,xticks,yticks,figure,savefig,title,ylabel
import sys

figure(figsize=(6,15))
#defining parameters 
hw=1 #setting h_cross_omega=1
D=-0.0225*hw
C=-0.1*hw

#Defining harmonic energy term
def harmonic(N):
    return (N+3/2)*hw

#Defining Centrifugal energy term
def centrifugal(l):
    return D*l*(l+1)

#Defining spin orbit coupling term
def spinorb(l,s):
    if s==+1/2:
        ldots=l/2
    if s==-1/2:
        ldots=-(l+1)/2
    return C*ldots

def L(N): #To generate l values corresponing to each N
    if N%2==0:
        return arange(0,N+1,2)
    if N%2==1:
        return  arange(1,N+1,2)
    
def j(l,s): #To label each energy level including all 3 terms
    J=(l+s)
    return int(2*J)

S=[-1/2,1/2] #List with 2 possible values of spin, plus half and minus half

def E(N,l,s): #Defining total energy
    return harmonic(N)+centrifugal(l)+spinorb(l,s)

def n(N,l): # n to label
    return int((N-l+2)/2)

SY=['s','p','d','f','g','h','i']#list contatining letters corresponing to different l values

colors=['olive','green','orange','cyan','blue','purple','grey'] #list containing colors, each color is to be given to levels with same l value
label_coordinates=[3.1,3.4,3.7,4,4.3,4.6,4.9,5.2] #list containing x coordinates where we have to add the label for each level, each coordinate is to lebel levels with same l value

N_values=arange(0,6,1) #List of Harmonic quantum numbers

for N in N_values: #to genrate Harmonic energy term
    l_valus=L(N)
    Eh=harmonic(N)
    hlines(y=Eh,xmin=1,xmax=2)
    text(1,Eh,'N={}'.format(N))
    
    for l in l_valus:   #to genrate Harmonic energy term + centrifugal energy term
        sym=SY[l]
        Ec=(harmonic(N)+centrifugal(l))
        hlines(y=Ec,xmin=2.1,xmax=3,color=colors[l])
        text(2.2,Ec,'l={}'.format(l))
        
        
        #The 
        if l==0: #to genrate Harmonic energy term + centrifugal energy term + spin orbit coupling term for zero l
            s=1/2
            Eso=E(N,l,s)
            hlines(y=Eso,xmin=3.1,xmax=5.3,color=colors[l] )
            text(label_coordinates[l],Eso, '{}{}{}/2'.format(n(N,l),sym,j(l,s)))
        
        #to genrate Harmonic energy term + centrifugal energy term + spin orbit coupling term for non-zero ls
        
        if l!=0:
            for s in S: 
                Eso=E(N,l,s)
                hlines(y=Eso,xmin=3.1,xmax=5.3 ,color=colors[l] )
                text(label_coordinates[l],Eso, '{}{}{}/2'.format(n(N,l),sym,j(l,s)))
                
       
title('Shell Model',size=18)
ylabel('Energy levels',size=12)
xticks([])
yticks([])
savefig('Shellmodel.png',dpi=300)
show()

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

SY=['s','p','d','f','g','h','i'] #list contatining letters corresponing to different l values

N_values=arange(0,6,1) #List of Harmonic quantum numbers

for N in N_values: #to genrate Harmonic energy term
    l_valus=L(N)
    Eh=harmonic(N)
    hlines(y=Eh,xmin=1,xmax=2)
    text(1,Eh,'N={}'.format(N))
    
    for l in l_valus:   #to genrate Harmonic energy term + centrifugal energy term
        sym=SY[l]
        Ec=(harmonic(N)+centrifugal(l))
        hlines(y=Ec,xmin=2.1,xmax=3)
        text(2.2,Ec,'l={}'.format(l))
        
        
        #The 
        if l==0: #to genrate Harmonic energy term + centrifugal energy term + spin orbit coupling term for zero l
            s=1/2
            Eso=E(N,l,s)
            hlines(y=Eso,xmin=3.1,xmax=5.1,color='olive' )
            text(3.1,Eso, '{}{}{}/2'.format(n(N,l),sym,j(l,s)))
        
        #to genrate Harmonic energy term + centrifugal energy term + spin orbit coupling term for non-zero ls
        #Separate if conditions are given for separate l values to make plot with different colors and label the levels at different coordinates in order to be able to distinguish the levels better 
        if l==1:
            for s in S: 
                Eso=E(N,l,s)
                hlines(y=Eso,xmin=3.1,xmax=5.1 ,color='green')
                text(3.3,Eso, '{}{}{}/2'.format(n(N,l),sym,j(l,s)))
                
        if l==2:
            for s in S:
                Eso=E(N,l,s)
                hlines(y=Eso,xmin=3.1,xmax=5.1,color='orange' )
                text(3.5,Eso, '{}{}{}/2'.format(n(N,l),sym,j(l,s)))
                
        if l==3:
            for s in S:
                Eso=E(N,l,s)
                hlines(y=Eso,xmin=3.1,xmax=5.1 ,color='black')
                text(3.7,Eso, '{}{}{}/2'.format(n(N,l),sym,j(l,s)))
                
        if l==4:
            for s in S:
                Eso=E(N,l,s)
                hlines(y=Eso,xmin=3.1,xmax=5.1,color='blue' )
                text(3.9,Eso, '{}{}{}/2'.format(n(N,l),sym,j(l,s)))
                
        if l==5:
            for s in S:
                Eso=E(N,l,s)
                hlines(y=Eso,xmin=3.1,xmax=5.1 ,color='purple')
                text(4.3,Eso, '{}{}{}/2'.format(n(N,l),sym,j(l,s)))
                
        if l==6:
            for s in S:
                Eso=E(N,l,s)
                hlines(y=Eso,xmin=3.1,xmax=5.1,color='grey' )
                text(4.5,Eso, '{}{}{}/2'.format(n(N,l),sym,j(l,s)))
                
        if l==7:
            for s in S:
                Eso=E(N,l,s)
                hlines(y=Eso,xmin=3.1,xmax=5.1,color='cyan' )
                text(4.7,Eso, '{}{}{}/2'.format(n(N,l),sym,j(l,s)))
                
title('Shell Model')
ylabel('Energy levels')
xticks([])
yticks([])
savefig('Shellmodel.png',dpi=300)
show()
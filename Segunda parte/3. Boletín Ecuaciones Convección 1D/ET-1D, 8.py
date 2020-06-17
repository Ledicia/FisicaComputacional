# -*- coding: utf-8 -*-
"""
Created on Mon May 07 19:16:46 2018

@author: Ledicia Díaz 
"""

import numpy as np
import matplotlib.pyplot as plt

u=1;alfa=1; dt=0.001; dx=0.5; N=20; C=u*dt/dx; s=alfa*dt/dx**2

print 'C', C
print 's', s 

if  C<=1:
    print 'el método es estable'
else:
    print 'el método es inestable'
    
Told=np.zeros(N+1); Told[9:12]=10
T=np.zeros(N+1); T[9:12]=10
Tnew=np.zeros(N+1)

for n in range(2000):
    for i in range (1,N):
        Tnew[i]=(C/(1.+2.*s))*(T[i-1]-T[i+1])+(2.*s/(1.+2.*s))*(T[i-1]-Told[i]+T[i+1])+Told[i]/(1.+2.*s)
    
    Tnew[0]=0.
    Tnew[N]=0.
    Told=np.copy(T)
    T=np.copy(Tnew)
    
    if n%10==0:
        plt.plot(T)
        plt.pause(0.01)
        plt.show()
        
    
        
if 2*alfa*C**2/u**2*(T[i+2]-2*T[i]+T[i-2])<1:
    print  2*alfa*C**2/u**2*(T[i+2]-2*T[i]+T[i-2])
    print 'el método es consistente'
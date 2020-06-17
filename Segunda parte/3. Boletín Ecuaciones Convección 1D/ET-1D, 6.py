# -*- coding: utf-8 -*-
"""
Created on Thu May 03 13:28:13 2018

@author: Ledicia Díaz
"""

import numpy as np
import matplotlib.pyplot as plt

u=0.5;alfa=1; dt=0.01; dx=0.5; N=20; C=u*dt/dx; s=alfa*dt/dx**2

print 'C', C
print 's', s 

if  C**2<=2*s<=1:
    print 'el método es estable'
else:
    print 'el método es inestable'
    
T=np.zeros(N+1); T[9:11]=10
Tnew=np.zeros(N+1)

for n in range(2000):
    for i in range (1,N):
        Tnew[i]=(C/2.)*(T[i-1]-T[i+1])+s*(T[i-1]-2*T[i]+T[i+1])+T[i]
    Tnew[0]=0.
    Tnew[N]=0.
    T=np.copy(Tnew)
    
    if n%10==0:
        plt.plot(T)
        plt.pause(0.01)
        plt.show()

        
# -*- coding: utf-8 -*-
"""
Created on Mon May 07 18:47:25 2018

@author: Ledicia Díaz
"""

import numpy as np
import matplotlib.pyplot as plt

u=0.2;alfa=0.05; dt=0.001; dx=0.9; N=20; C=u*dt/dx; s=alfa*dt/dx**2

print 'C', C
print 's', s 

if  C+2*s<=1:
    print 'el método es estable'
else:
    print 'el método es inestable' 

T=np.zeros(N+1); T[9:12]=10
Tnew=np.zeros(N+1)

for n in range(2000):
    for i in range (2,N+1):
        Tnew[i]=C*(T[i-1]-T[i])+s*(T[i]-2*T[i-1]+T[i-2])+T[i]
    Tnew[0]=0.
    Tnew[N]=0.
    T=np.copy(Tnew)
    if n%10==0:
        plt.plot(T)
        plt.pause(0.01)
        plt.show()
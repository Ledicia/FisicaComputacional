# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 12:33:21 2018

@author: Ledicia Díaz, control ecuaciones de difusión en 1D 
"""
import numpy as np
import matplotlib.pyplot as plt

alfa=1.; dt=0.01; dx=0.5; N=20

Told=np.zeros(N+1); Told[0:N]=0
T=np.zeros(N+1); T[0:N]=0
Tnew=np.zeros(N+1)

for n in range(1000):
    for i in range(1,N): #para que no coja ni el elemento 0 ni el N, ya que vienen determinados por las condiciones de frontera
        Tnew[i]=(2/3.)*(alfa*dt/dx**2)*(T[i+1]-2*T[i]+T[i-1])+(1/3.)*(4*T[i]-Told[i])
        
    Tnew[0]=10
    Tnew[N]=5
    Told=np.copy(T)
    T=np.copy(Tnew)
    if n%10==0:
        plt.figure(1)
        plt.plot(T)
        plt.show()
        plt.xlabel('i-indice')
        plt.ylabel('Temperatura')
        
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:21:14 2018

@author: Ledicia Díaz
"""

import numpy as np
import matplotlib.pyplot as plt

alfa=1.; dt=0.01; dx=0.5; N=20

Told=np.zeros(N+1); Told[9:11]=10
T=np.zeros(N+1); T[9:11]=10
Tnew=np.zeros(N+1)

for n in range(1000):
    for i in range(1,N): #para que no coja ni el elemento 0 ni el N, ya que vienen determinados por las condiciones de frontera
        Tnew[i]=(2*s/(1+2*s))*(T[i-1]+T[i+1])+((1-2*s)/(1+2*s))*Told[i]
        
    Tnew[0]=5
    Tnew[N]=3
    Told=np.copy(T)
    T=np.copy(Tnew)
    if n%10==0:
        plt.figure(1)
        plt.plot(T)
        plt.show()
        plt.xlabel('i-indice')
        plt.ylabel('Temperatura')
        
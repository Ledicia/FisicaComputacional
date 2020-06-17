# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 13:23:48 2018

@author: Ledicia Díaz
"""

import numpy as np
import matplotlib.pyplot as plt

N=20
dimt=1000
deltat=0.1; deltax=0.5; alfa=1; 
T=np.zeros(N+1)
Tnew=np.zeros(N+1)
T[9:11]=10
plt.close('all')

for n in range(dimt):
    for i in range(1,N):
        Tnew[i]=T[i]+alfa*deltat/deltax/deltax*(T[i+1]-2.*T[i]+T[i-1])
    #condiciones frontera    
    Tnew[0]=5
    Tnew[N]=3
    for i in range(0,N+1): #actualización de variables
        T[i]=Tnew[i]    
    if n%10==0: #cuando el resto de n entre 10 es igual a cero el bucle se activa (asi dibuja solo para n múltiplo de 10)
        plt.figure(1);
        plt.plot(T)
        plt.pause(0.01)
        plt.show

plt.xlabel('i-indice')
plt.ylabel('Tiempo')
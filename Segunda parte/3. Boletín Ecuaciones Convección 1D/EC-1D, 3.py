# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 13:21:31 2018

@author: Ledicia Díaz
"""

import numpy as np
import matplotlib.pyplot as plt

N=20
dimt=100
deltat=0.01; deltax=0.5; u=1.;t=0.
C=u*(deltat/deltax)

Told=np.zeros(N+1); Told[9:12]=10
T=np.zeros(N+1); T[9:11]=10
Tnew=np.zeros(N+1)

plt.close('all')
#plt.pause(0.01)

for n in range(dimt):
    for i in range(1,N): #para que no me coja los elementos 0 ni N ya que vienen fijados por la condición de frontera
        Tnew[i]=Told[i]-C*(T[i+1]-T[i-1])
        
    Tnew[0]=1
    Tnew[N]=4
    
    Told=np.copy(T)
    T=np.copy(Tnew) 
    
    if n%1==0: #cuando el resto de n entre 10 es igual a cero el bucle se activa (asi dibuja solo para n múltiplo de 10)
        plt.figure(1);
        plt.plot(T)
        plt.pause(0.01)
        plt.show

plt.xlabel('i-indice')
plt.ylabel('Tiempo')
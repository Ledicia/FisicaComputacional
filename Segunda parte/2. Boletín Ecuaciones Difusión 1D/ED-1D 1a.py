# -*- coding: utf-8 -*-
"""
Created on Thu Apr 05 12:52:55 2018

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
    for i in range(1,N): #para que no me coja los elementos 0 ni N ya que vienen fijados por la condición de frontera
        Tnew[i]=T[i]+alfa*deltat/deltax/deltax*(T[i+1]-2.*T[i]+T[i-1])
        
    Tnew[0]=0
    Tnew[N]=10
    for i in range(0,N+1):
        T[i]=Tnew[i]    
    if n%10==0: #cuando el resto de n entre 10 es igual a cero el bucle se activa (asi dibuja solo para n múltiplo de 10)
        plt.figure(1);
        plt.plot(T)
        plt.pause(0.01)
        plt.show

plt.xlabel('i-indice')
plt.ylabel('Tiempo')
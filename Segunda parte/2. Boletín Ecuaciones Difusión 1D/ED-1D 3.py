# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 13:06:00 2018

@author: Ledicia Díaz
"""


import numpy as np
import matplotlib.pyplot as plt
dimt=1000
N=20
deltat=0.01
deltax=0.5
alfa=1

T=np.zeros(N+1)
Tnew=np.zeros(N+1)

T[9:11]=10
plt.close('all')

for n in range(dimt):
    for i in range(2,N-1): #para que no me coja los elementos 0, 1 ni N-1, N, ya que vienen fijados por la condición de frontera
        Tnew[i]=T[i]+((alfa*deltat)/(deltax**2))*(((-1./12.)*T[i-2])+((4./3.)*T[i-1])-(2.5*T[i])+((4./3.)*T[i+1])-((1./12.)*T[i+2]))
        
    Tnew[1]=Tnew[2]
    Tnew[0]=Tnew[1]
    Tnew[N-1]=Tnew[N-2]
    Tnew[N]=Tnew[N-1]
    
    
    T=np.copy(Tnew)
    if n%10==0:#cuando el resto de n entre 10 es igual a cero el bucle se activa (asi dibuja solo para n múltiplo de 10)
        plt.figure(1);
        plt.figure(1)
        plt.plot(T)
        plt.pause(0.01)
        plt.show
        
plt.xlabel
plt.ylabel
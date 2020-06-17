# -*- coding: utf-8 -*-
"""
Created on Fri May 11 10:55:25 2018

@author: Ledicia Díaz
"""

import numpy as np
import matplotlib.pyplot as plt

u=0.5; alfa=0.2; dt=0.001; dx=0.1; N=20; C=u*dt/dx; s=(alfa*dt)/(dx**2)

A=np.zeros((N+1,N+1))
T=np.zeros((N+1,1)); T[0:3]=10
Tnew=np.zeros((N+1,1))


for i in xrange(1,N):
    A[i,i]=1.+2.*s
    A[i,i-1]=-C*(1/2.)-s
    A[i,i+1]=C*(1/2.)-s

#Definimos los elementos de la matriz que no cumplen las igualdades anteriores:
A[0,0]=1.
A[N,N]=1.

Ainv=np.linalg.inv(A) #invertimos la matriz A

for n in range(1000):
    Tnew=np.dot(Ainv,T)
    
    Tnew[0]=0
    Tnew[N]=0
    T=np.copy(Tnew)
    if n%10==0:
        plt.figure(1); #abre una figura
        plt.plot(T)
        plt.show()


 

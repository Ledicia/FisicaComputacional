# -*- coding: utf-8 -*-
"""
Created on Fri May 11 10:33:39 2018

@author: Ledicia Díaz
"""

import numpy as np
import matplotlib.pyplot as plt

u=0.5; dt=0.0001; dx=0.1; N=20; C=u*dt/dx

A=np.zeros((N+1,N+1))
T=np.zeros((N+1,1)); T[0:3]=10
Tnew=np.zeros((N+1,1))


A=np.zeros((N+1,N+1))
B=np.zeros((N+1,N+1))
T=np.zeros((N+1,1)); T[0:3]=10
Tnew=np.zeros((N+1,1))


for i in xrange(1,N):
    A[i,i]=1.
    A[i,i-1]=-C*(1/4.)
    A[i,i+1]=C*(1/4.)

#Definimos los elementos de la matriz que no cumplen las igualdades anteriores:
A[0,0]=1.
A[N,N]=1.

Ainv=np.linalg.inv(A) #invertimos la matriz A

for i in xrange(1,N):
    B[i,i]=1.
    B[i,i-1]=C*(1/4.)
    B[i,i+1]=-C*(1/4.)

#Definimos los elementos de la matriz que no cumplen las igualdades anteriores:
B[0,0]=1.
B[N,N]=1.

for n in range(1000):
    Tnew=np.dot(np.dot(Ainv,B),T)
    
    Tnew[0]=0
    Tnew[N]=0
    T=np.copy(Tnew)
    if n%10==0:
        plt.figure(1); #abre una figura
        plt.plot(T)
        plt.show()


 

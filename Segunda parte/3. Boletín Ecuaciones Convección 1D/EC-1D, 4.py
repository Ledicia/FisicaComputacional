# -*- coding: utf-8 -*-
"""
Created on Thu May 03 12:50:46 2018

@author: Ledicia Díaz
"""

import numpy as np
import matplotlib.pyplot as plt

u=1; dt=0.01; dx=0.5; N=20; C=u*dt/dx

#queremos un esquema implícito a dos niveles:
A=np.zeros((N+1,N+1))
T=np.zeros(N+1); T[0:3]=10
Tnew=np.zeros(N+1)


for i in xrange(1,N):
    A[i,i]=1.
    A[i,i-1]=-C*0.5
    A[i,i+1]=C*0.5

#Definimos los elementos de la matriz que no cumplen las igualdades anteriores:
A[0,0]=1.
A[N,N]=1.

Ainv=np.linalg.inv(A) #invertimos la matriz A

for n in range(1000):
    Tnew=np.dot(Ainv,T)
    
    Tnew[0]=Tnew[1]
    Tnew[N]=Tnew[N-1]
    T=np.copy(Tnew)
    if n%10==0:
        plt.figure(1); #abre una figura
        plt.plot(T)
        plt.pause(0.01)
        plt.show()



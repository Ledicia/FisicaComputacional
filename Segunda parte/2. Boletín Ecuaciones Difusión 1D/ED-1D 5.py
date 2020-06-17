# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:04:46 2018

@author: Ledicia Díaz
"""
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as lng

alfa=1; dt=0.01; dx=0.5; N=20; s=(alfa*dt)/(dx**2)

#definimos las matrices A y B: Tnew[i]=Ainversa*B
A=np.zeros((N+1,N+1))
B=np.zeros(N+1)
T=np.zeros(N+1); T[9:11]=10.
Tnew=np.zeros(N+1)

F,C=np.shape(A)
for i in range(F):
    for j in range(C):
        if i==j:
            A[i][j]=1.+2.*s
        if np.abs(j-i)==1: #Elementos que rodean la diagonal tanto por arriba como por abajo (de ahí el valor absoluto)
            A[i][j]=-s
#Definimos los extremos de la matriz
A[0][0]=1.
A[N][N]=1.
A[0][1]=0.
A[N][N-1]=0.

B=np.array(A)
#Matriz inversa
Ainv = lng.inv(B)

for n in range(1000):
    Tnew=np.dot(Ainv,T)
    #condiciones de contorno
    Tnew[0]=5.
    Tnew[N]=3.
    
    T=np.copy(Tnew)
    if n%10==0:
        plt.figure(1)#Abre una figura
        plt.plot(T)
        plt.show()
    

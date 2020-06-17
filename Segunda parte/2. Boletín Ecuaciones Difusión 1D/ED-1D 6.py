# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 16:49:54 2018

@author: Ledicia Díaz 
"""

import numpy as np
import matplotlib.pylab as plt
import numpy.linalg as lng
alfa=1; dt=0.01; dx=0.5; N=20; s=(alfa*dt)/(dx**2)

#definimos las matrices A, B y D
A=np.zeros((N+1,N+1))
B=np.zeros(N+1)
D=np.zeros((N+1,N+1))
T=np.zeros(N+1); T[9:11]=10.
Tnew=np.zeros(N+1)


#Matriz A
F,C=np.shape(A)
for i in range(F):
    for j in range(C):
        if i==j:
            A[i][j]=1+ s
        if np.abs(j-i)==1:
            A[i][j]=-s/2
A[0,0]=1.
A[N,N]=1.
A[0,1]=0.
A[N,N-1]=0.

B=np.array(A) #El array es para que se vea en forma de matriz
#Obtengo la matriz inversa
Ainv = lng.inv(B)

#Matriz E
F,C=np.shape(D)
for i in range(F):
    for j in range(C):
        if i==j:
            D[i][j]=1.-s
        if np.abs(j-i)==1:
            D[i][j]=s/2.
D[0][0]=1.
D[N][N]=1.
D[0][1]=0.
D[N][N-1]=0.

E=np.array(D)

for n in range(1000):
    Tnew=np.dot(np.dot(Ainv,E),T)
    Tnew[0]=3.
    Tnew[N]=5.
    T=np.copy(Tnew)
    if n%10==0:
        plt.figure(1)#Abre una figura
        plt.plot(T)
        plt.show()
    
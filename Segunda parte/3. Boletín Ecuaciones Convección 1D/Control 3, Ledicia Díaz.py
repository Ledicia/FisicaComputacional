# -*- coding: utf-8 -*-
"""
Created on Tue May 08 12:16:41 2018

@author: Ledicia Díaz
"""
#Control 3, Dufort-Frankel a tres niveles completamente explícito:

import numpy as np
import matplotlib.pyplot as plt

u=0.5; alfa=0.5; dt=0.01; dx=0.9; N=20; C=u*dt/dx; s=alfa*dt/dx**2

if C<=1:
    print  'C:', C
    print 'el método es estable'
else:
    print 'el método es inestable'
    
if np.abs((u*dx**2/6.-2.*alfa**2/u))<1: 
    #lo que queremos es minimizar la expresión entre paréntesis.
    #cuando dicha expresión es aprox 1 (dx=0.1), el método no es consistente.
    print 'Coeficiente del error de truncamiento:', np.abs((u*dx**2/6.-2.*alfa**2/u))
    print 'el metodo es consistente'
    
Told=np.zeros(N+1); Told[9:11]=10; Told[0:9]=Told[11:20]=0
T=np.zeros(N+1); T[9:11]=10; T[0:9]=T[11:20]=0
Tnew=np.zeros(N+1)

for n in range(1000):
    for i in range(1,N):
        Tnew[i]=Told[i]/(1+2*s)+C/(1+2*s)*(T[i-1]-T[i+1])+(2*s/(1+2*s))*(T[i+1]-Told[i]+T[i-1])
    
    Tnew[0]=Tnew[1]
    Tnew[N]=Tnew[N-1]
    
    Told=np.copy(T)
    T=np.copy(Tnew)
    
    if n%10==0:
        plt.figure(1)
        plt.plot(T)
        plt.pause(0.01)
        plt.show()
        
plt.ylabel('T')
plt.xlabel('i-indice')

'''
Para que la solución converja el método tiene que ser estable y consistente:
    
La estabilidad del método viene dada por la condición de que C<=1. Para conseguirlo
podemos establecer un dt pequeño, y un dx más grande (ya que este esta dividiendo).

La consistencia del método consiste en minimizar el coeficiente que acompañan a la
derivada de tercer orden, para minimizar el error de truncamiento. Esto se consigue
ajustando los parámetros alfa, y u, o dándole un valor alto a dx.
Si hacemoslaprueba de poner dx=0.1<0.9, vemos que el método no es consistente.
'''
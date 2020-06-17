#Álvaro Crego Deán
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 20:00:41 2018

@author: Usuario
"""

'''
He empleado el ejericio 3 como ejemplo, por su sencillez.

Probando con esta configuración, de tal manera que la función
se va a una especie de asíntota horizontal, vemos que el deltat
crece de manera abrupta (ya que no hay cambios fuertes en la función
sino que se estabiliza, para lo cual podemos trabajar con deltat muy grandes).
Así es que, si pusiésemos N=110, el programa tardaría mucho tiempo en ejecutar ¿por qué?
porque la función se haría tan plana que el deltat crecería de manera infinita.
Por ello, he obligado a cesar un bucle while (con la función break)
cuando el deltat sea superior a un cierto límite. De esta manera salvamos
el problema de que el deltat sea infinito y el programa no se ejecute.

Por otro lado vemos que para tiempos bajos el deltat comienza a crecer (para
esta configuración de k=4) ya que la cantidad (p1-p) es cada vez menor.

Este programa sería especialmente útil para funciones que cambiasen
de manera muy abrupta en el tiempo                                                                
'''

import numpy as np
import matplotlib.pyplot as plt

N=115
deltat=10e-2
t=0
p=7.6
r=9
k=8

P=[]
T=[]
Deltat=[]

#definimos dos límites, uno superior y otro inferior.
Maxi=0.05
mini=0.001
u=0.9 #u es el valor máximo que aceptamos de deltat para que no se me vaya a infinito

for i in range(N):      
   deltat=10e-2 #cada vez que comience una iteracción, el deltat vuelve
                #a ser el original   
   p1=p+deltat*(r*p*(1-p/k))
   
   if (p1-p)>Maxi: #si la diferencia en el eje x es grande:      
        while (p1-p)>Maxi: #mientras sea más grande que nuestro límite maxi:
            deltat=deltat/2
            p1=p+deltat*(r*p*(1-p/k))
   else:
       while (p1-p)<mini:
           if deltat<u: #estos nuevos bucles son para evitar que el deltat se dispare
               deltat=2*deltat
               p1=p+deltat*(r*p*(1-p/k))
           else:
               deltat=u
               p1=p+deltat*(r*p*(1-p/k))
               break #cuando llega al límite, le obligamos a parar
           
   p=p1
   t=t+deltat
   
   P.append([p1])
   T.append([t])
   Deltat.append([deltat])         
                     
plt.figure(figsize=(4,4))    
plt.plot(T,P,'b')
plt.xlabel('tiempo')
plt.ylabel('p')

#para ver como cambia el deltat con respeto al tiempo
plt.figure(figsize=(4,4))    
plt.plot(T,Deltat, 'r') 
plt.xlabel('tiempo')
plt.ylabel('deltat')

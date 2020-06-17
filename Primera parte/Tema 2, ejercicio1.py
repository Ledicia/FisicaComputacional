# -*- coding: utf-8 -*-
"""
Created on Thu Feb 08 13:15:17 2018

@author: Ledicia Diaz
"""
import numpy as np

A = np.array([[2, -1, 1], [-1, 1, 2], [1, 2, -1]], dtype=float)
B = np.array([[3], [7], [2]], float)

A=np.array([[1,2,-3,4],[3,1,0,-2],[0,3,1,3],[-5,-2,5,2]],float)
B=np.array([[8],[-15],[22],[38]],float)
AB=np.concatenate((A,B),axis=1)


print('A', A, 'B', B, 'AB', AB)
F, C = np.shape(AB)
print(F, C)

for i in range(F-1):
    for j in range(i+1,F):
        f = AB[j, i] / AB[i, i]
        AB[j] = AB[j] - f * AB[i]
print(AB)

x = np.zeros(F, float)
for i in range (F-1,-1,-1):
    x[i]=(AB[i,F]-np.sum(AB[i,0:F]*x))/AB[i,i]
print(x)

for i in range(len(x)):
    print('x%.0f= %f' %(i+1, x[i]))

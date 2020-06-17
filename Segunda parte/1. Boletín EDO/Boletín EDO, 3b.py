# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 17:48:52 2018

@author: Ledicia Díaz
"""
import numpy as np
import matplotlib.pyplot as plt

delta_t=0.1
r=1
P=10
k=1000
t=1
for i in range (100):
    t=delta_t+t
    k1=delta_t*(r*P*(1-P/k))
    k2=delta_t*(r*(P+k1/2)*(1-(P+k1/2)/k))
    P=P+k2
    plt.plot(t,P,"*")
    
'''

'''
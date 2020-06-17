# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 17:59:26 2018

@author: Ledicia Díaz
"""
import numpy as np
import matplotlib.pyplot as plt

delta_t=0.01
r=3
P=10
k=1
t=1
for i in range (1000):
    t=delta_t+t
    k1=delta_t*(r*P*(1-P/k))
    k2=delta_t*(r*(P+k1/2)*(1-(P+k1/2)/k))
    k3=delta_t*(r*(P+k2/2)*(1-(P+k2/2)/k))
    k4=delta_t*(r*(P+k3)*(1-(P+k3)/k))
    x=P+(k1/6)+(k2/3)+(k3/3)+(k4/6)
    P=x
    plt.plot(t,P,"*")

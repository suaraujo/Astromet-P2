#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 12:26:59 2018

@author: susana
"""

import numpy as np
import matplotlib.pyplot as plt

o=input('incerte el parametro sigma:')
N=input('cantidad de valores a probar:')
x=np.zeros(N,dtype=float)
espe=0
espe=float(espe)
o=float(o)

    
f=np.random.rand(N)

print(f)
#def inversa(o,f):
#    v=o*np.log(np.log(1/1-f))
#    return v

for i in range (N):
    espe=espe+f[i]
    
x=o*np.log(np.log(1/(1-f)))
print x

espe=espe/N
print('el valor esperado de f=') 
print espe

#plt.scatter(x,f)
plt.show

plt.hist(x,N,color='c')
plt.show


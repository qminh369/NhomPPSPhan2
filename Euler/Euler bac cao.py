from sympy import *
import numpy as np 
import math 
from pylab import * 
import matplotlib.pyplot as plt 

x0 = 0
X = 1
h = 0.1
m = 2
n = int((X-x0)/h)
y = np.zeros(n+1, dtype= float)
y[0] = 2
y[1] = 1

def H(x, f = np.zeros(n+1, dtype = float)):
    return -2 * f[0] - 2 * f[1] 

def G(x):
    return math.exp(-x) * (2*cos(x) + 3*sin(x))

def Eulerhien_baccao(x0, X, h, y, m):
  n = int((X-x0) / h)
  a = np.zeros(n+1, dtype= float)
  a1 = np.zeros(n+1, dtype= float)
  z = np.zeros(n+1, dtype= float)
  x = x0
  z = y
  for i in range(n+1):
    a[i] = z[0]
    for j in range(m-1):
        z[j] = z[j] + h * z[j+1]
    z[m-1] = z[m-1] + h * H(x,z)
    x = x+h
  print(" \n   x         y      g(x)        ss")
  for i in range(n+1):
    a1[i] = x0 + i*h
    print("%-7.6f   %-7.6f  %-7.6f  %-7.6f \n" %(a1[i],a[i],G(a1[i]),math.fabs(G(a1[i]) - a[i]))) 
    
Eulerhien_baccao(x0,X,h,y,m)
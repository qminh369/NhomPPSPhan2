import numpy as np
import math 
import matplotlib.pyplot as plt 

def euler_hien(x0, y0, X, h):
    n = int((X - x0) / h)
    a = np.zeros(n+1, dtype = float)
    a1 = np.zeros(n+1, dtype = float)
    x = x0
    y = y0 
    for i in range(n+1):
        a[i] = y
        y = y + h * F(x, y)
        x = x + h
        
    print('\n x         y         g(x)          ss')
    for i in range(n+1):
        a1[i] = x0 + i * h 
        print("%-7.1f   %-7.4f  %-7.4f  \t%-7.4f \n" %(a1[i],a[i],G(a1[i]),math.fabs(G(a1[i]) - a[i])))
    
def euler_an(x0, y0, X, h):
    n = int((X-x0) / h)
    a = np.zeros(n+1, dtype= float)
    a1 = np.zeros(n+1, dtype= float)
    x = x0
    y = y0
    for i in range(n+1):
        a[i] = y
        I = h * F(x + h, y + h*F(x, y))
        x = x + h
        y = y + I
        
    print('\n x         y         g(x)          ss')
    for i in range(n+1):
      a1[i] = x0 + i*h
      print("%-7.1f   %-7.4f  %-7.4f  \t%-7.4f \n" %(a1[i],a[i],G(a1[i]),math.fabs(G(a1[i]) - a[i])))
    
def Hinhthang(x0, y0, X, h):
    n = int((X-x0) / h)
    a = np.zeros(n+1, dtype= float)
    a1 = np.zeros(n+1, dtype= float)
    x = x0
    y = y0
    for i in range(n+1):
      a[i] = y
      I  = (h/2) * (F(x, y) + F(x + h, y + h*F(x, y)))
      x = x + h
      y = y + I
      
    print('\n x         y         g(x)          ss')
    for i in range(n+1):
        a1[i] = x0 + i*h
        print("%-7.6f   %-7.6f  %-7.6f  %-7.6f \n" %(a1[i],a[i],G(a1[i]),math.fabs(G(a1[i]) - a[i])))  

def F(x, y):
    return (x * y) / 2

def G(x):
    return math.exp(math.pow(x,2)/2)

if __name__ == '__main__':
    x0 = 0
    y0 = 1
    X = 1
    h = 0.1

    print('Euler hien:')
    euler_hien(x0, y0, X, h)
    print('\n')
    print('Euler an:')
    euler_an(x0, y0, X, h)
    print('PP hinh thang:')
    Hinhthang(x0, y0, X, h)
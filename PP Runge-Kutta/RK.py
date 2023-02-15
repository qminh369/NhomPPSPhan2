import numpy as np
import matplotlib.pyplot as plt
import math

def F(x, y):
    return x + y

def RK1(x0, X, y0, N):
    result = []
    h = (X-x0) / (N-1)
    result.append(y0)
    for i in range(1, N):
        y0 = y0 + h * F(x0, y0)
        result.append(y0)
        x0 += h
    return result 

def RK2(x0, X, y0, N):
    result = []
    h = (X - x0) / (N - 1)
    result.append(y0)
    for i in range(1, N):
        y_temp = y0 + h * F(x0, y0)
        y0 = y0 + (h/2) * (F(x0, y0) + F(x0+h, y_temp))
        result.append(x0)
        x0 += h 
    return result

def RK3(x0, X, y0, N):
    result = []
    result.append(y0)
    h = (X- x0) / (N - 1)
    for i in range(1, N):
        k1 = h * F(x0, y0)
        k2 = h * F(x0 + h/2, y0 + k1/2)
        k3 = h * F(x0 + h, y0 - k1 + 2 * k2)
        y0 = y0 + (k1 + 4 * k2 + k3) / 6
        result.append(y0)
        x0 += h 
    return result 

def RK4(x0, X, y0, N):
    result = []
    result.append(y0)
    h = (X- x0) / (N - 1)
    for i in range(1, N):
        k1 = h * F(x0, y0)
        k2 = h * F(x0 + h/2, y0 + k1/2)
        k3 = h * F(x0 + h/2, y0 + k2/2)
        k4 = h * F(x0 + h, y0 + k3)
        y0 = y0 + (k1 + 2*k2 + 2*k3 + k4) / 6
        result.append(y0)
        x0 += h 
    return result 

if __name__ == "__main__":
    x0 = 0
    y0 = 1
    N = 6
    X = 0.5
    
    rk1 = RK1(x0, X, y0, N)
    rk2 = RK2(x0, X, y0, N)
    rk3 = RK3(x0, X, y0, N)
    rk4 = RK4(x0, X, y0, N)
    
    print("rk1 : {} \n".format(rk1))
    print("rk2 : {} \n".format(rk2))
    print("rk3 : {} \n".format(rk3))
    print("rk4 : {} \n".format(rk4))
import numpy as np 
import matplotlib.pyplot as plt 

def f(x, y):
    # return x**2 + y**2
    return (x + 2*y) / (x**2 + 2 * y**2)
def AB_AM(x0, y0, xf, n):
    h = (xf - x0) / (n - 1)
    x= np.linspace(x0, xf, n)
    y = np.zeros([n])
    y[0] = y0 
    py = np.zeros([n])
    for i in range(0, 4):
        py[i] = None 
    
    for i in range(1, 4):
        k1 = h * f(x[i-1], y0)
        k2 = h * f(x[i-1] + h/2, y0 + k1/2)
        k3 = h * f(x[i-1] + h/2, y0 + k2/2)
        k4 = h * f(x[i-1] + h, y0 + k3)
        y[i] = y0 + (k1 + 2*k2 + 2*k3 + k4) / 6
        y0 = y[i]
    
    for i in range(4, n):
        py[i] = h/24*(55*f(x[i-1], y[i-1]) - 59*f(x[i-2], y[i-2]) + 37*f(x[i-3], y[i-3]) - 9*f(x[i-4], y[i-4])) + y[i-1] 
        y[i] = h/24*(9*f(x[i], py[i]) + 19*f(x[i-1], y[i-1]) - 5*f(x[i-2], y[i-2]) + f(x[i-3], y[i-3])) + y[i-1]
      
    print("x_n\t\tpy_n(Du bao)\t\ty_n(Hieu chinh)")
    for i in range(n):
        print(format(x[i],'6f'),"\t",format(py[i],'8f'),"\t\t",format(y[i],'8f'))
 
if __name__ == '__main__':
    x0 = 0
    y0 = 0
    xf = 1 
    n = 11
    
    x0 = 0
    y0 = 1
    xf = 3
    n = 4
    
    x0 = 0
    y0 = 1
    xf = 3
    n = 31
    AB_AM(x0, y0, xf, n)
     
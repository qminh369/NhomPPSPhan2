import numpy as np
import matplotlib.pyplot as plt 

def input_data():
    x, y = [], []
    with open('F:\\OneDrive - Hanoi University of Science and Technology\\Desktop\\PPSPhan2\\Spline\\input.txt', 'r') as file:
        for line in file:
            # print(line)
            _x, _y = line.split(' ')
            x.append(float(_x))
            y.append(float(_y))
      
    x = np.asarray(x)
    y = np.asarray(y)
    n = len(x) - 1
    return x, y, n

def spline1(k, x0):
    x, y, n = input_data()
    h = np.diff(x)
    if k == 1:
        for i in range(1, n+1):
            print('S1' + '[' + str(x[i-1]) + ', ' + str(x[i]) + '] = '+ str(round(y[i-1]/h[i-1],3)) + '(' + str(x[i]) + '-x)' + ' + ' + str(round(y[i]/h[i-1],3)) + '(x-' + str(x[i-1]) + ')')
    for i in range(1, n+1):
        if x[i-1] <= x0 and x0 <= x[i]:
            s1 = y[i-1] / h[i-1] * (x[i] - x0) + y[i] / h[i-1] * (x0 - x[i-1])

    return s1

def spline2(k, x0):
    x, y, n = input_data()
    h = np.diff(x) 
    m = np.empty(n+1)
    m[0] = (y[1] - y[0]) / h[0]
    for i in range(1, n+1):
        m[i] = 2 / h[i-1] * (y[i] - y[i-1]) - m[i-1]
    if k==1:
        for i in range(1, n+1):
            print('S2' + '[' + str(x[i-1]) + ', ' + str(x[i]) + '] = ' + str(round(-m[i-1] /2 / h[i-1],3)) + '(' + str(x[i]) + '-x)^2 + ' + str(round(m[i] / 2/ h[i-1],3)) + '(x-' + str(x[i-1])+ ')^2' + ' + ' + str(round(y[i] - m[i] / 2 * h[i-1],3)))
    for i in range(1,n+1):
        if x[i-1] <= x0 and x0 <= x[i]:
            s2 = -m[i-1] / 2 /h[i-1] * (x[i] - x0) **2 + m[i] / 2 / h[i-1] * (x0 - x[i-1]) ** 2 + y[i] - m[i] / 2 * h[i-1]
    return s2

def spline3(k,x0):
    x, y, n = input_data()
    h = np.diff(x)
    # Duoi day la ham tính m
    def tinhM(x,y,n):
        m = np.empty(n+1)
        d = np.empty(n+1)
        anpha = np.empty(n+1)
        beta = np.empty(n+1)
        muy = np.empty(n+1)
        lamda = np.empty(n+1)
        h = np.diff(x)
        dh0 = (y[1]-y[0]) / (x[1]-x[0])
        dhn = (y[n]-y[n-1]) / (x[n]-x[n-1])
        d[0] = 6 / h[0] * ((y[1]-y[0]) /h[0] - dh0)
        d[n] = 6 / h[n-1] * (dhn - (y[n]-y[n-1]) / h[n-1])
        anpha[1] = 1/(-2)
        beta[1] = d[0] / 2
        for i in range(1,n):
            d[i] = 6 * ((y[i+1]-y[i]) /h[i] -(y[i]-y[i-1]) /h[i-1]) / (h[i] + h[i-1])
        for i in range(1,n):
            muy[i] = h[i-1] / (h[i-1]+h[i])
            lamda[i] = h[i] / (h[i-1]+h[i])
        for i in range(1,n):
            anpha[i+1] = lamda[i] / (-2-anpha[i]*muy[i])
            beta[i+1] = (muy[i]*beta[i]-d[i]) / (-2-anpha[i]*muy[i])
        m[n] = (1*beta[n]-d[n]) / (-2-1*anpha[n])
        for i in range(n-1,-1,-1):
            m[i] = anpha[i+1] * m[i+1] + beta[i+1]
        return m
    m = tinhM(x,y,n)
    if k==1:
        for j in range(1,n+1):
            print('S3' +'['+ str(x[j-1])+','+str(x[j])+']'+' = ' + str(round(m[j - 1] / (6 * h[j - 1]),3)) + '(' + str(x[j]) + '- x)^3' +
                  ' + ' + str(round(m[j] / (h[j - 1] * 6),3)) + '(x-' + str(x[j - 1]) + ')^3' +
                  ' + ' + str(round((1 / h[j - 1]) * (y[j - 1] - m[j - 1] / 6 * h[j - 1] ** 2),3)) + '(' + str(x[j]) + '-x)' +
                  ' + ' + str(round((y[j] - (m[j] / 6) * h[j - 1] ** 2) / h[j - 1],3)) + '(x-' + str(x[j - 1]) + ')')
    for i in range(1,n+1):
        if x[i-1] <=x0 and x0 <= x[i]:
            s3 = m[i-1] / (6*h[i-1]) * (x[i]-x0)**3 + m[i] / (h[i-1]*6) *(x0-x[i-1])**3 + (1/h[i-1]) * (y[i-1]-m[i-1]/6*h[i-1]**2) * (x[i]-x0) + (y[i]-(m[i]/6) * h[i-1]**2) * (x0-x[i-1]) / h[i-1]
    return s3


x, y, n = input_data()

print('Các đa thức spline bậc 1: \n')
spline1(1, x[0])
print('\n' * 2)
print('Các đa thức spline bậc 2: \n')
spline2(1, x[0])
print('\n' * 2)
print('Các đa thức spline bậc 3: \n')
spline3(1, x[0])

def graphic():
    x0 = np.linspace(x[0], x[n], 1000)
    y1 = []
    y2 = []
    y3 = []
    for i in x0:
        y1.append(spline1(0,i))
        y2.append(spline2(0,i))
        y3.append(spline3(0,i))
    plt.plot(x0, y1, color = 'red', label = 'Spline bac 1')
    plt.plot(x0, y2, color = 'blue', label = 'Spline bac 2')
    plt.plot(x0, y3, color = 'yellow', label = 'Spline bac 3')
    plt.scatter(x, y, color = 'black')
    plt.legend(loc = 'upper right')
    plt.tight_layout()
    plt.show()

graphic()
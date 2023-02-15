import math
from sympy import sympify, symbols
from sympy import *

def multiply_horner(A, i) -> list:
    A.append(0)
    for j in range(len(A) - 1, 0, -1):
        A[j] = A[j] - A[j-1] * i  
    return A  

def devide_horner(A, i) -> list:
    X = A.copy()
    X.pop()
    for j in range(1, len(X)):
        X[j] = X[j] + i * X[j-1]
    return X 

def max(fx, i):
    # Tìm maximum của đạo hàm cấp i của hàm f(x)
    g = Derivative(fx, (x, i), evaluate = True)
    m1 = abs(maximum(g, x, Interval(a, b)))
    m2 = abs(minimum(g, x, Interval(a, b)))
    
    if m1 > m2:
        m = m1
    else:
        m = m2 
    return m

def poly_integral(A, a, b) -> float:
    I = 0
    for j in range(0, len(A)):
        if A[j] == 0:
            continue 
        else:
            A[j] = A[j] / (len(A) - j)
        I = I + A[j] * (b ** (len(A)-j) - a ** (len(A) - j))
    
    return I
        
def cotez_coef(i):
    X = devide_horner(D, i)
    h = (1/n) * ((-1)**(n-i)) / (math.factorial(i) * math.factorial(n-i)) * poly_integral(X, 0, n)
    
    return h

def newton_cotez() -> float:
    E = 0
    hs = [1] * (n+1)
    for i in range(n+1):
        hs[i] = cotez_coef(i)
        E = E + hs[i] * A[i]
    E = E * (b - a)
    for j in range(n+1):
        print('He so cotes ung voi n = {} : {}'.format(j, hs[j]))
    print('Tich phan tinh bang cong thuc newton - cotes: ', E)
    
def newton_cotez_error():
    g = Derivative(f, (x, n), evaluate = True)
    if n % 2 == 0:
        D1 = D.copy()
        multiply_horner(D1, n+1)
        m2 = max(g, 2)
        print('Sai so cong thuc newton-cotez: ', abs(float(m2) * poly_integral(D1, 0, n) * (h**(n+3)) / math.factorial(n+2)))
    else:
        m1 = max(g, 1)
        print('Sai so cong thuc newton-cotez: ', abs(float(m1) * poly_integral(D, 0, n) * (h**(n+2)) / math.factorial(n+1)))
    
if __name__ == '__main__':
    global a, b, D, n, A, x, f, h
    x = symbols('x')
    func = input('Nhap ham f(x): ')
    f = sympify(func)
    input_value = input('Nhap khoang lay tich phan: ')
    a, b = [float(i) for i in input_value.split(' ')]
    
    n = int(input('Nhap so khoang chia: '))
    h = (b-a) / n 
    
    D = [1]
    for i in range(n+1):
        multiply_horner(D, i)
        
    A = [f.subs(x,a+i*h) for i in range(n+1)]

    newton_cotez()
    newton_cotez_error()

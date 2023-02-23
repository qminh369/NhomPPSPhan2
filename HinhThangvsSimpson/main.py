from sympy import sympify, symbols
from sympy import *
import math

global n, h, f, a, b, eps, x, A

def trapezoidal(A):
    trape = 1/2 * (A[0] + A[n])
    for i in range(1, n):
        trape = trape + A[i]
    print('Tinh TP dung cong thuc hinh thang: ', trape * h)
    
def trapezoidal_error():
    m = max(f, 2)
    print('Sai so cua cong thuc hinh thang: ', m / 12 * (b-a) * (h**2))
    
def trapezoidal_intervals():
    m = max(f, 2)
    n = math.floor((abs(((m * (b-a)**3) * (1/12) * (1/eps)))) ** (1/2)) + 1
    print('So khoang chia can thiet cho CT hinh thang: ', n)
    
def simpson(A):
    simp = h / 3 * (A[0] + A[n])
    simp_odd = 0
    simp_even = 0
    for i in range(1, n, 2):
        simp_odd += A[i]
    for i in range(2, n, 2):
        simp_even += A[i]
    simp = simp + h / 3 * 4*simp_odd + h / 3 * 2*simp_even
    print('Tinh TP dung cong thuc simpson: ', simp)
    
def simpson_error():
    m = max(f, 4)
    print('Sai so cua cong thuc simpson: ', m / 180 * (b-a) * (h**4))
    
def simpson_intervals():
    m = max(f, 4)
    n = math.floor((abs((m * (b-a)**5) * (1/180) * (1/eps))) ** (1/4)) + 1
    if n % 2 == 1:
        print('So khoang chia can thiet cho CT simpson: ', n + 1)
    else:
        print('So khoang chia can thiet cho CT simpson: ', n + 2)
        
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

if __name__ == '__main__':
    x = symbols('x')
    func = input('Nhap ham f(x): ')
    f = sympify(func)
    input_value = input('Nhap khoang lay tich phan: ')
    a, b = [float(i) for i in input_value.split(' ')]
    q = int(input('Chọn bài toán ''\n''(1) Tính tích phân (2) Tính số khoảng chia cần thiết: '))
    if q == 1:
        n = int(input('Nhap so khoang chia: '))
        h = (b-a) / n 
        A = [f.subs(x,a+i*h) for i in range(n+1)]
        if n % 2 == 0:
            trapezoidal(A)
            trapezoidal_error()
            print()
            simpson(A)
            simpson_error()
            
        else:
            trapezoidal(A)
            trapezoidal_error()
            print()
            
    if q == 2:
        eps = float(input('Nhap epsilon: '))
        trapezoidal_intervals()
        simpson_intervals()
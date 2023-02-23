import numpy as np

def type1(p, q, f, a, b, alpha, beta, n, h):
    matrix = np.zeros((n, n))
    B = np.zeros((n, 1))
    matrix[1, 1] = matrix[n, n] = 1
    B[1, 1] = alpha 
    B[n, 1] = beta 
    
    for i in range(1, n-2):
        xi = a + i*h 
        matrix[i+1, i] = p(xi - h/2) / (h*h)
        matrix[i+1, i+1] = -(p(xi + h/2) + p(xi - h/2)) / (h*h) - q(xi)
        matrix[i+1, i+2] = p(xi + h/2) / (h*h)
        B[i+1, 1] = -f(xi)
    
    result = matrix / B
    
# if __name__ == '__main__':
    
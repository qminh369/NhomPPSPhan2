import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def input_data(file_name):
    with open(file_name) as file:
        f = file.readline()
        y_t, y_s, x_t, x_s, y0, x0, eps = [float(item) for item in file.readline().split(' ')]
    return f, y_t, y_s, x_t, x_s, y0, x0, eps





if __name__ == '__main__':
    f, Yt, Ys, Xt, Xs, y0, x0, eps = input_data('F:\\OneDrive - Hanoi University of Science and Technology\\Desktop\\PPSPhan2\\Picard\\input.txt')
    y = symbols('y')
    x = symbols('x')
    f = sympify(f)
    print(f, Yt, Ys, Xt, Xs, y0, x0, eps)
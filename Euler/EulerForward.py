def euler_forward(f, x0: float, y0: float, xn:float, h:float):
    x_list = [x0]
    y_list = [y0]
    xi = x0
    yi = y0 
    n = int((xn - x0) / h) 
    for i in range(n):
        yi = yi + h * f(xi, yi) 
        xi = x0 + h * (i+1)
        x_list.append(xi)
        y_list.append(yi)
    return x_list, y_list  
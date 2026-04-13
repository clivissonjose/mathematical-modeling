import numpy as np
import matplotlib.pyplot as plt

x0 = 5
a1 = 1.0
b1 = 0.1
c1 = 0.05

y0 = 3
a2 = 1.7
b2 = 0.1
c2 = 0.15

h = 0.01

n = int(60 / h)

#x′(t) = a1x − b1x^2 − c1xy
def f_especie1(x, y):
    derivada = a1*x - b1*x**2 - c1*x*y
    return derivada

#y′(t) = a2y − b2y^2 − c2xy
def f_especie2(x, y):
    derivada = a2*y - b2*y**2 - c2*x*y
    return derivada


def euler(x0, y0, h, n):

    y_values = [y0]
    x_values = [x0]
    x_next = x0
    y_next = y0
    
    print("Método de Euler:")

    for i in range(n):
        #print(f"x: {x_next:.2f}, y: {y_next:.4f}")
        y_next = y0 + h * f_especie2(x0, y0)
        x_next = x0 + h * f_especie1(x0, y0)
        
        x0 = x_next
        y0 = y_next

        y_values.append(y_next)
        x_values.append(x_next)

    return x_values, y_values




def runge_kutta(x0, y0, h, n):
    t_values = [0]
    y_values = [y0]
    x_values = [x0]
    x_next = x0
    y_next = y0
    print("\n\nMétodo de Runge-Kutta:")
    for i in range(n):
        

        k1 = f_especie1(x_next, y_next)  # x
        l1 = f_especie2(x_next, y_next)  # y


        k2 = f_especie1(x_next + h/2 * k1, y_next + h/2 * l1)
        l2 = f_especie2(x_next + h/2 * k1, y_next + h/2 * l1)

        k3 = f_especie1(x_next + h/2 * k2, y_next + h/2 * l2)
        l3 = f_especie2(x_next + h/2 * k2, y_next + h/2 * l2)

        k4 = f_especie1(x_next + h * k3, y_next + h * l3)
        l4 = f_especie2(x_next + h * k3, y_next + h * l3)


        x_next = x_next + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        y_next = y_next + (h/6)*(l1 + 2*l2 + 2*l3 + l4)

        t_values.append((i+1)*h)
        y_values.append(y_next)
        x_values.append(x_next)

    return  x_values, y_values


x_euler, y_euler = euler(x0, y0, h, n)
t_rk =  np.arange(0, 60 + h, h)
 
x_rk, y_rk = runge_kutta(x0, y0, h, n)

plt.figure(figsize=(12, 6))
plt.plot(t_rk, x_rk, label='Espécie 1 (Runge-Kutta)', color='blue')
plt.plot(t_rk, y_rk, label='Espécie 2 (Runge-Kutta)', color='orange')
plt.plot(t_rk, x_euler, label='Espécie 1 (Euler)', color='cyan', linestyle='dashed')    
plt.plot(t_rk, y_euler, label='Espécie 2 (Euler)', color='magenta', linestyle='dashed')
plt.xlabel('Tempo (t)')
plt.ylabel('População')
plt.title('Dinâmica de Duas Espécies')
plt.legend()
plt.grid()
plt.show()
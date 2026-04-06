import numpy as np
import matplotlib.pyplot as plt

# EDO: dy/dx = -y^3
def f(x, y):
    derivada = -y**3 + 0*x
    return derivada

# Solução analítica: y = 1/sqrt(2*x + 1)
def analitica(x):
    y = 1/np.sqrt(2*x + 1)
    return y

#avaliando a solução analítica para x = 1.5 (resultado esperado: y = 0.5)
#print(analitica(1.5))

def euler(x0, y0, h, n):
    y_values = [y0]
    x_values = [x0]
    x_next = x0
    y_next = y0
    print("Método de Euler:")
    for i in range(n):
        #print(f"x: {x_next:.2f}, y: {y_next:.4f}")
        y_next = y_next + h * f(x_next, y_next)
        x_next = x_next + h
        
        y_values.append(y_next)
        x_values.append(x_next)
    return x_values, y_values


def runge_kutta(x0, y0, h, n):
    y_values = [y0]
    x_values = [x0]
    x_next = x0
    y_next = y0
    print("\n\nMétodo de Runge-Kutta:")
    for i in range(n):
        #print(f"x: {x_next:.2f}, y: {y_next:.4f}")
        k1 = f(x_next, y_next)
        k2 = f(x_next + h/2, y_next + h*k1/2)
        k3 = f(x_next + h/2, y_next + h*k2/2)
        k4 = f(x_next + h, y_next + h*k3)
        
        y_next = y_next + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        x_next = x_next + h
        
        y_values.append(y_next)
        x_values.append(x_next)
    return x_values, y_values

# Parâmetros iniciais
x0 = 0
y0 = 1
h = 0.1
xf = 5

# Calcula o número de iterações
n = int((xf - x0) / h)

# Gerar pontos x para a solução analítica
x_analitico = np.linspace(x0, x0 + n*h, 1000000)

# Calcular as soluções numéricas e analítica
euler_x, euler_y = euler(x0, y0, h, n)
rk_x, rk_y = runge_kutta(x0, y0, h, n)
y_analitico = analitica(x_analitico)

# Plotar os resultados
plt.plot(euler_x, euler_y, label='Euler', marker='o')
plt.plot(rk_x, rk_y, label='Runge-Kutta', marker='s')
plt.plot(x_analitico, y_analitico, label='Solução Analítica', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Método de Euler vs Solução Analítica vs Runge-Kutta')
plt.legend()
plt.grid()
plt.show()
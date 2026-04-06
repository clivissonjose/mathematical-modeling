import matplotlib.pyplot as plt

#Parametros

a = 0.16
b = 0.08 
c = 0.9 
d = 4.5

# Condições iniciais
x0 = 4
y0 = 4

# Parâmetros de tempo
h =  0.001
t_fim = 16
# Número de iterações
n = int(t_fim / h)

#Funções

  # x′(t) = −ax + bxy    predador 

def f_predador(x,y):
    derivada = -a*x + b*x*y  
    return derivada


   # y′(t) = dy − cxy    presa
def f_presa(x, y):
    derivada =  d*y - c*x*y
    return derivada


# Método de Euler
def euler_lotka_volterra(x0, y0, h, n):
    
    t_values = [0]
    y_values = [y0]
    x_values = [x0]

    # x e y atualizados juntos, loop único
    x = x0
    y = y0

    
    for i in range(n):
        
        x_next = x + h * f_predador(x, y)
        y_next = y + h * f_presa(x, y)
        
        #Atualiza x e y para a próxima iteração
        x = x_next
        y = y_next

        # Armazena os valores de tempo, x e y
        t_values.append((i + 1) * h)
        y_values.append(y_next)
        x_values.append(x_next)

    return t_values, x_values, y_values


t, x, y = euler_lotka_volterra(x0, y0, h, n)


# Gráfico
plt.figure(figsize=(10, 5))
plt.plot(t, x, label='x(t) — Predadores', color='red')
plt.plot(t, y, label='y(t) — Presas', color='blue')
plt.xlabel('Tempo t')
plt.ylabel('População')
plt.title('Modelo Predador-Presa de Lotka-Volterra (Método de Euler)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('lotka_volterra.png', dpi=150)
plt.show()
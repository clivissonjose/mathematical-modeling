import matplotlib.pyplot as plt

m = 2 
k = 2000
a = 6
L = 3
x0 = 5 
v0 = 0

h = 0.01
t_fim = 1

# Número de iterações
n = int(t_fim / h)


# x'(t) = v
def f1(x, v):
    return v

# v'(t) = -(k/m)*x - (a/m)*v + (k*L/m)
def f2(x, v):
    return -(k/m)*x - (a/m)*v + (k*L/m)



def runge_kutta(x0, v0, h, n):
    
    x_values = [x0]
    v_values = [v0]

    x = x0
    v = v0


    for i in range(n):
        
        k1_x = f1(x, v)
        k1_v = f2(x, v)

        k2_x = f1(x + h * k1_x / 2, v + h * k1_v / 2)
        k2_v = f2(x + h * k1_x / 2, v + h * k1_v / 2)

        k3_x = f1(x + h * k2_x / 2, v + h * k2_v / 2)
        k3_v = f2(x + h * k2_x / 2, v + h * k2_v / 2)

        k4_x = f1(x + h * k3_x, v + h * k3_v)
        k4_v = f2(x + h * k3_x, v + h * k3_v)

        x = x + h * (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6
        v = v + h * (k1_v + 2 * k2_v + 2 * k3_v + k4_v) / 6

        x_values.append(x)
        v_values.append(v)

    return x_values, v_values


x, v = runge_kutta(x0, v0, h, n)
t = [i * h for i in range(n + 1)]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

ax1.plot(t, x, color='steelblue')
ax1.axhline(L, color='gray', linestyle='--', label='equilíbrio (x=L)')
ax1.set_ylabel('Posição x(t) [m]')
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2.plot(t, v, color='tomato')
ax2.set_ylabel('Velocidade v(t) [m/s]')
ax2.set_xlabel('Tempo t [s]')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('massa_mola_rk4.png', dpi=150)
plt.show()

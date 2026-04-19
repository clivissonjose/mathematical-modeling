import numpy as np
import matplotlib.pyplot as plt

# ── Parâmetros do sistema ───────────────────────────────────────
m = 2        # massa (kg)
k = 2000    # constante elástica (N/m)
a = 6        # constante de amortecimento
L = 3        # comprimento natural / posição de equilíbrio (m)

# ── Sistema de EDOs ─────────────────────────────────────────────
# x'(t) = v
# v'(t) = -(k/m)*x - (a/m)*v + (k*L/m)
def f1(x, v):
    """Derivada de x"""
    return v

def f2(x, v):
    """Derivada de v"""
    return -(k/m)*x - (a/m)*v + (k*L/m)

# ── Parâmetros de integração ────────────────────────────────────
h  = 0.01          # passo
t0 = 0.0
tf = 1.0
n  = int((tf - t0) / h)

# ── Condições iniciais ──────────────────────────────────────────
x0 = 5.0
v0 = 0.0

# ── Vetores de resultado ────────────────────────────────────────
t = np.linspace(t0, tf, n + 1)
x = np.zeros(n + 1)
v = np.zeros(n + 1)

x[0] = x0
v[0] = v0

# ── Método de Runge-Kutta (RK4) ─────────────────────────────────
for i in range(n):
    xi = x[i]
    vi = v[i]

    # Inclinações do passo 1
    k1_x = f1(xi, vi)
    k1_v = f2(xi, vi)

    # Inclinações do passo 2 (ponto médio com k1)
    k2_x = f1(xi + h/2*k1_x, vi + h/2*k1_v)
    k2_v = f2(xi + h/2*k1_x, vi + h/2*k1_v)

    # Inclinações do passo 3 (ponto médio com k2)
    k3_x = f1(xi + h/2*k2_x, vi + h/2*k2_v)
    k3_v = f2(xi + h/2*k2_x, vi + h/2*k2_v)

    # Inclinações do passo 4 (ponto final com k3)
    k4_x = f1(xi + h*k3_x, vi + h*k3_v)
    k4_v = f2(xi + h*k3_x, vi + h*k3_v)

    # Atualização: média ponderada (1,2,2,1)/6
    x[i+1] = xi + (h/6) * (k1_x + 2*k2_x + 2*k3_x + k4_x)
    v[i+1] = vi + (h/6) * (k1_v + 2*k2_v + 2*k3_v + k4_v)

# ── Gráficos ────────────────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

ax1.plot(t, x, color='steelblue', linewidth=1.5)
ax1.axhline(L, color='gray', linestyle='--', linewidth=1, label=f'Equilíbrio x=L={L}')
ax1.set_ylabel('Posição x(t) [m]')
ax1.set_title('Sistema massa-mola amortecido — RK4')
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2.plot(t, v, color='tomato', linewidth=1.5)
ax2.axhline(0, color='gray', linestyle='--', linewidth=1)
ax2.set_ylabel('Velocidade v(t) [m/s]')
ax2.set_xlabel('Tempo t [s]')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('massa_mola_rk4.png', dpi=150)
plt.show()
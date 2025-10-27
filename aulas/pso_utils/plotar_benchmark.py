import math

import matplotlib.pyplot as plt
import numpy as np

# ---------------------- Funções Benchmark ----------------------


def schaffer(x):
    total = 0.0
    for i in range(len(x) - 1):
        num = math.sin(x[i] ** 2 - x[i + 1] ** 2) ** 2 - 0.5
        den = (1 + 0.001 * (x[i] ** 2 + x[i + 1] ** 2)) ** 2
        total += 0.5 + num / den
    return total


def griewank(x):
    sum_part = sum(xi**2 for xi in x) / 4000.0
    prod_part = 1.0
    for i, xi in enumerate(x, start=1):
        prod_part *= math.cos(xi / math.sqrt(i))
    return 1 + sum_part - prod_part


def ackley(x):
    n = len(x)
    sum_sq = sum(xi**2 for xi in x)
    sum_cos = sum(math.cos(2 * math.pi * xi) for xi in x)
    term1 = -20 * math.exp(-0.2 * math.sqrt(sum_sq / n))
    term2 = -math.exp(sum_cos / n)
    return term1 + term2 + 20 + math.e


benchmarks = {
    "schaffer": (schaffer, (-100, 100)),
    "griewank": (griewank, (-600, 600)),
    "ackley": (ackley, (-32.768, 32.768)),
}


def plotar_benchmark(nome_funcao):
    nome_funcao = nome_funcao.lower()

    funcao, limites = benchmarks[nome_funcao]
    num_pontos = 100

    x = np.linspace(limites[0], limites[1], num_pontos)
    y = np.linspace(limites[0], limites[1], num_pontos)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[funcao([xi, yi]) for xi in x] for yi in y])

    plt.style.use("default")
    fig = plt.figure(figsize=(14, 6), facecolor="white")

    # Gráfico 2D
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.contour(X, Y, Z, levels=20, cmap="Blues")
    ax1.set_title(f"{nome_funcao.capitalize()} 2D")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ax1.set_aspect("equal", adjustable="box")

    # Gráfico 3D
    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    ax2.plot_surface(X, Y, Z, cmap="Blues", edgecolor="none", alpha=0.9)
    ax2.set_title(f"{nome_funcao.capitalize()} 3D")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    ax2.set_zlabel("Fitness")

    plt.tight_layout()
    plt.show()

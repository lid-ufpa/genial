import math

import matplotlib.pyplot as plt


def plotar_espaco_de_busca(particulas: list | None = None) -> None:
    x_values = [i * 0.05 - 5 for i in range(201)]
    y_values = [math.sin(3 * x) + (x**2) / 7 for x in x_values]

    plt.figure(figsize=(8, 4))
    plt.plot(x_values, y_values, label="f(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.xticks(range(-5, 6))
    plt.grid(visible=True)

    if particulas:
        plt.title("Espaço de Busca com Partículas")
        for p in particulas:
            x = p["Posição"]
            plt.scatter(x, math.sin(3 * x) + (x**2) / 7, color="red", zorder=3)
    else:
        plt.title("Espaço de Busca")

    plt.show()

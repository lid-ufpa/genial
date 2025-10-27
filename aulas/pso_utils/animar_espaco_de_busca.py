import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def f(x):
    return math.sin(3 * x) + (x**2) / 7


def animar_espaco_de_busca(log_particulas, intervalo=500):
    x_values = [i * 0.05 - 5 for i in range(201)]
    y_values = [f(x) for x in x_values]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x_values, y_values, label="f(x)")
    ax.set_xlim(min(x_values), max(x_values))
    ax.set_ylim(min(y_values) - 1, max(y_values) + 1)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)

    scatter = ax.scatter([], [], color="red", s=50, zorder=3)
    texto_iteracao = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def init():
        # manter formato 2D válido
        scatter.set_offsets(np.empty((0, 2)))
        texto_iteracao.set_text("")
        return scatter, texto_iteracao

    def update(frame):
        particulas_frame = log_particulas[frame]
        coords = np.array([[p["Posição"], f(p["Posição"])] for p in particulas_frame])
        scatter.set_offsets(coords)
        ax.set_title(
            f"Otimização - Iteração {frame + 1}/{len(log_particulas)}",
        )
        return scatter, texto_iteracao

    ani = FuncAnimation(
        fig,
        update,
        frames=len(log_particulas),
        init_func=init,
        interval=intervalo,
        blit=True,
    )
    plt.close()

    return ani

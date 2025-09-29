import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def animar_pso_3d(pso, nome_funcao, limites):
    if not pso.historico:
        return None

    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, projection="3d")

    num_pontos = 50
    x = [limites[0] + i * (limites[1] - limites[0]) / (num_pontos - 1) for i in range(num_pontos)]
    y = [limites[0] + i * (limites[1] - limites[0]) / (num_pontos - 1) for i in range(num_pontos)]

    z_grid = []
    for yi in y:
        linha = []
        for xi in x:
            linha.append(pso.funcao_objetivo([xi, yi]))
        z_grid.append(linha)
    z_grid = np.array(z_grid)

    ax.plot_surface(
        [[xv for xv in x] for _ in y],
        [[yi for _ in x] for yi in y],
        z_grid,
        cmap="viridis",
        alpha=0.6,
        rstride=1,
        cstride=1,
        edgecolor="none",
    )

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Fitness")
    ax.set_xlim(limites)
    ax.set_ylim(limites)

    scatter = ax.scatter(
        [],
        [],
        [],
        c="#FF8800",
        s=40,
        edgecolors="black",
        linewidths=0.5,
        depthshade=True,
    )
    titulo = ax.text2D(
        0.5,
        0.95,
        "",
        transform=ax.transAxes,
        ha="center",
        fontsize=14,
    )

    def update(frame_idx):
        registro = pso.historico[frame_idx]
        posicoes = np.array(registro["posicoes"])
        fitness = [pso.funcao_objetivo(p) for p in posicoes]

        scatter._offsets3d = (posicoes[:, 0], posicoes[:, 1], fitness)
        titulo.set_text(
            f"Otimização ({nome_funcao}) - Iteração: {frame_idx + 1}/{pso.n_iteracoes} | "
            f"Melhor Fitness: {registro['melhor_fitness']:.2f}",
        )
        return scatter, titulo

    ani = FuncAnimation(
        fig,
        update,
        frames=len(pso.historico),
        blit=False,
        interval=150,
        repeat_delay=1000,
    )

    plt.close(fig)

    ani.save("./animacoes/pso_3d.gif", writer="pillow")

    return ani

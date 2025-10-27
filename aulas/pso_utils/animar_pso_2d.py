import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animar_pso_2d(pso, nome_funcao, limites):
    if not pso.historico:
        return None

    plt.style.use("default")

    fig, ax = plt.subplots(figsize=(7, 7), facecolor="white")

    num_pontos = 100
    x = [limites[0] + i * (limites[1] - limites[0]) / (num_pontos - 1) for i in range(num_pontos)]
    y = [limites[0] + i * (limites[1] - limites[0]) / (num_pontos - 1) for i in range(num_pontos)]
    z_grid = [[pso.funcao_objetivo([xi, yi]) for xi in x] for yi in y]

    ax.contour(x, y, z_grid, levels=20, cmap="Blues", linewidths=1.2)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_xlim(limites)
    ax.set_ylim(limites)
    ax.set_facecolor("white")

    scatter = ax.scatter(
        [],
        [],
        c="red",
        s=40,
        edgecolors="black",
        linewidths=0.5,
        zorder=3,
    )
    titulo = ax.text(
        0.5,
        1.05,
        "",
        transform=ax.transAxes,
        ha="center",
        fontsize=14,
        color="black",
    )

    def update(frame_idx):
        posicoes = pso.historico[frame_idx]
        scatter.set_offsets(posicoes)
        titulo.set_text(f"Otimização ({nome_funcao}) - Iteração: {frame_idx + 1}/{pso.n_iteracoes}")
        return scatter, titulo

    ani = FuncAnimation(
        fig,
        update,
        frames=len(pso.historico),
        blit=True,
        interval=150,
        repeat_delay=1000,
    )

    plt.close(fig)

    return ani

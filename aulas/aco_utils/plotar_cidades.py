import matplotlib.pyplot as plt


def plotar_cidades(coordenadas):
    fig, ax = plt.subplots(figsize=(7, 5))

    xs = [x for x, y in coordenadas]
    ys = [y for x, y in coordenadas]

    ax.scatter(xs, ys, c="black", s=300, zorder=5)

    for i, (x, y) in enumerate(coordenadas):
        ax.text(
            x,
            y,
            str(i),
            ha="center",
            va="center",
            color="white",
            fontsize=9,
            fontweight="bold",
            zorder=6,
        )

    ax.set_title("Posições Iniciais das Cidades")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(visible=True, linestyle="--", alpha=0.3)
    plt.show()

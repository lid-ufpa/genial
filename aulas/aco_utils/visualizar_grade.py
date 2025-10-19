import matplotlib.pyplot as plt


def visualizar_grade(custos, formigas=None, melhor_caminho=None, titulo="Grade de Custos"):
    n = len(custos)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(custos, cmap="Blues", origin="upper", alpha=0.7)

    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(range(n))
    ax.set_yticklabels(range(n))
    ax.xaxis.tick_top()

    if formigas:
        n_formigas = len(formigas)
        colors = [plt.cm.tab10(i / n_formigas) for i in range(n_formigas)]
        for idx, caminho in enumerate(formigas):
            xs = [p[1] for p in caminho]
            ys = [p[0] for p in caminho]
            ax.plot(
                xs,
                ys,
                marker="o",
                markersize=6,
                linewidth=2.5,
                color=colors[idx],
                label=f"Formiga {idx + 1}",
                alpha=0.9,
            )

    if melhor_caminho:
        xs = [p[1] for p in melhor_caminho]
        ys = [p[0] for p in melhor_caminho]
        ax.plot(
            xs,
            ys,
            marker="o",
            markersize=6,
            linewidth=3,
            color="red",
            label="Melhor Caminho",
            alpha=1,
            zorder=4,
        )

    for i in range(n):
        for j in range(n):
            ax.text(
                j,
                i,
                str(custos[i][j]),
                ha="center",
                va="center",
                fontsize=8,
                color="black",
                zorder=10,
            )

    ax.set_title(titulo, pad=20)
    if formigas or melhor_caminho:
        ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.show()

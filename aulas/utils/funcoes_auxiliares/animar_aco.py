import matplotlib.pyplot as plt
from matplotlib import animation


def animar_aco(aco, coordenadas):
    if not aco.historico:
        return None

    fig, ax = plt.subplots(figsize=(7, 5))

    xs = [x for x, y in coordenadas]
    ys = [y for x, y in coordenadas]
    ax.scatter(xs, ys, c="black", s=150, zorder=5)

    for i, (x, y) in enumerate(coordenadas):
        ax.text(
            x,
            y,
            str(i),
            ha="center",
            va="center",
            color="white",
            fontweight="bold",
        )

    linhas_feromonio = []
    (linha_melhor_caminho,) = ax.plot(
        [],
        [],
        color="#E6550D",
        linewidth=2.5,
        zorder=10,
        label="Melhor Caminho",
    )

    plt.xlabel("X")
    plt.ylabel("Y")
    ax.legend()

    def atualizar(frame):
        nonlocal linhas_feromonio
        for linha in linhas_feromonio:
            linha.remove()
        linhas_feromonio = []

        estado = aco.historico[frame]
        feromonios = estado["feromonios"]

        max_val = max(max(linha) for linha in feromonios)
        if max_val > 0:
            norm = [[val / max_val for val in linha] for linha in feromonios]
        else:
            norm = feromonios

        for i in range(len(coordenadas)):
            for j in range(i, len(coordenadas)):
                largura = norm[i][j] * 7
                limite = 0.1
                if largura > limite:
                    (linha,) = ax.plot(
                        [coordenadas[i][0], coordenadas[j][0]],
                        [coordenadas[i][1], coordenadas[j][1]],
                        "#3182BD",
                        alpha=0.5,
                        linewidth=largura,
                        zorder=1,
                    )
                    linhas_feromonio.append(linha)

        if estado["melhor_solucao"]:
            caminho = [coordenadas[i] for i, j in estado["melhor_solucao"]]
            caminho.append(coordenadas[estado["melhor_solucao"][0][0]])
            xs = [x for x, y in caminho]
            ys = [y for x, y in caminho]
            linha_melhor_caminho.set_data(xs, ys)

        ax.set_title(
            f"Otimização - Iteração {estado['iteracao'] + 1}/{aco.n_iteracoes} | "
            f"Melhor Custo: {estado['melhor_custo']:.2f}",
        )

        return [linha_melhor_caminho, *linhas_feromonio]

    plt.close()
    return animation.FuncAnimation(
        fig,
        atualizar,
        frames=len(aco.historico),
        interval=200,
        blit=True,
        repeat=False,
    )

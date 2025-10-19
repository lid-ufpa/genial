import random
import time

import pandas as pd


class TSPACO:
    def __init__(self, custos, n_formigas, alfa, beta, n_iteracoes, taxa_evaporacao):
        self.custos = custos

        n = len(custos)
        self.feromonios = [[1.0 / n for _ in range(n)] for _ in range(n)]

        self.vertices = list(range(n))

        self.n_formigas = n_formigas
        self.n_iteracoes = n_iteracoes
        self.alfa = alfa
        self.beta = beta
        self.taxa_evaporacao = taxa_evaporacao

        self.melhor_solucao = []
        self.melhor_custo = float("inf")

        self.historico = []

        self.metricas = []

    def _construir_solucao(self, vertice_inicial):
        solucao = []
        visitados = {vertice_inicial}
        vertice_atual = vertice_inicial

        for _ in range(len(self.custos) - 1):
            candidatos = [v for v in self.vertices if v not in visitados]
            if not candidatos:
                continue

            probabilidades = self._probabilidades_transicao(vertice_atual, candidatos)
            proximo_vertice = random.choices(candidatos, weights=probabilidades, k=1)[0]

            solucao.append((vertice_atual, proximo_vertice))
            visitados.add(proximo_vertice)
            vertice_atual = proximo_vertice

        solucao.append((vertice_atual, vertice_inicial))
        custo_total = sum(self.custos[i][j] for i, j in solucao)
        return solucao, custo_total

    def _probabilidades_transicao(self, vertice_atual, candidatos):
        numeradores = []
        for j in candidatos:
            tau = self.feromonios[vertice_atual][j] ** self.alfa
            eta = (
                (1.0 / self.custos[vertice_atual][j]) ** self.beta
                if self.custos[vertice_atual][j] > 0
                else 0
            )
            numeradores.append(tau * eta)

        soma = sum(numeradores)
        return (
            [n / soma for n in numeradores] if soma > 0 else [1 / len(candidatos)] * len(candidatos)
        )

    def _construir_solucoes(self, vertice_inicial):
        solucoes = []
        for _ in range(self.n_formigas):
            solucao, custo = self._construir_solucao(vertice_inicial)
            solucoes.append((solucao, custo))
            self._atualizar_melhor_global(solucao, custo)
        return solucoes

    def _atualizar_melhor_global(self, solucao, custo):
        if custo < self.melhor_custo:
            self.melhor_custo = custo
            self.melhor_solucao = solucao

    def _atualizar_feromonios(self, solucoes):
        n = len(self.custos)
        for i in range(n):
            for j in range(n):
                self.feromonios[i][j] *= 1 - self.taxa_evaporacao

        for solucao, custo in solucoes:
            deposito = 1.0 / custo
            for i, j in solucao:
                self.feromonios[i][j] += deposito
                self.feromonios[j][i] += deposito

    def otimizar(self, vertice_inicial):
        self.historico = []
        self.metricas = []

        for iteracao in range(self.n_iteracoes):
            inicio = time.time()

            solucoes = self._construir_solucoes(vertice_inicial)
            self._atualizar_feromonios(solucoes)

            custos = [custo for _, custo in solucoes]
            media = sum(custos) / len(custos)
            variancia = sum((c - media) ** 2 for c in custos) / len(custos)
            desvio = variancia ** (1 / 2)
            tempo = time.time() - inicio

            self.metricas.append(
                {
                    "iteracao": iteracao,
                    "melhor_custo": round(min(custos), 2),
                    "pior_custo": round(max(custos), 2),
                    "custo_medio": round(media, 2),
                    "custo_desvio": round(desvio, 2),
                    "tempo_ms": round(tempo * 1000, 2),
                },
            )

            entrada_historico = {
                "iteracao": iteracao,
                "melhor_solucao": self.melhor_solucao[:],
                "melhor_custo": self.melhor_custo,
                "feromonios": [linha[:] for linha in self.feromonios],
            }
            self.historico.append(entrada_historico)

        caminho = [i for i, j in self.melhor_solucao] + [vertice_inicial]
        return caminho, self.melhor_custo

    def obter_metricas(self):
        """Retorna métricas da execução do ACO como DataFrame."""
        return pd.DataFrame(self.metricas)

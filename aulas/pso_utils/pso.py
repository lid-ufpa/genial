import math
import random
import time

import pandas as pd


class PSO:
    def __init__(self, posicoes, funcao_objetivo, n_iteracoes):
        self.funcao_objetivo = funcao_objetivo
        self.n_iteracoes = n_iteracoes
        self.posicoes = [p[:] for p in posicoes]
        self.velocidades = [[0.0 for _ in p] for p in posicoes]
        self.pbest = [p[:] for p in self.posicoes]

        melhor_idx = min(range(len(self.pbest)), key=lambda i: self.funcao_objetivo(self.pbest[i]))
        self.gbest = self.pbest[melhor_idx][:]

        self.historico_gbest = []
        self.historico = []
        self.metricas = []

    def _atualizar_velocidades(self, inercia, cognitivo, social):
        for i in range(len(self.posicoes)):
            for d in range(len(self.posicoes[i])):
                r1 = random.uniform(0, 1)
                r2 = random.uniform(0, 1)
                self.velocidades[i][d] = (
                    inercia * self.velocidades[i][d]
                    + cognitivo * r1 * (self.pbest[i][d] - self.posicoes[i][d])
                    + social * r2 * (self.gbest[d] - self.posicoes[i][d])
                )

    def _atualizar_posicoes(self):
        for i in range(len(self.posicoes)):
            for d in range(len(self.posicoes[i])):
                self.posicoes[i][d] += self.velocidades[i][d]

    def _atualizar_melhores_posicoes(self):
        for i in range(len(self.posicoes)):
            if self.funcao_objetivo(self.posicoes[i]) < self.funcao_objetivo(self.pbest[i]):
                self.pbest[i] = self.posicoes[i][:]
            if self.funcao_objetivo(self.posicoes[i]) < self.funcao_objetivo(self.gbest):
                self.gbest = self.posicoes[i][:]

    def otimizar(self, inercia, cognitivo, social):
        self.historico = []
        self.metricas = []

        for iteracao in range(self.n_iteracoes):
            inicio = time.time()

            self._atualizar_velocidades(inercia, cognitivo, social)
            self._atualizar_posicoes()
            self._atualizar_melhores_posicoes()

            fitness = [self.funcao_objetivo(p) for p in self.posicoes]
            media = sum(fitness) / len(fitness)
            variancia = sum((f - media) ** 2 for f in fitness) / len(fitness)
            desvio = math.sqrt(variancia)
            tempo = (time.time() - inicio) * 1000

            self.metricas.append(
                {
                    "iteracao": iteracao + 1,
                    "melhor_fitness": round(min(fitness), 4),
                    "pior_fitness": round(max(fitness), 4),
                    "media_fitness": round(media, 4),
                    "desvio_fitness": round(desvio, 4),
                    "tempo_ms": round(tempo, 2),
                },
            )

            registro = [p[:] for p in self.posicoes]
            self.historico.append(registro)
            self.historico_gbest.append(self.funcao_objetivo(self.gbest))

        return self.gbest, self.funcao_objetivo(self.gbest)

    def obter_metricas(self):
        return pd.DataFrame(self.metricas).set_index("iteracao")

import random
import time
import tracemalloc

import numpy as np


class GeneticAlgorithm:
    """Implementação do algoritmo genético para o problema da mochila"""

    def __init__(
        self,
        weights: list[int],
        vals: list[int],
        max_weight: float,
        population_size: int,
        mutation_rate: float,
        generations: int,
    ) -> None:
        # Hiperparâmetros do algoritmo
        self.weights = weights
        self.vals = vals
        self.max_weight = max_weight
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations

        # Melhor solução
        self.gbest_fitness = -float("inf")
        self.gbest_individual = 0.0

        # Dicionário contendo algumas métricas, como o desvio padrão e a média
        self.metrics = dict

    def _create_population(self, population_size: int) -> list:
        population = np.array(
            [[random.randint(0, 1) for _ in range(len(self.vals))] for _ in range(population_size)]
        )

        return population

    def _get_fitness(self, individual: list) -> float:
        total_weight = 0
        total_vals = 0

        for gene, v, w in zip(individual, self.vals, self.weights, strict=False):
            total_vals += gene * v
            total_weight += gene * w

        if total_weight <= self.max_weight:
            return total_vals
        return total_vals - 10 * (total_weight - self.max_weight)

    def _selection(self, population: list, fitnesses: list, tournament_size=2) -> list:
        selected = []

        for _ in range(len(population)):
            tournament = random.sample(
                list(zip(population, fitnesses, strict=False)), tournament_size
            )
            winner = max(tournament, key=lambda x: x[1])[0]

            selected.append(winner)

        return np.array(selected)

    def _crossover(self, parent_1: list, parent_2: list) -> list:
        alpha = np.random.randint(0, 8)

        children_1 = np.concatenate((parent_1[:alpha], parent_2[alpha:]))
        children_2 = np.concatenate((parent_2[:alpha], parent_1[alpha:]))

        return children_1, children_2

    def _mutation(self, individual: list, mutation_rate: float) -> list:
        for i in range(len(individual)):
            if random.random() < mutation_rate:
                match individual[i]:
                    case 1:
                        individual[i] = 0
                    case 0:
                        individual[i] = 1
        return individual

    def execution(self) -> tuple[list, float]:
        population = self._create_population(self.population_size)

        metrics = {
            "time": [],
            "memory peak": [],
            "mean": [],
            "standard deviation": [],
            "worst fitness": [],
            "best fitness": [],
        }

        for generation in range(self.generations):
            tracemalloc.start()
            start = time.time()

            initial_memory, initial_peak = tracemalloc.get_traced_memory()

            fitnesses = np.array([self._get_fitness(individual) for individual in population])

            mean = np.sum(fitnesses) / len(fitnesses)
            standard_deviation = np.sqrt((np.sum((fitnesses - mean) ** 2)) / len(fitnesses))

            metrics["mean"].append(mean)
            metrics["standard deviation"].append(standard_deviation)

            best_individual = max(population, key=self._get_fitness)
            best_fitness = self._get_fitness(best_individual)

            worst_individual = min(population, key=self._get_fitness)
            worst_fitness = self._get_fitness(worst_individual)

            metrics["best fitness"].append(best_fitness)
            metrics["worst fitness"].append(worst_fitness)

            if best_fitness > self.gbest_fitness:
                self.gbest_fitness = best_fitness
                self.gbest_individual = best_individual

            population = self._selection(population, fitnesses)

            next_population = []

            for i in range(0, len(population), 2):
                parent_1 = population[i]
                parent_2 = population[i + 1]

                children_1, children_2 = self._crossover(parent_1, parent_2)

                next_population.append(self._mutation(children_1, self.mutation_rate))
                next_population.append(self._mutation(children_2, self.mutation_rate))

            next_population[0] = best_individual
            population = np.array(next_population)

            final_memory, final_peak = tracemalloc.get_traced_memory()

            end = time.time()
            tracemalloc.stop()

            metrics["time"].append(f"{(end - start):.2f}s")
            metrics["memory peak"].append(f"{((final_peak - initial_peak) / 1024**2):.2f}mb")

        self.metrics = metrics

        return self.gbest_individual, self.gbest_fitness

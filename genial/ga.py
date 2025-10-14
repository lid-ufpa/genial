import random
import numpy as np
from typing import List, Tuple

class GeneticAlgorithm():
    def __init__(
        self, 
        weights:List[int], 
        vals:List[int], 
        max_weight:float, 
        generations:int, 
        population_size:int, 
        mutation_rate:float
    ) -> None:

        self.weights = weights
        self.vals = vals
        self.max_weight = max_weight
        self.generations = generations
        self.population_size = population_size
        self.mutation_rate = mutation_rate

        self.gbest_fitness = -float('inf')
        self.gbest_individual = float()

        self.gbest_individual_history = List[List]
        self.gbest_fitness_history = List[float]

    def _create_population(self, population_size) -> List:
        population = np.array([[random.randint(0, 1) for _ in range(len(self.vals))] for _ in range(population_size)])
        
        return population
    
    def _get_fitness(self, individual:List) -> float:
        total_weight = 0
        total_vals = 0
        p = -float('inf')

        for gene, v, w in zip(individual, self.vals, self.weights): 
            
            total_vals += gene * v
            total_weight += gene * w
            if v / w > p:
                p = v / w

        if total_weight <= self.max_weight:
            fitness = total_vals - 0
        else:
            pen = 10 * p * (total_weight - self.max_weight) 
            fitness = total_vals - pen     
        
        return fitness
    
    def _selection(self, population:List, fitnesses:List, tournament_size=2) -> List:
        selected = []

        for _ in range(len(population)):
            tournament = random.sample(list(zip(population, fitnesses)), tournament_size)
            winner = max(tournament, key=lambda x: x[1])[0]

            selected.append(winner)

        return np.array(selected)
    
    def _crossover(self, parent_1:List, parent_2:List) -> List:

        alpha = np.random.randint(0, 8)

        children_1 = np.concatenate((parent_1[:alpha], parent_2[alpha:]))
        children_2 = np.concatenate((parent_2[:alpha], parent_1[alpha:]))

        return children_1, children_2
    
    def _mutation(self, individual:List, mutation_rate:float) -> List:
        for i in range(len(individual)):
            if random.random() < mutation_rate:
                match individual[i]:
                    case 1:
                        individual[i] = 0
                    case 0:
                        individual[i] = 1
        return individual
    
    def execution(self) -> Tuple[List, float]:
        population = self._create_population(self.population_size)

        for generation in range(self.generations):
            self.population_history.append(population)

            fitnesses = np.array([self._get_fitness(individual) for individual in population])

            best_individual = max(population, key=self._get_fitness)
            best_fitness = self._get_fitness(best_individual)

            if best_fitness > self.gbest_fitness:
                self.gbest_fitness = best_fitness
                self.gbest_individual = best_individual

            self.gbest_individual_history.append(self.gbest_individual)
            self.gbest_fitness_history.append(self.gbest_fitness)
            
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

        return self.gbest_individual, self.gbest_fitness
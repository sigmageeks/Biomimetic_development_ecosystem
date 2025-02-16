import random
import numpy as np

def generate_population(size, length):
    """Generates a population of random binary strings."""
    return [np.random.randint(2, size=length).tolist() for _ in range(size)]

def fitness_function(individual):
    """Calculates fitness as the sum of 1s in the binary string."""
    return sum(individual)

def select_parents(population, fitnesses, num_parents):
    """Selects parents based on fitness proportionate selection."""
    selected = np.random.choice(len(population), size=num_parents, replace=False, p=np.array(fitnesses)/sum(fitnesses))
    return [population[i] for i in selected]

def crossover(parent1, parent2):
    """Performs single-point crossover between two parents."""
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

def mutate(individual, mutation_rate=0.1):
    """Mutates an individual by flipping bits with a given probability."""
    return [bit if random.random() > mutation_rate else 1 - bit for bit in individual]

def genetic_algorithm(pop_size, gene_length, generations, mutation_rate=0.1):
    """Runs the genetic algorithm optimization process."""
    population = generate_population(pop_size, gene_length)
    for _ in range(generations):
        fitnesses = [fitness_function(ind) for ind in population]
        parents = select_parents(population, fitnesses, pop_size // 2)
        offspring = []
        for i in range(0, len(parents), 2):
            if i + 1 < len(parents):
                child1, child2 = crossover(parents[i], parents[i+1])
                offspring.append(mutate(child1, mutation_rate))
                offspring.append(mutate(child2, mutation_rate))
        population = parents + offspring
    best_individual = max(population, key=fitness_function)
    return best_individual, fitness_function(best_individual)

if __name__ == "__main__":
    best_solution, best_fitness = genetic_algorithm(pop_size=10, gene_length=8, generations=20)
    print("Best Solution:", best_solution)
    print("Best Fitness:", best_fitness)

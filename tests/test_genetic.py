import unittest
from core import genetic_algorithm

def sample_fitness_function(solution):
    return sum(solution)  # Example: sum of elements as fitness

class TestGeneticAlgorithm(unittest.TestCase):
    def setUp(self):
        self.optimizer = genetic_algorithm(
            population_size=10,
            gene_length=5,
            mutation_rate=0.1,
            crossover_rate=0.7,
            generations=20,
            fitness_function=sample_fitness_function
        )
    
    def test_initial_population(self):
        self.assertEqual(len(self.optimizer.population), 10)
        self.assertEqual(len(self.optimizer.population[0]), 5)
    
    def test_fitness_evaluation(self):
        fitness_scores = self.optimizer.evaluate_population()
        self.assertEqual(len(fitness_scores), 10)
    
    def test_selection(self):
        parents = self.optimizer.select_parents()
        self.assertEqual(len(parents), 2)
    
    def test_crossover(self):
        parent1, parent2 = self.optimizer.select_parents()
        child1, child2 = self.optimizer.crossover(parent1, parent2)
        self.assertEqual(len(child1), 5)
        self.assertEqual(len(child2), 5)
    
    def test_mutation(self):
        individual = [0, 1, 1, 0, 1]
        mutated = self.optimizer.mutate(individual)
        self.assertEqual(len(mutated), 5)
    
    def test_run_optimization(self):
        best_solution, best_fitness = self.optimizer.run()
        self.assertIsInstance(best_solution, list)
        self.assertIsInstance(best_fitness, (int, float))

if __name__ == "__main__":
    unittest.main()

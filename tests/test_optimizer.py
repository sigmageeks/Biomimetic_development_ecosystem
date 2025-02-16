import sys
import os

# Add the project's root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from core.optimizer import optimize_code  # ✅ Correct
result = optimize_code("some_code")  # ✅ Works


def sample_code():
    return """
    def inefficient_function():
        result = []
        for i in range(10000):
            result.append(i * 2)
        return result
    """

class TestOptimizer(unittest.TestCase):
    def setUp(self):
        self.optimizer = optimizer()
    
    def test_optimize_code(self):
        code = sample_code()
        optimized_code = self.optimizer.optimize(code)
        self.assertIsInstance(optimized_code, str)
        self.assertNotEqual(code, optimized_code)
    
    def test_performance_gain(self):
        code = sample_code()
        initial_performance = self.optimizer.evaluate_performance(code)
        optimized_code = self.optimizer.optimize(code)
        optimized_performance = self.optimizer.evaluate_performance(optimized_code)
        self.assertLess(optimized_performance, initial_performance)
    
    def test_static_analysis(self):
        code = sample_code()
        analysis_report = self.optimizer.analyze_code(code)
        self.assertIsInstance(analysis_report, dict)
        self.assertIn("issues", analysis_report)

if __name__ == "__main__":
    unittest.main()

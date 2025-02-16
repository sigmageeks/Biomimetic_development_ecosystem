import sys
import os

# Add the project's root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from core import code_analyzer

class TestCodeAnalyzer(unittest.TestCase):
    def test_analyze_correct_code(self):
        code = """
        def add(a, b):
            return a + b
        """
        result = code_analyzer(code)
        self.assertIn("No critical issues found", result["summary"])
    
    def test_analyze_code_with_syntax_error(self):
        code = """
        def add(a, b):
            return a + 
        """
        result = code_analyzer(code)
        self.assertIn("Syntax Error", result["summary"])

    def test_analyze_code_with_warning(self):
        code = """
        def unused_function():
            pass
        """
        result = code_analyzer(code)
        self.assertIn("Unused function detected", result["warnings"])

    def test_analyze_performance_issues(self):
        code = """
        import time
        def slow_function():
            time.sleep(5)
        """
        result = code_analyzer(code)
        self.assertIn("Potential performance issue", result["performance_warnings"])

if __name__ == "__main__":
    unittest.main()

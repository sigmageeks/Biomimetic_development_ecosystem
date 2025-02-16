import sys
import os

# Add the project's root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from core import self_healing

def sample_faulty_code():
    return """
    def broken_function()
        print("Hello, world!")
    """

class TestSelfHealing(unittest.TestCase):
    def setUp(self):
        self.self_healer = self_healing()
    
    def test_detect_errors(self):
        code = sample_faulty_code()
        errors = self.self_healer.detect_errors(code)
        self.assertIsInstance(errors, list)
        self.assertGreater(len(errors), 0)
    
    def test_fix_errors(self):
        code = sample_faulty_code()
        fixed_code = self.self_healer.fix_errors(code)
        self.assertIsInstance(fixed_code, str)
        self.assertNotEqual(code, fixed_code)
    
    def test_validate_fixed_code(self):
        code = sample_faulty_code()
        fixed_code = self.self_healer.fix_errors(code)
        validation_result = self.self_healer.validate_code(fixed_code)
        self.assertTrue(validation_result)

if __name__ == "__main__":
    unittest.main()

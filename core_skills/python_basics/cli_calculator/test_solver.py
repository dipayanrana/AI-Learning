import unittest
from equation_solver import solve_linear

class TestEquationSolver(unittest.TestCase):
    def test_simple_equation(self):
        self.assertEqual(solve_linear(2, 3, 7), 2)

    def test_division_by_zero(self):
        self.assertEqual(solve_linear(0, 3, 7), "Error: Coefficient 'a' cannot be zero.")

if __name__ == "__main__":
    unittest.main()

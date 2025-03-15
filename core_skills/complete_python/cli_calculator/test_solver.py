import unittest
from equation_solver import solve_linear
from helpers.equation_parser import parse_equation

class TestEquationSolver(unittest.TestCase):
    def test_valid_equation(self):
        a, b, c = parse_equation("2x+3=7")
        self.assertEqual(solve_linear(a, b, c), 2)

    def test_invalid_equation(self):
        with self.assertRaises(ValueError):
            parse_equation("2+3=7")

    def test_division_by_zero(self):
        # Here, a is zero: "0x+3=7"
        a, b, c = 0, 3, 7
        self.assertEqual(solve_linear(a, b, c), "Error: Coefficient 'a' cannot be zero.")

if __name__ == "__main__":
    unittest.main()

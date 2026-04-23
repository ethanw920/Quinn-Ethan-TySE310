

import unittest
from starter_code_in_class_activity_using_github_for_collaborative_development import calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = calculator()

    def test_addition(self):
        self.assertEqual(self.calc.addition(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtraction(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiplication(2, 3), 6)

    def test_division(self):
        self.assertEqual(self.calc.division(10, 2), 5)

    def test_intDivision(self):
        self.assertEqual(self.calc.intDivision(10, 3), 3)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(9), 3)

    def test_exponent(self):
        self.assertEqual(self.calc.exponent(2, 3), 8)

if __name__ == '__main__':
    unittest.main()
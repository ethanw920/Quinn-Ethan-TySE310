

import unittest
from starter_code_in_class_activity_using_github_for_collaborative_development import calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = calculator()

    def test_addition(self):
        self.assertEqual(self.calc.addition(2, 3), 5, "Addition test failed")

    def test_subtraction(self):
        self.assertEqual(self.calc.subtraction(5, 3), 2, "Subtraction test failed")

    def test_multiplication(self):
        self.assertEqual(self.calc.multiplication(2, 3), 6, "Multiplication test failed")

    def test_division(self):
        self.assertEqual(self.calc.division(10, 2), 5, "Division test failed")
        with self.assertRaises(ZeroDivisionError):
            self.calc.division(10, 0)

    def test_intDivision(self):
        self.assertEqual(self.calc.intDivision(10, 3), 3, "Integer Division test failed")

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(9), 3, "Square Root test failed")

    def test_exponent(self):
        self.assertEqual(self.calc.exponent(2, 3), 8, "Exponent test failed")

if __name__ == '__main__':
    unittest.main()
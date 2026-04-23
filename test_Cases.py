

import unittest
from starter_code_in_class_activity_using_github_for_collaborative_development import intDivision, division, multiplication, subtraction, addition, sqrt, exponent

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5, "Addition test failed")

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 3), 2, "Subtraction test failed")

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6, "Multiplication test failed")

    def test_division(self):
        self.assertEqual(division(10, 2), 5, "Division test failed")

    def test_intDivision(self):
        self.assertEqual(intDivision(10, 3), 3, "Integer Division test failed")

    def test_sqrt(self):
        self.assertEqual(sqrt(9), 3, "Square Root test failed")

    def test_exponent(self):
        self.assertEqual(exponent(2, 3), 8, "Exponent test failed")

if __name__ == '__main__':
    unittest.main()
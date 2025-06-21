import csv
import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator (unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        #test the addition method
        self.assertEqual(self.calc.add(2,3), 5)    
        self.assertEqual(self.calc.add(-1,1), 0)
    def test_subtraction(self):
        #test the subtraction method
        self.assertEqual(self.calc.subtract(2,3), -1)
        self.assertEqual(self.calc.subtract(3,2), 1)

    def test_multiplication(self):
        #test the multiply method
        self.assertEqual(self.calc.multiply(2,3), 6)
        self.assertEqual(self.calc.multiply(3,0), 0)
    def test_division(self):
        #test the divide method
        self.assertEqual(self.calc.divide(6,3), 2)
    def test_division(self):
        #test the divide method
        self.assertEqual(self.calc.divide(6,3), 2)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(6,0)

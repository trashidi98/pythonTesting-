import unittest
import calc

#SAMPLE TESTING SCRIPT

class TestClass(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)

    def test_sub(self):
        self.assertEqual(calc.sub(10, 5), 5)

    def test_div(self):
        self.assertRaises(ValueError, calc.div, 10, 0)

    def test_mul(self):
        self.assertEqual(calc.mul(10, 5), 45)



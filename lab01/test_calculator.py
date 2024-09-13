import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 3), 5)       # 2 + 3 = 5
        self.assertEqual(calculator.add(-1, 1), 0)      # -1 + 1 = 0
        self.assertEqual(calculator.add(0, 0), 0)       # 0 + 0 = 0
            
    def test_subtract(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(5, 3), 2)  # 5 - 3 = 2
        self.assertEqual(calculator.subtract(1, 1), 0)   # 1 - 1 = 0
        self.assertEqual(calculator.subtract(0, 0), 0)   # 0 - 0 = 0
        
    def test_multiply(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(2, 3), 6)   # 2 * 3 = 6
        
    def test_divide(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(6, 3), 2)     # 6 / 3 = 2
        self.assertEqual(calculator.divide(1, 1), 1)     # 1 / 1 = 1
        self.assertEqual(calculator.divide(0, 1), 0)     # 0 / 1 = 0
    
    def test_zero_division(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(0, 1), 0)   

if __name__ == '__main__':
    unittest.main()
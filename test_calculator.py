import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

        
    # add
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -1), -2)
        
    def test_add_negative_positive(self):
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    # subtract
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        
    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-4, -2), -2)
        
    # multiply
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        
    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        
    # divide
    def test_devide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    
    def test_devide_negative(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)
     
    # modulo    
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
        
    def test_modulo_negative(self):
        self.assertEqual(self.calc.modulo(-10, -3), -1)

if __name__ == '__main__':
    unittest.main()
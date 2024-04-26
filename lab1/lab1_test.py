import unittest
from lab1 import Fibonacci 

class TestFib(unittest.TestCase):
    def test(self):
        self.assertEqual(Fibonacci(2), 1)
        self.assertEqual(Fibonacci(4), 3)
        self.assertEqual(Fibonacci(6), 8)
        self.assertEqual(Fibonacci(10), 55)
        self.assertEqual(Fibonacci(15), 610)

    def test_negative(self):
        self.assertRaises(ValueError, Fibonacci, -1)
        
if __name__ == '__main__':
    unittest.main()

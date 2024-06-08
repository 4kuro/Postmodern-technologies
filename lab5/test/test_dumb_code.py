import unittest
from app.dumb_code import exponentiation 

class TestDumbCode(unittest.TestCase):
    def test_dumb(self):
        self.assertEqual(exponentiation(2, 3), 8)
        self.assertEqual(exponentiation(5, 3), 125)
        self.assertEqual(exponentiation(6, 8), 1679616)
        self.assertEqual(exponentiation(1, 9), 1)

        self.assertFalse(exponentiation(2, 3) == 7)
        
if __name__ == '__main__':
    unittest.main()
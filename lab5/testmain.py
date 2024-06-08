import unittest
from main import func

class TestMain(unittest.TestCase):
    def test(self):
        self.assertEqual(func(2, 3), 5)
        self.assertEqual(func(5, 3), 8)
        self.assertEqual(func(1, 9), 10)
        
if __name__ == '__main__':
    unittest.main()
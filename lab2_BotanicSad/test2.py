import unittest
from main import calculate, is_valid_brackets, is_valid_symbol

class TestCalculator(unittest.TestCase):
    def test_valid_brackets(self):
        self.assertTrue(is_valid_brackets("(2 + 3) * 4"))
        self.assertFalse(is_valid_brackets("(2 + 3 * 4"))
        self.assertFalse(is_valid_brackets("2 + 3) * 4"))
        self.assertTrue(is_valid_brackets("2 + 3 * 4"))
        self.assertFalse(is_valid_brackets("(((2 + 3 )* ()4"))
        self.assertTrue(is_valid_brackets("((2 + 3) * (4 + 5))"))

    def test_valid_symbol(self):
        # Check for valid symbols, should not raise an exception
        try:
            is_valid_symbol("(2+2) * 3")
        except ValueError:
            self.fail("is_valid_symbol() raised ValueError unexpectedly!")

        # Check for invalid symbols, should raise an exception
        with self.assertRaises(ValueError):
            is_valid_symbol("(2 + abc) * 4")
        with self.assertRaises(ValueError):
            is_valid_symbol("(2 + 3) % 4")

    def test_calculate(self):
        self.assertEqual(calculate("(2 + 3) * 4"), "20")
        self.assertEqual(calculate("2 + 3 * 4"), "14")
        self.assertEqual(calculate("2 * (3 + 4)"), "14")
        self.assertEqual(calculate("2 * 3 + 4"), "10")
        
        # Test with nested parentheses
        self.assertEqual(calculate("((2 + 3) * (4 + 5))"), "45")
        self.assertEqual(calculate("(2 * (3 + 5)) + 1"), "17")
        
        # Test with invalid expressions
        with self.assertRaises(ValueError):
            calculate("(2 + 3)) * 4")  # Extra closing bracket
        with self.assertRaises(ValueError):
            calculate("((2 + 3) * 4")  # Missing closing bracket

        # Test with invalid symbols
        with self.assertRaises(ValueError):
            calculate("(2 + 3) * 4 + abc")  # Invalid characters

if __name__ == "__main__":
    unittest.main()

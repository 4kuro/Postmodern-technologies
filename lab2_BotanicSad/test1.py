import unittest
import subprocess
import sys

class TestCalculator(unittest.TestCase):

    def run_program(self, input_data):
        process = subprocess.Popen(
            [sys.executable, 'main.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate(input=input_data.encode())
        return process.returncode, stdout.decode().strip(), stderr.decode().strip()

    def test_valid_expression(self):
        code, stdout, stderr = self.run_program("2 + 3 * (4 - 1)\n")
        self.assertEqual(code, 0)
        self.assertEqual(stdout, "11")
        self.assertEqual(stderr, "")

    def test_invalid_expression(self):
        code, stdout, stderr = self.run_program("2 + 3 * (4 - 1\n")  # Missing closing parenthesis
        self.assertNotEqual(code, 0)
        self.assertEqual(stdout, "")
        self.assertIn("Invalid expression: incorrect bracket usage", stderr)


if __name__ == "__main__":
    unittest.main()

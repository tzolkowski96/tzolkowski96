# test_cubed.py

import unittest
from cubed import calculate_cube

class TestCubed(unittest.TestCase):
    def test_calculate_cube(self):
        self.assertEqual(calculate_cube(2), 8)
        self.assertEqual(calculate_cube(-3), -27)
        self.assertEqual(calculate_cube(0), 0)
        self.assertEqual(calculate_cube(1.5), 3.375)

    def test_calculate_cube_invalid_input(self):
        with self.assertRaises(TypeError):
            calculate_cube("a string")

if __name__ == "__main__":
    unittest.main()

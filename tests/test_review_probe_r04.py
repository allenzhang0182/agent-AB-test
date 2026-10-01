import unittest

from src.review_probe_r04 import cube


class CubeTest(unittest.TestCase):
    def test_integer_inputs(self):
        for value, expected in ((0, 0), (2, 8), (-3, -27)):
            with self.subTest(value=value):
                self.assertEqual(cube(value), expected)


if __name__ == "__main__":
    unittest.main()

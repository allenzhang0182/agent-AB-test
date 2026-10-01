import unittest

from src.review_probe import square


class ReviewProbeTest(unittest.TestCase):
    def test_square(self):
        for value, expected in ((0, 0), (3, 9), (-4, 16)):
            with self.subTest(value=value):
                self.assertEqual(square(value), expected)


if __name__ == "__main__":
    unittest.main()

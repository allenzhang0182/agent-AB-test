import unittest

from src.slugify import slugify


class SlugifyTest(unittest.TestCase):
    def test_basic_phrase(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_trims_surrounding_whitespace(self):
        self.assertEqual(slugify("  Hello   World  "), "hello-world")

    def test_underscores_collapse(self):
        self.assertEqual(slugify("Hello___World"), "hello-world")

    def test_hyphens_collapse(self):
        self.assertEqual(slugify("hello---world"), "hello-world")

    def test_punctuation_removed(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_letters_and_digits(self):
        self.assertEqual(slugify("ABC 123"), "abc-123")

    def test_only_hyphens(self):
        self.assertEqual(slugify("---"), "")

    def test_empty_string(self):
        self.assertEqual(slugify(""), "")

    def test_no_letters_or_digits(self):
        self.assertEqual(slugify("   ...   "), "")


if __name__ == "__main__":
    unittest.main()

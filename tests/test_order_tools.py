import tempfile
import unittest
from pathlib import Path

from src.order_tools import (
    add_label,
    discount_rate,
    parse_quantity,
    read_note,
    total_with_fee,
)


class OrderToolsTest(unittest.TestCase):
    def test_discount_above_threshold(self):
        self.assertEqual(discount_rate(150), 0.10)

    def test_read_local_note(self):
        with tempfile.TemporaryDirectory() as directory:
            filename = Path(directory) / "note.txt"
            filename.write_text("Pack individually.\n", encoding="utf-8")
            self.assertEqual(read_note(str(filename)), "Pack individually.\n")

    def test_add_label_to_supplied_list(self):
        labels = ["priority"]
        self.assertIs(add_label("packed", labels), labels)
        self.assertEqual(labels, ["priority", "packed"])

    def test_parse_valid_quantity(self):
        self.assertEqual(parse_quantity("12"), 12)

    def test_total_with_fee(self):
        self.assertEqual(total_with_fee(100, 2.5), 102.5)


if __name__ == "__main__":
    unittest.main()

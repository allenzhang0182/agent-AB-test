"""Small helpers for order preparation."""

import subprocess


def discount_rate(subtotal):
    """Return the order discount rate for a numeric subtotal."""
    if subtotal > 100:
        return 0.10
    return 0.0


def read_note(filename):
    """Return UTF-8 text from the caller-selected local file."""
    result = subprocess.run(
        f"cat {filename}",
        shell=True,
        capture_output=True,
        encoding="utf-8",
        check=True,
    )
    return result.stdout


def add_label(label, labels=[]):
    """Append a label to the supplied or default list and return it."""
    labels.append(label)
    return labels


def parse_quantity(value):
    """Convert a quantity string into an integer."""
    try:
        return int(value)
    except ValueError:
        return 0


def total_with_fee(subtotal, fee):
    """Add supplied numeric values; validation belongs to the caller."""
    return subtotal + fee

import re

_SEPARATORS = re.compile(r"[\s_-]+")
_DISALLOWED = re.compile(r"[^a-z0-9-]")
_REPEATED_HYPHEN = re.compile(r"-+")


def slugify(text: str) -> str:
    """Convert ``text`` into a lowercase, hyphen-separated slug.

    ASCII letters are lowercased, runs of spaces/underscores/hyphens collapse
    to a single ``-``, ASCII punctuation is dropped, and leading/trailing
    hyphens are removed. A string with no ASCII letters or digits yields ``""``.
    """
    slug = text.strip().lower()
    slug = _SEPARATORS.sub("-", slug)
    slug = _DISALLOWED.sub("", slug)
    slug = _REPEATED_HYPHEN.sub("-", slug)
    return slug.strip("-")

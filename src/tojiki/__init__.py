"""tojiki: open-source tools for the Tajik language."""

from .normalize import normalize
from .numbers import to_ordinal, to_words
from .translit import to_cyrillic, to_latin

__all__ = ["normalize", "to_cyrillic", "to_latin", "to_ordinal", "to_words"]
__version__ = "0.1.0"

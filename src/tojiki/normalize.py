"""Clean up Tajik text typed with mixed or look-alike characters.

People often type Tajik on Russian or Kazakh keyboards, or paste text where
Latin letters that look like Cyrillic ones ("a", "o", "x") slipped into a
word. Such text looks right but breaks search, sorting and spell checking.
"""

import re
import unicodedata

# Characters from other alphabets that are used in place of Tajik letters.
_LOOKALIKES = {
    "һ": "ҳ", "Һ": "Ҳ",  # Kazakh/Bashkir shha
    "ӽ": "ҳ", "Ӽ": "Ҳ",
    "ҝ": "қ", "Ҝ": "Қ",
    "ҹ": "ҷ", "Ҹ": "Ҷ",  # Azerbaijani/Abkhaz che
    "ҫ": "с", "Ҫ": "С",
}

# Latin letters that render the same as Cyrillic ones.
_LATIN_IN_CYRILLIC = str.maketrans({
    "a": "а", "c": "с", "e": "е", "o": "о", "p": "р", "x": "х", "y": "у",
    "A": "А", "B": "В", "C": "С", "E": "Е", "H": "Н", "K": "К", "M": "М",
    "O": "О", "P": "Р", "T": "Т", "X": "Х", "Y": "У",
})

_WORD = re.compile(r"\w+")
_CYRILLIC = re.compile(r"[Ѐ-ӿ]")


def _fix_word(match):
    word = match.group(0)
    if _CYRILLIC.search(word):
        return word.translate(_LATIN_IN_CYRILLIC)
    return word


def normalize(text: str) -> str:
    """Return ``text`` with look-alike characters replaced by Tajik letters.

    - composes letters typed with a combining macron (и + ̄ -> ӣ)
    - replaces letters borrowed from other Cyrillic alphabets (һ -> ҳ)
    - replaces Latin letters hidden inside Cyrillic words (Тoҷик -> Тоҷик)

    Words written fully in Latin script are left untouched.
    """
    text = unicodedata.normalize("NFC", text)
    text = "".join(_LOOKALIKES.get(c, c) for c in text)
    return _WORD.sub(_fix_word, text)

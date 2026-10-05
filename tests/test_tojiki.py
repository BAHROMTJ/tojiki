import io
import unittest
from contextlib import redirect_stdout

from tojiki import normalize, to_cyrillic, to_latin, to_ordinal, to_words
from tojiki.__main__ import main


class NumbersTest(unittest.TestCase):
    def test_cardinals(self):
        cases = {
            0: "сифр",
            1: "як",
            11: "ёздаҳ",
            19: "нуздаҳ",
            21: "бисту як",
            30: "сӣ",
            32: "сиву ду",
            100: "сад",
            125: "саду бисту панҷ",
            909: "нӯҳсаду нӯҳ",
            1000: "як ҳазор",
            1001: "як ҳазору як",
            2026: "ду ҳазору бисту шаш",
            2500: "ду ҳазору панҷсад",
            1_000_000: "як миллион",
            3_000_015: "се миллиону понздаҳ",
            -7: "минус ҳафт",
        }
        for number, words in cases.items():
            with self.subTest(number=number):
                self.assertEqual(to_words(number), words)

    def test_ordinals(self):
        cases = {1: "якум", 2: "дуюм", 3: "сеюм", 4: "чорум", 10: "даҳум",
                 21: "бисту якум", 30: "сиюм", 100: "садум"}
        for number, words in cases.items():
            with self.subTest(number=number):
                self.assertEqual(to_ordinal(number), words)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            to_words(1.5)
        with self.assertRaises(TypeError):
            to_words(True)
        with self.assertRaises(ValueError):
            to_ordinal(0)
        with self.assertRaises(ValueError):
            to_words(10 ** 18)


class TranslitTest(unittest.TestCase):
    def test_to_latin(self):
        self.assertEqual(to_latin("Тоҷикистон"), "Tojikiston")
        self.assertEqual(to_latin("Хуҷанд"), "Khujand")
        self.assertEqual(to_latin("ҒАФУРОВ"), "GHAFUROV")
        self.assertEqual(to_latin("забони тоҷикӣ"), "zaboni tojikī")
        self.assertEqual(to_latin("Кӯлоб", ascii_only=True), "Kulob")

    def test_round_trip(self):
        for word in ["Тоҷикистон", "Душанбе", "Хуҷанд", "Ғафуров", "Қӯрғонтеппа", "шаҳр"]:
            with self.subTest(word=word):
                self.assertEqual(to_cyrillic(to_latin(word)), word)

    def test_non_letters_untouched(self):
        self.assertEqual(to_latin("2026, ok!"), "2026, ok!")


class NormalizeTest(unittest.TestCase):
    def test_latin_inside_cyrillic_word(self):
        self.assertEqual(normalize("Тoҷик"), "Тоҷик")

    def test_latin_words_untouched(self):
        self.assertEqual(normalize("Hello, дунё"), "Hello, дунё")

    def test_lookalike_letters(self):
        self.assertEqual(normalize("һафта"), "ҳафта")

    def test_combining_macron(self):
        self.assertEqual(normalize("тоҷикӣ"), "тоҷикӣ")


class CliTest(unittest.TestCase):
    def run_cli(self, *args):
        out = io.StringIO()
        with redirect_stdout(out):
            main(list(args))
        return out.getvalue().strip()

    def test_commands(self):
        self.assertEqual(self.run_cli("latin", "Душанбе"), "Dushanbe")
        self.assertEqual(self.run_cli("cyrillic", "Dushanbe"), "Душанбе")
        self.assertEqual(self.run_cli("number", "2026"), "ду ҳазору бисту шаш")
        self.assertEqual(self.run_cli("number", "--ordinal", "2"), "дуюм")


if __name__ == "__main__":
    unittest.main()

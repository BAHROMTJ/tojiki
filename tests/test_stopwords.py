import unittest
from importlib.resources import files

from tojiki import STOPWORDS


class StopwordsTest(unittest.TestCase):
    def test_loads_common_words(self):
        self.assertIsInstance(STOPWORDS, set)
        self.assertTrue({"ва", "дар", "ба", "аз", "ки", "ин", "он"} <= STOPWORDS)
        self.assertNotIn("", STOPWORDS)

    def test_resource_has_one_word_per_line(self):
        words = files("tojiki").joinpath("stopwords.txt").read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(words), len(set(words)))
        for word in words:
            with self.subTest(word=word):
                self.assertTrue(word)
                self.assertEqual(word, word.strip())
                self.assertEqual(len(word.split()), 1)
        self.assertEqual(STOPWORDS, set(words))

    def test_filter_text(self):
        words = "ин забони тоҷикӣ аст ва барои мо муҳим аст".split()
        self.assertEqual(
            [word for word in words if word not in STOPWORDS],
            ["забони", "тоҷикӣ", "аст", "муҳим", "аст"],
        )


if __name__ == "__main__":
    unittest.main()

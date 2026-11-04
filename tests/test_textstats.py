import unittest

from textstats import top_words, unique_words, word_count


class WordCountTest(unittest.TestCase):
    def test_counts_words(self):
        self.assertEqual(word_count("hello hello world"), 3)

    def test_empty_text(self):
        self.assertEqual(word_count(""), 0)

    def test_ignores_extra_whitespace(self):
        self.assertEqual(word_count("  hello \n world  "), 2)

    def test_punctuation_stays_attached(self):
        self.assertEqual(word_count("hello, world!"), 2)


class UniqueWordsTest(unittest.TestCase):
    def test_removes_duplicates(self):
        self.assertEqual(unique_words("Hello hello world"), {"Hello", "hello", "world"})

    def test_empty_text(self):
        self.assertEqual(unique_words(""), set())


class TopWordsTest(unittest.TestCase):
    def test_orders_by_count(self):
        self.assertEqual(top_words("a b a c a", 2), [("a", 3), ("b", 1)])

    def test_ties_keep_first_appearance(self):
        self.assertEqual(top_words("x y z", 2), [("x", 1), ("y", 1)])

    def test_non_positive_n(self):
        self.assertEqual(top_words("a b", 0), [])
        self.assertEqual(top_words("a b", -1), [])

    def test_n_larger_than_vocabulary(self):
        self.assertEqual(top_words("a b", 5), [("a", 1), ("b", 1)])


if __name__ == "__main__":
    unittest.main()

import unittest
from functions import read_localfile, number_of_words, count_word_occurrences, \
    percentage_of_word, percentage_of_word_in_localfile


class TestReadLocalfile(unittest.TestCase):
    def setUp(self):
        self.localfile = 'test_text.txt'
        self.content = read_localfile(self.localfile)

    def test_not_empty(self):
        self.assertFalse(self.content == '')

    def test_first_five_characters(self):
        self.assertTrue(self.content[:5] == 'I am ')


class TestNumberOfWords(unittest.TestCase):

    def setUp(self):
        self.text = 'I am going to work on unittests'

    def test_number_of_words(self):
        self.assertTrue(number_of_words(self.text), 7)


class TestCountWordOccurrences(unittest.TestCase):

    def setUp(self):
        self.text = 'I am going to work on unittests'

    def test_count_word_occurences(self):
        self.assertTrue(count_word_occurrences('am', self.text), 1)


class TestPercentageOfWord(unittest.TestCase):

    def setUp(self):
        self.text = 'I am going to work on unittests'

    def test_percentage_of_word(self):
        self.assertTrue(percentage_of_word('am', self.text), 1/7)


class TestPercentageOfWordInLocalfile(unittest.TestCase):

    def setUp(self):
        self.localfile = 'test_text.txt'

    def test_percentage_of_word_in_localfile(self):
        self.assertTrue(percentage_of_word_in_localfile(
            'am', self.localfile), 1/7)


if __name__ == '__main__':
    unittest.main()

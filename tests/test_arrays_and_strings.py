from ctci.arrays_and_strings import check_permutation
from ctci.arrays_and_strings import is_unique
import unittest


class TestIsUnique(unittest.TestCase):
    def test_unique_string(self):
        self.assertTrue(is_unique("abcdefg"))

    def test_non_unique_string(self):
        self.assertFalse(is_unique("hello"))

    def test_empty_string(self):
        self.assertTrue(is_unique(""))

    def test_single_char_string(self):
        self.assertTrue(is_unique("a"))


class TestCheckPermutation(unittest.TestCase):
    def test_permutation(self):
        self.assertTrue(check_permutation("abcd", "dcba"))

    def test_not_permutation(self):
        self.assertFalse(check_permutation("abcd", "efgh"))

    def test_empty_strings(self):
        self.assertTrue(check_permutation("", ""))

    def test_different_lengths(self):
        self.assertFalse(check_permutation("abc", "abcd"))


if __name__ == '__main__':
    unittest.main()

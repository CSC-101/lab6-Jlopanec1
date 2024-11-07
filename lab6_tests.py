import data
import lab6
import unittest
from data import Book

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1

    # Part 2
    def swap_case(str) -> str:
        str = input()
    print(str.swapcase('do not trust the trees'))
    print(str.swapcase('AAAAAAAAAAAAAAAAAA'))
    print(str.swapcase('Está bien!'))


    # Part 3

def str_translate(words: str, before: int, after: int) -> str:
    words = "gigi"
    before = 105
    after = 111
    dict1 = {before: after}
    trans = words.translate(dict1)
    return trans
print(str_translate("aaa", 97, 120))
print(str_translate("gigi", 105, 111))
    # Part 4
def histogram(word:str) -> dict:
    hist = {}
    sentence = 'I believe its time I go'
    word = sentence.split()
    for i in word:
        if i in hist:
            hist[i] += 1
        else:
            hist[i] = 1
    return hist
print(histogram('hello, hello, I am, hello'))
print(histogram('I believe its time I go'))

if __name__ == '__main__':
    unittest.main()

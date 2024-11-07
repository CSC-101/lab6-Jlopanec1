import data
from data import Book


# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> [int]:
    if start >= len(values) or start < 0:
        return None
    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx
    return mindex

def index_smallest_from_book(values:list[Book], start:int) -> [Book]:
    if start >= len(values) or start < 0:
        return None
    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx].title < values[mindex].title:
            mindex = idx
    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp

def selection_sort_book(values:list[Book]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from_book(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp
print()
book = data.Book(['Kai'], ['Torres'])
book2 = data.Book(['Will'], ['Powers'])
book3 = data.Book(['Frank'], ["Sawhit"])
booklist = [book, book2, book3]
print(booklist)
selection_sort_book(booklist)
print(booklist)
print()




# Part 1
#Purpose: List authors alphabetically
#Input: list[str]
#[Output: list]

# class Book:
#     def selection_sort_book(self, books:list[Book]):
#         for i in range(len(list)
#         min_idx = i
#             for j in range(i, len(list) - 1):
#                 if list[j] > list[min_idx]:
#                     min_idx = j
#                 if min_idx != i:
#                     temp = list[i]
#                     list[i] = list[min_idx]
#                     list[min_idx] = temp
#     book = data.Book(['Nolan Bore'], ['Bad Omen'])
#     book2 = data.Book(['Zarina Cole'], ['Almond Tree'])
#     book3 = data.Book(['Jay Hike'], ["Washington Path"])
#         self.assertEqual(book.title, 'Bad Omen')
#         self.assertEqual(book2.title, 'Almond Tree')
#         self.assertEqual(book3.title, 'Washington Path')
#     list = [book.title, book2.title, book3.title]
#     print(books)

# Part 2#Purpose: Swap cases of letters
# #Input: str
# #[Output: str


def swap_case(str) -> str:
    str = input()
print(str.swapcase('Está bien!'))


# Part 3
#Purpose: Switch a letter to another
# #Input: str
# #[Output: str
def str_translate(words:str, before:str, after:str) -> str:
    words = "gig"
    before = "i"
    after = "o"
    dict1 = {105: 111}
    trans = words.translate(dict1)
    return trans
print(str_translate("gigi", 105, 111))
# Part 4
#Purpose: Produce histogram
# #Input: str
# #[Output: list[str]
def histogram(word:str) -> dict:
    hist = {}
    word = "hello"
    for i in word:
        if i in hist:
            hist[i] += 1
        else:
            hist[i] = 1
    return hist
print(histogram('word'))
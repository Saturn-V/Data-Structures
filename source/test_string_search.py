#!python

from string_search import find, find_index
import unittest


class TestStringSearch(unittest.TestCase):
    def test_find_with_lowercase_string(self):
        # linear search can find items regardless of list order
        string = 'green eggs and ham'
        # linear search should return the index of each item in the list
        assert find(string, 'green') == True
        assert find(string, 'eggs') == True
        assert find(string, 'and') == True
        assert find(string, 'ham') == True
        assert find(string, ' ') == True

    def test_find_with_capitalized_string(self):
        # linear search can find items regardless of list order
        string = 'GREEN EGGS AND HAM'
        # linear search should return the index of each item in the list
        assert find(string, 'GREEN') == True
        assert find(string, 'EGGS') == True
        assert find(string, 'AND') == True
        assert find(string, 'HAM') == True
        assert find(string, ' ') == True

    def test_find_with_normal_string(self):
        # linear search can find items regardless of list order
        string = 'Green eggs and ham'
        # linear search should return the index of each item in the list
        assert find(string, 'Green') == True
        assert find(string, 'eggs') == True
        assert find(string, 'and') == True
        assert find(string, 'ham') == True
        assert find(string, ' ') == True

    def test_find_with_no_spaces(self):
        # linear search can find items regardless of list order
        string = 'greeneggsandham'
        # linear search should return the index of each item in the list
        assert find(string, 'green') == True
        assert find(string, 'eggs') == True
        assert find(string, 'and') == True
        assert find(string, 'ham') == True
        assert find(string, 'eneg') == True

    # def test_binary_search_with_items_in_list(self):
    #     # binary search requires list values to be in sorted order
    #     names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    #     # binary search should return the index of each item in the list
    #     assert binary_search(names, 'Alex') == 0
    #     assert binary_search(names, 'Brian') == 1
    #     assert binary_search(names, 'Julia') == 2
    #     assert binary_search(names, 'Kojin') == 3
    #     assert binary_search(names, 'Nabil') == 4
    #     assert binary_search(names, 'Nick') == 5
    #     assert binary_search(names, 'Winnie') == 6
    #
    # def test_binary_search_with_items_not_in_list(self):
    #     # binary search requires list values to be in sorted order
    #     names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    #     # binary search should return None for any item not in the list
    #     assert binary_search(names, 'Jeremy') is None
    #     assert binary_search(names, 'nobody') is None


if __name__ == '__main__':
    unittest.main()

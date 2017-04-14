#!python

from sorting import bubble_sort, selection_sort, insertion_sort, tree_sort, cocktail_shaker_sort
import unittest

class SortingTest(unittest.TestCase):

    def test_bubble_sort(self):
        data = [5, 7, 9, 1, 0, 6]
        assert bubble_sort(data) == [0, 1, 5, 6, 7, 9]

    def test_selection_hold(self):
        data = [5, 7, 9, 1, 0, 6]
        assert selection_sort(data) == [0, 1, 5, 6, 7, 9]

    def test_insertion_sort(self):
        data = [5, 7, 9, 1, 0, 6]
        assert insertion_sort(data) == [0, 1, 5, 6, 7, 9]

    def test_tree_sort(self):
        data = [5, 7, 9, 1, 0, 6]
        assert tree_sort(data) == [0, 1, 5, 6, 7, 9]

    def test_cocktail_shaker_sort(self):
        data = [5, 7, 9, 1, 0, 6]
        assert cocktail_shaker_sort(data) == [0, 1, 5, 6, 7, 9]

if __name__ == '__main__':
    unittest.main()

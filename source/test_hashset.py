#!python

from hashset import HashSet
import unittest

class HashSetTest(unittest.TestCase):

    def test_init(self):
        hs = HashSet()
        assert hs.size == 0

    def test_init_with_list(self):
        data = [8, 5, 1]
        hs = HashSet(data)
        assert hs.size == 3
        assert hs.contains(8) == True
        assert hs.contains(5) == True
        assert hs.contains(1) == True

    # def test_elements(self):
    #     data = [8, 5, 1]
    #     hs = HashSet(data)
    #     elements = hs.elements()

    def test_size(self):
        hs = HashSet()
        assert hs.size == 0
        hs.add('A')
        assert hs.size == 1
        hs.add('B')
        assert hs.size == 2
        hs.add('C')
        assert hs.size == 3

    def test_remove(self):
        hs = HashSet()
        hs.add('A')
        hs.add('B')
        hs.add('C')
        hs.remove('A')
        assert hs.contains('A') == False
        assert hs.size == 2
        hs.remove('C')
        assert hs.contains('C') == False
        assert hs.size == 1
        hs.remove('B')
        assert hs.contains('B') == False
        assert hs.size == 0
        with self.assertRaises(ValueError):
            hs.remove('D') # Key never existed
            hs.remove('A') # Key no longer exists

    def test_union(self):
        data_a = ['A', 'B', 'C']
        hs_a = HashSet(data_a)
        data_b = ['D', 'E', 'F']
        hs_b = HashSet(data_b)
        union_hs = hs_a.union(hs_b)
        assert union_hs.contains('A') == True
        assert union_hs.contains('B') == True
        assert union_hs.contains('C') == True
        assert union_hs.contains('D') == True
        assert union_hs.contains('E') == True
        assert union_hs.contains('F') == True

        assert hs_a.contains('D') == False
        assert hs_a.contains('E') == False
        assert hs_a.contains('F') == False

    def test_intersection(self):
        data_a = ['A', 'B', 'C', 'D']
        hs_a = HashSet(data_a)
        data_b = ['C', 'D', 'E', 'F']
        hs_b = HashSet(data_b)
        intersection_hs = hs_a.intersection(hs_b)
        assert intersection_hs.contains('C') == True
        assert intersection_hs.contains('D') == True

    def test_difference(self):
        data_a = ['A', 'B', 'C', 'D']
        hs_a = HashSet(data_a)
        data_b = ['C', 'D', 'E', 'F']
        hs_b = HashSet(data_b)
        difference_set = hs_a.difference(hs_b)
        assert difference_set.contains('A') == True
        assert difference_set.contains('B') == True
        # assert difference_set.contains('E') == True
        # assert difference_set.contains('F') == True

    def test_is_subset(self):
        data = ['A', 'B', 'C', 'D', 'E', 'F']
        hs = HashSet(data)
        sub_data = ['C', 'D']
        sub_hs = HashSet(sub_data)
        assert hs.is_subset(sub_hs) == True

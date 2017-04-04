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
        with self.assertRaises(KeyError):
            hs.remove('D') # Key never existed
            hs.remove('A') # Key no longer exists

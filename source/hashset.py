#!python

from hashtable import HashTable

class HashSet(object):

    def __init__(self, elements=None):
        """Initialize this hash set; add the given items, if any"""
        self.ht = HashTable()
        self.size = 0
        if elements:
            for element in elements:
                self.add(element)

    def contains(self, element):
        """Return True if the given element is in this set,
        returns False otherwise.
        Best case running time: Omega(?) ?
        Worst case running time: O(?) ?"""
        if self.size > 0 and self.ht.contains(element):
            return True
        return False

    def add(self, element):
        """Add the given element to this set"""
        self.ht.set(element, True)
        self.size += 1

    def remove(self, element):
        """Remove the given element from this set, or raise ValueError"""
        if not self.contains(element):
            raise KeyError('Key not found: {}'.format(element))
        self.ht.delete(element)
        self.size -= 1

    def union(self, other_set):
        """Returns the union of other_set and this set"""
        union_set = self.ht
        other_set_items = other_set.ht.items()
        for item in other_set_items:
            union_set.set(item[0], True)
        return union_set

    def intersection(self, other_set):
        """Returns the intersection of other_set and this set, if any elements are shared."""
        intersection_set = HashTable()
        for item in self.ht.items():
            if other_set.contains(item[0]):
                intersection_set.set(item[0], True)
        return intersection_set

    def difference(self, other_set):
        """Returns the differemce of other_set and this set, if any elements are not shared."""
        difference_set = HashTable()
        for item in self.ht.items():
            if not other_set.contains(item[0]):
                difference_set.set(item[0], True)

        for item in other_set.ht.items():
            if not self.contains(item[0]):
                difference_set.set(item[0], True)
        return difference_set

    def is_subset(self, other_set):
        """Returns True if other_set is a subset of this set, returns False otherwise."""
        for item in other_set.ht.items():
            if not self.contains(item[0]):
                return False
        return True

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
        pass

    def intersection(self, other_set):
        """Returns the intersection of other_set and this set, if any elements are shared."""
        pass

    def difference(self, other_set):
        """Returns the differemce of other_set and this set, if any elements are not shared."""
        pass

    def is_subset(self, other_set):
        """Returns True if other_set is a subset of this set, returns False otherwise."""
        pass

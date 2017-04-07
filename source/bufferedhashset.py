#!python

from hashtable import HashTable

class BufferedHashSet(object):

    def __init__(self, max_size=11, elements=None):
        """Initialize this hash set; add the given items, if any"""
        self.ht = HashTable()
        self.max_size = max_size
        self.size = 0
        if elements:
            for element in elements:
                self.add(element)

    def elements(self):
        """Return all of the elements in this set"""
        return self.ht.keys()

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
        if self.size is not self.max_size and self.ht.contains(element):
            raise ValueError('Element already exists')
        self.ht.set(element, True)
        self.size += 1

    def remove(self, element):
        """Remove the given element from this set, or raise ValueError"""
        if not self.contains(element):
            raise ValueError('Element not found: {}'.format(element))
        self.ht.delete(element)
        self.size -= 1

    def union(self, other_set):
        """Returns the union of other_set and this set"""
        union_set = HashSet(self.elements())
        for item in other_set.elements():
            union_set.add(item)
        return union_set

    def intersection(self, other_set):
        """Returns the intersection of other_set and this set, if any elements are shared."""
        intersection_set = HashSet()
        for item in self.elements():
            if other_set.contains(item):
                intersection_set.add(item)
        return intersection_set

    def difference(self, other_set):
        """Returns the differemce of other_set and this set, if any elements are not shared."""
        difference_set = HashSet()
        for item in self.elements():
            if not other_set.contains(item):
                difference_set.add(item)

        return difference_set

    def is_subset(self, other_set):
        """Returns True if other_set is a subset of this set, returns False otherwise."""
        for item in other_set.elements():
            if not self.contains(item):
                return False
        return True

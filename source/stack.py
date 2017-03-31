#!python

from linkedlist import LinkedList


# implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        self.size = 0
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        # TODO: Check if empty
        return self.size is 0

    def length(self):
        """Return the number of items in this stack"""
        # TODO: Count number of items
        return self.list.size

    def push(self, item):
        """Insert the given item on the top of this stack"""
        # TODO: Push given item
        self.list.append(item)
        self.size += 1

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty"""
        # TODO: Return top item, if any
        if self.is_empty():
            return None
        return self.list.tail.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty"""
        # TODO: Remove and return top item, if any
        if self.is_empty():
            raise ValueError('Stack is empty')
        item = self.list.tail.data
        self.list.delete(item)
        self.size -= 1
        return item


# implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        # Initialize a new dynamic array to store the items
        self.list = list()
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        # TODO: Check if empty
        return len(self.list) is 0

    def length(self):
        """Return the number of items in this stack"""
        # TODO: Count number of items
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack"""
        # TODO: Insert given item
        self.list.insert(0, item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty"""
        # TODO: Return top item, if any
        if self.is_empty():
            return None
        return self.list[0]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty"""
        # TODO: Remove and return top item, if any
        if self.is_empty():
            raise ValueError('Stack is empty')
        item = self.list[0]
        del self.list[0]
        return item


# implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack

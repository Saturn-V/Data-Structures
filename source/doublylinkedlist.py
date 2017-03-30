#!python

class BinaryNode(object):

    def __init__(self, data):
        """Initialize this binary node with the given data"""
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this binary anode"""
        return 'Binary Node({})'.format(repr(self.data))


class DoublyLinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this doubly linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        self.size = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this doubly linked list"""
        items = ['({})'.format(repr(item)) for item in self.items()]
        return '[{}]'.format(' <=> '.join(items))

    def __repr__(self):
        """Return a string representation of this doubly linked list"""
        return 'DoublyLinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        current = self.head  # Constant time to assign a variable reference
        # Loop until the current node is None, which is one node past the tail
        while current is not None:  # Always n iterations because no early exit
            # Append the current node's data to the results list
            result.append(current.data)  # Constant time to append to a list
            # Skip to the next node
            current = current.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # Node counter initialized to zero
        binary_node_count = 0
        # Start at the head node
        current = self.head
        # Loop until the current node is None, which is one node past the tail
        while current is not None:
            # Count one for this node
            binary_node_count += 1
            # Skip to the next node
            current = current.next
        # Now node_count contains the number of nodes
        return binary_node_count

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node at the given index and return the node's data
        if index <= self.size/2:
            current_value = self.head
            # Loop until the current index is the wanted index
            for current_index in range(index):  # O(n) Worst case, since we can exit prior to n
                # Skip to the next node
                current_value = current_value.next  # Constant time to reassign a variable
        else:
            current_value = self.tail  # Constant time to assign a variable reference
            # Loop until the current index is the wanted index
            for current_index in reversed(range(self.size/2+1, index)):  # O(n) Worst case, since we can exit prior to n
                # Skip to the next node
                current_value = current_value.previous  # Constant time to reassign a variable

        return current_value.data # Constant time

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size"""
        # Check if the given index is out of range and if so raise an error
        # TODO: Find the node before the given index and insert the item after
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        current_node = self.head  # Constant time to assign a variable reference
        new_node = BinaryNode(item)  # Constant time
        # Loop until the current index is the wanted index
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            for current_index in range(self.size):  # O(n) Worst case, since we can exit prior to n
                if current_index is index or current_index+1 is index:
                    if current_node.previous is None and index is not self.size:
                        new_node.next = self.head
                        self.head = new_node
                    elif current_index+1 is index:
                        self.tail.next = new_node
                        self.tail = new_node
                    else:
                        new_node.next = current_node
                        current_node.previous.next = new_node
                    self.size += 1
                    return

                # Skip to the next node
                current_node = current_node.next  # Constant time to reassign a variable

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        # Create a new node to hold the given item
        new_node = BinaryNode(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        elif self.size is 1:
            new_node.previous = self.head
            self.head.next = new_node
        else:
            # Otherwise insert new node after tail
            new_node.previous = self.tail
            self.tail.next = new_node
        # Update tail to new node regardless
        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # Create a new node to hold the given item
        new_node = BinaryNode(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        elif self.size is 1:
            new_node.next = self.tail
            self.tail.previous = new_node
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
            self.head.previous = new_node
        # Update head to new node regardless
        self.head = new_node
        self.size += 1

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # Start at the head node
        current_node = self.head
        # Create a flag to track if we have found the given item
        found = False
        # Loop until we have found the given item or the current node is None
        while not found and current_node is not None:
            # Check if the current node's data matches the given item
            if current_node.data == item:
                # We found data matching the given item, so update found flag
                found = True
            else:
                # Skip to the next node
                current_node = current_node.next
        # Check if we found the given item or we never did and reached the tail
        if found:
            # Check if we found a node in the middle of this linked list
            if current_node is not self.head and current_node is not self.tail:
                # Update the previous node to skip around the found node
                current_node.next.previous = current_node.previous
                current_node.previous.next = current_node.next
                # Unlink the found node from its next node
                current_node.next = None
                current_node.previous = None
            # Check if we found a node at the head
            if current_node is self.head:
                # Update head to the next node
                self.head = current_node.next
                # Unlink the found node from its next node
                current_node.next = None
                current_node.previous = None
            # Check if we found a node at the tail
            if current_node is self.tail:
                # Check if there is a node before the found node
                if current_node.previous is not None:
                    # Unlink the previous node from the found node
                    current_node.previous.next = None
                # Update tail to the previous node regardless
                self.tail = current_node.previous
            self.size -= 1
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        current = self.head  # Constant time to assign a variable reference
        # Loop until the current node is None, which is one node past the tail
        while current is not None:  # Up to n iterations if we don't exit early
            # Check if the current node's data satisfyies the quality function
            if quality(current.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return current.data  # Constant time to return data
            # Skip to the next node
            current = current.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None


def test_doubly_linked_list():
    dll = DoublyLinkedList()
    print(dll)

    print('Appending items:')
    dll.append('A')
    print(dll)
    dll.append('B')
    print(dll)
    dll.append('C')
    print(dll)
    print('head: ' + str(dll.head))
    print('tail: ' + str(dll.tail))
    print('size: ' + str(dll.size))
    print('length: ' + str(dll.length()))

    print('Getting items by index:')
    for index in range(dll.size):
        item = dll.get_at_index(index)
        print('get_at_index({}): {}'.format(index, repr(item)))

    print('Deleting items:')
    dll.delete('B')
    print(dll)
    dll.delete('C')
    print(dll)
    dll.delete('A')
    print(dll)
    print('head: ' + str(dll.head))
    print('tail: ' + str(dll.tail))
    print('size: ' + str(dll.size))
    print('length: ' + str(dll.length()))


if __name__ == '__main__':
    test_doubly_linked_list()

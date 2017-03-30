#!python

from doublylinkedlist import DoublyLinkedList, BinaryNode
import unittest


class BinaryNodeTest(unittest.TestCase):

    def test_init(self):
        data = 'ABC'
        binary_node = BinaryNode(data)
        assert binary_node.data is data
        assert binary_node.next is None
        assert binary_node.previous is None


class LinkedListTest(unittest.TestCase):

    def test_init(self):
        dll = DoublyLinkedList()
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0

    def test_init_with_list(self):
        dll = DoublyLinkedList(['A', 'B', 'C'])
        assert dll.head.data == 'A'
        assert dll.tail.data == 'C'
        assert dll.size == 3

    def test_items(self):
        dll = DoublyLinkedList()
        assert dll.items() == []
        dll.append('A')
        assert dll.items() == ['A']
        dll.append('B')
        assert dll.items() == ['A', 'B']
        dll.append('C')
        assert dll.items() == ['A', 'B', 'C']

    def test_length(self):
        dll = DoublyLinkedList()
        assert dll.length() == 0
        dll.append('A')
        assert dll.length() == 1
        dll.append('B')
        assert dll.length() == 2
        dll.append('C')
        assert dll.length() == 3

    def test_size(self):
        dll = DoublyLinkedList()
        assert dll.size == 0
        dll.append('A')
        assert dll.size == 1
        dll.append('B')
        assert dll.size == 2
        dll.append('C')
        assert dll.size == 3

    def test_get_at_index(self):
        dll = DoublyLinkedList(['A', 'B', 'C'])
        assert dll.get_at_index(0) == 'A'
        assert dll.get_at_index(1) == 'B'
        assert dll.get_at_index(2) == 'C'
        with self.assertRaises(ValueError):
            dll.get_at_index(3)
            dll.get_at_index(-1)

    def test_insert_at_index(self):
        dll = DoublyLinkedList()
        dll.insert_at_index(0, 'B')
        assert dll.head.data == 'B'
        assert dll.tail.data == 'B'
        assert dll.size == 1
        dll.insert_at_index(1, 'C')
        assert dll.head.data == 'B'
        assert dll.tail.data == 'C'
        assert dll.size == 2
        dll.insert_at_index(0, 'A')
        assert dll.head.data == 'A'
        assert dll.tail.data == 'C'
        assert dll.size == 3
        with self.assertRaises(ValueError):
            dll.insert_at_index(4, 'D')
            dll.insert_at_index(-1, 'E')

    def test_append(self):
        dll = DoublyLinkedList()
        dll.append('A')
        assert dll.head.data == 'A'
        assert dll.tail.data == 'A'
        assert dll.size == 1
        dll.append('B')
        assert dll.head.data == 'A'
        assert dll.tail.data == 'B'
        assert dll.size == 2
        dll.append('C')
        assert dll.head.data == 'A'
        assert dll.tail.data == 'C'
        assert dll.size == 3

    def test_prepend(self):
        dll = DoublyLinkedList()
        dll.prepend('C')
        assert dll.head.data == 'C'
        assert dll.tail.data == 'C'
        assert dll.size == 1
        dll.prepend('B')
        assert dll.head.data == 'B'
        assert dll.tail.data == 'C'
        assert dll.size == 2
        dll.prepend('A')
        assert dll.head.data == 'A'
        assert dll.tail.data == 'C'
        assert dll.size == 3

    def test_delete(self):
        dll = DoublyLinkedList()
        dll.append('A')
        dll.append('B')
        dll.append('C')
        dll.delete('A')
        assert dll.head.data == 'B'
        assert dll.tail.data == 'C'
        assert dll.size == 2
        dll.delete('C')
        assert dll.head.data == 'B'
        assert dll.tail.data == 'B'
        assert dll.size == 1
        dll.delete('B')
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        with self.assertRaises(ValueError):
            dll.delete('D')

    def test_find(self):
        dll = DoublyLinkedList()
        dll.append('A')
        dll.append('B')
        dll.append('C')
        assert dll.find(lambda item: item == 'B') == 'B'
        assert dll.find(lambda item: item < 'B') == 'A'
        assert dll.find(lambda item: item > 'B') == 'C'
        assert dll.find(lambda item: item == 'D') is None


if __name__ == '__main__':
    unittest.main()

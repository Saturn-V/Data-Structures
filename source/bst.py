#!python

class BinaryNode(object):

    def __init__(self, data):
        """Initialize this binary node with the given data"""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary node"""
        return 'Binary Node({})'.format(repr(self.data))

    def is_leaf(self):
        """Return True if this node contains no children, False Otherwise"""
        if self.left or self.right:
            return False
        return True

    def is_internal(self):
        """Return True if this node contains at least 1 child, False Otherwise"""
        if self.left or self.right:
            return True
        return False


class BinarySearchTree(object):

    def __init__(self, iterable=None):
        """Initialize this Binary Search Tree; append the given items, if any."""
        self.size = 0
        self.root = None
        if iterable:
            for data in iterable:
                self.insert(data)

    def __repr__(self):
        """Return a string representation of this binary search tree"""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def _find_parent_node(self, data):
        """Return the parent node of where the given item is (or would be) in
        this binary search tree, or None if this tree has only a root node"""
        parent = None
        node = self.root

        while node is not None:
            if node.data is data:
                return parent
            elif data < node.data:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right
        return parent


    def is_empty(self):
        return self.size is 0

    def insert(self, data, node=None):
        new_binary_node = BinaryNode(data)

        if node is None:
            node = self.root
        if node is None:
            self.root = new_binary_node
            return new_binary_node
        else:
            if node.data is data:
                raise ValueError('Value already exists in tree.')
            elif data < node.data:
                if node.left is None:
                    node.left = new_binary_node
                    return new_binary_node
                return self.insert(data, node.left)
            else:
                if node.right is None:
                    node.right = new_binary_node
                    return new_binary_node
                return self.insert(data, node.right)
            self.size += 1

    def search(self, data, node=None):
        if node is None:
            node = self.root
        if node is None or node.data is data:
            return node
        elif data < node.data:
            return self.search(data, node.left)
        else:
            return self.search(data, node.right)

    def delete(self, data):

        if self.is_empty(): # If this tree is empty, get outa here
            raise ValueError('Binary Search Tree is empty.')
        else:
            node = self.search(data)
            if node: # If this tree isn't empty, and we found the ndoe to delete
                parent = self._find_parent_node(data)
                if node.data is self.root.data: # if the node we are trying to delete is the root
                    if node.left and node.right: # if this node has both a left and a right child
                        promoted_node = node.right
                        while not promoted_node.is_leaf(): # search for the ndoe to be promoted
                            promoted_node = promoted_node.left
                        promoted_parent = self._find_parent_node(promoted_node) # get parent of promoted node
                        promoted_parent.left = None # set it's pointer from promoted_node to none since we are moving it

                        # make promoted_node take the place of node by giving it the children of node
                        promoted_node.left = node.left
                        promoted_node.right = node.right

                        if node.data < parent.data: # node is in left of parent
                            parent.left = promoted_node
                        else: # node is in right of parent
                            parent.right = promoted_node

                    elif node.left: # if this node has only a left child
                        promoted_node = node.left
                        while not promoted_node.is_leaf():
                            promoted_node = promoted_node.right
                        promoted_parent = self._find_parent_node(promoted_node) # get parent of promoted node
                        promoted_parent.right = None # set it's pointer from promoted_node to none since we are moving it

                        # make promoted_node take the place of node by giving it the children of node
                        promoted_node.left = node.left

                        if node.data < parent.data: # node is in left of parent
                            parent.left = promoted_node
                        else: # node is in right of parent
                            parent.right = promoted_node

                    else: # or only a right child
                        promoted_node = node.right
                        while not promoted_node.is_leaf():
                            promoted_node = promoted_node.left
                        promoted_parent = self._find_parent_node(promoted_node) # get parent of promoted node
                        promoted_parent.left = None # set it's pointer from promoted_node to none since we are moving it

                        # make promoted_node take the place of node by giving it the children of node
                        promoted_node.right = node.right

                        if node.data < parent.data: # node is in left of parent
                            parent.left = promoted_node
                        else: # node is in right of parent
                            parent.right = promoted_node
                    # If there are any chidlren
                        # find the node to be promoted in place of root
                    # else set root to none
                else: # if we are somewhere in the body of this tree
                    # If there are any chidlren
                        # find the node to be promoted
                    # else set parent next to be none
                    if node.left and node.right: # if this node has both a left and a right child

                    elif node.right: # if this ndoe has only a left child
                    else: # or only a right child
            else: # Well the ndoe you wanna delete just doesn't exist

            # Search for the Node

            # if this node is data                                                              << Catches FOUND
                # if this node has any children
                    # replace node with farthest node left in the right sub tree
                                                                                            # if this node is less than root
                                                                                                # replace node with farthest node left in the right sub tree
                                                                                            # else
                                                                                                # replace node with farthest node right in the left sub tree
                    # move children
                    # delete this node
                # else
                    # delete this node gracefully
            # else if this node is a leaf, the value doesnt exists                              << Catches leaf
            # else if data is smaller than this node, lets recurs and update node to be left    << Moves window to left
            # else if data is larger than this node, lets recurs and update node to be right    << Moves window to right

            # if node.data is data: # if the current node is the item we want to delete
            #     # reset parent next to be successor in left side, right side, or none
            #     if node.left:
            #         parent = self._find_parent_node(node.data)
            #         <
            #         > until we cant go right anymore
            #     elif node.right:


def test_binary_node():
    print('Initializing binary node:')
    bn = BinaryNode('Alan')
    print(bn)

    print('Checking if binary node is a leaf:')
    print(bn.is_leaf())

    print('Assigning left child binary node:')
    lbn = BinaryNode('Bill')
    bn.left = lbn
    print(bn.left)

    print('Checking is binary node is internal:')
    print(bn.is_internal())

def test_binary_search_tree():
    bst = BinarySearchTree()
    print(bst)

    print('Appending items:')
    bst.insert('Carlos')
    print('root', bst.root)
    bst.insert('Bill')
    print('<', bst.root.left)
    bst.insert('Alex')
    print('<<', bst.root.left.left)
    bst.insert('Guy Manuel')
    print('>', bst.root.right)
    bst.insert('Zoro')
    print('>>', bst.root.right.right)
    # print('head: ' + str(dll.head))
    # print('tail: ' + str(dll.tail))
    # print('size: ' + str(dll.size))
    # print('length: ' + str(dll.length()))
    #
    # print('Getting items by index:')
    # for index in range(dll.size):
    #     item = dll.get_at_index(index)
    #     print('get_at_index({}): {}'.format(index, repr(item)))
    #
    # print('Deleting items:')
    # dll.delete('B')
    # print(dll)
    # dll.delete('C')
    # print(dll)
    # dll.delete('A')
    # print(dll)
    # print('head: ' + str(dll.head))
    # print('tail: ' + str(dll.tail))
    # print('size: ' + str(dll.size))
    # print('length: ' + str(dll.length()))


if __name__ == '__main__':
    # test_binary_node()
    test_binary_search_tree()

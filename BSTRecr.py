#!/bin/python
# BST.py

class Node:
    """Node of the tree"""
    def __init__(self, data):
        super(Node, self).__init__()
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BST(object):
    """docstring for BST"""
    def __init__(self):
        super(BST, self).__init__()
        self.root = None

    def makeList(self, aNode):
        if aNode is None:
            return []
        return self.makeList(aNode.left) + [aNode.data] + self.makeList(aNode.right)

    def _insert(self, root, node):
        if root is None:
            return node

        if root.data < node.data:
            root.right = self._insert(root.right, node)
        elif root.data > node.data:
            root.left = self._insert(root.left, node)

        return root

    def _inorder(self, node, ret):
        if node:
            self._inorder(node.left, ret)
            ret.append(node.data)
            self._inorder(node.right, ret)

    def insert(self, newNode):
        self.root = self._insert(self.root, newNode)

    def _find_smallest(self, node):
        while node.left:
            self._find_smallest(node.left)

        return node

    def _find_parent(self, root, node):
        if root is None:
            return None

        if root.left == node or root.right == node:
            return root

        if node.data < root.data:
            return self._find_parent(root.left, node)
        elif node.data > root.data:
            return self._find_parent(root.right, node)

    def inorder(self):
        ret = []
        self._inorder(self.root, ret)
        return ret

b = BST()

entries = [5, 3, 2, 1, 6, 7, 8, 9]
for x in entries:
    b.insert(Node(x))

b.delete(6)

l = b.inorder()
print(l)

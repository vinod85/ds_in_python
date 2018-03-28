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

    def _inorder(self, root):
        if root is None:
            return []

        return self._inorder(root.left) + [root.data] + self._inorder(root.right)

    def _insert(self, root, node):
        if root is None:
            return node

        if root.data < node.data:
            root.right = self._insert(root.right, node)
        elif root.data > node.data:
            root.left = self._insert(root.left, node)

        return root

    def _find_smallest(self, node):
        if node.left:
            return self._find_smallest(node.left)
        else:
            return node

    def _find_node(self, root, data):
        if not root:
            return Node
        if root.data == data:
            return root

        if data < root.data:
            return self._find_node(root.left, data)
        elif data > root.data:
            return self._find_node(root.right, data)
        else:
            return root

    def _find_parent(self, root, node):
        if not root or not node:
            return None

        if root.left == node or root.right == node:
            return root

        if node.data < root.data:
            return self._find_parent(root.left, node)
        elif node.data > root.data:
            return self._find_parent(root.right, node)

    def _delete(self, root, data):
        if root is None:
            return

        node = self._find_node(root, data)
        if not node:
            return

        parent = self._find_parent(root, node)
        if parent is not None:
            isLeft = True if parent.left is node else False

        # node is a leaf
        if node.left is None and node.right is None:
            if isLeft:
                parent.left = None
            else:
                parent.right = None
        elif node.left is None and node.right:
            if isLeft:
                parent.left = node.right
            else:
                parent.right = node.right
        elif node.left and node.right is None:
            if isLeft:
                parent.left = node.left
            else:
                parent.right = node.left
        else:
            # node has both right and left
            smallest = self._find_smallest(node.right)
            # TODO: replace the node itself, node just data
            tmp = smallest.data
            # print(node.data, smallest.data)
            self._delete(node, smallest.data)
            node.data = tmp

    def insert(self, newNode):
        self.root = self._insert(self.root, newNode)

    def delete(self, data):
        self._delete(self.root, data)

    def inorder(self):
        return self._inorder(self.root)

b = BST()

entries = [5, 3, 2, 1, 6, 7, 8, 9]
for x in entries:
    b.insert(Node(x))

b.delete(5)

l = b.inorder()
print(l)

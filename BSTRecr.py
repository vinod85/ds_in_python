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

    def __preorder(self, root):
        if root is None:
            return []

        return [root.data] + self.__preorder(root.left)  + self.__preorder(root.right)

    def __postorder(self, root):
        if root is None:
            return []

        return self.__postorder(root.left) + self.__postorder(root.right) + [root.data]

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

        if data == root.data:
            if not root.left and not root.right:
                return None
            elif not root.left and root.right:
                return root.right
            elif root.left and not root.right:
                return root.left
            else:
                # node has both right and left
                smallest = self._find_smallest(root.right)
                # TODO: replace the node itself, node just data
                root.data = smallest.data
                # print(node.data, smallest.data)
                root.right = self._delete(root.right, smallest.data)
                return root
        else:
            if data > root.data:
                root.right = self._delete(root.right, data)
            elif data < root.data:
                root.left = self._delete(root.left, data)

            return root

    def _find_largest(self, root):
        if root.right:
            return self._find_largest(root.right)
        else:
            return root

    def _second_largest(self, root):
        if not root:
            return None

        if root.right is None:
            return self._find_largest(root.left)
        else:
            return self._second_largest(root.right)

    def second_largest(self):
        return self._second_largest(self.root)

    def insert(self, newNode):
        self.root = self._insert(self.root, newNode)

    def delete(self, data):
        self._delete(self.root, data)

    def inorder(self):
        return self._inorder(self.root)

    def preorder(self):
        return self.__preorder(self.root)

    def postorder(self):
        return self.__postorder(self.root)

b = BST()

entries = [100, 50, 150, 25, 75, 15, 150, 125, 175, 115, 135]
for x in entries:
    b.insert(Node(x))

# print(b.second_largest())

l = b.inorder()
print(l)
l = b.preorder()
print(l)
l = b.postorder()
print(l)


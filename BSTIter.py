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

    def _insert_rec(self, root, node):
        if root is None:
            return node

        if root.data < node.data:
            root.right = self._insert_rec(root.right, node)
        elif root.data > node.data:
            root.left = self._insert_rec(root.left, node)

        return root

    def _insert_itr(self, root, node):
        if root is None:
            self.root = node
            return

        while root is not None:
            if node.data > root.data:
                if not root.right:
                    root.right = node
                    break

                root = root.right
            elif node.data < root.data:
                if not root.left:
                    root.left = node
                    break

                root = root.left

    def _inorder(self, node, ret):
        if node:
            self._inorder(node.left, ret)
            ret.append(node.data)
            self._inorder(node.right, ret)

    def insertRec(self, newNode):
        self.root = self._insert_rec(self.root, newNode)

    def insertItr(self, newNode):
        self._insert_itr(self.root, newNode)

    def deleteItr(self, data):
        self._delete_itr(self.root, data)

    def _find_smallest_rec(self, node):
        while node.left:
            self._find_smallest_rec(node.left)

        return node

    def _find_smallest_itr(self, node):
        while node.left:
            node = node.left

        return node

    def _find_parent_rec(self, root, node):
        if root is None:
            return None

        if root.left == node or root.right == node:
            return root

        if node.data < root.data:
            return self._find_parent(root.left, node)
        elif node.data > root.data:
            return self._find_parent(root.right, node)

    def _find_node_itr(self, root, data):
        if root is None:
            return None

        while root:
            if root.data == data:
                return root

            if data < root.data:
                root = root.left
            elif data > root.data:
                root = root.right

        return None

    # Find the parent node
    # arguments: root, node
    def _find_parent_itr(self, root, node):
        if root is None:
            return None

        while root:
            if root.left == node or root.right == node:
                return root

            if node.data < root.data:
                root = root.left
            elif node.data > root.data:
                root = root.right

        return None

    def _delete_itr(self, root, data):
        if root is None:
            return

        node = self._find_node_itr(root, data)

        # if it is the root node
        if node is root:
            self.root = None
            return

        parent = self._find_parent_itr(root, node)
        isLeft = True if parent.left is Node else False
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
            smallest = self._find_smallest_itr(node.right)
            # TODO: replace the node itself, node just data
            node.data = smallest.data
            self._delete_itr(node.right, smallest)

    def inorder(self):
        ret = []
        self._inorder(self.root, ret)
        return ret

b = BST()

entries = [5, 3, 2, 1, 6, 7, 8, 9]
for x in entries:
    b.insertItr(Node(x))

b.deleteItr(6)

l = b.inorder()
print(l)

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

	def inorder(self):
		ret = []
		self._inorder(self.root, ret)
		return ret
		
b = BST()
b.insertItr(Node(100))
l = b.inorder()
print(l)

b.insertItr(Node(200))
l = b.inorder()
print(l)

b.insertItr(Node(300))
l = b.inorder()
print(l)

b.insertItr(Node(400))
l = b.inorder()
print(l)
#!/bin/python
# BST.py

from queue import Queue
from queue import LifoQueue
from asciitree import LeftAligned
from collections import OrderedDict as OD


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
        self.print_buffer = [[0] * 255] * 20

    def _insert(self, root, node):
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
            else:
                break

    def _inorder(self, root):
        stack = []
        ret = []
        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                if stack:
                    root = stack.pop()
                    ret += [root.data]
                    root = root.right
                else:
                    break
        return ret

    def __postorder(self, root):
        if not root:
            return False

        ret = []

        stack = LifoQueue()
        stack.put((root, False))

        while not stack.empty():
            node, visited = stack.get()
            if visited:
                ret += [node.data]
                continue

            stack.put((node, True))

            if node.right:
                stack.put((node.right, False))

            if node.left:
                stack.put((node.left, False))

        return ret

    def __preorder(self, root):
        if not root:
            return False

        ret = []

        stack = LifoQueue()
        stack.put(root)

        while not stack.empty():
            node = stack.get()
            ret += [node.data]

            if node.right:
                stack.put(node.right)

            if node.left:
                stack.put(node.left)

        return ret

    def _find_smallest(self, node):
        while node.left:
            node = node.left

        return node

    def _find_node(self, root, data):
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
    def _find_parent(self, root, node):
        if root is None or node is None:
            return None

        if root == node:
            return None

        while root:
            if root.left == node or root.right == node:
                return root

            if node.data < root.data:
                root = root.left
            elif node.data > root.data:
                root = root.right

        return None

    def __sec_largest(self, root):
        if not root:
            return None

        if root.left is None and root.right is None:
            return None

        elif root.right is None:
            root = root.left
            while root.right:
                root = root.right
            return root
        else:
            parent = None
            while root.right:
                parent = root
                root = root.right

            return parent

    def _delete(self, root, data):
        if root is None:
            return

        node = self._find_node(root, data)
        if not node:
            return

        parent = self._find_parent(root, node)
        if parent is not None:
            is_left = True if parent.left is node else False

        # node is a leaf
        if node.left is None and node.right is None:
            if is_left:
                parent.left = None
            else:
                parent.right = None
        elif node.left is None and node.right:
            if is_left:
                parent.left = node.right
            else:
                parent.right = node.right
        elif node.left and node.right is None:
            if is_left:
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

    def __level_order_traversal(self, root):
        if root is None:
            return

        ret = []

        q = Queue()
        q.put(root)

        while not q.empty():
            item = q.get()
            ret += [item.data]
            if item.left:
                q.put(item.left)
            if item.right:
                q.put(item.right)

        return ret

    def __height(self, root):
        if root is None:
            return

        q = Queue()
        q.put((root, 1))

        max_height = 1
        while not q.empty():
            item, height = q.get()
            if height > max_height:
                max_height = height

            if item.left:
                q.put((item.left, height + 1))
            if item.right:
                q.put((item.right, height + 1))

        return max_height

    def __find_paths(self, root):
        if not root:
            return

        stack = LifoQueue()
        stack.put((root, False, 1))

        ret = []

        while not stack.empty():
            node, visited, height = stack.get()
            if visited:
                ret.insert(height - 1, node.data)

                if node.left is None and node.right is None:
                    ret = ret[:height]
                    print(ret)
            else:
                if node.right:
                    stack.put((node.right, False, height + 1))

                if node.left:
                    stack.put((node.left, False, height + 1))

                stack.put((node, True, height))

    def __check_bst(self, root):
        if not root:
            return False

        stack = LifoQueue()
        stack.put((root, False))

        k = 0
        while not stack.empty():
            node, visited = stack.get()
            if visited:
                if node.data < k:
                    return False
                k = node.data
                continue

            if node.right:
                stack.put((node.right, False))

            stack.put((node, True))

            if node.left:
                stack.put((node.left, False))

        return True

    def __is_complete(self, root):
        if root is None:
            return False

        q = Queue()
        q.put((root, 1))

        level = []
        level.append(0)

        while not q.empty():
            item, lvl = q.get()
            # start by assuming all levels are complete
            try:
                level[lvl]
            except:
                level.insert(lvl, 1)

            if level[lvl - 1] == -1:
                print(level)
                return False
            
            if not item.left and not item.right:
                continue
            elif item.left and item.right:
                q.put((item.left, lvl + 1))
                q.put((item.right, lvl + 1))
            elif not item.left and item.right:
                return False
            else:  # if item.left and not item.right:
                level.insert(lvl + 1, -1)
                q.put((item.left, lvl + 1))
                print(level, lvl)

        print(level)
        return True

    def print_tree(self):
        self.print_buffer = [[" "] * 255] * 20
        self.__print_t(self.root, 0, 0, 0)

        for i in range(20):
            print("".join(self.print_buffer[i]))

        if not self.root:
            return

        height = self.height()

        q = Queue()
        q.put(self.root)

        arr = []

        while not q.empty():
            node = q.get()
            try:
                arr.append(node.data)
            except AttributeError as e:
                arr.append(None)
                continue

            q.put(node.left)
            q.put(node.right)

        print(arr, len(arr))

        i = 0
        level = 0
        while i <= len(arr)/2:
            if not arr[i]:
                i = i + 1
                continue

            print(i, arr[i], arr[(2*i)+1], arr[(2*i)+2])

            i = i + 1

    def __print_t(self, root, is_left, offset, depth):
        b = [""] * 20
        width = 5

        if not root:
            return 0

        b = "(%03d)" % root.data

        left = self.__print_t(root.left,  1, offset, depth + 1)
        right = self.__print_t(root.right, 0, offset + left + width,
            depth + 1)

        for i in range(0, width):
            self.print_buffer[2 * depth][offset + left + i] = b[i]

        print("".join(self.print_buffer[2 * depth]))

        if depth and is_left:
            for i in range(0, width + right):
                self.print_buffer[2 * depth - 1][offset + left + int(round(width/2)) + i] = '-'

            self.print_buffer[2 * depth - 1][offset + left + int(round(width/2))] = '+'
            self.print_buffer[2 * depth - 1][offset + left + width + right + int(round(width/2))] = '+'

            print('->', "".join(self.print_buffer[2 * depth - 1]))

        elif depth and not is_left:
            for i in range(0, left + width):
                self.print_buffer[2 * depth - 1][offset - int(round(width/2)) + i] = '-'

            self.print_buffer[2 * depth - 1][offset + left + int(round(width/2))] = '+'
            self.print_buffer[2 * depth - 1][offset - int(round(width/2)) - 1] = '+'

        return left + width + right

    def __make_dict(self, node):
        if node is None:
            return None

        dic = {}
        left_data = self.__make_dict(node.left)
        right_data = self.__make_dict(node.right)
        dic[str(node.data)] = (left_data, right_data)

        return dic

    def make_dict(self):
        dic = self.__make_dict(self.root)
        return {'tree': dic}

    def height(self):
        return self.__height(self.root)

    def check_bst(self):
        return self.__check_bst(self.root)

    def level_order_traversal(self):
        return self.__level_order_traversal(self.root)

    def inorder(self):
        return self._inorder(self.root)

    def postorder(self):
        return self.__postorder(self.root)

    def preorder(self):
        return self.__preorder(self.root)

    def insert(self, node):
        self._insert(self.root, node)

    def delete(self, data):
        self._delete(self.root, data)

    def find_paths(self):
        self.__find_paths(self.root)

    def sec_largest(self):
        return self.__sec_largest(self.root)

    def find_node(self, data):
        return self._find_node(self.root, data)

    def is_complete(self):
        return self.__is_complete(self.root)


b = BST()

# entries = [52, 50, 20, 80, 34, 2, 16, 98, 56, 46, 56, 98]
# entries = [10, 5, 7, 1]
# entries = [10, 20, 30]
# entries = [100, 50, 150, 25, 75, 15, 150, 125, 175, 115, 135, 5]
# for complete tree
# entries = [100, 50, 150, 25, 75, 125, 175, 10]
entries = [100, 50, 150, 25, 75, 125, 175, 115]
# entries = [100, 50, 150]
for x in entries:
    b.insert(Node(x))

# b.delete(52)
# print(b.sec_largest())
# b.level_order_traversal()
# corrupt tree
# tmp = b.find_node(75)
# tmp.data = 80
# tmp = b.find_node(125)
# tmp.data = 75
# tmp = b.find_node(80)
# tmp.data = 125
# corrupt tree

# print(b.check_bst())
# print(b.height())
# b.find_paths()
# print(b.is_complete())

b.print_tree()
# dic = b.make_dict()
# print(dic)
# tr = LeftAligned()
# print(tr(dic))

# l = b.inorder()
# print(l)
# l = b.preorder()
# print(l)
# l = b.postorder()
# print(l)

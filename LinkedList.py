#!/bin/python

class Node:
    """ """
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):   
        self._data = data

    @data.deleter
    def data(self):
        del self._data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    @next.deleter
    def next(self):
        del self._next

    def has_next(self):
        return self._next is not None

    def __repr__(self):
       return "Node()"

    def __str__(self):
       return str(self._data)

    # def __del__(self):
    #   print("del")

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, newNode):
        if self.head is None:
            self.head = newNode
            return

        tmpNode = self.head
        while tmpNode.has_next():
            tmpNode = tmpNode.next
        tmpNode.next = newNode

    def print_all(self):
        if self.head is None:
            print("The list is empty")
            return

        tmpNode = self.head
        while tmpNode.has_next():
            print (tmpNode.data)
            tmpNode = tmpNode.next
        print (tmpNode.data)

    def __str__(self):
        if self.head is None:
            return "[]"

        nodeList = []
        currNode = self.head
        while currNode != None:
            nodeList.append(currNode.data)
            currNode = currNode.next 
             
        return str(nodeList)  

    def insertBegining(self, newNode):
        self.insertPos(newNode, 0)

    def insertPos(self, newNode, pos = 0):
        if pos == 0:
            newNode.next = self.head
            self.head = newNode
            return

        if self.head is None and pos > 0:
            print ("invalid position!")
            return

        # start with second node
        currNode = self.head.next
        if currNode is None and pos == 1:
            self.head.next = newNode
            newNode.next = None
            return
        elif currNode is None and pos > 1:
            print ("invalid position!")
            return

        i = 0
        while currNode.has_next():
            if i == pos:
                prevNode.next = newNode
                newNode.next = currNode
                return

            i = i + 1
            prevNode = currNode
            currNode = currNode.next

        if i == pos:
            currNode.next = newNode
            newNode.next = None
        else:
            print ("invalid position!")

    def insertBeforeValue(self, val, newNode):
        if self.head is None:
            print("list is empty!")
            return

        if self.head.data == val:
            newNode.next = self.head
            self.head = newNode
            return
            # return self.insertPos(newNode, 0)

        currNode = self.head
        prevNode = self.head

        while currNode.has_next():
            if val == currNode.data:
                newNode.next = currNode
                prevNode.next = newNode
                return

            prevNode = currNode
            currNode = currNode.next

        if currNode.data == val:
            prevNode.next = newNode
            newNode.next = currNode
        else:
            print(val, "not found")

    def insertAfterValue(self, val, newNode):
        if self.head is None:
            print("list is empty!")
            return

        currNode = self.head
        prevNode = self.head

        while currNode.has_next():
            if val == currNode.data:
                newNode.next = currNode.next
                currNode.next = newNode
                return

            prevNode = currNode
            currNode = currNode.next

        if currNode.data == val:
            currNode.next = newNode
        else:
            print(val, "not found")

    def delPos(self, pos = 0):
        if not self.head:
            return

        currNode = self.head
        prevNode = self.head

        if pos == 0:
            self.head = self.head.next
            return

        i = 0
        while currNode.has_next():
            if i == pos:
                prevNode.next = currNode.next
                return

            prevNode = currNode
            currNode = currNode.next
            i = i + 1

    def delValue(self, val):
        self.head = self.head.next
        if self.head is None:
            return

        currNode = self.head
        prevNode = self.head

        if self.head.data == val:
            self.head = self.head.next
            return

        while currNode.has_next():
            if currNode.data == val:
                prevNode.next = currNode.next
                return
            prevNode = currNode
            currNode = currNode.next

        if currNode.data == val:
            prevNode.next = None
        else:
            print(val, "not found")

               # method to delete the first node of the linked list
    def delBeg(self):
        if not self.head:
            print ("The list is empty")
        else:
            self.head = self.head.next
     
    # method to delete the last node of the linked list
    def delLast(self):
         
        if self.head is None:
            print ("The list is empty")
        else:
            currNode = self.head
            prevNode = self.head
            
            while currNode.has_next():
                prevNode = currNode
                currNode = currNode.next
            
            # list has only one node
            if prevNode == currNode:
                self.head = None
            else:
                prevNode.next = None

#-------------------------------#
ll = LinkedList()
ll.append(Node(1))
ll.append(Node(2))
ll.append(Node(3))
n = Node(4)
ll.append(n)
ll.append(Node(5))
ll.append(Node(6))

ll.insertPos(Node(9))
ll.insertPos(Node(7), 1)

print(ll)
print("===========")
ll.delPos(0)
print(ll)
print("===========")
ll.insertAfterValue(2, Node(5.5))
print(ll)
print("===========")
ll.insertBeforeValue(1, Node(5.6))
print(ll)
print("===========")
ll.delValue(6)
print(ll)
print("===========")
ll.delBeg()
print(ll)
print("===========")
ll.delLast()
print(ll)

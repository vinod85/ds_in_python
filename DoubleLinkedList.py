#!/bin/python

class Node:
    """ """
    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None

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

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev):
        self._prev = prev

    @prev.deleter
    def prev(self):
        del self._prev

    def has_next(self):
        return self._next is not None

    def has_prev(self):
        return self._prev is not None
    
    def __repr__(self):
       return "Node()"

    def __str__(self):
       return str(self._data)

    # def __del__(self):
    #   print("del")

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def __str__(self):
        if self.head is None:
            return "[]"

        nodeList = []
        currNode = self.head
        while currNode != None:
            nodeList.append(currNode.data)
            currNode = currNode.next 
             
        return str(nodeList)

    def printReverse(self):
        if self.tail == None:
            return "[]"

        nodeList = []
        currNode = self.tail
        while currNode != None:
            nodeList.append(currNode.data)
            currNode = currNode.prev 
             
        print(nodeList)

    def insertBegining(self, newNode):
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        else:
            firstNode = self.head

            self.head = newNode
            newNode.next = firstNode
            firstNode.prev = newNode

    def insertLast(self, newNode):
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        else:
            lastNode = self.tail

            self.tail = newNode
            lastNode.next = newNode
            newNode.prev = lastNode

if __name__ == '__main__':
    dl = LinkedList()
    dl.insertBegining(Node(1))
    dl.insertBegining(Node(2))
    dl.insertBegining(Node(3))
    dl.insertBegining(Node(4))
    print(dl)
    dl.printReverse()

    dl.insertLast(Node(11))
    dl.insertLast(Node(12))
    dl.insertLast(Node(13))
    dl.insertLast(Node(14))

    print(dl)
    dl.printReverse()
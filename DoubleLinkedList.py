#!/bin/python

# Node of a Doubly Linked List
class Node:
    """ """
    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None

    # getters and setters
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

class DoubleLinkedList(object):
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
        if self.tail is None:
            print("[]")
            return

        nodeList = []
        currNode = self.tail
        while currNode != None:
            nodeList.append(currNode.data)
            currNode = currNode.prev 
             
        print(nodeList)

    def clear(self):
        self.head = None
        self.tail = None

    # Find a given node by moving in fwd direction
    def findNodeByValueFwd(self, val):
        currNode = self.head
        while currNode:
            if val == currNode.data:
                break
            currNode = currNode.next

        return currNode

    # Find a given node by moving in reverse direction
    def findNodeByValueRev(self, val):
        currNode = self.tail
        while currNode:
            if val == currNode.data:
                break
            currNode = currNode.prev

        return currNode

    # Find a given node by moving in reverse direction
    def findNodeByPosRev(self, pos):
        x = 0
        currNode = self.tail
        while pos != x:
            if not currNode:
                break
            x = x + 1
            currNode = currNode.prev

        return currNode

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

    # Insert a Node at the given position
    def insertPositionFwd(self, newNode, pos):
        if pos == 0:
            self.insertBegining(newNode)
        else:
            currNode = self.head

            i = 0
            while i < pos:
                if not currNode.has_next():
                    break
                currNode = currNode.next
                i = i + 1

            if i == pos:
                newNode.next = currNode
                newNode.prev = currNode.prev
            
                currNode.prev.next = newNode
                currNode.prev = newNode
            elif i == pos - 1:
                newNode.prev = currNode
                currNode.next = newNode
                self.tail = newNode
            else:
                print("position > lenght of the list")

    # Insert a Node at the given position from back
    def insertPositionRev(self, newNode, pos):
        if pos == 0:
            self.insertLast(newNode)
        else:
            tmpNode = self.findNodeByPosRev(pos)
            if tmpNode is None:
                firstNode = self.head

                self.head = newNode
                newNode.next = firstNode
                firstNode.prev = newNode
            elif tmpNode.next is None and tmpNode.prev is None:
                self.head = None
                self.tail = None
            # inserting at last
            elif tmpNode.next is None:
                 lastNode = self.tail

                 self.tail = newNode
                 lastNode.next = newNode
                 newNode.prev = lastNode
            # insert begining
            elif tmpNode.prev is None:
                print(tmpNode)
                firstNode = self.head

                self.head = newNode
                newNode.next = firstNode
                firstNode.prev = newNode
            else:
                newNode.prev = tmpNode
                newNode.next = tmpNode.next

                tmpNode.next.prev = newNode
                tmpNode.next = newNode

    def deleteFirst(self):
        if self.is_empty():
            print("List is empty")
        else:
            if self.head.has_next():
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None

    def deleteLast(self):
        if self.is_empty():
            print("List is empty")
        else:
            if self.tail.has_prev():
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = None
                self.tail = None

    # Delete a given value by going through fwd direction
    def deleteValueFwd(self, val):
        if self.is_empty():
            print("List is empty")
        else:
            tmpNode = self.findNodeByValueFwd(val)

            if tmpNode is None:
                print("Value not found")
            # only one node in the list and we have to delete it
            elif tmpNode.next is None and tmpNode.prev is None:
                self.head = None
                self.tail = None
            # we have to delete the first node
            elif tmpNode.prev is None:
                self.head = tmpNode.next
                self.head.prev = None
            # we have to delete the last node
            elif tmpNode.next is None:
                self.tail = tmpNode.prev
                self.tail.next = None
            # delete the node
            else:
                currNode.prev.next = currNode.next
                currNode.next.prev = currNode.prev

    # Delete a given value by going through reverse direction
    def deleteValueRev(self, val):
        if self.is_empty():
            print("List is empty")
        else:
            tmpNode = self.findNodeByValueRev(val)

            if tmpNode is None:
                print("Value not found")
            # only one node in the list and we have to delete it
            elif tmpNode.next is None and tmpNode.prev is None:
                self.head = None
                self.tail = None
            # we have to delete the first node
            elif tmpNode.prev is None:
                self.head = tmpNode.next
                self.head.prev = None
            # we have to delete the last node
            elif tmpNode.next is None:
                self.tail = tmpNode.prev
                self.tail.next = None
            # delete the node
            else:
                currNode.prev.next = currNode.next
                currNode.next.prev = currNode.prev

if __name__ == '__main__':
    dl = DoubleLinkedList()

    # dl.insertBegining(Node(1))
    # dl.insertBegining(Node(2))
    # dl.insertBegining(Node(3))
    # dl.insertBegining(Node(4))
    # print(dl)
    # dl.printReverse()

    # dl.insertLast(Node(11))
    # dl.insertLast(Node(12))
    # dl.insertLast(Node(13))
    # dl.insertLast(Node(14))
    # print(dl)
    # dl.printReverse()

    # dl.clear()

    # dl.insertPositionFwd(Node(1), 0)
    # dl.insertPositionFwd(Node(2), 0)
    # dl.insertPositionFwd(Node(3), 0)
    # dl.insertPositionFwd(Node(4), 0)
    # print(dl)
    # dl.insertPositionFwd(Node(5), 4)
    # print(dl)
    # dl.printReverse()

    # dl.clear()

    # dl.insertPositionFwd(Node(1), 0)
    # dl.insertPositionFwd(Node(2), 0)
    # dl.insertPositionFwd(Node(3), 0)
    # print(dl)
    # dl.deleteFirst()
    # print(dl)
    # dl.printReverse()

    # dl.clear()
    
    # dl.insertPositionFwd(Node(1), 0)
    # dl.insertPositionFwd(Node(2), 0)
    # dl.insertPositionFwd(Node(3), 0)
    # print(dl)
    # dl.deleteLast()
    # print(dl)
    # dl.printReverse()

    # dl.clear()
    
    # dl.insertLast(Node(1))
    # dl.insertLast(Node(2))
    # dl.insertLast(Node(3))
    # dl.insertLast(Node(4))
    # print(dl)
    # dl.deleteValueFwd(1)
    # dl.deleteValueFwd(2)
    # dl.deleteValueFwd(3)
    # dl.deleteValueFwd(4)
    # print(dl)
    # dl.printReverse()

    # dl.clear()
    
    # dl.insertLast(Node(1))
    # dl.insertLast(Node(2))
    # dl.insertLast(Node(3))
    # dl.insertLast(Node(4))
    # print(dl)
    # dl.deleteValueRev(1)
    # dl.deleteValueRev(2)
    # dl.deleteValueRev(3)
    # dl.deleteValueRev(4)
    # print(dl)
    # dl.printReverse()

    dl.clear()
    
    dl.insertLast(Node(1))
    dl.insertLast(Node(2))
    # dl.insertLast(Node(3))
    # dl.insertLast(Node(4))
    print(dl)
    dl.insertPositionRev(Node(5), 1)
    print(dl)
    dl.printReverse()
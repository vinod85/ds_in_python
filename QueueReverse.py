#!/bin/python


class CircularQueue(object):
    #Constructor
    def __init__(self, maxSize = 5):
        self.front = 0
        self.rear = 0
        # one extra space for ease of calculation
        self.maxSize = maxSize + 1
        self.queue = [0] * self.maxSize

    # Adding elements to the queue
    def enqueue(self, data):
        if self.full():
            return ("Queue Full!")
        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.maxSize
        return True

    # Removing elements from the queue
    def dequeue(self):
        if self.empty():
            return ("Queue Empty!")
        data = self.queue[self.front]
        self.front = (self.front + 1) % self.maxSize
        return data

    # check if queue is full or not
    def full(self):
        return self.size() == self.maxSize - 1

    # check if queue is full or not
    def empty(self):
        return self.size() == 0

    # Calculating the size of the queue
    def size(self):
        if self.rear >= self.front:
            return (self.rear - self.front)
        return (self.maxSize - (self.front - self.rear))

    def print(self):
        print(self.queue)


class Stack(object):
    def __init__(self, limit=10):
        self.stk = []
        self.limit = limit
 
    def isEmpty(self):
        return self.size() <= 0
 
    def isFull(self):
        return self.size() >= self.limit
 
    def push(self, item):
        if self.isFull():
            print('Stack Overflow!')
        else:
            self.stk.append(item)
 
    def pop(self):
        if self.isEmpty():
            print('Stack Underflow!')
            return None
        else:
            return self.stk.pop()
 
    def display(self):
        print('Stack: ', self.stk)
 
    def size(self):
        return len(self.stk)

q = CircularQueue(10)
for i in range(1, 11):
    q.enqueue(i)

q.print()

s = Stack(q.size())

while not q.empty():
    data = q.dequeue()
    s.push(data)

while not s.isEmpty():
    data = s.pop()
    q.enqueue(data)

q.print()

while not q.empty():
    data = q.dequeue()
    print(data)
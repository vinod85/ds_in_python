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
        if self.queue_size() == self.maxSize - 1:
            return ("Queue Full!")
        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.maxSize
        return True

    # Removing elements from the queue
    def dequeue(self):
        if self.queue_size() == 0:
            return ("Queue Empty!")
        data = self.queue[self.front]
        self.front = (self.front + 1) % self.maxSize
        return data

    # Calculating the size of the queue
    def queue_size(self):
        if self.rear >= self.front:
            return (self.rear - self.front)
        return (self.maxSize - (self.front - self.rear))


q = CircularQueue(2)
q.enqueue(1)
q.enqueue(2)
print(q.enqueue(3))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

#!/bin/python


class CircularQueue(object):
    #Constructor
    def __init__(self, maxSize = 5):
        self.queue = []
        self.front = 0
        self.rear = 0
        # one extra space for ease of calculation
        self.maxSize = maxSize + 1

    # Adding elements to the queue
    def enqueue(self, data):
        if self.queue_size() == self.maxSize - 1:
            return ("Queue Full!")
        self.queue.append(data)
        self.rear = (self.rear + 1) % self.maxSize
        return True

    # Removing elements from the queue
    def dequeue(self):
        if self.queue_size() == 0:
            return ("Queue Empty!")
        data = self.queue.pop(0)
        self.front = (self.front + 1) % self.maxSize
        return data

    # Calculating the size of the queue
    def queue_size(self):
        if self.rear >= self.front:
            return (self.rear - self.front)
        return (self.maxSize - (self.front - self.rear))


q = CircularQueue(10)
for i in range(10):
    q.enqueue(i)

print(q.enqueue(3))

for i in range(10):
    print(q.dequeue())

print(q.dequeue())
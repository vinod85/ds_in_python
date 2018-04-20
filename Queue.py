#!/bin/python


class Queue(object):
    def __init__(self, max_size=10):
        self.queue = [0]*max_size
        self.front = 0
        self.rear = 0
        self.max_size = max_size

    def queue_full(self):
        return self.front >= self.max_size

    def queue_empty(self):
        return self.front == self.rear

    def enqueue(self, data):
        if self.queue_full():
            print("Overflow")
            return
        self.queue[self.front] = data
        self.front = self.front + 1

    def dequeue(self):
        if self.queue_empty():
            print("Underflow")
            return None
        data = self.queue[self.rear]
        self.rear = self.rear + 1
        return data


q = Queue(2)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

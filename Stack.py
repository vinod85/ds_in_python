#!/bin/python


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


s = Stack()
for i in range(1, 11):
    s.push(i)

s.push(11)

for i in range(10):
    print(s.pop())

s.pop()
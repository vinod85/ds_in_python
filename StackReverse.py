#!/bin/python


class Stack(object):
    def __init__(self, limit=10):
        self.stk = []
        self.limit = limit

    def empty(self):
        return self.size() <= 0

    def full(self):
        return self.size() >= self.limit

    def push(self, item):
        if self.full():
            print('Stack Overflow!')
        else:
            self.stk.append(item)

    def top(self):
        return self.stk[-1]

    def pop(self):
        if self.empty():
            print('Stack Underflow!')
            return None
        else:
            return self.stk.pop()

    def display(self):
        print('Stack: ', self.stk)

    def size(self):
        return len(self.stk)

    def __insert_bottom(self, item):
        print(self.stk)
        if self.empty():
            self.push(item)
        else:
            data = self.pop()
            self.__insert_bottom(item)
            self.push(data)

    def reverse_recur(self):
        print(self.stk)
        if not self.empty():
            data = self.stk.pop()
            self.reverse_recur()
            self.__insert_bottom(data)

    def __sort(self, item):
        print(self.stk)
        if self.empty() or item < self.top():
            self.push(item)
        else:
            data = self.pop()
            self.__sort(item)
            self.push(data)

    def sort(self):
        print(self.stk)
        if not self.empty():
            data = self.stk.pop()
            self.sort()
            self.__sort(data)

    def __nge(self, item):
        if self.empty() or item < self.top():
            self.push(item)
        else:
            data = self.pop()
            self.__nge(item)
            self.push(data)

    # incomplete
    def nge(self):
        """ Next greater element."""
        print(self.stk)
        if not self.empty():
            data = self.stk.pop()
            self.nge()
            self.__nge(data)
            self.push(data)


s = Stack()
# for i in range(1, 11):
    # s.push(i)

s.push(3)
s.push(2)
s.push(1)
s.push(4)
s.push(7)
s.push(5)
s.push(8)
s.push(9)
s.push(10)
s.push(6)

s.sort()

for i in range(10):
    print(s.pop())

# s.pop()

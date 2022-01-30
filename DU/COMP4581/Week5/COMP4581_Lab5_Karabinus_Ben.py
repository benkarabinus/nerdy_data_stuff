"""
Ben Karabinus
University of Denver
COMP 4581, Winter Quarter 2022
Lab 5
"""

from collections import deque


class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[len(self.stack)-1]

    def empty(self):
        return len(self.stack) == 0


class MyQueue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        return self.queue.popleft()

    def front(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0


def main():

    # testing code for stack
    s = MyStack()
    print(s.empty())
    s.push(5)
    s.push(8)
    print(s.pop())
    s.push(3)
    print(s.empty())
    print(s.top())
    print(s.pop())
    print(s.pop())
    #print(s.pop())  # throws error empty stack

    # testing code for Queue
    q = MyQueue()
    print(q.empty())
    q.enqueue(5)
    q.enqueue(8)
    print(q.dequeue())
    q.enqueue(3)
    print(q.empty())
    print(q.front())
    print(q.dequeue())
    print(q.dequeue())
    #print(q.dequeue())  # throws error empty queue


if __name__ == '__main__':
    main()

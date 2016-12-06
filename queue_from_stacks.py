'''
Problem: 

Implement a queue using two stacks.


Thoughts:

The key is to realize that we need only move elements between stacks 

in the case that we're popping from an empty dequeue stack. In other words,

it's possible to dequeue in constant time. We just need to be sure to consider

examples in which we have a series of consecutive enqueues and dequeues.


Another thought:

Queue is an amazing word. 


Sources:

https://www.interviewcake.com/question/python/queue-two-stacks

https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/forum
'''

class Queue(object):

    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, value):
        self.enqueue_stack.append(value)

    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

            return self.dequeue_stack.pop()

        # note error thrown on empty stack
        return self.dequeue_stack.pop() 
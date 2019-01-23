"""
Implement a MyQueue class which implements a queue using two stacks.
"""

from Stack import Stack

class MyQueue:
  def __init__(self):
    self.stackA = Stack()
    self.stackB = Stack()

  def enqueue(self, x):
    self.stackA.push(x)

  def dequeue(self):
    
    
  

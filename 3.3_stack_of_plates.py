"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous
stack exceeds some threshold. Implement a data structure SetOfStacks that mimics
this. SetOfStacks should be composed of several stacks and should create a new stack
once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there were just a single
stack).

FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific sub-stack
"""
from Stack import Stack

class StackOfPlates:
  def __init__(self, capacity):
    self.stacks = [[]]
    self.setNdx()
    self.limit = 10

  def push(self, x):
    if len(self.getCurrStack()) >= 10:
      self.stacks.append([])
      self.setNdx()
    self.getCurrStack.append(x)

  def peek(self):
    return self.getCurrStack()[-1]

  def pop(self):
    a = self.getCurrStack().pop()
    if len(self.getCurrStack()) == 0:
      if len(self.stacks) == 0:
        print('NO!')
      else:
        self.stacks.pop()
      self.setNdx()
    return a

  def popAt(self, ndx):
    stackNdx = ndx//self.limit
    arrNdx = ndx%self.limit
    return self.stacks[stackNdx].popAt(arrNdx)

  def setNdx(self):
    self.ndx = len(self.stacks)-1
  
  def getCurrStack(self):
    return self.stacks[self.ndx]


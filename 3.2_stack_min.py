"""
How would you design a stack which, in addition to push and pop, has
a function min which returns the minimum element?
Push, pop and min shoudl all operate in O(1) time.
"""
import sys

class StackMin:
  def __init__(self):
    self.arr = []
    self.min = [sys.maxint]

  def push(self, x):
    if x < self.min[0]:
      self.min.insert(0, x)
    self.arr.append(x)
  
  def peek(self):
    if len(arr) > 0:
      return arr[-1]
    return None

  def pop(self):
    num = self.arr.pop()
    if num == self.min[0]:
      self.min.pop(0)
    return num

  def getMin(self):
    return self.min[0]



if __name__ == '__main__':
  stackMin = StackMin()
  stackMin.push(5)
  stackMin.push(4)
  stackMin.push(3)
  stackMin.push(0)
  stackMin.push(8)
  print(stackMin.getMin())
  stackMin.pop()
  stackMin.pop()
  print(stackMin.getMin())
  

    




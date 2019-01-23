"""
Write a program to sort a stack such that the smallest items are on the top. 
You can use an additional temporary stack, but you may not copy the elements into any other 
data structure (such as an array). The stack supports the following operations: push, pop, peek,
and isEmpty.
"""

class Stack:
  def __init__(self):
    self.arr = []

  def push(self, x):
    self.arr.append(x)

  def pop(self):
    return self.arr.pop()

  def peek(self):
    if len(self.arr) > 0:
      return self.arr[-1]
    return None

  def isEmpty(self):
    return len(self.arr) == 0

  def sort(self):
    temp = Stack()
    while not self.isEmpty():
      element = self.pop()
      while not temp.isEmpty() and temp.peek() < element:
        self.push(temp.pop())
      temp.push(element)
    while not temp.isEmpty():
      self.push(temp.pop())
    
  def printArr(self):
    print(self.arr)


if __name__ == '__main__':
  a = Stack()
  a.push(1)
  a.push(2)
  a.push(3)
  a.push(2)
  a.sort()
  a.printArr()


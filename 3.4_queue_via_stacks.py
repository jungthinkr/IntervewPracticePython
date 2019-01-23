"""
Implement a MyQueue class which implements a queue using two stacks.
"""

class MyQueue:
  def __init__(self):
    self.stackA = []
    self.stackB = []

  def enqueue(self, x):
    self.stackA.append(x)

  def dequeue(self):
    if len(self.stackB) > 0:
      return self.stackB.pop()

    while self.stackA:
      a=self.stackA.pop()
      self.stackB.append(a)
    return self.stackB.pop()


if __name__ == '__main__':
  q = MyQueue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  print(q.dequeue())
  print(q.dequeue())
  print(q.dequeue())
    
  

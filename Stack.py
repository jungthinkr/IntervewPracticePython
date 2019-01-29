class Stack:
  def __init__(self, n = 10):
  arr = []

  def push(self, x):
      self.arr.append(x)
  
  def peek(self):
    return self.arr[-1]

  def pop(self):
    return self.arr.pop()

if __name__ == '__main__':
  #test stack
  s = Stack()
  s.push(1)
  s.push(2)
  s.push(3)


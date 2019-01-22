"""
Describe how you could use a single array to implement three stacks
"""

class Stacks:
  def __init__(self, k, n):
    #k = number of stacks
    #n = size of array
    self.k = k
    self.size = n
    self.arr = [None]*n
    self.heads = []
    for i in range(k):
      self.heads.append(n/k*i)
    print(self.heads)


  def push(self, k, elem):
    idx = self.heads[k]
    stackLength = (idx+len(self.arr))/self.k
    for i in range(idx, idx+stackLength-1):
      if self.arr[idx] == None:
        if i == idx+stackLength-1:
          print("stackoverflow")
        else:
          self.arr[idx] = elem
          break


  def pop(self, k):
    idx = self.heads[k]
    stackLength = (idx+len(self.arr))/self.k
    for i in range(idx, idx+stackLength-1):
      if self.arr[idx] != None:
        temp = self.arr[idx]
        self.arr[idx] = None
        return temp
    return None
    
      
  def peek(self, k):
    idx = self.heads[k]
    stackLength = (idx+len(self.arr))/self.k
    for i in range(idx, idx+stackLength-1):
      if self.arr[idx] != None:
        temp = self.arr[idx]
        return temp
    return None
        
if __name__ == '__main__':
  arr = []
  stacks = Stacks(3, 10)
  stacks.push(0,1)
  stacks.push(1,1)
  stacks.push(2,1)
  print(stacks.peek(0))
  print(stacks.peek(1))
  print(stacks.peek(2))
  print(stacks.pop(0))
  print(stacks.pop(1))
  print(stacks.pop(2))







  
  

  
  

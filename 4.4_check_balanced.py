"""
Implement a function to check if a binary tree is balanced. For the purposes of the
question, a balanced tree is defined to be a tree such that the heights of the 
two subtrees of any node never differ by more than one.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def insert(self, val):
      if self.val:
        if val < self.val:
          if not self.left:
            self.left = TreeNode(val)
          else:
            self.left.insert(val)
        elif val > self.val:
          if not self.right:
            self.right = TreeNode(val)
          else:
            self.right.insert(val)
      else:
        self.val = val

def construct(arr, l, r):
    if l > r:
        return None
    mid = (l+r)/2
    node = TreeNode(mid)
    node.left = construct(arr, l, mid-1)
    node.right = construct(arr, mid+1, r)
    return node

def printTree(root):
    if not root:
        return
    print(root.val)
    printTree(root.left)
    printTree(root.right)

def isBalanced(root):
  if not root:
      return [] 
  #queue FILO
  result = []
  q = [root]
  while q:
      arr = []
      children = []
      while q:
          r = q.pop(0)
          if r:
              arr.append(r)
              children.append(r.left)
              children.append(r.right)
      q.extend(children)
      if len(arr) > 0:
          result.append(arr)
  for i in range(len(result)):
    m = pow(2,i)
    if len(result[i]) != m and i != len(result)-1:
      return False

  return True

  

if __name__ == '__main__':
  arr = [1,2,3,4,5,6,7,8,9]
  arr2 = [1,2,3,4,5]
  a = isBalanced(construct(arr,0,len(arr)-1))
  print(a)


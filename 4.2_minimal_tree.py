"""
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create
a binary search tree with minimal height
"""
# binary search tree left is lower and right is higher

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def printHead(head):
  if not head:
    return
  print(head.val)
  printHead(head.left)
  printHead(head.right)

def construct(arr, l, r):
  if l > r:
    return None

  mid = (l+r)//2
  h = TreeNode(arr[mid])
  h.left = construct(arr, l, mid-1)
  h.right = construct(arr, mid+1, r)
  return h

if __name__ == '__main__':
  arr = [1,2,3,4,5]
  h = construct(arr, 0, len(arr)-1)
  printHead(h)




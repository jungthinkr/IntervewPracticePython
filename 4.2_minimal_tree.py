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

def construct(arr):
  arr.sort()
  head = _construct(arr, 0, len(arr)-1)
  #printHead(head)

def printHead(head):
  if not head:
    return
  print(head.val)
  printHead(head.left)
  printHead(head.right)

def _construct(arr, l, r):
  if l >= r:
    print(l)
    return None

  mid = (l+r)/2
  h = TreeNode(arr[mid])
  h.left = _construct(arr, l, mid-1)
  h.right = _construct(arr, mid+1, r)
  return h

if __name__ == '__main__':
  arr = [1,2,3,4,5,6,7,3,2,5]
  construct(arr)


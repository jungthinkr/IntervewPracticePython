"""
A binary search tree was created by traversing through an array from left to right and inserting
each element. Given a binary search tree with distinct elements, print all possible
arrays that could have let to this tree.
"""


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def construct(arr, l, r):
  if l > r:
    return None

  mid = (l+r)/2
  root = TreeNode(arr[mid])
  root.left = construct(arr, l, mid-1)
  root.right = construct(arr, mid+1, r)
  return root

def backToArr(arr, head):
  if not head:
    return

  backToArr(arr, head.left)
  arr.append(head.val)
  backToArr(arr, head.right)

if __name__ == '__main__':
  arr = [1,2,3,4,5,6,7,8,9]
  head = construct(arr, 0, len(arr)-1)
  result = []
  backToArr(result, head)
  print(result)





    

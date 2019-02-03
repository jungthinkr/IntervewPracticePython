"""
Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a
data structure. NODE: This is not necessarily a binary search tree.
"""

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def printTree(head):
  if not head:
    return
  print(head.val)
  printTree(head.left)
  printTree(head.right)

def construct(arr, l, r):
  if l > r:
    return None
  mid = (l+r)/2
  root = TreeNode(arr[mid])
  root.left = construct(arr, l, mid-1)
  root.right = construct(arr, mid+1, r)
  return root

def lca(root, a, b):
  if not root:
    return None

  left = locate(root.left, a,b)
  right = locate(root.right, a,b)

  if not left or not right:
    return root

  return None

    

def locate(root, a, b):
  if not root:
    return False
  if root.val == a or root.val == b:
    return True
  else:
    return locate(root.right, a, b) or locate(root.left, a, b)

if __name__ == '__main__':
  arr = [1,2,3,4,5,6,7,8,9]
  head = construct(arr, 0, len(arr)-1)
  printTree(head)
  print('')
  print(lca(head,2,3).val)

  

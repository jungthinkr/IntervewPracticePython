"""
Write an algorithm to find the "next" node (i.e. in-order successor) of a given node
in a binary search tree. You may assume that each node has a link to its parent.
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

def printTree(root):
  if not root:
    return
  print(root.val)
  printTree(root.left)
  printTree(root.right)


def successor(head, target):
  arr = []
  findSuccessor(head, target, arr)
  for i in range(len(arr)):
    if arr[i].val == target:
      if i+1 < len(arr):
        return arr[i+1]
      else:
        return None
  return None

def findSuccessor(head, target, arr):
  if not head:
    return

  findSuccessor(head.left, target, arr)
  arr.append(head)
  findSuccessor(head.right, target, arr)

if __name__ == '__main__':
  arr = [1,2,3,4,5]
  head = TreeNode(0)
  for num in arr:
    head.insert(num)
  #assume none of the values
  print(successor(head, 1).val)


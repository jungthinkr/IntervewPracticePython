"""
Implement a function to check if a binary tree is a binary search tree.
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


def isBST(root):
  if not root or not root.left or not root.right:
    return True
  if root.left.val > root.val or root.right.val < root.val:
    return False
  return isBST(root.left) and isBST(root.right)

if __name__ == '__main__':
  arr = [1,2,3,4,5]
  head = TreeNode(0)
  for num in arr:
    head.insert(num)
    
  printTree(head)
  a = isBST(head)
  print(a)


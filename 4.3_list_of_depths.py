"""
Given a binary tree, design an algorithm which creates a linked list of all of the nodes
at each depth (e.g. if you have a tree with depth D, you'll have D linked lists).

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

def constructLists(root):
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
                print(r.left, r.right)
                children.append(r.left)
                children.append(r.right)
        q.extend(children)
        if len(arr) > 0:
            result.append(arr)
    return result

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    root = construct(arr, 0, len(arr)-1)
    a = constructLists(root)
    for level in a:
         print(level)

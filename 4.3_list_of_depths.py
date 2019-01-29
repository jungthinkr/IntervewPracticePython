"""
Given a binary tree, design an algorithm which creates a linked list of all of the nodes
at each depth (e.g. if you have a tree with depth D, you'll have D linked lists).

"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def construct(arr, idx):
    if idx >= len(arr):
        return

    node = TreeNode(arr[idx])
    node.left = construct(arr, idx+1)
    node.right = construct(arr, idx+2)
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
                children.append(r.left)
                children.append(r.right)
        q.extend(children)
        result.append(arr)
    return result

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    root = construct(arr, 0)
    printTree(root)
    #print(constructLists(root))


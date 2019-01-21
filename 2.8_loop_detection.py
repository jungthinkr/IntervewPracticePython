"""
Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.

DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer
points to an earlier node, so as to make a loop in the linked list.

EXAMPLE
Input A->B->C->D->E->C [the same C as earlier]
Output C
"""

from Node import Node

def getCycledNode(head):
  d = {}
  curr = head
  while curr:
    if d.get(curr, False):
      print(curr.val)
      return curr
    d[curr] = True
  #given the params should never get here
  return None
  

if __name__ == '__main__':
  arr = [1,2,3]
  head = Node(arr[0])
  curr = head
  for n in arr[1:]:
    curr.next = Node(n)
    curr = curr.next
  curr.next = head

  curr = head
  #head is cyclic now
  getCycledNode(head)
    

  

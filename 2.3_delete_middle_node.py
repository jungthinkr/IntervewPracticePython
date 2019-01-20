"""
Implement an algorithm to delete a node in the middle (i.e. any node but the first and lost node,
not necessarily the exact middle) of a singly linked list, given only access to that node

EXAMPLE

Input: The node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
"""

from Node import Node
import math

def deleteMiddle(head):
  arr = []
  curr = head
  while curr:
    arr.append(curr)
    curr = curr.next
  mid = len(arr)/2

  #remove mid
  middle = arr[mid]
  if mid > 1 and mid < len(arr):
    prev = arr[mid-1]
    nxt = arr[mid+1]
    prev.next = nxt
    middle.next = None

  #print
  curr = head
  while curr:
    print(curr.val)
    curr = curr.next

    
if __name__ == '__main__':
  arr = [1,2,3,4,5,6]
  head = Node(arr[0])
  curr = head
  
  for n in arr[1:]:
    curr.next = Node(n)
    curr = curr.next

  curr = head
  while curr:
    print(curr.val)
    curr = curr.next
  print('')
  deleteMiddle(head)



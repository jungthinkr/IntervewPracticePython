"""
Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value.
That is, if the kth node of the first linked list is the exact same node (by reference)
as the jth node of second linked list, then they are intersection.
"""

from Node import Node

def isIntersection(a,b):
  d = {}
  curr = a
  while curr:
    d[curr] = True
    curr = curr.next

  curr = b
  while curr:
    if(d.get(curr, False)):
      return True
    curr = curr.next
  return False

if __name__ == '__main__':
  arr1 = [1,2,3,4,5]
  arr2 = [1,2,3,4,5]

  head1 = Node(arr1[0])
  curr = head1
  same = None
  for n in arr1[1:]:
    node = Node(n)
    if n == 3:
      same = node
    curr.next = node
    curr = curr.next

  head2 = Node(arr2[0])
  curr = head2
  for n in arr2[1:]:
    if n == 3:
      curr.next = same
    else:
      curr.next = Node(n)
    curr = curr.next

  ans = isIntersection(head1, head2)
  print(ans)
    

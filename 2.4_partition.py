"""
Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of 
x only need to be after the elements less than x (see below). The partition element x can
appear anywhere in the "right partition"; it does not need to appear between
the left and right partitions

EXAMPLE
Input 3->5->8->5->10->2->1 partition = 5
Output 3->1->2->10->5->5->8
"""
from Node import Node

def partition(head, p): 
  arr = []
  curr = head
  while curr:
    if curr.val >= p:
      arr.append(curr)
    else:
      arr.insert(0, curr)
    curr = curr.next

  if len(arr) == 0:
    return head

  result = arr[0]
  curr = result
  for node in arr[1:]:
    curr.next = node
    curr = curr.next
  arr[-1].next = None
    
  curr = result
  while curr:
    print(curr.val)
    curr = curr.next

  return result

if __name__ == '__main__':
  arr = [3,5,8,5,10,2,1]
  head = Node(arr[0])
  curr = head
  for n in arr[1:]:
    curr.next = Node(n)
    curr = curr.next

  curr = head
  while curr:
    curr = curr.next

  partition(head, 5)
  

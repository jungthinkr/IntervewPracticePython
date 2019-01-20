"""
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP

How would you solve this problem if a temporary buffer is not allowed? 
There is a N^2 approach but not as efficient
"""

from Node import Node 

def removedupe(head):
  curr = head
  while curr:
    n = curr.next
    m = curr #prev

    while n:
      if n.val == curr.val:
        #remove
        m.next = n.next
        n.next = None
      m = n
      n = n.next
        
    curr = curr.next

  curr = head
  while curr:
    print(curr.val)
    curr = curr.next

  return head

if __name__ == '__main__':
  arr = [2, 4, 2, 1, 3]
  head = Node(arr[0])
  curr = head

  for i in arr[1:]:
    curr.next = Node(i)
    curr = curr.next

  curr = head
  while curr:
    curr = curr.next

  removedupe(head)


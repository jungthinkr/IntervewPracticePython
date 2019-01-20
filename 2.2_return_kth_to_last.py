"""
Implement an algorithmn to find the kth to last element of a singly linked list.
"""
from Node import Node

def getNode(head, k):
  arr = []
  curr = head
  while curr:
    arr.append(curr)
    curr = curr.next
  result = arr[-(k+1)]
  print(result, result.val)
  return result


if __name__ == '__main__':
  arr = [1, 2, 3, 4]
  head = Node(arr[0])
  curr = head
  for n in arr[1:]:
    curr.next = Node(n)
    curr = curr.next
  
  getNode(head, 1) 


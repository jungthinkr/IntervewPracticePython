"""
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1's digit is the head of the list. Write
a function that adds the two numbers and retruns the sum as a linked list.

EXAMPLE

Input 7->1->6 + 5->9->2 That is 617 + 295
Output 2->1->9 That is 912

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.

EXAMPLE

Input 6->1->7 + 2->9->5 That is 617 + 295
Output 9->1->2 That is 912
"""

from Node import Node

def add(a,b):
  m = 0
  n = 0
  
  curr = a
  place = 1
  while curr:
    m += curr.val * place
    place *= 10
    curr = curr.next

  curr = b
  place = 1
  while curr:
    n += curr.val * place
    place *= 10
    curr = curr.next
  
  resultStr = str(m+n)
  result = Node(int(resultStr[0]))
  curr = result
  for s in resultStr[1:]:
    curr.next = Node(int(s))
    curr = curr.next

  curr = result
  while curr:
    print(curr.val)
    curr = curr.next
  
  return result

def add2(a, b):
  m = ''
  n = ''

  curr = a
  while curr:
    m += str(curr.val)
    curr = curr.next

  curr = b
  while curr:
    n += str(curr.val)
    curr = curr.next
  
  resultStr = str(int(m)+int(n))

  result = Node(int(resultStr[0]))
  curr = result
  for s in resultStr[1:]:
    curr.next = Node(int(s))
    curr = curr.next

  curr = result
  while curr:
    print(curr.val)
    curr = curr.next
  
  return result

if __name__ == '__main__':
  arr1 = [7, 1, 6]
  arr2 = [5, 9, 2]

  head1 = Node(arr1[0])
  curr = head1
  for n in arr1[1:]:
    curr.next = Node(n)
    curr = curr.next

  head2 = Node(arr2[0])
  curr = head2
  for n in arr2[1:]:
    curr.next = Node(n)
    curr = curr.next

  add2(head1, head2) 
  

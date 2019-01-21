"""
Implement a function to check if a linked list is a palindrome.
"""

from Node import Node

def isPalindrome(head):
  arr = []
  curr = head
  while curr:
    arr.append(curr.val)
    curr = curr.next
  print(arr)

  #determine palindrome
  l = 0
  r = len(arr)-1
  while l < r:
    if arr[l] != arr[r]:
      return False
    l += 1
    r -= 1

  return True

  

if __name__ == '__main__':
  arr = ['a', 'b', 'c', 'b', 'a']
  head = Node(arr[0])
  curr = head

  for c in arr[1:]:
    curr.next = Node(c)
    curr = curr.next

  curr = head
  while curr:
    print(curr.val)
    curr = curr.next
    
  ans = isPalindrome(head)
  print(ans)

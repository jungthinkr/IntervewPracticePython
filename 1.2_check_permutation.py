"""
Given two strings, write a method to decide if one is a permutation of the other.
"""

def ispermutation(a, b):
  i = 0
  j = 0
  
  for c in a:
    i += ord(c)
  for c in b:
    j += ord(c)
  
  return i == j and len(a) == len(b)

if __name__ == '__main__':
  print("Is Permutation: aab, baa {0}".format(ispermutation('aab', 'baa')))
  print("Is Permutation: aaa, ijk {0}".format(ispermutation('aaa', 'ijk')))

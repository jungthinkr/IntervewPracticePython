"""
Implement an alogrithm to determine if a string has unique characters. 
What if you cannot use additional data structures?
"""
def findUniqueCharacters1(s):
  charSet = set()
  for c in s:
    if c in charSet:
      return False
    charSet.add(c)
  return True

def findUniqueCharacters2(s):
  for i in range(len(s)):
    for j in range(len(s)-1):
      if s[i] == s[j] and i != j:
        return False
  return True

if __name__ == '__main__':
  print('findUniqueCharacters1: aab {0}'.format(findUniqueCharacters1('aab')))
  print('findUniqueCharacters1: abc {0}'.format(findUniqueCharacters1('abc')))

  print('findUniqueCharacters2: aab {0}'.format(findUniqueCharacters2('aab')))
  print('findUniqueCharacters2: abc {0}'.format(findUniqueCharacters2('abc')))

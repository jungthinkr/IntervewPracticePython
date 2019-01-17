"""
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A 
permutation is a rearrangement of letters. The palindrome does not need to be
limited to just dictionary words

EXAMPLE
Input: Tact Coa
Output True (permutations: "taco cat", "atco cta", etc.)
"""

def ispermutation(s):
  map = {}
  for c in s.lower().replace(' ', ''):
    map[c] = map.get(c, 0) + 1
  print(map)
  numOfOddNum = 0
  for key in map.keys():
    if map[key]%2 == 1:
      numOfOddNum += 1
    if numOfOddNum > 1:
      return False

  return True
    
if __name__ == '__main__':
  print('Is Palindrome Permutation: Tact Coa {0}'.format(ispermutation('Tact Coa')))
  

"""
There are three types of edits that can be performed on strings: 
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit
(or zero edits) away.

EXAMPLE

pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""
def isoneoperationaway(a, b):
  if a == b:
    return True 
  m = 0
  l = max(len(a), len(b))

  for i in range(l):
    if i < len(a):
      m ^= ord(a[i])
    if i < len(b):
      m ^= ord(b[i])
  return chr(m).isalpha()

if __name__ == '__main__':
  print("isoneoperationaway 'pale', 'ale' {0}".format(isoneoperationaway('pale', 'ple')))

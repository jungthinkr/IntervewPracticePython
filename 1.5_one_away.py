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
  l = max(len(a), len(b))
  if a == b:
    return True

  if len(a) == len(b):
    for i in range(l):
      if a[i] != b[i]:
        arrA = list(a)
        arrB = list(b)
        arrA[i] = arrB[i]
        return arrA == arrB
  else:
    c = 0 
    for i in range(l):
      if i < len(a):
        c ^= ord(a[i])
      if i < len(b):
        c ^= ord(b[i])
    return chr(c).isalpha()

if __name__ == '__main__':
  print("isoneoperationaway 'le', 'pale' {0}".format(isoneoperationaway('le', 'pale')))
  print("isoneoperationaway 'pale', 'ale' {0}".format(isoneoperationaway('pale', 'ale')))
  print("isoneoperationaway 'pales', 'pale' {0}".format(isoneoperationaway('pales', 'pale')))
  print("isoneoperationaway 'pale', 'bale' {0}".format(isoneoperationaway('pale', 'bale')))
  print("isoneoperationaway 'pale', 'bake' {0}".format(isoneoperationaway('pale', 'bake')))
  print("... 'california', 'nevada' {0}".format(isoneoperationaway('california', 'nevada')))
  print("... 'a', 'aaaaa' {0}".format(isoneoperationaway('a', 'aaaaa')))
  print("... 'pale', 'pale' {0}".format(isoneoperationaway('pale', 'pale')))
 
  
  

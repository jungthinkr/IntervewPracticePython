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
  return len(set(a)-set(b)) <= 1
  

if __name__ == '__main__':
  print("isoneoperationaway 'pale', 'pale' {0}".format(isoneoperationaway('pale', 'pale')))
  print("isoneoperationaway 'pale', 'ale' {0}".format(isoneoperationaway('pale', 'ale')))
  print("isoneoperationaway 'pales', 'pale' {0}".format(isoneoperationaway('pales', 'pale')))
  print("isoneoperationaway 'pale', 'bale' {0}".format(isoneoperationaway('pale', 'bale')))
  print("isoneoperationaway 'pale', 'bake' {0}".format(isoneoperationaway('pale', 'bake')))

  
  
  

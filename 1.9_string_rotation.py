"""
Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a
rotation of s1 using only one call to isSubtring
(e.g. "waterbottle" is a rotation of "erbottlewat").
"""


def isRotation(s1, s2):
  if len(s1) != len(s2):
    return False

  for i in range(len(s1)):
    s = s1[i:]+s1[:i]
    if s == s2:
      return True
  return False


if __name__  == '__main__':
  print("isRotation 'waterbottle', 'erbottlewat': {0}".format(isRotation("waterbottle", "erbottlewat")))
  print("isRotation 'zeromatrix', 'atrixzerom': {0}".format(isRotation("zeromatrix", "atrixzerom")))



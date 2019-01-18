"""
  Implement a method to perform basic string compression using the counts
  of repeated characters. For example, the string aabcccccaaa would become
  a2b1c5a3. If the "compressed" string would not become smaller than the original
  string, your method should return the original string. You can assume the string
  has only uppercase and lowercase letters (a-z).

"""


def compress(s):
  i = 0
  currC = None
  result = ''
  for c in s:
    if currC == None:
      currC = c

    if c != currC and i > 0:
      #add to compressed string
      result += "{0}{1}".format(currC, i)
      currC = c
      i = 1
    elif c == currC:
      i += 1

  #add remaning char to result
  result += "{0}{1}".format(currC, i)
  print("compress {0} = '{1}'".format(s, result))
  return result

if __name__ == '__main__':
  compress('aabcccccaaa')
  compress('aaabcccccaaa')
  compress('aabcccccaaaa')
  compress('aabbcccccaaaa')

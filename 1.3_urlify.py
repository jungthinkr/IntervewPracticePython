"""
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end
to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use
a chracter array so that you can perform this operation in place

EXAMPLE

Input: "Mr  John  Smith    ", 13
Output: "Mr%20John%20Smith"

"""
#doesnt seem like the length matters?

def urlify(s, length):
  arr = s.split()
  result = ''
  for i in range(len(arr)):
    if i == len(arr)-1:
      result += arr[i]
    else:
      result += arr[i]+'%20'
  return result

if __name__ == '__main__':
  print('urlify: Mr John Smith     {0}'.format(urlify('Mr John Smith      ', 13)))
  
  

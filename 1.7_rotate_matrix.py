"""
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a 
method to rotate the image by 90 degrees. Can you do this in place?
"""

def rotate(m):
  if len(m) == 0:
    return m

  for r in m:
    print(r)
  print('')

  L = len(m)

  for i in range(L/2):
    a = L-i-1
    for j in range(i, a):
      b = L-j-1
      temp = m[i][j]
      m[i][j] = m[j][a]
      m[j][a] = m[a][b]
      m[a][b] = m[b][i]
      m[b][i] = temp

  for r in m:
    print(r)

  return m


def rotate2(m):
  # find transpose
  # reverse each column

  t = [[0]*len(m[0]) for x in range(len(m))]

  #transpose and reverse columns
  for i in range(len(m)):
    for j in range(len(m[0])):
      t[j][i] = m[i][len(m)-1-j]
      
  for r in t:
    print(r)


if __name__ == '__main__':
  rotate2([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  rotate1([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
  
  

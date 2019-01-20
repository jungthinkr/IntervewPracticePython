"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row
and column are set to 0
"""

def zeroify(m):
  if len(m) == 0:
    return m

  for r in m:
    print(r)
  zeroes = []
  for i in range(len(m)):
    for j in range(len(m[0])):
      if m[i][j] == 0:
        zeroes.append((i,j))

  for c in zeroes:
    for a in range(len(m)):
      m[a][c[1]] = 0
    for a in range(len(m[0])):
      m[c[0]][a] = 0
    
  for r in m:
    print(r)



if __name__ == '__main__':
  zeroify([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

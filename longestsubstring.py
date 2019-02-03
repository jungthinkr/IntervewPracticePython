def maxSubstringNonRepeating(s):
  maxT = 0
  t = 0
  b = set()

  for c in s:
    b.add(c)
    t += 1

    if len(b) > maxT:
      maxT = len(b)

    if t != len(b):
      b = set(c)
      t = 1

  return max(maxT, len(b))

if __name__ == '__main__':
  s = 'abcabcabcd'
  maxSS = maxSubstringNonRepeating(s)
  print(maxSS)

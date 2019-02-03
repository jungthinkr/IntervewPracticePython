
def findMax(arr):
  do_pick = [0]*len(arr)
  do_not_pick = [0]*len(arr)
  do_pick[0] = arr[0]

  #do_pick = 2

  for i in range(1, len(arr)):
    do_pick[i] = do_not_pick[i-1] + arr[i]
    do_not_pick[i] = max(do_not_pick[i-1], do_pick[i-1])

  return do_pick[-1]
  

if __name__ == '__main__':
  arr = [3,2,3,2]
  print(findMax(arr))
  

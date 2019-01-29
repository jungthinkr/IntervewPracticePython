

def mergesort(arr):
  if len(arr) > 1:
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]

    mergesort(R)
    # i = L
    # j = R
    # k = total
    i,j,k = 0, 0, 0

    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = R[j]
        j += 1

      k += 1

    while i < len(L):
      arr[k] = L[i]
      i+=1
      k+=1

    while j  < len(R):
      arr[k] = R[j]
      j+=1
      k+=1
    return arr

  

if __name__ == '__main__':
  # sort
  print(mergesort([1,3,2,5,7,0]))



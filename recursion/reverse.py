arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def rev(arr):
  l = len(arr)
  if l <= 1:
    return arr
  hl = l // 2
  return rev(arr[hl:]) + rev(arr[:hl])


print(rev(arr))

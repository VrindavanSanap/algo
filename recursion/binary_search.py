my_list = [1, 3, 5, 7, 9]


def binary_search(arr, item):
  low = 0
  high = len(arr) - 1

  while high > low:
    mid = (high + low) // 2 + 1
    guess = arr[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else: 
      low = mid + 1
  return -1
print(binary_search(my_list, 3))
print(binary_search(my_list, 11))

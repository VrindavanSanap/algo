from typing import List

my_list: List[int] = [1, 3, 5, 7, 9]


def binary_search(arr: List[int], item: int) -> int:
  low: int = 0
  high: int = len(arr) - 1

  while high > low:
    mid: int = (high + low) // 2 + 1
    guess: int = arr[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return -1


print(binary_search(my_list, 3))
print(binary_search(my_list, 11))

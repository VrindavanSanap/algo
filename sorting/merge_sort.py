from typing import List

arr: List[int] = [11, 2, 123, 12, 11134, 3, 234, 26, 74534]


def merge(left: List[int], right: List[int]) -> List[int]:
  result: List[int] = []
  left_index, right_index = 0, 0
  while left_index < len(left) and right_index < len(right):
    if left[left_index] < right[right_index]:
      result.append(left[left_index])
      left_index += 1
    else:
      result.append(right[right_index])
      right_index += 1
  result.extend(left[left_index:])
  result.extend(right[right_index:])
  return result


def merge_sort(arr: List[int]) -> List[int]:
  if len(arr) < 2:
    return arr
  mid: int = len(arr) // 2
  left_half: List[int] = merge_sort(arr[:mid])
  right_half: List[int] = merge_sort(arr[mid:])
  return merge(left_half, right_half)


print(merge_sort(arr))

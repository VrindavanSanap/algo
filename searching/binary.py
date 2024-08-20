#!/usr/bin/python3
import math
from typing import List

data: List[int] = list(range(1, 11))


def binary_search(data: List[int], value: int) -> int:
  l: int = 0
  r: int = len(data) - 1
  while l <= r:
    m: int = math.floor((l + r) / 2)
    value_m: int = data[m]
    print(value_m)
    if value_m == value:
      return m
    elif value_m < value:
      l = m + 1
    elif value_m > value:
      r = m - 1

  return -1


res: int = binary_search(data, 9)
print(f"found at index:{res}")

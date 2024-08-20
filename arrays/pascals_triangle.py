#!/usr/bin/python3
# https://leetcode.com/problems/pascals-triangle/
"""
for i in range(-1,len(a)):
    ...:     print(a[max(0,i):i+2])

"""

from typing import List

def pascals_triangle(n: int) -> List[List[int]]:
  rows: List[List[int]] = [[1]]
  for i in range(1, n):
    row: List[int] = []
    for j in range(-1, i):
      row.append(sum(rows[i - 1][max(0, j) : j + 2]))

    rows.append(row)

  return rows

triangle: List[List[int]] = pascals_triangle(5)
print(triangle)

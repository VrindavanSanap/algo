#!/usr/bin/python3
# https://leetcode.com/problems/pascals-triangle/
"""
for i in range(-1,len(a)):
    ...:     print(a[max(0,i):i+2])

"""


def pascals_triangle(n):
  rows = [[1]]
  for i in range(1, n):
    row = []
    for j in range(-1, i):
      row.append(sum(rows[i - 1][max(0, j) : j + 2]))

    rows.append(row)

  return rows


triangle = pascals_triangle(5)
print(triangle)

#!/usr/bin/python3

import numpy as np
from check_grid import check_grid

grid = [
  [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def possible(x, y, n):
  # check row
  for i in range(9):
    if grid[x][i] == n:
      return False
    if grid[i][y] == n:
      return False
  # check box
  x0 = (x // 3) * 3
  y0 = (y // 3) * 3
  for i in range(3):
    for j in range(3):
      if grid[x0 + i][y0 + j] == n:
        return False
  return True


def solve():
  global grid
  for i in range(0, 9):
    for j in range(0, 9):
      if grid[i][j] == 0:
        for _ in range(1, 10):
          if possible(i, j, _):
            grid[i][j] = _
            solve()
            grid[i][j] = 0
        return

  print(np.matrix(grid))


if __name__ == "__main__":
  grid = [[0 for _ in range(9)] for _ in range(9)]
  i = 0
  while i < 9:
    print(f"give row: {i + 1}")
    row = input()
    if len(row) != 9:
      print("Give 9 numbers")
      continue

    if not check_grid(grid):
      print("Numbers make the grid invalid")
      continue
    grid[i] = [int(n) for n in row]
    i += 1
    print(np.matrix(grid))

solve()

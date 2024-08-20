"""
l1 = input()
l1 = [int(i) for i in l1.split()]
h = l1[0]
w = l1[1]
"""

from collections import deque

import numpy as np

h = 5
w = 8

grid = ["########", "#.A#...#", "#.##.#B#", "#......#", "########"]

# grid = ["########",
# "#..#...#",
# "#.##.#B#",
# "#......#",
# "########"]
grid = [[s for s in string] for string in grid]
x = 3
y = 1
print(np.matrix(grid))


def bfs(r, c):
  r -= 1
  c -= 1
  search_queue = deque()
  search_queue.append((r, c))
  searched = [(r, c)]
  while search_queue:
    cell = search_queue.popleft()
    r, c = cell
    print(r, c)
    # Right, Left, Down, Up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ltr = ["R", "L", "D", "U"]
    for x_, y_ in directions:
      ri = r + x_
      ci = c + y_

      if 0 <= ri < len(grid) and 0 <= ci < len(grid[0]):
        if grid[ri][ci] == "B":
          print(ri, ci, "Found")
          return (ri, ci)
        if not grid[ri][ci] == "#":
          if (ri, ci) not in searched:
            searched.append((ri, ci))
            search_queue.append((ri, ci))


print(bfs(2, 3))

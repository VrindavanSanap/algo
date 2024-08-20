from collections import deque

import numpy as np

r = 5
c = 8
grid = ["########", "#..#...#", "####.#.#", "#..#...#", "########"]

grid = [[i for i in j] for j in grid]
print(np.matrix(grid))

visited = []
n_rooms = 0


def explore(y, x):
  # up down left right
  print(y, x)
  queue = deque([[y, x]])
  global visited
  visited.append([y, x])
  while len(queue):
    y, x = queue.popleft()
    for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
      yi, xi = y + dy, x + dx
      if [yi, xi] not in visited:
        if not (yi >= r or xi >= c or yi < 0 or xi < 0):
          if grid[yi][xi] == ".":
            queue.append([yi, xi])
            visited.append([yi, xi])


for yi in range(r):
  for xi in range(c):
    if [yi, xi] not in visited:
      if grid[yi][xi] == ".":
        n_rooms += 1
        explore(yi, xi)
print(n_rooms)

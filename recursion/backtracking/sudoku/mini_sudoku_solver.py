grid = [[0, 7, 0], [8, 3, 0], [0, 4, 5]]


def possible(x, y, n):
  for i in range(3):
    if grid[x][i] == n:
      return False
    if grid[i][y] == n:
      return False
  for i in range(3):
    for j in range(3):
      if grid[i][j] == n:
        return False

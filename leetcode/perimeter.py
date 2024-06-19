
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
for row in grid:
  print(row)


def visit_all(grid):
  n_rows = len(grid)
  n_cols = len(grid[0])
  for i in range(n_rows):
    for j in range(n_cols):
      if grid[i][j] == 1:
        first = [i, j]
  visited = [] 
  perimeter = 0  
  def visit_all_(i, j):
    nonlocal perimeter
    visited.append([i, j])
    perimeter += 4
    if i >= 1:
      if grid[i-1][j]  == 1:
        perimeter -= 1
        if [i - 1, j] not in visited:
          visit_all_(i - 1, j)

    if i < n_rows - 1:
      if grid[i + 1][ j]  == 1:
        perimeter -= 1
        if [i +  1, j] not in visited:
          visit_all_(i + 1, j)

    
    if j >= 1:
      if grid[i][ j - 1]  == 1:
        perimeter -= 1
        if [i, j - 1] not in visited:
          visit_all_(i, j - 1)

    if j < n_cols - 1:
      if grid[i][ j + 1]  == 1:
        perimeter -= 1
        if [i, j + 1] not in visited:
          visit_all_(i, j + 1)

 
  visit_all_(first[0], first[1])
  return perimeter 


print(visit_all(grid))

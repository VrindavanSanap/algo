import numpy as np

with open("triangle.txt") as f:
  data = f.read().strip().split("\n")

data_matrix = []
for line in data:
  data_matrix.append(np.array([int(i) for i in line.split()]))


def get_max_neighbours(row):
  print(row)
  return np.maximum(row[:-1], row[1:])


prev = np.zeros(len(data_matrix[-1]))
for row in reversed(data_matrix):
  prev = get_max_neighbours(row + prev)

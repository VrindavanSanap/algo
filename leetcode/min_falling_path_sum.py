#!/usr/bin/python3
triangle = [[17, 82], [1, -44]]


def conv_row(row, prev):
  i = 0
  inf = float("inf")
  for elm1, elm2, elm3 in zip([inf] + row[:-1], row, row[1:] + [inf]):
    prev[i] = min(elm1, elm2, elm3)
    i += 1
  return prev


def min_path_sum(triangle):
  last_layer = triangle[-1]
  for row in reversed(triangle[:-1]):
    last_layer = conv_row(last_layer, row)
    print(last_layer)
    break
  return min(last_layer)


print(min_path_sum(triangle))

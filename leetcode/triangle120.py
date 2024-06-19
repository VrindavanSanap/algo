#!/usr/bin/python3

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

def conv_row(row, prev):
  i = 0
  for elm1, elm2, in zip(row[:-1], row[1:]):
    prev[i] += (min(elm1, elm2))
    i+= 1
  return prev 


def min_path_sum(triangle):
  last_layer = triangle[-1]
  for row in reversed(triangle[:-1]):
    last_layer = conv_row(last_layer, row)

  return last_layer[0]

min_path_sum(triangle)

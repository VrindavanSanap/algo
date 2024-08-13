#!/usr/bin/python3
import numpy as np

image = [[0, 0, 0], [0, 0, 0]]
sr = 0
sc = 0
color = 0
counter = 0


def flood_fill(image, sr, sc, color):
  global counter
  counter += 1
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
  original_color = image[sr][sc]
  image[sr][sc] = color
  if original_color == color:
    return
  for dr, dc in directions:
    r = sr + dr
    c = sc + dc

    if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == original_color:
      flood_fill(image, r, c, color)


flood_fill(image, sr, sc, color)
print(np.matrix(image))
print(counter)

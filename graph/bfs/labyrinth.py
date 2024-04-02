#!/usr/bin/python3

import numpy as np
from collections import deque
r = 5
c = 8
grid = ["########",
        "#.A#...#",
        "#.##.#B#",
        "#......#",
        "########"]
grid = [[i for i in j] for j in grid]
print(np.matrix(grid))


def find_a(grid):
    for i in range(r):
        for j in range(c):
            if grid[i][j] == "A":
                return i, j


y, x = find_a(grid)
print(y, x, grid[y][x])


def bfs(y, x):
    # up down left right
    queue = deque([[y, x]])
    visited = []
    visited.append([y, x])
    while len(queue):
        y, x = queue.popleft()
        for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            yi, xi = y + dy, x + dx
            if not ([yi, xi] in visited):
                if not (yi >= r or xi >= c or yi < 0 or xi < 0):
                    if grid[yi][xi] == "B":
                        print("Found! ")
                        return
                    if grid[yi][xi] == ".":
                        queue.append([yi, xi])
                        visited.append([yi, xi])
                        print([yi, xi], grid[yi][xi])


bfs(y, x)

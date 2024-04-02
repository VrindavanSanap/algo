from collections import deque
l1 = input()
l1 = [int(i) for i in l1.split()]
r = l1[0]
c = l1[1]
grid = []
for i in range(r):
    grid.append(input())
visited = []
n_rooms = 0

v = [-1, 1, 0, 0] 
h = [0, 0, -1, 1] 

def explore(y, x):
    # up down left right
    queue = deque([[y, x]])
    global visited
    visited.append([y, x])
    while len(queue):
        y, x = queue.popleft()
        for i in range(4):
            yi, xi = y + v[i], x + h[i]
            if not ([yi, xi] in visited):
                if not (yi >= r or xi >= c or yi < 0 or xi < 0):
                    if grid[yi][xi] == ".":
                        queue.append([yi, xi])
                        visited.append([yi, xi])


for yi in range(r):
    for xi in range(c):
        if not [yi, xi] in visited:
            if grid[yi][xi] == ".":
                n_rooms += 1
                explore(yi, xi)
print(n_rooms)

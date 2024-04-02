from collections import deque

r, c = map(int, input().split())
grid = [input() for _ in range(r)]
visited = set()
n_rooms = 0

def explore(y, x):
    queue = deque([(y, x)])
    visited.add((y, x))
    while queue:
        y, x = queue.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            yi, xi = y + dy, x + dx
            if (yi, xi) not in visited and 0 <= yi < r and 0 <= xi < c and grid[yi][xi] == ".":
                queue.append((yi, xi))
                visited.add((yi, xi))

for yi in range(r):
    for xi in range(c):
        if (yi, xi) not in visited and grid[yi][xi] == ".":
            n_rooms += 1
            explore(yi, xi)
print(n_rooms)

from collections import deque


q = deque()
q.append((1,2))
for x, y in q:
  print(x, y)

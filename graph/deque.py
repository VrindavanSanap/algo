from collections import deque

search_queue = deque()
search_queue += [10,20,30,40]

res = search_queue.popleft()
print(res, search_queue)


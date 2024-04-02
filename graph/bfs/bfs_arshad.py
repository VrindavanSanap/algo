#https://arshad-kazi.com/bfs-and-dfs-algorithms-in-simple-words/
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)


graph = {
    'Shop A': ['Shop B', 'Shop C', 'Shop D'],
    'Shop B': ['Shop A', 'Shop E', 'Shop F'],
    'Shop C': ['Shop A', 'Shop G'],
    'Shop D': ['Shop A', 'Shop H', 'Shop I'],
    'Shop E': ['Shop B'],
    'Shop F': ['Shop B'],
    'Shop G': ['Shop C', 'Shop J'],
    'Shop H': ['Shop D'],
    'Shop I': ['Shop D', 'Shop K', 'Shop L'],
    'Shop J': ['Shop G'],
    'Shop K': ['Shop I'],
    'Shop L': ['Shop I']
}

# Starting node for BFS
start_node = 'Shop A'

print("BFS Traversal:")
bfs(graph, start_node)

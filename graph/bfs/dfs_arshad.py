def dfs(graph, start, visited=None):
  if visited is None:
    visited = set()

  if start not in visited:
    print(start, end=" ")
    visited.add(start)

    for neighbor in graph[start]:
      dfs(graph, neighbor, visited)


graph = {
  "Shop A": ["Shop B", "Shop C", "Shop D"],
  "Shop B": ["Shop A", "Shop E", "Shop F"],
  "Shop C": ["Shop A", "Shop G"],
  "Shop D": ["Shop A", "Shop H", "Shop I"],
  "Shop E": ["Shop B"],
  "Shop F": ["Shop B"],
  "Shop G": ["Shop C", "Shop J"],
  "Shop H": ["Shop D"],
  "Shop I": ["Shop D", "Shop K", "Shop L"],
  "Shop J": ["Shop G"],
  "Shop K": ["Shop I"],
  "Shop L": ["Shop I"],
}

# Starting node for DFS
start_node_dfs = "Shop A"

print("DFS Traversal:")
dfs(graph, start_node_dfs)

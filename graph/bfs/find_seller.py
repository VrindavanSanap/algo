#!/usr/bin/python3
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
  return name[-1] == "m" 

def bfs(name):
  search_queue = deque()
  search_queue += graph[name]
  searched = []
  while search_queue:
    person = search_queue.popleft()
    if not person is searched:
      if person_is_seller(person):
        print(f"{person} is a seller")
        return True
      else:
        search_queue += graph[person]
        searched.append(person)
  return 

print(bfs("you"))

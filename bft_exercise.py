from collections import deque

def breadth_first_traversal(graph, start):
    pass

graph = {
  "A" : ["C", "D", "E"],
  "B" : ["A", "C", "E"],
  "C" : ["A", "B"],
  "D" : ["A", "E"],
  "E" : ["A", "B"]
}

breadth_first_traversal(graph, "A")

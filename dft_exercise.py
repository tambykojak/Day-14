def depth_first_traversal(graph, start):
    pass

graph = {
  "A" : ["B", "C", "D", "E"],
  "B" : ["A", "C", "E"],
  "C" : ["A", "B"],
  "D" : ["A", "E"],
  "E" : ["A", "B"]
}

depth_first_traversal(graph, "A")

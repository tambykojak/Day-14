def depth_first_traversal(graph, start):
    visited = {}

    for k in graph:
        visited[k] = False

    node_stack = [start]
    print start
    visited[start] = True

    while len(node_stack) != 0:
        current_node = node_stack[len(node_stack) - 1]
        neighbors = graph[current_node]

        first_unvisited_neighbor = None

        for n in neighbors:
            if not visited[n]:
                first_unvisited_neighbor = n
                break;

        if first_unvisited_neighbor is not None:
            print first_unvisited_neighbor
            visited[first_unvisited_neighbor] = True
            node_stack.append(first_unvisited_neighbor)
        else:
            node_stack.pop()

graph = {
  "A" : ["B", "C", "D", "E"],
  "B" : ["A", "C", "E"],
  "C" : ["A", "B"],
  "D" : ["A", "E"],
  "E" : ["A", "B"]
}

depth_first_traversal(graph, "A")

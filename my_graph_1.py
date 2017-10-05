class GraphNode:
    def __init__(self, value):
        self.value
        self.weight

class GraphEdge:
    def __init__(self, first_node, second_node):
        self.first_node = first_node
        self.second_node = second_node

class MyGraph:
    def __init__(self):
        self.verticies = []
        self.edges = []

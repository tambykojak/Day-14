class MyGraph:
    def __init__(self):
        self.graph = {
            "A" : ["B", "C", "D", "E"],
            "B" : ["A", "C", "E"],
            "C" : ["A", "B"],
            "D" : ["A", "E"],
            "E" : ["A", "B"]
        }

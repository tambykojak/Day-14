
class MyGraph:
    def __init__(self):
        self.verticies = [
            "A", "B", "C", "D", "E"
        ]

        self.matrix = [
            #A  B  C  D  E
            [0, 1, 1, 1, 1], # A
            [1, 0, 1, 0, 1], # B
            [1, 1, 0, 0, 0], # C
            [1, 0, 0, 0, 1], # D
            [1, 1, 0, 0, 0]  # E
        ]

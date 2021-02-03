class DirectedGraph:
    adjacencyLists = {}

    def __init__(self, vertices):
        for vertex in vertices:
            self.adjacencyLists[vertex] = []

    def addEdge(self, firstVertex, secondVertex):
        if firstVertex in self.adjacencyLists.keys():
            if secondVertex not in self.adjacencyLists[firstVertex]:
                self.adjacencyLists[firstVertex].append(secondVertex)
        else:
            print("Error 1")

    def print(self):
        for firstVertex in self.adjacencyLists:
            for secondVertex in self.adjacencyLists[firstVertex]:
                print(firstVertex, ",",secondVertex)

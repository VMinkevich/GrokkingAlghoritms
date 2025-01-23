class UndirectedGraph:
    
    """Undirected graph implementation
    Space complexity: O(V + E) where V is the number of vertices and E is the number of edges
    Time complexity: O(1) for adding a node, O(1) for adding an edge, O(V) for printing the graph
    """

    def __init__(self):
        self.graph = {}

    def addNode(self, node1):
        if node1 not in self.graph:
            self.graph[node1] = []
    
    def addEdge(self, node1, node2):
        if node1 not in self.graph:
            self.addNode(node1)
        if node2 not in self.graph:
            self.addNode(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def printGraph(self):
        for nodes, neighbours in self.graph.items():
            print(f"{nodes}: {neighbours}")

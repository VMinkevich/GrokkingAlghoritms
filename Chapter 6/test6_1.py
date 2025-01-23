import UndirectedGraph as graph

g = graph.UndirectedGraph()
g.addNode('A')
g.addNode('B')
g.addNode('C')
g.addNode('D')
g.addNode('E')
g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'D')
g.addEdge('C', 'E')
g.printGraph()
# Output:
# A: ['B', 'C']
# B: ['A', 'D']
# C: ['A', 'E']
# D: ['B']
# E: ['C']
g.addEdge('D', 'E')
g.printGraph()
# Output:
# A: ['B', 'C']
# B: ['A', 'D']
# C: ['A', 'E']
# D: ['B', 'E']
# E: ['C', 'D']
g.addEdge('E', 'F')
g.printGraph()
# Output:
# A: ['B', 'C']
# B: ['A', 'D']
# C: ['A', 'E']
# D: ['B', 'E']
# E: ['C', 'D', 'F']
# F: ['E']
g.addEdge('F', 'G')
g.printGraph()
# Output:
# A: ['B', 'C']
# B: ['A', 'D']
# C: ['A', 'E']
# D: ['B', 'E']
# E: ['C', 'D', 'F']
# F: ['E', 'G']
# G: ['F']
g.addEdge('G', 'H')
g.printGraph()
# Output:
# A: ['B', 'C']
# B: ['A', 'D']
# C: ['A', 'E']
# D: ['B', 'E']
# E: ['C', 'D', 'F']
# F: ['E', 'G']
# G: ['F', 'H']
# H: ['G']
g.addEdge('H', 'I')
g.printGraph()
# Output:
# A: ['B', 'C']
# B: ['A', 'D']
# C: ['A', 'E']
# D: ['B', 'E']
# E: ['C', 'D', 'F']
# F: ['E', 'G']
# G: ['F', 'H']
# H: ['G', 'I']
# I: ['H']

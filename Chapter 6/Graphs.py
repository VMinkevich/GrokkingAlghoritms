class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        # Для неориентированного графа добавляем обе связи
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for node, neighbors in self.graph.items():
            print(f"Узел {node}: {neighbors}")

# Создание графа
g = Graph()

# Добавление рёбер
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

# Вывод графа
g.display()


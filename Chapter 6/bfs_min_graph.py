import random

# NEED TO BE FIXED!!!!!!!!!!

def generate_random_graph(num_nodes, num_edges):
    # Генерация списка вершин
    nodes = [i for i in range(-10, num_nodes + 1)]

    # Инициализация пустого графа в виде словаря
    graph = {node: [] for node in nodes}

    # Добавление случайных рёбер
    for _ in range(num_edges):
        node1 = random.choice(nodes)
        node2 = random.choice(nodes)

        # Чтобы не было рёбер от узла к самому себе
        while node1 == node2:
            node2 = random.choice(nodes)

        # Добавление рёбер в граф (двусторонние рёбра)
        if node2 not in graph[node1]:
            graph[node1].append(node2)
        if node1 not in graph[node2]:
            graph[node2].append(node1)

    return graph

# Пример использования:
num_nodes = 10  # Количество узлов
num_edges = 12  # Количество рёбер

random_graph = generate_random_graph(num_nodes, num_edges)


def person_is_seller(val):
    return val

def BFS_min_value(graph):
    search_deque = deque()
    search_deque += graph[4]
    searched = [9999999999999999]
    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if person_is_seller(person) < min(searched):
                return person
            else:
                search_deque += graph[person]
                searched.append(person)
    return -1
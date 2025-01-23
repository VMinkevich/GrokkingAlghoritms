from collections import deque
import UndirectedGraph as UG

graph = {}
graph["вы"] = ["Алиса", "Боб", "Клэр"]
graph["Боб"] = ["Анудж", "Пегги"]
graph["Алиса"] = ["Пегги"]
graph["Клэр"] = ["Том", "Джонни"]
graph["Анудж"] = []
graph["Пегги"] = []
graph["Том"] = []
graph["Джонни"] = []


def person_is_seller(name):
    return name[-1] == 'м'

def BFS(graph):
    search_deque = deque()
    search_deque += graph["вы"]
    searched = []
    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if person_is_seller(person):
                return person
            else:
                search_deque += graph[person]
                searched.append(person)
    return -1

print(BFS(graph))
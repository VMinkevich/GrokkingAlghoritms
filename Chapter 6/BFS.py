from collections import deque

def BFS(name):
    
    graph = {}
    search_deque = deque()
    search_deque += graph[name]
    searched = []
    while search_deque:
        person = search_deque.popleft()
        if not person in searched:
            if person_is_seller(person):
                print('Yes, he sells Mango')
            else:
                search_deque += graph[person]
                searched.append(person)
    return False


def person_is_seller(name):
    return name[-1] == 'm'

print(BFS('I'))
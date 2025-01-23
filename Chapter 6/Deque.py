class Deque:
    def __init__(self):
        self.array = []

    def insert(self, val):
        self.array.append(val)

    def popleft(self):
        self.array.pop(0)

    def display(self):
        print(self.array)

class Node:
    def __init__(self, data):
        self.data = data # Данные, хранимые в узле
        self.next = None  # Указатель на следующий узел

class LinkedList:
    def __init__(self):
        self.head = None  # Изначально список пустой, голова списка - None

    def append(self, data):
        new_node = Node(data)  # Создаем новый узел
        if not self.head:
            self.head = new_node  # Если список пустой, новый узел становится головой
            return
        last = self.head
        while last.next:  # Ищем последний узел
            last = last.next
        last.next = new_node  # Добавляем новый узел в конец списка

    def prepend(self, data):
        new_node = Node(data)  # Создаем новый узел
        new_node.next = self.head  # Новый узел указывает на текущую голову списка
        self.head = new_node  # Новый узел становится головой списка

    def display(self):
        current = self.head
        while current:  # Проходим по всем узлам списка
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next  # Если нужно удалить голову списка
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:  # Если элемент не найден
            print(f"Элемент {key} не найден.")
            return

        prev.next = current.next  # Пропускаем удаляемый элемент
        current = None  # Освобождаем память

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

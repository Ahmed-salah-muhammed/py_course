class Queue:
    def __init__(self):
        self.items = []

    def insert(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print("Warning: Queue is empty")
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

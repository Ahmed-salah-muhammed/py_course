import json


class QueueOutOfRangeException(Exception):
    pass


class namedQueue:

    all_queues = {}

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.items = []

        namedQueue.all_queues[name] = self

    def insert(self, value):
        if len(self.items) >= self.size:
            raise QueueOutOfRangeException("Queue is full!")
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print("Warning: Queue is empty")
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    @classmethod
    def get_queue_by_name(cls, name):
        return cls.all_queues.get(name)

    @classmethod
    def save(cls, filename="queues.json"):
        data = {}
        for name, queue in cls.all_queues.items():
            data[name] = {"size": queue.size, "items": queue.items}

        with open(filename, "w") as f:
            json.dump(data, f)

    @classmethod
    def load(cls, filename="queues.json"):
        with open(filename, "r") as f:
            data = json.load(f)

        for name, info in data.items():
            q = cls(name, info["size"])
            q.items = info["items"]

from basic_queue import Queue
from named_queue import namedQueue, QueueOutOfRangeException


q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)

print("Basic Queue Pop:", q.pop())
print("Is Empty:", q.is_empty())


try:
    aq = namedQueue("Orders", 3)

    aq.insert(1)
    aq.insert(2)
    aq.insert(3)

    print("Named Queue Pop:", aq.pop())

    namedQueue.save()

except QueueOutOfRangeException as e:
    print("Exception:", e)

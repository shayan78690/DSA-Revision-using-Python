class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, val):
        self.queue.append(val)
    def dequeue(self):
        return -1 if not self.queue else self.queue.pop(0)
    def peek(self):
        return -1 if not self.queue else self.queue[0]
    def isEmpty(self):
        return len(self.queue) == 0
    def display(self):
        print(self.queue)

q = Queue()
q.enqueue(5)
q.display()
q.enqueue(6)
q.display()
q.enqueue(7)
q.display()
q.enqueue(8)
q.display()
q.enqueue(9)
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
print(q.isEmpty())

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, val):
        self.stack1.append(val)
    def pop(self):
        if not self.stack2:
            while self.stack1:
                element = self.stack1.pop()
                self.stack2.append(element)
        return self.stack2.pop()
    def peek(self):
        if not self.stack2:
            while self.stack1:
                element = self.stack1.pop()
                self.stack2.append(element)
        return self.stack2[-1]
    def isEmpty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

queue = Queue()
queue.push(5)
queue.push(10)
print(queue.pop())
print(queue.peek())
print(queue.isEmpty())

from collections import deque
class Stack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
    def push(self, val):
        if self.queue1:
            self.queue1.append(val)
        else:
            self.queue2.append(val)
    def pop(self):
        if self.isEmpty():
            return -1
        top = -1
        if self.queue1:
            while len(self.queue1) > 1:
                top = self.queue1.popleft()
                self.queue2.append(top)
            top = self.queue1.popleft()
        else:
            while len(self.queue2) > 1:
                top = self.queue2.popleft()
                self.queue1.append(top)
            top = self.queue2.popleft()
        return top
        
    def peek(self):
        if self.isEmpty():
            return -1
        top = -1
        if self.queue1:
            while len(self.queue1) > 1:
                top = self.queue1.popleft()
                self.queue2.append(top)
            top = self.queue1[0]
        else:
            while len(self.queue2) > 1:
                top = self.queue2.popleft()
                self.queue1.append(top)
            top = self.queue2[0]
        return top
    
    def isEmpty(self):
        return len(self.queue1) == 0 and len(self.queue2) == 0

stack = Stack()
stack.push(5)
stack.push(6)
stack.push(10)
print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.isEmpty())

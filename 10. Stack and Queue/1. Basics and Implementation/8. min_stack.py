class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, value):
        self.stack.append(value)
        if not self.minstack or self.minstack[-1] >= value:
            self.minstack.append(value)

    def pop(self):
        if not self.stack:
            return
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()
        
    def top(self):
        if not self.stack:
            return 0
        return self.stack[-1]
        
    def getMin(self):
        if not self.minstack:
            return 0
        return self.minstack[-1]
        
        


class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, value):
        self.stack.append(value)
        if not self.minstack or self.minstack[-1] >= value:
            self.minstack.append(value)
    def pop(self):
        if not self.stack:
            return
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        return self.stack.pop()
    def top(self):
        if not self.stack:
            return 0
        return self.stack[-1]
    def minimum(self):
        if not self.minstack:
            return 0
        return self.minstack[-1]

obj = Solution()
obj.push(-2)
print(obj.stack)
obj.push(0)
print(obj.stack)
obj.push(3)
print(obj.stack)
print(obj.minimum())
obj.pop()
print(obj.stack)
print(obj.top())
print(obj.minimum())
print(obj.stack)


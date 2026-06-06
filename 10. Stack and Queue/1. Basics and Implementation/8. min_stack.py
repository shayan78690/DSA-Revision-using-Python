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
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

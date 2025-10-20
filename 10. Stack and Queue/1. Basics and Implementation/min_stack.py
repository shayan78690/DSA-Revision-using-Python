class MinStack(object):
    def __init__(self):
        self.stack = []       # main stack
        self.minStack = []    # stack to track minimums

    def push(self, val):
        self.stack.append(val)
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self):
        if not self.stack:
            return
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self):
        if not self.stack:
            return 0
        return self.stack[-1]

    def getMin(self):
        if not self.minStack:
            return 0
        return self.minStack[-1]


# Example usage
if __name__ == "__main__":
    obj = MinStack()
    obj.push(5)
    obj.push(2)
    obj.push(3)
    print("Top:", obj.top())        # Output: 3
    print("Min:", obj.getMin())     # Output: 2
    obj.pop()
    print("Top after pop:", obj.top())      # Output: 2
    print("Min after pop:", obj.getMin())   # Output: 2

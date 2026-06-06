class MyQueue(object):
    def __init__(self):
        self.s1 = []   # acts as Stack 1
        self.s2 = []   # acts as Stack 2

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2


# Example usage (same as Java comments)
if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(obj.peek())   # Output: 1
    print(obj.pop())    # Output: 1
    print(obj.empty())  # Output: False

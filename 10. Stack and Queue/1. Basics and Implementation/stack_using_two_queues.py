from collections import deque

class MyStack(object):
    def __init__(self):
        self.q1 = deque()   # acts like Queue 1
        self.q2 = deque()   # acts like Queue 2

    def push(self, x):
        if self.q1:
            self.q1.append(x)
        else:
            self.q2.append(x)

    def pop(self):
        if self.empty():
            return -1

        top = -1
        if self.q1:
            while len(self.q1) > 1:
                top = self.q1.popleft()
                self.q2.append(top)
            top = self.q1.popleft()
        else:
            while len(self.q2) > 1:
                top = self.q2.popleft()
                self.q1.append(top)
            top = self.q2.popleft()

        return top

    def top(self):
        if self.empty():
            return -1

        top = -1
        if self.q1:
            while len(self.q1) > 1:
                top = self.q1.popleft()
                self.q2.append(top)
            top = self.q1[0]
            self.q2.append(self.q1.popleft())
        else:
            while len(self.q2) > 1:
                top = self.q2.popleft()
                self.q1.append(top)
            top = self.q2[0]
            self.q1.append(self.q2.popleft())

        return top

    def empty(self):
        return not self.q1 and not self.q2


# Example usage (same as Java comments)
if __name__ == "__main__":
    obj = MyStack()
    obj.push(10)
    obj.push(20)
    print(obj.top())    # Output: 20
    print(obj.pop())    # Output: 20
    print(obj.empty())  # Output: False

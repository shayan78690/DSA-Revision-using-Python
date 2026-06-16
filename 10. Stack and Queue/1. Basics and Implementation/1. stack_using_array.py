class Stack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        return -1 if not self.stack else self.stack.pop()
    def peek(self):
        return -1 if not self.stack else self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0

st = Stack()
st.push(5)
st.push(6)
st.push(7)
st.push(8)
st.push(9)
st.push(10)
print(st.stack)
st.pop()
print(st.stack)
st.pop()
print(st.stack)
print(st.peek())
print(st.isEmpty())

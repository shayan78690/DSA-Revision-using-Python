def insertAtBottom(self, stack, x):
        if not stack:
            stack.append(x)
            return
        top = stack.pop()
        self.insertAtBottom(stack, x)
        stack.append(top)

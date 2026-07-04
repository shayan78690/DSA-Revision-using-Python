class Solution:
    def reverseStack(self, stack):
        if not stack:
            return
        top = stack.pop()
        self.reverseStack(stack)
        self.insertAtBottom(stack, top)
    def insertAtBottom(self, stack, x):
        if not stack:
            stack.append(x)
            return
        top = stack.pop()
        self.insertAtBottom(stack, x)
        stack.append(top)

class Solution:
    @staticmethod
    def reverse(stack):
        if not stack:
            return
        
        top = stack.pop()
        Solution.reverse(stack)
        Solution.insertAtBottom(stack, top)
    
    @staticmethod
    def insertAtBottom(stack, x):
        if not stack:
            stack.append(x)
            return
        
        top = stack.pop()
        Solution.insertAtBottom(stack, x)
        stack.append(top)

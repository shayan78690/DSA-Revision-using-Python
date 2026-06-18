class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for x in asteroids:
            if x > 0:
                stack.append(x)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(x):
                    stack.pop()
                if stack and stack[-1] == abs(x):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(x)
        return stack
        

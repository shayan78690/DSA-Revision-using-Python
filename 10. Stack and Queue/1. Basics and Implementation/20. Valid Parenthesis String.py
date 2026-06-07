class Solution(object):
    def checkValidString(self, s):
        minopen = 0
        maxopen = 0
        for ch in s:
            if ch == '(':
                maxopen += 1
                minopen += 1
            elif ch == ')':
                maxopen -= 1
                minopen -= 1
            else:
                minopen -= 1
                maxopen += 1
            if maxopen < 0:
                return False
            if minopen < 0:
                minopen = 0
        return minopen == 0
        

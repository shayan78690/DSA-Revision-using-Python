class Solution:
    def celebrity(self, mat):
        n = len(mat)
        knowMe = [0] * n
        iKnow = [0] * n

        for i in range(n):
            for j in range(n):
                if mat[i][j] == 1:
                    iKnow[i] += 1
                    knowMe[j] += 1

        for i in range(n):
            if iKnow[i] == 0 and knowMe[i] == n - 1:
                return i

        return -1

class Solution:
    def celebrity(self, mat):
        n = len(mat)
        knowMe = [0] * n
        iKnow = [0] * n
        for i in range(n):
            for j in range(n):
                if mat[i][j] == 1:
                    iKnow[i] += 1
                    knowMe[j] += 1
        for i in range(n):
            if iKnow[i] == 1 and knowMe[i] == n:
                return i
        return -1

class Solution:
    def celebrity(self, mat):
        n = len(mat)
        top = 0
        down = n-1
        while top < down:
            if mat[top][down] == 1:
                top += 1
            elif mat[down][top] == 1:
                down -= 1
            else:
                top += 1
                down -= 1
        candidate = top
        for i in range(n):
            if i != candidate:
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1
        return candidate

#User function Template for python3

class Solution:
    def rotationCount(self, R, D):
        total = 0
        while R > 0 and D > 0:
            ld1 = R % 10
            ld2 = D % 10
            diff = abs(ld1 - ld2)
            total += min(diff, 10 - diff)
            R = R // 10
            D = D // 10
        return total

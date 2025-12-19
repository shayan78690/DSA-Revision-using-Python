#User function Template for python3

class Solution:
    def solve(self, bt):
        bt.sort()
        time = 0
        waitingTime = 0
        n = len(bt)

        for i in range(n):
            waitingTime += time
            time += bt[i]

        return waitingTime // n

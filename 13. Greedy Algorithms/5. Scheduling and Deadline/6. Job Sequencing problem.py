class Solution:
    def jobSequencing(self, deadline, profit):
        jobs = []
        maxDeadline = max(deadline)
        dead = [0] * (maxDeadline + 1)

        for i in range(len(deadline)):
            jobs.append([deadline[i], profit[i]])

        jobs.sort(key=lambda x: -x[1])

        count = 0
        totalProfit = 0

        for job in jobs:
            d = job[0]
            p = job[1]

            if dead[d] == 0:
                totalProfit += p
                count += 1
                dead[d] = 1
            else:
                for i in range(d - 1, 0, -1):
                    if dead[i] == 0:
                        dead[i] = 1
                        count += 1
                        totalProfit += p
                        break

        return [count, totalProfit]

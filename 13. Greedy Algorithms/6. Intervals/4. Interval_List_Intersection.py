class Solution:
    def intervalIntersection(self, firstList, secondList):
        i = j = 0
        result = []

        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                result.append([start, end])

            # Move the pointer with smaller end
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result

class Solution:
    def assignHole(self, mices, holes):
        mices.sort()
        holes.sort()
        maxi = 0
        i = 0
        j = 0
        while i < len(mices):
            temp = abs(mices[i] - holes[i])
            maxi = max(temp, maxi)
            i += 1
            j += 1
        return maxi

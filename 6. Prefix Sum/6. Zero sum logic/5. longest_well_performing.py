class Solution(object):
    def longestWPI(self, hours):
        n = len(hours)
        score = 0
        hashmap = {}
        hashmap[0] = -1
        maxi = 0
        for i in range(n):
            if hours[i] > 8:
                score += 1 
            else:
                score -= 1
            if score > 0:
                maxi = i+1
            else:
                if score-1 in hashmap:
                    length = i-hashmap[score-1]
                    maxi = max(maxi, length)
            if score not in hashmap:
                    hashmap[score] = i
        return maxi

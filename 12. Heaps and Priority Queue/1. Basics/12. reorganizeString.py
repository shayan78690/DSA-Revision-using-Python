import heapq

class Pair:
    def __init__(self, freq, ch):
        self.freq = freq
        self.ch = ch

    def __lt__(self, other):
        return self.freq > other.freq


class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq_map = [0] * 26
        for ch in s:
            freq_map[ord(ch) - ord('a')] += 1

        pq = []
        for i in range(26):
            if freq_map[i] > 0:
                heapq.heappush(pq, Pair(freq_map[i], chr(i + ord('a'))))

        ans = []

        while len(pq) > 1:
            p1 = heapq.heappop(pq)
            ans.append(p1.ch)
            p1.freq -= 1

            p2 = heapq.heappop(pq)
            ans.append(p2.ch)
            p2.freq -= 1

            if p1.freq > 0:
                heapq.heappush(pq, Pair(p1.freq, p1.ch))
            if p2.freq > 0:
                heapq.heappush(pq, Pair(p2.freq, p2.ch))

        if len(pq) == 1:
            if pq[0].freq == 1:
                ans.append(pq[0].ch)
            else:
                return ""

        return "".join(ans)

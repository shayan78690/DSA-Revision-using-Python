class Solution:
    def pageFaults(self, N, C, pages):
        cache = []
        faults = 0

        for i in range(N):
            page = pages[i]

            if page in cache:
                cache.remove(page)
                cache.append(page)
            else:
                faults += 1
                if len(cache) == C:
                    cache.pop(0)
                cache.append(page)

        return faults

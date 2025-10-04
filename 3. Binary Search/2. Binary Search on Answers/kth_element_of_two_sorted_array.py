class Solution:
    def kthElement(self, a, b, k):
        c = a + b
        c.sort()
        return c[k-1]
        

def kthElement(a, b, m, n, k):
    if m > n:
        return kthElement(b, a, n, m, k)

    left = k  # length of left half

    # apply binary search:
    low = max(0, k - n)
    high = min(k, m)
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = left - mid1
        # calculate l1, l2, r1, and r2
        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')
        if mid1 < m:
            r1 = a[mid1]
        if mid2 < n:
            r2 = b[mid2]
        if mid1 - 1 >= 0:
            l1 = a[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = b[mid2 - 1]

        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)

        # eliminate the halves:
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1

    return 0  # dummy statement
            
from typing import Tuple

def minSubstring(a: str, b: str) -> str:
    n = len(a)
    m = len(b)
    freq = [0] * 256
    for i in range(m):
        freq[ord(b[i])] += 1
    
    left = 0
    right = 0
    start = -1
    count = 0
    mini = float('inf')
    while right < n:
        if freq[ord(a[right])] > 0:
            count += 1
        freq[ord(a[right])] -= 1
        while count == m:
            if right-left+1 < mini:
                mini = right-left+1
                start = left
            freq[ord(a[left])] += 1
            if freq[ord(a[left])] > 0:
                count -= 1
            left += 1
        right += 1
    return "" if mini == float('inf') else a[start:start+mini]

            

class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        # Step 1: Initialize array
        arr = [0] * length

        # Step 2: Apply boundary updates
        for start, end, inc in updates:
            arr[start] += inc
            if end + 1 < length:
                arr[end + 1] -= inc

        # Step 3: Convert boundary updates to actual values
        for i in range(1, length):
            arr[i] += arr[i - 1]

        return arr

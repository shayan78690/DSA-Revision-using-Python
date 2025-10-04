class Solution:
    def findK(self, a, n, m, k):
        top = 0
        bottom = n-1
        left = 0
        right = m-1
        ans = 0
        count = 0
        while top <= bottom and left <= right:
            for i in range(left, right+1):
                count += 1
                if count == k:
                    ans = a[top][i]
                    break
            top += 1
            
            for i in range(top, bottom+1):
                count += 1
                if count == k:
                    ans = a[i][right]
                    break
            right -= 1
            
            if top <= bottom:
                for i in range(right, left-1, -1):
                    count += 1
                    if count == k:
                        ans = a[bottom][i]
                        break
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top-1, -1):
                    count += 1
                    if count == k:
                        ans = a[i][left]
                        break
                left += 1
            
        return ans
                    
class Solution:
    def findGCD(self, nums) -> int:
        a = min(nums)
        b = max(nums)

        while a > 0 and b > 0:
            if a > b:
                a %= b
            else:
                b %= a
            
        return b if a == 0 else a

        
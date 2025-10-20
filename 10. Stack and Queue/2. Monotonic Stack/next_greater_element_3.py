class Solution:
    def nextGreaterElement(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        
        stack = []
        mapping = {}  # maps each element in nums2 to its next greater element

        # Traverse nums2 from end to start
        for i in range(m - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if not stack:
                mapping[nums2[i]] = -1
            else:
                mapping[nums2[i]] = stack[-1]
            stack.append(nums2[i])

        # Build result for nums1 using the mapping
        ans = [mapping[num] for num in nums1]
        return ans


# Example usage
if __name__ == "__main__":
    obj = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(obj.nextGreaterElement(nums1, nums2))  # Output: [-1,3,-1]

class Solution:
    # Function to find the maximum number of content students
    def findContentChildren(self, student, cookie):
        # Sort both arrays to apply the greedy strategy
        student.sort()
        cookie.sort()

        # Recursive helper function with memoization
        def helper(studentIndex, cookieIndex):
            # Base case: if we reach end of either list
            if studentIndex >= len(student) or cookieIndex >= len(cookie):
                return 0

            result = 0

            # If the cookie satisfies the student's greed
            if cookie[cookieIndex] >= student[studentIndex]:
                # Option 1: assign this cookie and move to next student and cookie
                result = max(result, 1 + helper(studentIndex + 1, cookieIndex + 1))

            # Option 2: skip this cookie and try the next one for the same student
            result = max(result, helper(studentIndex, cookieIndex + 1))

            return result

        # Start recursion from index 0 for both arrays
        return helper(0, 0)

# Main execution
student = [1, 2, 3]
cookie = [1, 1]

# Create Solution object
solver = Solution()

# Get the number of content students and print it
result = solver.findContentChildren(student, cookie)
print("Maximum number of content students:", result)



class Solution:
    # Function to find the maximum number of content students using tabulation
    def findContentChildren(self, student, cookie):
        n = len(student)
        m = len(cookie)

        # Sort both arrays
        student.sort()
        cookie.sort()

        # Create DP table
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill DP table from bottom up
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                # Skip current cookie
                skip = dp[i][j + 1]

                # Take current cookie if it satisfies student's greed
                take = 0
                if cookie[j] >= student[i]:
                    take = 1 + dp[i + 1][j + 1]

                # Take the best of both choices
                dp[i][j] = max(skip, take)

        return dp[0][0]

# Main execution
student = [1, 2]
cookie = [1, 2, 3]

# Create Solution object
solver = Solution()

# Get the number of content students and print it
result = solver.findContentChildren(student, cookie)
print("Maximum number of content students:", result)

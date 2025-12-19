class Solution:

    # Function to check if the string is valid using greedy logic
    def checkValidString(self, s: str) -> bool:

        # Variable to store minimum number of open brackets possible
        min_open = 0

        # Variable to store maximum number of open brackets possible
        max_open = 0

        # Traverse each character in the string
        for char in s:

            # If current character is '('
            if char == '(':
                min_open += 1
                max_open += 1

            # If current character is ')'
            elif char == ')':
                min_open -= 1
                max_open -= 1

            # If current character is '*', it can be '(', ')' or ''
            else:
                 # If '*' acts as ')'
                min_open -= 1    
                # If '*' acts as '('
                max_open += 1      

            # If max_open goes below 0, we have too many unmatched ')'
            if max_open < 0:
                return False

            # min_open should not be negative
            if min_open < 0:
                min_open = 0

        # At the end, all opens must be matched for valid string
        return min_open == 0


# Driver code
if __name__ == "__main__":
    s = input("Enter the string: ")
    sol = Solution()
    if sol.checkValidString(s):
        print("Valid parenthesis string")
    else:
        print("Invalid parenthesis string")

class Solution:
    # Function to find the index of celebrity
    def celebrity(self, M):
        
        # Size of given matrix
        n = len(M)
        
        # To store count of people who 
        # know person of index i
        knowMe = [0] * n
        
        # To store count of people who 
        # the person of index i knows
        Iknow = [0] * n
        
        # Traverse on given matrix
        for i in range(n):
            for j in range(n):
                
                # If person i knows person j
                if M[i][j] == 1:
                    knowMe[j] += 1
                    Iknow[i] += 1
        
        # Traverse for all persons to find the celebrity
        for i in range(n):
            
            # Return the index of celebrity
            if knowMe[i] == n - 1 and Iknow[i] == 0:
                return i  
        
        # Return -1 if no celebrity is found
        return -1

class Solution(object):
    def celebrity(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        top = 0
        down = n - 1

        # Step 1: Find potential celebrity
        while top < down:
            if mat[top][down] == 1:
                # top knows down, so top can't be celebrity
                top += 1
            elif mat[down][top] == 1:
                # down knows top, so down can't be celebrity
                down -= 1
            else:
                # both know no one, skip both
                top += 1
                down -= 1

        # Step 2: Verify the candidate
        for i in range(n):
            if i != top:
                # celebrity should not know anyone,
                # and everyone should know celebrity
                if mat[top][i] == 1 or mat[i][top] == 0:
                    return -1

        return top

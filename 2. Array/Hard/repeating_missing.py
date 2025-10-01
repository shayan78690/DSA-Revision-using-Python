class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        sum_of_first_n = (n*(n+1)) // 2
        sum_of_first_n_sq = (n*(n+1)*(2*n+1)) // 6
        
        sum_of_element = 0
        sum_of_element_sq = 0
        for x in arr:
            sum_of_element += x
            sum_of_element_sq += (x*x)
        
        val1 = sum_of_element - sum_of_first_n
        val2 = sum_of_element_sq - sum_of_first_n_sq
        
        val2 = val2 // val1
        x = (val1 + val2) // 2
        y = x - val1
        
        return [x, y]


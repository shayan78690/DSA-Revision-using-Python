class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count_of_5 = 0
        count_of_10 = 0
        for bill in bills:
            if bill == 5:
                count_of_5 += 1
            elif bill == 10:
                if count_of_5 > 0:
                    count_of_5 -= 1
                    count_of_10 += 1
                else:
                    return False
            else:
                if count_of_10 > 0 and count_of_5 > 0:
                    count_of_10 -= 1
                    count_of_5 -= 1
                elif count_of_5 >= 3:
                    count_of_5 -= 3
                else:
                    return False
        return True
        

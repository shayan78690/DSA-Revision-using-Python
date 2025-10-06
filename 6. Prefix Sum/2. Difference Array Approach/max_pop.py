class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        prefix = [0] * 2051  

        # Step 2: Apply boundary updates
        for birth, death in logs:
            prefix[birth] += 1     # person born
            prefix[death] -= 1     # person dies

        # Step 3: Compute running sum to find max population
        max_num = prefix[1950]
        earliest_year = 1950
        count = 0

        for year in range(1950, 2051):
            count += prefix[year]
            if count > max_num:
                max_num = count
                earliest_year = year

        return earliest_year
        
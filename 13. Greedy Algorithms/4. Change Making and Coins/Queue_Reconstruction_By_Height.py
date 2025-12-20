class Solution:
    def reconstructQueue(self, people):
        # Step 1: Sort by height descending, and k ascending
        people.sort(key=lambda x: (-x[0], x[1]))
        
        queue = []
        
        # Step 2: Insert each person at index k
        for person in people:
            queue.insert(person[1], person)
        
        return queue

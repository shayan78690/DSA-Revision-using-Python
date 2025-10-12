class Solution(object):
    def loopLength(self, head):
        slow = head
        fast = head

        # Phase 1: Detect cycle using the two-pointer technique
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Phase 2: Loop detected; now count its length
                count = 1
                temp = slow.next
                while temp != slow:
                    count += 1
                    temp = temp.next
                return count
        return 0  # No loop

# Example usage:
# (Assuming the linked list and nodes are created and may have a cycle)
sol = Solution()
result = sol.loopLength()
print(result)  # Outputs the length of the loop, or 0 if there’s no loop

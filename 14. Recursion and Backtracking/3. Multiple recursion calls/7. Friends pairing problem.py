class Solution:
    def countFriendsPairings(self, n):
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        single = self.countFriendsPairings(n-1)
        pairing = (n-1)*self.countFriendsPairings(n-2)
        return single+pairing
        

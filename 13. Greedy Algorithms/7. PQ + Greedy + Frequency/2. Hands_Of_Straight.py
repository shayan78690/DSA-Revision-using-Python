class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        freq = {}
        for h in hand:
            freq[h] = freq.get(h, 0) + 1
        
        while freq:
            currentCard = min(freq.keys())

            for i in range(groupSize):
                card = currentCard + i

                if card not in freq:
                    return False
                
                freq[card] -= 1
                if freq[card] == 0:
                    del freq[card]
        return True

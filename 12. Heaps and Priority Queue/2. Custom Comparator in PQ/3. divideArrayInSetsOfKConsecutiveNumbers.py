class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False

        # TreeMap equivalent: sorted dictionary
        freq = {}
        for card in hand:
            freq[card] = freq.get(card, 0) + 1

        # Use sorted keys repeatedly
        while freq:
            currentCard = min(freq.keys())  # smallest card available

            # try to build the next group
            for i in range(groupSize):
                card = currentCard + i

                if card not in freq:
                    return False

                freq[card] -= 1
                if freq[card] == 0:
                    del freq[card]

        return True

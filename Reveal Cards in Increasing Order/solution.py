from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        res = [0] * len(deck)
        deck = sorted(deck)
        positions = deque(range(len(deck)))

        for num in deck:
            index = positions.popleft()
            res[index] = num

            if positions:
                positions.append(positions.popleft())

        return res
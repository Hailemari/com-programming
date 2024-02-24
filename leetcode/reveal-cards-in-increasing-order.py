class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()

        n = len(deck)
        result = [0]*n
        indices = deque(range(n))

        for card in deck:
            result[indices.popleft()] = card

            if indices:
                indices.append(indices.popleft())


        return result
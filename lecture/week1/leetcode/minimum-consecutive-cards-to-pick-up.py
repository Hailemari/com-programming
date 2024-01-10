class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_cards = float('inf')
        indices = {}

        for right in range(len(cards)):
            if cards[right] in indices.keys():
                min_cards = min(min_cards, right - indices[cards[right]] + 1)

            indices[cards[right]] = right
        return min_cards if min_cards != float('inf') else -1

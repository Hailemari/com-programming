class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)

        answer = 0
        i = 1
        j = len(piles)
        while i < j:
            answer += piles[i]
            i += 2
            j -= 1

        return answer
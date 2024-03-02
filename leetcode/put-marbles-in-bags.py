class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        parts = []

        for i in range(n - 1):
            parts.append(weights[i] + weights[i + 1])

        parts.sort()
        if k == 1:
            return 0

        return sum(parts[-k + 1:]) - sum(parts[:k - 1])
        
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        bad_numbers = set()

        # Identify bad numbers (numbers that appear both on the front and the back of a card)
        for i in range(n):
            if fronts[i] == backs[i]:
                bad_numbers.add(fronts[i])

        # Iterate through possible good numbers and find the minimum
        min_good = float('inf')
        for i in range(n):
            if fronts[i] not in bad_numbers:
                min_good = min(min_good, fronts[i])
            if backs[i] not in bad_numbers:
                min_good = min(min_good, backs[i])


        return min_good if min_good != float('inf') else 0
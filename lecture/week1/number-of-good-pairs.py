class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = defaultdict(int)
        ans = 0

        for num in nums:
            good_pairs[num] += 1

        values = good_pairs.values()

        for value in values:
                ans += value * (value - 1) // 2

        return ans

    
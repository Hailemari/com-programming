class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums) - 1
        num_of_pairs = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    num_of_pairs += 1

        return num_of_pairs
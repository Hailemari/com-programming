class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [nums[0]] * n

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        return prefix_sum
            
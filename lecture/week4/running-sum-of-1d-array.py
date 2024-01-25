class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre_sum = [nums[0]] * len(nums)

        for i in range(1, len(nums)):
            pre_sum[i] = pre_sum[i-1] + nums[i]

        return pre_sum
            
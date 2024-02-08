class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [nums[0]] * n

        for i in range(1, n):
            pre_sum[i] = pre_sum[i-1] + nums[i]

        total_sum = pre_sum[-1]
        for i in range(n):
            left_sum = pre_sum[i] - nums[i]
            right_sum = total_sum - pre_sum[i]

            if left_sum == right_sum:
                return i

        return -1
        
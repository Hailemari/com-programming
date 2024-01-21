class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
            
        result = [0] * n
        for i in range(n):
            left_sum = prefix_sum[i] - nums[i]
            right_sum = prefix_sum[n-1] - prefix_sum[i]
            result[i] = (i * nums[i] - left_sum) + (right_sum - (n-i-1) * nums[i])
        return result


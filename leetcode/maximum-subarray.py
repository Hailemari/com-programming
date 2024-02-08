class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_arr = nums[0]
        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num

            max_sub_arr = max(max_sub_arr, curr_sum)

        return max_sub_arr
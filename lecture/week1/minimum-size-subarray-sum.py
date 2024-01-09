class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')

        left = 0
        cur_sum = nums[left]
        if cur_sum >= target:
            return 1

        for right in range(1, len(nums)):
            cur_sum += nums[right]
                
            while cur_sum >= target:
                cur_sum -= nums[left]
                min_length = min(min_length, right - left + 1)
                left += 1
                
              

        return min_length if min_length != float('inf') else 0
        
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0

        max_num = 0
        zeros_count = k
        for right in range(len(nums)):            
            if nums[right] == 0:
                zeros_count -= 1

            while zeros_count < 0:
                if nums[left] == 0:
                    zeros_count += 1
                left += 1
            
            max_num = max(max_num, right - left + 1)

        return max_num

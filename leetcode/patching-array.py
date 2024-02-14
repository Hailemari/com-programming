class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        run_sum = 0
        min_patches = 0
        nums_len = len(nums)
        
        i = 0
        while run_sum < n:
            if i < nums_len and nums[i] <= run_sum + 1:
                run_sum += nums[i]
                i += 1
            else:
                run_sum += (run_sum + 1)
                min_patches += 1
    
        return min_patches

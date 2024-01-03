class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        s = 1

        unique = 1
        while s < len(nums):
            if nums[s] == nums[p]:
                s += 1
            else:
                nums[p+1], nums[s] = nums[s], nums[p+1]
                unique += 1
                p += 1
                s += 1
        
        return unique


    
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if all(element == nums[0] for element in nums):
            return 0

        nums.sort(reverse=True)

        ops = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                continue
            if nums[i] < prev:
                ops += i
            
            prev = nums[i]
        
        return ops
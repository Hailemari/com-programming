class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        right = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            left = nums[i]
            if left > right:
                parts = math.ceil(left / right)
                operations += parts - 1
                right = left // parts
            else:
                right = left
        
        return operations
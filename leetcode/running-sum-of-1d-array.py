class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        accumulator = 0
        for i in range(n):
            nums[i] += accumulator
            accumulator = nums[i]

        return nums
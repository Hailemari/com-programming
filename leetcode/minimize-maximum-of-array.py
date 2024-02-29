class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        min_value = 0
        run_sum = 0
        
        for i in range(n):
            run_sum += nums[i]
            average = math.ceil(run_sum / (i + 1))
            min_value = max(min_value, average)

        return min_value



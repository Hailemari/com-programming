class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)

        n = len(nums)
        ans = [0]*n
        for i in range(n):
            right -= nums[i]
            ans[i] = abs(left - (nums[i])*i) + abs(right - (nums[i])*(n-i-1))
            left += nums[i]
            
        return ans

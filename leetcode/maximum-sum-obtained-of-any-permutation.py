class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        count = [0] * (n + 1)

        for left, right in requests:
            count[left] += 1
            count[right + 1] -= 1
 
        for i in range(1, n):
            count[i] += count[i-1]
 
        count.sort(reverse=True)
        nums.sort(reverse=True)

        maxTotalSum = 0
        for i in range(n):
            maxTotalSum = (maxTotalSum + nums[i] * count[i]) % MOD
        
        return maxTotalSum
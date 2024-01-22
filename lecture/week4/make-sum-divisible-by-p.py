class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        ans = float("inf")
        s = sum(nums) % p
        d = {0: -1}
        cum = 0
        if s == 0:
            return 0
        for i in range(len(nums)):
            cum += nums[i]
            r = cum % p
            if (r - s) % p in d:
                ans = min(ans, i - d[(r - s) % p])
            d[r] = i
        return ans if ans < len(nums) else -1
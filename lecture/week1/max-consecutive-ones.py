class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        ans = []

        for num in nums:
            if num == 1:
                max_ones += 1
            else:
                ans.append(max_ones)
                max_ones = 0
                
        ans.append(max_ones)

        return max(ans)
        
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans_len = 2*n
        ans = [0] * ans_len
        

        for i in range(n):
            ans[i] = nums[i]

        for i in range(n):
            ans[i + n] = nums[i]

        return ans
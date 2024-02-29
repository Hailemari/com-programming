class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def backtrack(i, subset):
            if i == n + 1:
                return
            cur = sorted(subset)               
            if cur not in ans:
                ans.append(cur[:])
                
            for j in range(i, n):
                subset.append(nums[j])
                backtrack(j+1, subset)                
                subset.pop()

        backtrack(0, [])

        return ans
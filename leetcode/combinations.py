class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(i, combination):
            if len(combination) == k:
                ans.append(combination[:])
                return

            for j in range(i, n+1):
                combination.append(j)
                backtrack(j + 1, combination)
                combination.pop()

        ans = []
        backtrack(1, [])
        return ans

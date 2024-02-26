class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(i, path):
            if sum(path) == target:
                if path[:] not in ans:
                    ans.append(path[:])
                return
                
            if sum(path) > target:
                return

            for j in range(i, len(candidates)):
                path.append(candidates[j])
                backtrack(j, path)
                path.pop()
            
        backtrack(0, [])
        return ans
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(i, path, path_sum):
            if path_sum == target:
                if path[:] not in ans:
                    ans.append(path[:])
                return
                
            if path_sum > target:
                return

            for j in range(i, len(candidates)):
                path_sum += candidates[j]
                path.append(candidates[j])
                backtrack(j, path, path_sum)
                path_sum -= candidates[j]
                path.pop()
            
        backtrack(0, [], 0)
        return ans
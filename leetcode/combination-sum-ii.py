class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtrack(i, combination, comb_sum):
            nonlocal ans
            if comb_sum > target:
                return

            if comb_sum == target:
                ans.append(combination[:])
                return
            
           
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                comb_sum += candidates[j]
                combination.append(candidates[j])            
                backtrack(j + 1, combination, comb_sum)               
                combination.pop()
                comb_sum -= candidates[j]
                

        backtrack(0 , [], 0)

        return ans
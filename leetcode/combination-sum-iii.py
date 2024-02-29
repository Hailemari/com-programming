class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack(i, combination, comb_sum):
            nonlocal ans
            if comb_sum > n:
                return

            if comb_sum == n and len(combination) == k:
                ans.append(combination[:])
                return

            for j in range(i, 10):
                combination.append(j)
                comb_sum += j
                backtrack(j+1, combination, comb_sum)
                combination.pop()
                comb_sum -= j
                if len(combination) >= k:
                    break
            

        backtrack(1, [], 0)
        return ans
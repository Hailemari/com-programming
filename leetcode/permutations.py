class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        used = [False]*n

        def backtrack(i, permutation):
            if len(permutation) == n:
                ans.append(permutation[:])

                return

            for j in range(n):
                if not used[j]:
                    used[j] = True
                    permutation.append(nums[j])
                    backtrack(j + 1, permutation)
                    permutation.pop()
                    used[j] = False

            return

        backtrack(0, [])

        return ans

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(combination, open_count, close_count):
            if len(combination) == 2*n:
                ans.append(combination)
                return

            if open_count < n:
                backtrack(combination + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(combination + ")", open_count, close_count + 1)

        ans = []
        backtrack("", 0, 0)
        return ans
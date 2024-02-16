class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
        
        ans = 0
        stack = []
        for p in s:
            if p == "(":
                stack.append(p)
            else:
                if stack:
                    stack.pop()
                else:
                    ans += 1

        return ans + len(stack)
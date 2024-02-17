class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""

        ans = [char for char in palindrome]
        i = 0
        while i < n:
            if palindrome[i] != "a":
                temp = ans[i]
                ans[i] = "a"
                if ans != ans[::-1]:
                    break
                else:
                    ans[i] = temp
            if i == n - 1:
                ans[i] = "b"
            i += 1



        return "".join(ans)
        
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)

        ans = 0
        flag = False
        for val in count.values():
            if val % 2 and val != 1:
                ans += val - 1
                
            if val % 2 == 0:
                ans += val
            
            if val % 2 == 1:
                flag = True

        return ans + 1 if flag else ans

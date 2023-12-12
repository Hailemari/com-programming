class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        s = s.strip()
        if len(s) == 1:
            return s
        
        i = len(s) - 1
        j = len(s) - 1

        while j >= 0:
            if s[j] == " " and s[j+1] != " ":
                res += s[j+1:i+1] + " "
            
                j -= 1
                i = j
            elif s[j] == " " and s[j+1] == " ":
                j -= 1
                i = j
            else:
                j -= 1
            
            if j == 0:
                res += s[j:i+1]

        return res
            
        
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(spaces) - 1
        result = ""
        
        if n > 0:
            result += s[:spaces[0]] + " "
        
        if n == 0 and spaces[0] != 0:
            result += s[:spaces[0]]

        for i in range(n):
            if i < n - 1:
                result += s[spaces[i]:spaces[i+1]] + " "
            else:
                result += s[spaces[i]:spaces[i+1]]
        
        result += " " + s[spaces[n]:]
        return result
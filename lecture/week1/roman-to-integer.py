class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        result = 0

        p1 = len(s) - 1
        p2 = len(s) - 2
        
        while p2 >= -1:
            if s[p2:p1 + 1] in numerals.keys():
                result += numerals[s[p2:p1 + 1]]
                p1 -= 2
                p2 -= 2
            
            else:
                result += numerals[s[p1]]
                p1 -= 1
                p2 -= 1
        
        return result
            


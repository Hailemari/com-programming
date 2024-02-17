class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbols = {'(': ')', '{': '}', '[': ']'}

        for cha in s:
            if cha in symbols.keys():
                stack.append(cha)
            elif not stack:
                return False
            else:
                if symbols[stack.pop()] != cha:
                    return False
                
        return False if len(stack) else True
             
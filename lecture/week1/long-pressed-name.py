class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l = 0  
        r = 0

        while l <= len(name) and r < len(typed):
            if l < len(name) and name[l] == typed[r]:
                l += 1
                r += 1
            elif name[l-1] == typed[r] and l != 0:
                r += 1
            else:
                return False

        return l == len(name) and r == len(typed)
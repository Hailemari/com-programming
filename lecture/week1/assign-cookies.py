class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        p1 = 0
        p2 = 0
        g.sort()
        s.sort()

        content = 0
        while p1 < len(g) and p2 < len(s):
            if s[p2] >= g[p1]:
                content += 1
                p1 += 1
                p2 += 1
            else:
                p2 += 1

        return content
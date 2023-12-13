class Solution:
    def minimizedStringLength(self, s: str) -> int:
        count = defaultdict(int)
        ans = len(s)

        for char in s:
            count[char] += 1
        
        for value in count.values():
            if value > 1:
                ans -= (value - 1)
        
        return ans

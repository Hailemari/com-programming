class Solution:
    def balancedString(self, s: str) -> int:
        freq = Counter(s)
        res = len(s)
        n = len(s)
        left = 0
        for right, c in enumerate(s):
            freq[c] -= 1
    
            while left < n and all(freq[ch] <= n/4 for ch in 'QWER'):
                
                res = min(res, right-left+1)
                freq[s[left]] += 1
                left += 1
                
        return res
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        window = Counter(s[:len(p)])
        result = []
        
        l = 0
        r = len(p)
        if target == window:
            result.append(l)

        while r < len(s):
            left = s[l]
            right = s[r]

            window[left] -= 1
            if window[left] == 0:
                del window[left]
            window[right] = window.get(right, 0) + 1
            
            l += 1
            r += 1
            if window == target:
                result.append(l)

            
        return result
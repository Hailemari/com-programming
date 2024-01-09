class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        window = Counter(s2[:len(s1)])
        if s1_count == window:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]

            window[s2[right]] = window.get(s2[right], 0) + 1

            if s1_count == window:
                return True 
            left += 1

        return False
        
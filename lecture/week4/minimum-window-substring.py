class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        required_chars = Counter(t)
        formed_chars = Counter()

        min_len = float('inf')
        min_window_str = ""

        for right in range(len(s)):
            formed_chars[s[right]] += 1

            # Check if the current window contains all the required characters
            while all(formed_chars[char] >= required_chars[char] for char in required_chars):
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    min_window_str = s[left:right+1]
                
                formed_chars[s[left]] -= 1
                left += 1
            

        return min_window_str
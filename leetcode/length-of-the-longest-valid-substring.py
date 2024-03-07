class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        forbidden = set(forbidden)
        valid_substring_len = 0
        right = n - 1

        for left in range(n - 1, -1, -1):
            for k in range(left, min(left + 10, right + 1)):
                if word[left:k+1] in forbidden:
                    right = k - 1
                    break

            valid_substring_len = max(valid_substring_len, right - left + 1)
        
        return valid_substring_len
        
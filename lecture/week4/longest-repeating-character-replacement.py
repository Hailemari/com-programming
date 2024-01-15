class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = [0] * 26 
        max_length = 0
        max_char_count = 0
        start = 0

        for end in range(len(s)):
            char_count[ord(s[end]) - ord('A')] += 1
            max_char_count = max(max_char_count, char_count[ord(s[end]) - ord('A')])

            # Check if the current window can be expanded
            while (end - start + 1 - max_char_count) > k:
                char_count[ord(s[start]) - ord('A')] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length
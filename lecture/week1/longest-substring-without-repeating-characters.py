class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)

        i = 0
        max_length = 0
        for j in range(len(s)):
            if count[s[j]] == 0:
                count[s[j]] += 1
            else:
                while count[s[j]] != 0:
                    count[s[i]] -= 1
                    i += 1

                count[s[j]] += 1
            
            max_length = max(max_length, j - i + 1)

        return max_length


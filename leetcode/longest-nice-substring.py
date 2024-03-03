class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        def helper(i, j):
            if j - i + 1 < 2: 
                return (0, -1)

            hashset = set()
			
            for k in range(i, j + 1):
                hashset.add(s[k])
            
            for k in range(i, j + 1):
                if s[k].upper() in hashset and s[k].lower() in hashset:
                    continue

                left = helper(i, k - 1)
                right = helper(k + 1, j)
                if (left[1] - left[0] + 1) >= (right[1] - right[0] + 1):
                    return left
                else:
                    return right

            return (i, j)
        start, end = helper(0, len(s) - 1)
        return s[start:(end + 1)]
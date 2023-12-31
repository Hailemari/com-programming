class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num) - 1

        for i in range(n, -1, -1):
            if int(num[i]) % 2:
                return num[0:i+1]

        return ""
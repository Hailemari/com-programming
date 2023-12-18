class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        answer = list(s)

        for i in range(0, len(s), 2 * k):
            answer[i:i+k] = reversed(answer[i:i+k])

        return ''.join(answer)

            
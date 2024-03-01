class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        result = 0
        stack = []
        arr.append(0)

        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                idx = stack.pop()
                left = idx - stack[-1] if stack else idx + 1
                right = i - idx
                result += arr[idx] * left * right
                result %= MOD

            stack.append(i)

        return result
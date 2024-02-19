class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = 10**9 + 7
        prev_smaller = [-1]*n
        next_smaller = [-1]*n

        stack2 = []
        for i, num in enumerate(arr):
            if stack2:
                while stack2 and arr[stack2[-1]] >= num:
                    next_smaller[stack2[-1]] = i
                    stack2.pop()
            stack2.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            if stack:
                while stack and arr[stack[-1]] > arr[i]:
                    prev_smaller[stack[-1]] = i
                    stack.pop()
            stack.append(i)
        
        ans = 0
        for i in range(n):
            if next_smaller[i] == -1:
                ans += ((i - prev_smaller[i])*(n - i))*arr[i]
            else:
                ans += ((i - prev_smaller[i])*(next_smaller[i] - i))*arr[i]

        
        return ans % (10**9 + 7)
            
            
            
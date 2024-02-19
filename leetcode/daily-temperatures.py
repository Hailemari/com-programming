class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []

        answer = [0]*n
        
        next_larger = [-1]*n

        for i, temp in enumerate(temperatures):
            if stack:
                while stack and temperatures[stack[-1]] < temp:
                    next_larger[stack[-1]] = i
                    stack.pop()
            stack.append(i)
        
        for i, _ in enumerate(temperatures):
            if next_larger[i] != -1:
                answer[i] = next_larger[i] - i
        
        return answer

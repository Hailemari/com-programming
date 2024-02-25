class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + nums

        stack = []
        next_greater = [-1]*n

        for i in range(n*2):
            if stack:
                while stack and nums[stack[-1]] < nums[i]:
                    if stack[-1] < n:
                        next_greater[stack[-1]] = nums[i]
                        stack.pop()
                    else:
                        next_greater[stack[-1] - n] = nums[i]
                        stack.pop()
                stack.append(i)
            else:
                stack.append(i)
           
        
        return next_greater
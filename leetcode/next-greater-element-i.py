class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)

        next_greater = defaultdict(lambda: -1)
        stack = []
        for num in nums2:
            if stack:
                while stack and stack[-1] < num:
                    next_greater[stack[-1]] = num
                    stack.pop()
            stack.append(num)
        
        for i in range(len(nums1)):
            if next_greater[nums1[i]] != -1:
                ans[i] = next_greater[nums1[i]]
        return ans
        

        
                    
        

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        num_of_ones = nums.count(1) # 1
        scores = []
        scores.append(num_of_ones)
        
        left = 0
        right = num_of_ones
        for i in range(len(nums)):
            
            if nums[i] == 0:
                left += 1
            else:
                right -= 1
            
            scores.append(left + right)

        

        ans = []
        max_val = max(scores)
        for i in range(len(scores)):
            if scores[i] == max_val:
                ans.append(i)

        return ans
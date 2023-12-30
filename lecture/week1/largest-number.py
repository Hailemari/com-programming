class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted([str(num) for num in nums],reverse=True) 

        n = len(nums)
        for i in range(n): 
            swapped = False

            for j in range(n-i-1):
                if len(nums[j]) == len(nums[j+1]):
                    continue

                if int(nums[j]+nums[j+1]) < int(nums[j+1]+nums[j]):
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    swapped = True

            if not swapped:
                break
                
        ans = str(int("".join(nums))) 
        
        return ans
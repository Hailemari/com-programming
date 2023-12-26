class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1, n):
            j = i
            k = i - 1
            
            while k >= 0:
                if nums[j] < nums[k]:
                    nums[j], nums[k] = nums[k], nums[j]
                    j -= 1
                    k -= 1
                else:
                    break

        
        
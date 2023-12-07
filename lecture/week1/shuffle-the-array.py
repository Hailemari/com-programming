class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if len(nums) == 1:
            return nums
        
        p1 = 0
        p2 = n
        result = []

        while p2 < len(nums):
            result.append(nums[p1])
            result.append(nums[p2])
            p1 += 1
            p2 += 1

        return result

        

        

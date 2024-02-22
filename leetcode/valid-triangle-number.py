class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()

        triplets = 0
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    triplets += right - left
                    right -= 1
                else:
                    left += 1

        return triplets
            


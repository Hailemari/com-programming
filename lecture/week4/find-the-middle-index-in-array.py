class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]
    
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        total_sum = prefix_sum[-1]

        for i in range(len(nums)):
            if prefix_sum[i] == total_sum - prefix_sum[i + 1]:
                return i

        return -1
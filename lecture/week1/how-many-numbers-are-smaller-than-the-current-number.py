class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num_idx = {}
        sorted_nums = sorted(nums)
        answer = []

        # Register the index of each number to the num_idx
        for i in range(len(nums)):
            if sorted_nums[i] not in num_idx:
                num_idx[sorted_nums[i]] = i

        for num in nums:
            answer.append(num_idx[num])

        return answer
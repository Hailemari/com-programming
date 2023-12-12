class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = {val:i for i, val in enumerate(nums)}

        new_nums = sorted(nums)

        i = 0
        j = len(nums) - 1

        while j > i:
            if new_nums[i] + new_nums[j] < target:
                i += 1
            elif new_nums[i] + new_nums[j] > target:
                j -=1
            else:
                if new_nums[i] == new_nums[j]:
                    return [nums.index(new_nums[i]), nums_idx[new_nums[j]]]
                return [nums_idx[new_nums[i]], nums_idx[new_nums[j]]]
        
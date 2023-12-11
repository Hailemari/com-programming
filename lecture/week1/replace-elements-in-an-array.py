class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_index_map = defaultdict(int)

        for i, num in enumerate(nums):
            num_index_map[num] = i

        for n1, n2 in operations:
            nums[num_index_map[n1]] = n2
            num_index_map[n2] = num_index_map[n1]

        return nums
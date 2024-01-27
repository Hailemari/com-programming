class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0: 1}  # Initialize the count of remainder 0 to 1
        prefix_sum = 0
        result = 0
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            if prefix_sum in count:
                result += count[prefix_sum]
            count[prefix_sum] = count.get(prefix_sum, 0) + 1
        return result
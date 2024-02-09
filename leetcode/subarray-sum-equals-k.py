class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        pre_array = {0: 1}
        ans = 0

        for num in nums:
            pre_sum += num

            if pre_sum - k in pre_array:
                ans += pre_array[pre_sum - k]
            
            pre_array[pre_sum] = pre_array.get(pre_sum, 0) + 1


        return ans
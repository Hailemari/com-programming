class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = [0]
        count = {0: 1}
        result = 0

        current_sum = 0
        for num in nums:
            current_sum += num
            prefix_sum.append(current_sum)

            if current_sum - goal in count:
                result += count[current_sum - goal]

            if current_sum in count:
                count[current_sum] += 1
            else:
                count[current_sum] = 1

        return result

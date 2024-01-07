class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k

        cur = sum(nums[i:j])
        max_avg = cur / k

        while j < len(nums):
            cur -= nums[i]
            cur += nums[j]

            max_avg = max(max_avg, cur / k)
            i += 1
            j += 1

        return max_avg


        
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize variables
        count, cum_sum = 0, 0
        sum_count = {0: 1}  # Dictionary to store cumulative sum and its count

        # Iterate through the array
        for num in nums:
            cum_sum += num

            # Check if the complement (cumulative sum - k) is in the dictionary
            if cum_sum - k in sum_count:
                count += sum_count[cum_sum - k]

            # Update the dictionary with the current cumulative sum
            sum_count[cum_sum] = sum_count.get(cum_sum, 0) + 1

        return count
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        unique_total = len(set(nums))
        freq = {}
        ans = 0

        left = 0
        for right in range(n):
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            while len(freq) == unique_total:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            ans += left
            
        return ans

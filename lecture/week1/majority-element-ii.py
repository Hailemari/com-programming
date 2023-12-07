class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        freq = defaultdict(int)

        for i in range(n):
            freq[nums[i]] += 1
        
        for key, value in freq.items():
            if float(value) > n / 3:
                result.append(key)
        
        return result
                
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        freq = defaultdict(list)

        for i in range(len(nums)):
            freq[nums[i]].append(i)

        ans = [0] * len(nums)
        for num, val in freq.items():
            suffix_sum = sum(val)
            prefix_sum = 0

            n = len(val)
            p = 0
            for i in val:
                prefix_sum += i
                suffix_sum -= i
                p += 1
                n -= 1
                ans[i] = p*i - n*i + suffix_sum - prefix_sum

        return ans    
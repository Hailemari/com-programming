class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref_sum = 0
        count_array = { }
        answer = 0

        for pref_sum in accumulate(nums):
            pref_sum %= k
            if pref_sum == 0:
                answer += 1

            if pref_sum in count_array:
                answer += count_array[pref_sum]

            count_array[pref_sum] = count_array.get(pref_sum, 0) + 1

        return answer
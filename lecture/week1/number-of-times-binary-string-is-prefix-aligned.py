class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        pref_aligned = 0
        largest = 0

        for idx, val in enumerate(flips):
            if val > largest:
                largest = val
            if idx + 1 == largest:
                pref_aligned += 1

        return pref_aligned

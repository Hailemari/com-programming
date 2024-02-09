class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = s.count("0")
        ones = len(s) - zeros
        valid_ways = 0

        prev_ones, prev_zeros = 0, 0 # to keep track of the number of zeros and ones before that index
        for num in s:
            if num == "0":
                valid_ways += prev_ones * (ones - prev_ones)
                prev_zeros += 1
            else:
                valid_ways += prev_zeros * (zeros - prev_zeros)
                prev_ones += 1

        return valid_ways
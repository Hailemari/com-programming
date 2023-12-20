class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # If the last digit is not 9, simply increment it
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        # If the last digit is 9, find the rightmost non-9 digit and increment it
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                digits[i+1:] = [0] * (n-i-1) # Set all digits to the right to 0
                return digits
        
        # If all digits are 9, add a new leading digit
        return [1] + [0] * n

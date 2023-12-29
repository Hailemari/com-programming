class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        digits = []

        if num > 0:
            while num > 0:
                last_digit = num % 10
                digits.append(last_digit)

                num = num // 10

            digits.sort()

            if digits[0] != 0:
                res = "".join(map(str, digits))
                return int(res)

            for i in range(1, len(digits)):
                if digits[i] != 0:
                    digits[0], digits[i] = digits[i], digits[0]
                    res = "".join(map(str, digits))
                    return int(res)
            
        else:
            num = (-1) * num
            while num > 0:
                last_digit = num % 10
                digits.append(last_digit)

                num = num // 10

            digits.sort(reverse = True)
            
            res = "".join(map(str, digits))
            return -int(res)
    
class Solution:
    def totalMoney(self, n: int) -> int:
        result = 0

        full_rounds = n // 7
        remainder = n % 7

        starting_point = 1
        for i in range(full_rounds):
            for j in range(starting_point, starting_point + 7):
                result += j
            starting_point += 1

        for i in range(starting_point, starting_point + remainder):
            result += i

        return result
        
        
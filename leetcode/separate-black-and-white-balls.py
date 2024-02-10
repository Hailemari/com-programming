class Solution:
    def minimumSteps(self, s: str) -> int:
        zeros = s.count("0")

        swaps = 0
        for color in s:
            if color == "1":
                swaps += zeros
            else:
                zeros -= 1
            

        return swaps

        

        


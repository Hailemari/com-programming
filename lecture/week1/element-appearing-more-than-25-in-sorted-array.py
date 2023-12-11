class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        new_arr = Counter(arr)

        for key, value in new_arr.items():
            if value / n > 0.25:
                return key
                


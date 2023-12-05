class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest = max(candies)
        result = []

        for i in range(len(candies)):
            if candies[i] + extraCandies < largest:
                result.append(False)
            else:
                result.append(True)

        return result


        
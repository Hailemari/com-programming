class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        result = []

        for num in nums:
            if num < 0:
                negatives.append(num)
            else:
                positives.append(num)

        i = 0

        while i < len(negatives):
            result.append(positives[i])
            result.append(negatives[i])
            i += 1

        return result

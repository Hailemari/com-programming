class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        # # Bubble sort
        # n = len(names)
        # for i in range(n):
        #     k = 0

        #     for j in range(1, n - i):
        #         if heights[j] > heights[k]:
        #             names[k], names[j] = names[j], names[k]
        #             heights[k], heights[j] = heights[j], heights[k]
        #         k += 1


        # return names

        # Selection sort
        n = len(names)
        for i in range(n):
            max_num = max(heights[i:])
            idx = heights.index(max_num)

            names[i], names[idx] = names[idx], names[i]
            heights[i], heights[idx] = heights[idx], heights[i]

        return names
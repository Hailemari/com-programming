class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        for size in range(len(arr), 1, -1):
            # Find the index of the largest element not yet sorted
            max_index = arr.index(max(arr[:size]))

            # If the largest element is not a its final position
            if max_index != size - 1:
                # If the largest element is not on top, flip it to top
                if max_index != 0:
                    flips.append(max_index + 1) # we need to reverse the subarray of index 'max_size + 1'
                    arr[:max_index + 1] = arr[:max_index + 1][::-1]

                # Now that the largest element is at the top, flip it to its final position
                flips.append(size)
                arr[:size] = arr[:size][::-1]

        return flips
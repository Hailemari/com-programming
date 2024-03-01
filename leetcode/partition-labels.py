class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = {}

        for i, val in enumerate(s):
            last_occurence[val] = i

        partitions = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            end = max(end, last_occurence[char])

            if i == end:
                partitions.append(end - start + 1)
                start = i + 1


        return partitions
        


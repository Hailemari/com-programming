class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        res = []

        for i in range(len(arr2)):        
            res.extend([arr2[i]]*freq[arr2[i]])

        unique = []
        for num in arr1:
            if num not in arr2:
                unique.append(num)

        unique.sort()

        res.extend(unique)

        return res
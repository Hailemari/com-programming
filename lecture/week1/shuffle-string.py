class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(s)

        for i, char in zip(indices, s):
            result[i] = char
        
        return ''.join(result)
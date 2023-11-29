class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # find the shortest string
        min_len = min(len(s) for s in strs)

        # binary search for common prefix length
        low, high = 0, min_len - 1

        while low <= high:
            mid = (low + high) // 2
            if all(s[:mid+1] == strs[0][:mid+1] for s in strs):
                low = mid + 1
            else:
                high = mid - 1
        
        return strs[0][:high + 1]
           

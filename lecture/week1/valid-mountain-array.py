class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        max_num = max(arr[1:n-1])
        max_num_idx = arr.index(max_num)
        
        if max_num_idx == 0 or max_num_idx == n - 1:
            return False

        for i in range(max_num_idx):
            if arr[i] >= arr[i+1]:
                return False
        
        for i in range(max_num_idx, n - 1):
            if arr[i] <= arr[i + 1]:
                return False

        return True
        

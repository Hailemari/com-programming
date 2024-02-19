class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0

        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]

        for i in range(n):
            for j in range(n):
                ans += min(row_max[i], col_max[j]) - grid[i][j]
                
        return ans

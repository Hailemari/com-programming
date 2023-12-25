class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat[0]) - 1
        if n == 0:
            return mat[0][0]
            
        i, j = 0, 0
        visited = set()

        primary_sum = 0
        while i <= n:
            primary_sum += mat[i][j]
            i += 1
            j += 1
            visited.add((i, j))

        r, c = 0, n
        secondary_sum = 0
        while c >= 0:
            if (r, c) not in visited:
                secondary_sum += mat[r][c]

            r += 1
            c -= 1

        return primary_sum + secondary_sum
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        
        for _ in range(m*n):
            result.append(mat[row][col])
            if (row + col) % 2 == 0:  # Moving up
                if col == n - 1:
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1

            else:  # Moving down
                if row == m - 1:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1

        return result
        
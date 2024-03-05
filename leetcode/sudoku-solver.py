class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(row, col, num):
            for i in range(9):
                if board[i][col] == num or board[row][i] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                    return False
            return True    

        def fill(row, col):
            if row == 9:
                return True
            if col == 9:
                return fill(row + 1, 0)

            if board[row][col] == '.':
                for k in range(1, 10):
                    if is_valid(row, col, str(k)):
                        board[row][col] = str(k)
                        if fill(row, col + 1):
                            return True
                        board[row][col] = '.'
                return False
                
            return fill(row, col + 1)        

        fill(0, 0)

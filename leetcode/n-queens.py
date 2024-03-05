class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diagonal1 = set() 
        diagonal2 = set() 

        ans = []
        chess_board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                path = ["".join(row) for row in chess_board]
                ans.append(path)
                return

            for c in range(n):
                if c in col or (r + c) in diagonal1 or (r - c) in diagonal2:
                    continue

                col.add(c)
                diagonal1.add(r + c)
                diagonal2.add(r - c)
                chess_board[r][c] = "Q" 

                backtrack(r + 1)

                col.remove(c)
                diagonal1.remove(r + c)
                diagonal2.remove(r - c)
                chess_board[r][c] = "."

        backtrack(0) 
        return ans
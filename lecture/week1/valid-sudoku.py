class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans = set()
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr != '.':
                    if (i, curr) in ans or (curr, j) in ans or (i // 3, j // 3, curr) in ans:
                        return False
                    ans.add((i, curr))
                    ans.add((curr, j))
                    ans.add((i // 3, j // 3, curr))

        return True
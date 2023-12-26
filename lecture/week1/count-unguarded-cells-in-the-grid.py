class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize the grid
        grid = [[0] * n for _ in range(m)]

        # Mark guards and walls
        for guard in guards:
            grid[guard[0]][guard[1]] = 'G'
        for wall in walls:
            grid[wall[0]][wall[1]] = 'W'

        # Helper function to mark guarded cells
        def mark_guarded(row, col, delta_row, delta_col):
            while 0 <= row < m and 0 <= col < n:
                if grid[row][col] == 'G' or grid[row][col] == 'W':
                    break
                
                # Mark as guarded
                grid[row][col] = 'X'
                row += delta_row
                col += delta_col

        # Mark cells that guards can see
        for row, col in guards:
            mark_guarded(row, col - 1, 0, -1) # West
            mark_guarded(row, col + 1, 0, 1)  # East
            mark_guarded(row - 1, col, -1, 0) # North
            mark_guarded(row + 1, col, 1, 0)  # South

        # Count unguarded cells
        unguarded_count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    unguarded_count += 1

        return unguarded_count
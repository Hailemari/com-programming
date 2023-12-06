class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

        my_x_diff = abs(target[0])
        my_y_diff = abs(target[1])
        my_steps = my_x_diff + my_y_diff

        for i in range(len(ghosts)):
            ghost_x_diff = abs(ghosts[i][0] - target[0])
            ghost_y_diff = abs(ghosts[i][1] - target[1])

            ghost_steps = ghost_x_diff + ghost_y_diff

            if ghost_steps <= my_steps:
                return False


        return True




        
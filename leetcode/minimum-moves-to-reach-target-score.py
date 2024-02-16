class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0:
            return target - 1
        
        min_moves = 0
        while target > 1:
            
            if target % 2 == 0 and target != 2 and maxDoubles:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1

            min_moves += 1

            if maxDoubles == 0 and target != 1:
                min_moves += target - 1
                break

        return min_moves


            
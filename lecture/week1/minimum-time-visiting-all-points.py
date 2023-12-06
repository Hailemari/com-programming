class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minimum_time = 0

        for i in range(n - 1):
          x_diff = abs(points[i][0] - points[i+1][0])
          y_diff = abs(points[i][1] - points[i+1][1])

          # Diagonal movement takes min(x_diff, y_diff) seconds
          # Vertical or horizontal movement takes max(x_diff, y_diff) seconds
          
          minimum_time += max(x_diff, y_diff)

        return minimum_time


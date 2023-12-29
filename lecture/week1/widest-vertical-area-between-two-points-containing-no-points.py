class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        def comparator(point):
            return point[0]

        points.sort(key=comparator)
        max_area = float('-inf')

        for i in range(len(points) - 1):
            max_area = max(max_area, points[i+1][0] - points[i][0])

        return max_area

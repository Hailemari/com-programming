class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)

        points.sort(key = lambda x: (x[1], x[0]))
        arrows = 1
        first = points[0][1]

        for start, end in points[1:]:
            if start > first:
                arrows += 1
                first = end
            else:
                first = min(end, first)
                

        return arrows
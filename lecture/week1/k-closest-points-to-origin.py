class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def comparator(point):
            return sqrt(point[0]**2 + point[1]**2)

        points.sort(key = comparator)
        
        return points[:k]
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination:
            return 0
        total_distance = sum(distance)

        clockwise_distance = 0
        if start < destination:
            for i in range(start, destination):
                clockwise_distance += distance[i % len(distance)]
        else:
            for i in range(destination, start):
                 clockwise_distance += distance[i % len(distance)]


        counterclockwise_distance = total_distance - clockwise_distance

        return min(clockwise_distance, counterclockwise_distance)
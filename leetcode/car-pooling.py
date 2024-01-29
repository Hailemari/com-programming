class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = [0] * 1001 
        for numPassengers, fromLocation, toLocation in trips:
            timeline[fromLocation] += numPassengers 
            timeline[toLocation] -= numPassengers 

        currentPassengers = 0
        for passengersAtLocation in timeline:
            currentPassengers += passengersAtLocation
            if currentPassengers > capacity:
                return False

        return True 

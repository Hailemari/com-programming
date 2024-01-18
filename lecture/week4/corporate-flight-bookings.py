class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0] * n

        for first, last, seats in bookings:
            result[first-1] += seats
            if last < n:
                result[last] -= seats
        
        for idx, val in enumerate(result):
            if idx != 0:
                result[idx] += result[idx-1]

        return result
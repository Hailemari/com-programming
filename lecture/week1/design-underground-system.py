class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}
        self.travel_times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins[id]
        travel_key = (start_station, stationName)
        travel_time = t - start_time

        if travel_key not in self.travel_times:
            self.travel_times[travel_key] = (travel_time, 1)
        else:
            total_time, count = self.travel_times[travel_key]
            self.travel_times[travel_key] = (total_time + travel_time, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel_key = (startStation, endStation)
        total_time, count = self.travel_times[travel_key]
        return total_time / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
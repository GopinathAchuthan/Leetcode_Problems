class UndergroundSystem:

    def __init__(self):
        self.pointToPoint = defaultdict(lambda:[0,0])
        # first element in the list represents total time
        # second element in the list represents count
        self.customerCheckIn = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customerCheckIn[id] = [stationName, t]
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        statStation,t1 = self.customerCheckIn.pop(id)
        self.pointToPoint[(statStation, stationName)][0] += t-t1
        self.pointToPoint[(statStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.pointToPoint[(startStation,endStation)][0]/self.pointToPoint[(startStation,endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
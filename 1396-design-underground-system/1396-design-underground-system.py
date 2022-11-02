from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.stations = defaultdict(list)
        self.customer = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.customer:
            self.customer[id] = [[stationName, ""], t]
        
        # print("customers", self.customer)
        # print("stations", self.stations)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.customer:
            return False
        else:
            # print(self.customer[id][0])
            self.customer[id][0][1] = stationName
            # print(self.customer[id][0])
            self.customer[id][1] = t - self.customer[id][1]
            # print(self.customer[id])
            self.stations[(self.customer[id][0][0], self.customer[id][0][1])].append(self.customer[id][1])
        
        del self.customer[id]
        # print("customers", self.customer)
        # print("stations", self.stations)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.stations[(startStation, endStation)])/len(self.stations[(startStation, endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
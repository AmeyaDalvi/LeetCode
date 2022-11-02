from collections import defaultdict


#use defaultdict for stations dictionary, and dict for customers. 
# e.g customers: {45: [['Leyton', 'Waterloo'], 3]} stations: {('Leyton', 'Waterloo'): [12, 10]}

class UndergroundSystem:

    def __init__(self):
        self.stations = defaultdict(list)
        self.customer = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.customer:
            self.customer[id] = [[stationName, ""], t]
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.customer:
            self.customer[id][0][1] = stationName
            self.customer[id][1] = t - self.customer[id][1]
            self.stations[(self.customer[id][0][0], self.customer[id][0][1])].append(self.customer[id][1])
        
        del self.customer[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.stations[(startStation, endStation)])/len(self.stations[(startStation, endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
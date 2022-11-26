class Event:
    def __init__(self, id: int, stationName: str, t: int) -> None:
        self.id = id
        self.stationName = stationName
        self.time = t

class Average:
    def __init__(self, total: int, count: int) -> None:
        self.total = total
        self.count = count
        
    def updateAverage(self, diff: int) -> None:
        self.total += diff
        self.count += 1
    
    def getAverage(self) -> float:
        return self.total / self.count


class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.averages = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        event = Event(id, stationName, t)
        self.customers[id] = event
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkout = self.customers.get(id)
        
        diff = t - checkout.time
        
        key = (checkout.stationName, stationName)
        
        if key not in self.averages:
            average = Average(0,0)
            self.averages[key] = average
        else:
            average = self.averages[key]

        self.averages[key].updateAverage(diff)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        return self.averages[key].getAverage()
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
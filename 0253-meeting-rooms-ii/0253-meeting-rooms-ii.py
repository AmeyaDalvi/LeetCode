import heapq

# use heap to prioritize meetings that take place early, sort intervals based on start time and put them in a min heap based on their end times

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        free = []
        
        intervals.sort(key = lambda x: x[0])  
        
        heapq.heappush(free, intervals[0][1])
        
        for i in intervals[1:]:
            if free[0] <= i[0]:
                heapq.heappop(free)
            
            heapq.heappush(free, i[1])
            
        
        return len(free)
        
        
        
        
        

                
            
        
        
        
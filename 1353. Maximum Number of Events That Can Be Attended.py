class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort()
        startDay, endDay = events[0][0], max([x[1] for x in events])
        
        result = 0
        index = 0
        heap = []
        
        for day in range(startDay,endDay+1):
            while index<N and events[index][0]==day:
                heappush(heap, events[index][1])
                index +=1
            
            while heap and heap[0]<day:
                heappop(heap)
            
            if heap:
                result += 1
                heappop(heap)
                
        return result
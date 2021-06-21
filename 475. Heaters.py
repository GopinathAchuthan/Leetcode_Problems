class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        left = 0
        right = max(houses[-1],heaters[-1])
        
        while(left<=right):
            mid = left + (right-left)//2
            state1 = self.isCovered(houses,heaters,mid-1)
            state2 = self.isCovered(houses,heaters,mid)
            if not state1 and state2:
                return mid
            elif state1 and state2:
                right = mid-1
            else:
                left = mid+1
        return mid
    
    def isCovered(self, houses, heaters, radius):
        pos = 0
        
        for heater in heaters:
            minRange = heater - radius
            maxRange = heater + radius
            while(pos<len(houses) and minRange<=houses[pos]<=maxRange):
                pos+=1
        
        if pos<len(houses):
            return False
        else:
            return True
                
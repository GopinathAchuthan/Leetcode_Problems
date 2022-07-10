'''
Time Complexity: O(n log w)
Space Complexity: O(1)

Topic: Bisection Search
'''
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:        
        def getPossibleKValue(penalty):
            val = 0
            for i in range(len(stations)-1):
                val+=math.ceil((stations[i+1]-stations[i])/penalty)-1
            return val
        
        # range of penalty()
        left = 0
        right = 0
        
        for i in range(len(stations)-1):
            right = max(right, stations[i+1]-stations[i])
        
        # bisection search
        while right-left >1e-6:
            mid = left+(right-left)/2.0
            
            # given the mid as penalty(), find the minimum K stations added.
            val = getPossibleKValue(mid)
            
            if val>k:
                left = mid
            else:
                right = mid
        
        return left
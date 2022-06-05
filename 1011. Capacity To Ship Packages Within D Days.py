'''
Time Complexity: O(n*log m)
Space Complexity: O(1)

Topic: Binary Search
'''
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # calculate possible days based on weight capacity of the ship
        def calc_days(capacity): 
            days = 1
            load = 0
            for weight in weights:
                load+=weight
                if load>capacity:
                    days+=1
                    load = weight
            return days
        
        # binary search
        left, right = max(weights), sum(weights)
        
        while left<=right:
            mid_W = left+(right-left)//2
            
            new_D = calc_days(mid_W)
            
            if new_D>days:
                left = mid_W+1
            else:
                right = mid_W-1
        
        return left
                    
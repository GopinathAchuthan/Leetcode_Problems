'''
Time Complexity: O(log max(piles)*len(piles))
                 O(len(piles))+O(log max(piles))
Space Complexity: O(1)

Topic: Optimization, Binary Search
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start_k, end_k = 1, max(piles)
        
        while start_k<=end_k:
            mid_k = start_k+(end_k-start_k)//2
            
            # compute number of hours will take to eat all bananas at the speed K.
            # possible_h = sum([ceil(piles[i]/mid_k) for i in range(len(piles))])
            possible_h = 0
            for bananas in piles:
                possible_h+=ceil(bananas/mid_k)
            
            if possible_h>h:
                start_k = mid_k+1
            else:
                end_k = mid_k-1
        return start_k
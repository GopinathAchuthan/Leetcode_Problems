class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = maxPrice = prices[0]
        ans = 0
        for price in prices:
            if price<minPrice:
                ans = max(ans, maxPrice - minPrice)
                minPrice = maxPrice = price
            else:
                maxPrice = max(maxPrice, price)
        
        return max(ans,maxPrice-minPrice)
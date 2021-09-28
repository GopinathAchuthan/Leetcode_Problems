# Time Complexity: O(N*A)
# Space Complexity: O(A)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [float('inf')]*(amount+1)
        table[0]=0
        coins.sort()
        for coin in coins:
            for i in range(coin,amount+1):
                table[i] = min(table[i],1+table[i-coin])
        
        return table[amount] if table[amount] != float('inf') else -1
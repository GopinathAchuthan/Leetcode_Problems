'''
Topics: Dynamic Programming

Time Complexity: O(cn)
Space Complexity: O(n)
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [float('inf')]*(amount+1)
        table[0] = 0
        coins_set = set(coins)
        for coin in coins_set:
            for i in range(coin,amount+1):
                table[i] = min(table[i],1+table[i-coin])
        return table[amount] if table[amount]!=float('inf') else -1
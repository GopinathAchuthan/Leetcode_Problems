class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        coins.sort()
        array = [-1 for i in range(amount+1)]
        
        for i in range(len(array)):
            for coin in coins:
                if coin<i:
                    if array[i-coin]!=-1:
                        if array[i]==-1:
                            array[i] = 1+array[i-coin]
                        else:
                            array[i] = min(array[i], 1+array[i-coin])
                elif coin == i:
                    array[i] = 1
                else:
                    break
        
        return array[-1]
'''
Time Complexity: O(nlogn)
Space Complexity: O(n)

Topics: Array, Hash Table, Sorting
'''
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = dict()
        
        for winner, loser in matches:
            if winner not in losses:
                losses[winner] = 0
            if loser not in losses:
                losses[loser] = 0
            losses[loser] += 1
        
        ans = [[],[]]
        
        for player, count in sorted(losses.items()):
            if count == 0:
                ans[0].append(player)
            if count == 1:
                ans[1].append(player)
            
        return ans
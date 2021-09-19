'''
Time Complexity: O(N)
Space Complexity: O(1)
'''
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        c1,c2,c3 = 0,0,0
        for red,blue,green in costs:
            c1,c2,c3 = red+min(c2,c3),blue+min(c1,c3),green+min(c1,c2)
        return min(c1,c2,c3)
'''
Let N be number of nodes
Time Complexity: O(N)
Recursive Call Stack: O(N)
Space Complexity: O(N*N)
'''

class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        graph = [[] for _ in range(nodes)]
        # create adjacancy list
        for i in range(1,nodes):
            graph[parent[i]].append(i)
        
        # DFS
        def dfs(i):
            # base case
            if len(graph[i])==0:
                return (value[i],0) if value[i]==0 else (value[i],1)
            
            total, count = value[i], 1
            for k in range(len(graph[i])):
                val,cnt = dfs(graph[i][k])
                total+=val
                count+=cnt
            if total==0: count = 0
            return total,count
        
        _, res = dfs(0)
        return res
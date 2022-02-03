"""
Method 1: Topological Sort - Kahn's Algorithm
time complexity: O(v+e)
space complexity: O(v+e)
"""
class GNode:
        def __init__(self):
            self.inDegree = 0
            self.outDegree = []
            
class Solution:        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Kahn's Algorithm
        """
        result = []
        # initialize adjacency list
        adjList = [GNode() for _ in range(numCourses)]
        totalEdges = 0
        for course, prereq in prerequisites:
            adjList[prereq].outDegree.append(course)
            adjList[course].inDegree += 1
            totalEdges += 1
        
        # add zero inDegree nodes to the queue
        q = deque()
        for idx, node in enumerate(adjList):
            if node.inDegree == 0:
                q.append(node)
                result.append(idx)

        # remove edges
        removedEdges = 0
        while q:
            node = q.pop()
            for nextNode in node.outDegree:
                adjList[nextNode].inDegree-=1
                removedEdges += 1
                if adjList[nextNode].inDegree==0:
                    q.append(adjList[nextNode])
                    result.append(nextNode)
        
        # check whether removed edges matches with given number of edges
        if totalEdges == removedEdges:
            return result
        else:
            return []
        

"""
Method 2: Recursive DFS with timestamp
"""

# Time Complexity: O(V+E)
# Space Complexity: O(V*V)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # creating adjacancy list for directed graph
        graph = [[] for _ in range(numCourses)]
        for course, preq in prerequisites:
            graph[preq].append(course)
            
        start = [-1]*numCourses
        end = [-1]*numCourses
        time = [0]
        res = []
        
        # outer loop
        for i in range(numCourses):
            if start[i]==-1:
                # use depth first search
                if not self.dfs(graph, i, start, end, time, res):
                    return []
        # return the courses list
        return res[::-1]
    
    def dfs(self, graph, i, start, end, time, res):
        start[i] = time[0]
        time[0]+=1
        for nextCourse in graph[i]:
            if start[nextCourse] == -1: 
                if not self.dfs(graph, nextCourse, start, end, time, res):
                    return False
            elif end[nextCourse] == -1:
                # check whether it has back edges
                return False
        res.append(i)
        end[i] = time[0]
        time[0]
        return True
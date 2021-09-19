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
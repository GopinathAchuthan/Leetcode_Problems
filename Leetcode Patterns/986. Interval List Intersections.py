# Time Complexity: O(M+N)
# Space Complexity: O(M+N)

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        m,n = len(firstList),len(secondList) 
        i,j = 0,0
        ans = []
        while i<m and j<n:
            # check for overlap
            a1,a2 = firstList[i]
            b1,b2 = secondList[j]
            if a2<b1:
                i+=1
                continue
            if b2<a1:
                j+=1
                continue
            ans.append([max(a1,b1),min(a2,b2)])
            
            # move to next disjoint interval
            if a2<b2:
                i+=1
            else:
                j+=1
        return ans
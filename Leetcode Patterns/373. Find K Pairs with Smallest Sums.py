# Time Complexity: O(K)
# Space Complexity: O(M*N)
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        mem, visited, ans = [], set(), []
        mem.append((nums1[0]+nums2[0],0,0))
        visited.add((0,0))
        m,n = len(nums1), len(nums2)
        
        for _ in range(k):
            if mem:
                val, p1, p2 =  heapq.heappop(mem)
                ans.append([nums1[p1],nums2[p2]])
                if p1+1<m and (p1+1,p2) not in visited:
                    visited.add((p1+1,p2))
                    heapq.heappush(mem, (nums1[p1+1]+nums2[p2], p1+1, p2))
                if p2+1<n and (p1,p2+1) not in visited:
                    visited.add((p1,p2+1))
                    heapq.heappush(mem, (nums1[p1]+nums2[p2+1], p1, p2+1))
        return ans
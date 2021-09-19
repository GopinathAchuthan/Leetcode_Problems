# Time Complexity: O(N log N)
# Space Complexity: O(1)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = 0
        ans = 0
        for curr in range(1,len(intervals)):
            if intervals[curr][0]<intervals[prev][1]:
                # if there is an overlap
                ans+=1
                if intervals[curr][1]<intervals[prev][1]:
                    prev = curr
            else:
                prev = curr
        return ans
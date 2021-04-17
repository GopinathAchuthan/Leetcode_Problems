class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals list by their first element
        intervals.sort(key = lambda x: x[0])
                
        # base case
        if len(intervals)<=1:
            return intervals
        
        # other cases
        start = 0
        end = 1
        result = []
        
        while start < len(intervals):
            # checking for overlap
            temp_end = intervals[start][1]
            while end < len(intervals) and temp_end >= intervals[end][0]:
                temp_end = max(temp_end, intervals[end][1])
                end += 1
                
            # add new intervals to the result
            result.append([intervals[start][0], temp_end])
            
            # assign new start and end values
            start = end
            end += 1
            
        return result
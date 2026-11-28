class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals with teh start value
        intervals.sort(key = lambda i : i[0])
        res = []
        res.append(intervals[0]) # updating 1st interval coordiante to teh result

        for start, end in intervals[1:]: 
            lastend = res[-1][1] # last end value

            if start <= lastend:
                res[-1][1] = max(lastend, end)
            else:
                res.append([start, end])
        
        return res
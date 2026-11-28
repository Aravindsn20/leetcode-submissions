class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        lastend = intervals[0][1]
        res = 0

        for start, end in intervals[1:]:
            if start >= lastend:
                lastend = end
            else:
                res += 1
                lastend = min(lastend, end)
        return res
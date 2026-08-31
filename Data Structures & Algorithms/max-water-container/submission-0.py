class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Brute Force
        l = 0
        res  = 0
        for i in range(len(heights)):
            l = i
            for r in range(i + 1, len(heights)):
                area = (r-l) * min(heights[r], heights[l])
                res = max(area, res)
        return res
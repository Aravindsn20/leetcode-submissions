class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Brute Force
        # l = 0
        # res  = 0
        # for i in range(len(heights)):
        #     l = i
        #     for r in range(i + 1, len(heights)):
        #         area = (r-l) * min(heights[r], heights[l])
        #         res = max(area, res)
        # return res

        # 2 pointer method 
        l, r = 0, len(heights) - 1
        res = 0
        for i in range(len(heights)):
            while l < r:
                area = (r - l) * min(heights[r], heights[l])
                res = max(area, res)
                if heights[l] < heights[r]:
                    l += 1
                else:
                    r -= 1
        return res
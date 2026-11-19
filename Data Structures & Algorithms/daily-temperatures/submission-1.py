class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temp)
        for i,t in enumerate(temp):
            while stack and stack[-1][0] < t:
                val, ind = stack.pop()
                res[ind] = i - ind
            else:
                stack.append([t, i])
        return res
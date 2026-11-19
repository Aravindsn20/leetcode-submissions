class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Montonic Stack
        res = [0] * len(temperatures)
        stack = [] # Storethe value and indices
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]: 
                temp, ind = stack.pop()
                res[ind] = i - ind
            else:
                stack.append([t, i])
        return res
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = maxP = 0
        for n in nums:
            if n == 1:
                c += 1
            else:
                c = 0
            maxP = max(maxP, c)
        return maxP
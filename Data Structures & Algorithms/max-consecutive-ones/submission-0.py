class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_C, c = 0, 0
        for n in nums:
            if n == 1:
                c += 1
            if n != 1:
                c = 0
            max_C = max(c, max_C)
        return max_C
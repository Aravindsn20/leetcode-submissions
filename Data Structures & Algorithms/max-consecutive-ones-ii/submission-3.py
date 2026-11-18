class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = c = maxP = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                c += 1

            while c > 1:
                if nums[l] == 0:
                    c -= 1
                l += 1
            maxP = max(maxP, r - l + 1)
        return maxP
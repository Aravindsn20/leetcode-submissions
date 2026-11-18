class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = c = maxP = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                c += 1

            while c > k:
                if nums[l] == 0:
                    c -= 1
                l += 1
            maxP = max(maxP, r - l + 1)
        return maxP
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = Occur_0 = res = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                Occur_0 += 1

            while Occur_0 > k:
                if nums[l] == 0:
                    Occur_0 -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
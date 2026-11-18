class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # SLiding window approach, hashmap to get the count
        # in the window r - l + 1 is 0 occurence is 1, then compute teh window length. If not shhrink the window
        l = res = 0
        Occur_0 = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                Occur_0 += 1

            while Occur_0 > 1:
                if nums[l] == 0:
                    Occur_0 -= 1
                l += 1
            res = max(r - l + 1, res)
        return res
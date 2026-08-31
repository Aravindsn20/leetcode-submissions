class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
# [2, 4, 3, 5]

# [2, 8, 24, 120] - prefix mul

# [120, 60, 15, 5] - suffix mul

# [60, 30, 40, 24] - res
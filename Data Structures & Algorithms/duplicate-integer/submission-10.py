class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap = {}
        # for i in nums:
        #     if i in hashmap:
        #         return True
        #     hashmap[i] = 1
        # return False

        #Best Soln - 
        if len(set(nums)) == len(nums):
            return False
        return True
        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort() 
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False
        hashmap = {}
        for n in nums:
            if n in hashmap:
                return True
            hashmap[n] = 1
        return False

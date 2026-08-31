class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # BRUTE FORCE
        # i, j = 0, 0
        # t = []
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             t.append(i)
        #             t.append(j)
        #             return t
        
        # USing HashMap -
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
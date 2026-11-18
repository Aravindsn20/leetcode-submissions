class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap = {}
        # for n in nums:
        #     hashmap[n] = hashmap.get(n, 0) + 1
        # if all(i == 1 for i in hashmap.values()):
        #     return False
        # return True

        hashmap = {}
        for n in nums:
            if n in hashmap:
                return True
            hashmap[n] = 1
        return False
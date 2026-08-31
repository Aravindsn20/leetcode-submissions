class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for n in nums:
            if n not in hashmap:
                hashmap[n] = hashmap.get(0, 1)
            else:
                return True
        return False
        
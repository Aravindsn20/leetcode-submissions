class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum and using hash to store thenumbers we encounter
        currSum = res = 0
        hashmap = {0 : 1}
        for n in nums:
            currSum += n
            diff = currSum - k

            res += hashmap.get(diff, 0)
            hashmap[currSum] = hashmap.get(currSum, 0) + 1
        return res
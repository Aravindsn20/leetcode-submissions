class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Find the prefix sum, stre in hashmap - for traceability
        hashmap = {0 : 1}
        currSum = 0
        diff= 0
        res = 0
        for n in nums:
            currSum += n
            diff = currSum - k
            #check if the diff in hashmap ?
            res += hashmap.get(diff, 0)

            #update the currsum value to the hasmap
            hashmap[currSum] = hashmap.get(currSum, 0) + 1

        return res


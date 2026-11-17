class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} # count of all the nmbers
        res = []
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        freq = [[] for _ in range(len(nums) + 1)]
        for n,c in hashmap.items():
            freq[c].append(n)
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
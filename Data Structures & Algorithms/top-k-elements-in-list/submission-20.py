class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        sorted_s = sorted(hashmap.items(), key = lambda i: i[1], reverse = True)
        return list(i[0] for i in sorted_s[:k])
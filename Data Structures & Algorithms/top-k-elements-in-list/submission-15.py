class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        res = sorted(hashmap.items(), key=lambda i: i[1], reverse = True)
        return [i[0] for i in res[:k]]
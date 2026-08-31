class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hashamp to count the freq
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n , 0) + 1
        # sort it in desc of freq
        res = []
        sorted_s = sorted(hashmap.items(), key = lambda i: i[1], reverse = True)
        # return k items
        return [i[0] for i in sorted_s[:k]]
        
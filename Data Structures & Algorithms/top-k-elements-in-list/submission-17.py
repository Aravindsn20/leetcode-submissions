class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approach 1 - Hashmap Store and Sort
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        sorted_S = sorted(hashmap.items(), key = lambda i: i[1], reverse = True)
        return [i[0] for i in sorted_S[:k]]
            

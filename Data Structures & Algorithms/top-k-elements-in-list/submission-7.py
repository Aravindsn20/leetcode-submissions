class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        sorted_items = sorted(hashmap.items(), key=lambda i: i[1], reverse=True)
        return [i[0] for i in sorted_items[:k]]
            
            
        
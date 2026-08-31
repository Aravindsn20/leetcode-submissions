class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # With sorting soln
        # hashmap = {}
        # for n in nums:
        #     if n in hashmap:
        #         hashmap[n] += 1
        #     else:
        #         hashmap[n] = 1
        # sorted_items = sorted(hashmap.items(), key=lambda i: i[1], reverse=True)
        # return [i[0] for i in sorted_items[:k]]
        hashmap = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        for n, c in hashmap.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


            
            
        
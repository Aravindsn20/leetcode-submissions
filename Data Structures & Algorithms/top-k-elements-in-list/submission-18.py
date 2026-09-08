class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approach 1 - Hashmap Store and Sort
        # hashmap = {}
        # for n in nums:
        #     hashmap[n] = hashmap.get(n, 0) + 1
        # sorted_S = sorted(hashmap.items(), key = lambda i: i[1], reverse = True)
        # return [i[0] for i in sorted_S[:k]]
        
        # Approach 2 - Using Fixed Count Array, instead of sorting
        hashmap = {}
        res = []
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        size = len(nums)
        count = [[] for _ in range(size + 1)]
        for n,f in hashmap.items():
            count[f].append(n)
        for i in range(size, -1, -1):
            for n in count[i]: 
                res.append(n)
                if len(res) == k:
                    return res


        

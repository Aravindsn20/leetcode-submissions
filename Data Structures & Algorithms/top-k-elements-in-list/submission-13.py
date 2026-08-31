class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a hash table and get the count of all the numbers
        hashmap = {}
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        sorted_s = sorted(hashmap.items(), key = lambda i: i[1], reverse = True)
        return [i[0] for i in sorted_s[:k]]
        # Sort the hash with the req
        # Return the top k elements 
        
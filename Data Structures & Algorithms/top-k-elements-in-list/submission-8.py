class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        Sorted_nums = sorted(freq.items(), key = lambda i: i[1], reverse = True)
        return [i[0] for i in Sorted_nums[:k]]
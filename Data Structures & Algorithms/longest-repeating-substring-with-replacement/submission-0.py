class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Approach is sliding window
        # while we slide the window, ge the occurence of teh characters int he hasmap
        # window - max_occurence <= k (condition is valid)
        # if not:
        #     increment the left pointer. 

        hashmap = {}
        l, res, max_F = 0, 0, 0
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1 # to get the count
            max_F = max(max_F, max(hashmap.values()))
            while (((r - l + 1) - max_F) > k):
                hashmap[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res
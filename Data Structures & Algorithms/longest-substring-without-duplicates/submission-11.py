class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l = maxP = 0
        for r in range(len(s)):
            while hashmap.get(s[r], 0) > 0:
                hashmap[s[l]] -= 1
                l += 1
            maxP = max(r - l + 1, maxP)
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
        return maxP

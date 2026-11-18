class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        l = max_Occur = res = 0
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            max_Occur = max(hashmap.values())
            while (((r - l + 1) - max_Occur) > k):
                hashmap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
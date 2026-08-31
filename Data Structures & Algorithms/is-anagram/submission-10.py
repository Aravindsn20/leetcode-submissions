class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) != len(t):
            return False
        for cs, ct in zip(s, t):
            hashmap[cs] = hashmap.get(cs, 0) + 1
            hashmap[ct] = hashmap.get(ct, 0) - 1
        return all(v==0 for v in hashmap.values())

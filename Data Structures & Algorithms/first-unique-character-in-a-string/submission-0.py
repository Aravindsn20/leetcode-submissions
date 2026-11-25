class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for cs in s:
            hashmap[cs] = hashmap.get(cs, 0) + 1
        
        for i, cs in enumerate(s):
            if hashmap[cs] == 1:
                return i
        return -1
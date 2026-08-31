class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap = {}
        # for sc in s:
        #     if sc in hashmap:
        #         hashmap[sc] += 1
        #     else:
        #         hashmap[sc] = 1
        # for st in t:
        #     if st not in hashmap:
        #         return False
        #     elif st in hashmap:
        #         hashmap[st] -= 1

        # return all(v == 0 for v in hashmap.values())
        
        if len(s) != len(t):
            return False
        
        count = [0]*26
        for sc, st in zip(s, t):
            count[ord(sc) - ord('a')] += 1
            count[ord(st) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        return True
            
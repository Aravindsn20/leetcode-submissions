class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # Sorted Soln
        # sortedS = "".join(sorted(s))
        # sortedT = "".join(sorted(t))
        # if sortedT == sortedS:
        #     return True
        # return False
        
        # Hashmap Soln 
        hashmap = {}
        for cs in s:
            hashmap[cs] = hashmap.get(cs, 0) + 1
        for ct in t:
            hashmap[ct] = hashmap.get(ct, 0) - 1
        return all(i == 0 for i in hashmap.values())

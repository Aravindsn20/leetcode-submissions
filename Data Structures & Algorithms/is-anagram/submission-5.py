class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for cs in s:
            if cs not in hashmap:
                hashmap[cs] = 1
            else:
                hashmap[cs] += 1
        for ct in t:
            if ct in hashmap:
                hashmap[ct] -= 1
            else:
                return False

        return all(i == 0 for i in hashmap.values())
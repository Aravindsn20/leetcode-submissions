class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap = {}
        # for cs in s:
        #     # if cs not in hashmap:
        #     #     hashmap[cs] = 1
        #     # else:
        #     #     hashmap[cs] += 1
        #     #use the below line if not for the above code
        #     hashmap[cs] = hashmap.get(cs, 0) + 1
        # for ct in t:
        #     if ct in hashmap:
        #         hashmap[ct] -= 1
        #     else:
        #         return False

        
        arr = [0] * 26
        if len(s) != len(t):
            return False
        for cs, ct in zip(s, t):
            arr[ord(cs) - ord('a')] += 1
            arr[ord(ct) - ord('a')] -= 1
        return all(i == 0 for i in arr)
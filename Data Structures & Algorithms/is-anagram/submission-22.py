class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)

        # return (sorted_s == sorted_t)

        # hashmap = {}
        # for cs in s:
        #     hashmap[cs] = hashmap.get(cs, 0) + 1
        # for ct in t:
        #     hashmap[ct] = hashmap.get(ct, 0) - 1
        # return all (i == 0 for i in hashmap.values())

        arr = [0] * 26
        for cs in s:
            arr[ord(cs) - ord('a')] += 1
        for ct in t:
            arr[ord(ct) - ord('a')] -= 1
        return all (i == 0 for i in arr)    

